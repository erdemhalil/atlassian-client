from __future__ import annotations

import httpx
import pytest

from atlassian.core.async_client import AsyncBaseClient
from atlassian.core.auth import AuthBase
from atlassian.core.exceptions import NotFoundError, ServerError


class HeaderAuth(AuthBase):
    def apply(self, request: httpx.Request) -> httpx.Request:
        request.headers["X-Test-Auth"] = "applied"
        return request


def test_client_init_rejects_negative_max_retries() -> None:
    with pytest.raises(ValueError, match="max_retries"):
        AsyncBaseClient(base_url="https://example.test", max_retries=-1)


def test_client_init_rejects_negative_retry_backoff_factor() -> None:
    with pytest.raises(ValueError, match="retry_backoff_factor"):
        AsyncBaseClient(base_url="https://example.test", retry_backoff_factor=-0.1)


@pytest.mark.asyncio
async def test_request_applies_auth_and_returns_response() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers["X-Test-Auth"] == "applied"
        return httpx.Response(200, json={"ok": True})

    client = AsyncBaseClient(
        base_url="https://example.test",
        auth=HeaderAuth(),
        transport=httpx.MockTransport(handler),
    )

    response = await client._request("GET", "/status")

    assert response.status_code == 200
    assert response.json() == {"ok": True}
    await client.aclose()


@pytest.mark.asyncio
async def test_request_retries_retryable_status(monkeypatch: pytest.MonkeyPatch) -> None:
    attempts = {"count": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        attempts["count"] += 1
        if attempts["count"] < 3:
            return httpx.Response(500, json={"errors": [{"message": "fail"}]})
        return httpx.Response(200, json={"ok": True})

    sleep_calls: list[float] = []

    async def fake_sleep(delay: float) -> None:
        sleep_calls.append(delay)

    monkeypatch.setattr("atlassian.core.async_client.asyncio.sleep", fake_sleep)

    client = AsyncBaseClient(
        base_url="https://example.test",
        max_retries=3,
        retry_backoff_factor=0.25,
        transport=httpx.MockTransport(handler),
    )

    response = await client._request("GET", "/retry")

    assert response.status_code == 200
    assert attempts["count"] == 3
    assert sleep_calls == [0.25, 0.5]
    await client.aclose()


@pytest.mark.asyncio
async def test_request_raises_non_retryable_http_error() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"errors": [{"message": "missing"}]})

    client = AsyncBaseClient(
        base_url="https://example.test",
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(NotFoundError):
        await client._request("GET", "/missing")

    await client.aclose()


@pytest.mark.asyncio
async def test_request_raises_after_max_retries() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"errors": [{"message": "still failing"}]})

    client = AsyncBaseClient(
        base_url="https://example.test",
        max_retries=1,
        retry_backoff_factor=0,
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(ServerError):
        await client._request("GET", "/always-fail")

    await client.aclose()
