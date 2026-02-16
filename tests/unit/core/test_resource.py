from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx
import pytest
from pydantic import BaseModel

from atlassian.core.async_client import AsyncBaseClient
from atlassian.core.resource import AsyncResource


class _Payload(BaseModel):
    name: str


class _TestResource(AsyncResource):
    pass


class _FakeClient(AsyncBaseClient):
    def __init__(self, response: httpx.Response) -> None:
        self._response = response
        self.calls: list[tuple[str, str, Mapping[str, Any] | None, Any, Any, Mapping[str, str] | None]] = []

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        self.calls.append((method, path, params, json, data, headers))
        return self._response


@pytest.mark.asyncio
async def test_resource_get_deserializes_model() -> None:
    response = httpx.Response(200, json={"name": "demo"})
    client = _FakeClient(response)
    resource = _TestResource(client)

    result = await resource._get("/x", model=_Payload)

    assert isinstance(result, _Payload)
    assert result.name == "demo"
    assert client.calls[0][0] == "GET"


@pytest.mark.asyncio
async def test_resource_post_returns_response_without_model() -> None:
    response = httpx.Response(201, json={"name": "demo"})
    client = _FakeClient(response)
    resource = _TestResource(client)

    result = await resource._post("/x", json={"name": "demo"})

    assert result is response
    assert client.calls[0][0] == "POST"
