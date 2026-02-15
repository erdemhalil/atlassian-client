from __future__ import annotations

import httpx
import pytest

from atlassian.bitbucket.async_client import AsyncBitBucketClient
from atlassian.bitbucket.async_resources import AsyncProjectsResource
from atlassian.core.auth import BasicAuth, TokenAuth


def test_async_bitbucket_client_builds_basic_auth() -> None:
    client = AsyncBitBucketClient(url="https://bitbucket.example.com", username="u", password="p")

    assert isinstance(client.auth, BasicAuth)


def test_async_bitbucket_client_builds_token_auth() -> None:
    client = AsyncBitBucketClient(url="https://bitbucket.example.com", token="pat")

    assert isinstance(client.auth, TokenAuth)


def test_async_bitbucket_client_rejects_invalid_auth_combination() -> None:
    with pytest.raises(ValueError):
        AsyncBitBucketClient(
            url="https://bitbucket.example.com",
            token="pat",
            username="u",
            password="p",
        )


def test_projects_namespace_is_lazy_resource() -> None:
    client = AsyncBitBucketClient(url="https://bitbucket.example.com")

    resource = client.projects

    assert isinstance(resource, AsyncProjectsResource)
    assert resource is client.projects


@pytest.mark.asyncio
async def test_projects_get_projects_paged_returns_items() -> None:
    payloads = [
        {
            "values": [{"key": "A"}, {"key": "B"}],
            "start": 0,
            "limit": 2,
            "size": 2,
            "isLastPage": False,
            "nextPageStart": 2,
        },
        {
            "values": [{"key": "C"}],
            "start": 2,
            "limit": 2,
            "size": 1,
            "isLastPage": True,
        },
    ]
    calls = {"index": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        payload = payloads[calls["index"]]
        calls["index"] += 1
        return httpx.Response(200, json=payload)

    client = AsyncBitBucketClient(
        url="https://bitbucket.example.com",
        transport=httpx.MockTransport(handler),
    )

    iterator = client.projects.get_projects()
    values = [item async for item in iterator]

    assert [value.key for value in values] == ["A", "B", "C"]
    assert calls["index"] == 2
    await client.aclose()


def test_async_bitbucket_client_normalizes_url_with_rest_suffix() -> None:
    client = AsyncBitBucketClient(url="https://bitbucket.example.com")
    assert str(client._client.base_url) == "https://bitbucket.example.com/rest/"


def test_async_bitbucket_client_keeps_existing_rest_suffix() -> None:
    client = AsyncBitBucketClient(url="https://bitbucket.example.com/rest")
    assert str(client._client.base_url) == "https://bitbucket.example.com/rest/"
