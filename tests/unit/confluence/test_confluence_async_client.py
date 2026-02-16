from __future__ import annotations

import httpx
import pytest

from atlassian.confluence.async_client import AsyncConfluenceClient
from atlassian.confluence.async_resources import (
    AsyncContentResource,
    AsyncSpaceResource,
)
from atlassian.confluence.models import Label
from atlassian.core.auth import BasicAuth, TokenAuth


def test_async_confluence_client_builds_basic_auth() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com", username="u", password="p")

    assert isinstance(client.auth, BasicAuth)


def test_async_confluence_client_builds_token_auth() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com", token="pat")

    assert isinstance(client.auth, TokenAuth)


def test_async_confluence_client_rejects_invalid_auth_combination() -> None:
    with pytest.raises(ValueError):
        AsyncConfluenceClient(
            url="https://confluence.example.com",
            token="pat",
            username="u",
            password="p",
        )


def test_async_confluence_client_normalizes_url_with_rest_suffix() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")
    assert str(client._client.base_url) == "https://confluence.example.com/rest/"


def test_async_confluence_client_keeps_existing_rest_suffix() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com/rest")
    assert str(client._client.base_url) == "https://confluence.example.com/rest/"


def test_content_namespace_is_lazy_resource() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")

    resource = client.content

    assert isinstance(resource, AsyncContentResource)
    assert resource is client.content


def test_space_namespace_is_lazy_resource() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")

    resource = client.space

    assert isinstance(resource, AsyncSpaceResource)
    assert resource is client.space


def test_content_umbrella_group_exposes_related_resources() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")

    assert client.content.labels is client.content_labels
    assert client.content.props is client.content_property
    assert client.content.restrictions is client.content_restrictions
    assert client.content.descendant is client.content_descendant
    assert client.content.child is client.child_content
    assert client.content.children is client.child_content
    assert client.content.attachments is client.attachments


def test_space_umbrella_group_exposes_related_resources() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")

    assert client.space.labels is client.space_label
    assert client.space.permissions is client.space_permissions
    assert client.space.props is client.space_property
    assert client.space.color_scheme is client.space_color_scheme
    assert client.space.colors is client.space_color_scheme


def test_short_aliases_map_to_existing_resources() -> None:
    client = AsyncConfluenceClient(url="https://confluence.example.com")

    assert client.colors is client.global_color_scheme
    assert client.info is client.server_info
    assert client.tasks is client.long_task
    assert client.backup is client.backup_restore


@pytest.mark.asyncio
async def test_content_get_content_paged_returns_items() -> None:
    payloads = [
        {
            "results": [
                {"id": "1", "title": "Page A"},
                {"id": "2", "title": "Page B"},
            ],
            "start": 0,
            "limit": 2,
            "size": 2,
            "_links": {"next": "/rest/api/content?start=2&limit=2"},
        },
        {
            "results": [{"id": "3", "title": "Page C"}],
            "start": 2,
            "limit": 2,
            "size": 1,
            "_links": {},
        },
    ]
    calls = {"index": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        payload = payloads[calls["index"]]
        calls["index"] += 1
        return httpx.Response(200, json=payload)

    client = AsyncConfluenceClient(
        url="https://confluence.example.com",
        transport=httpx.MockTransport(handler),
    )

    iterator = client.content.get_content()
    values = [item async for item in iterator]

    assert len(values) == 3
    assert calls["index"] == 2
    await client.aclose()


@pytest.mark.asyncio
async def test_confluence_pagination_stops_without_next_link() -> None:
    """A single page without _links.next should not trigger a second request."""
    payloads = [
        {
            "results": [{"id": "1", "title": "Only"}],
            "start": 0,
            "limit": 25,
            "size": 1,
            "_links": {},
        },
    ]
    calls = {"index": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        payload = payloads[calls["index"]]
        calls["index"] += 1
        return httpx.Response(200, json=payload)

    client = AsyncConfluenceClient(
        url="https://confluence.example.com",
        transport=httpx.MockTransport(handler),
    )

    iterator = client.content.get_content()
    values = [item async for item in iterator]

    assert len(values) == 1
    assert calls["index"] == 1
    await client.aclose()


@pytest.mark.asyncio
async def test_add_labels_uses_post_and_sends_body_for_paged_response() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "results": [{"name": "label", "prefix": "my"}],
                "start": 0,
                "limit": 25,
                "size": 1,
                "_links": {},
            },
        )

    client = AsyncConfluenceClient(
        url="https://confluence.example.com",
        transport=httpx.MockTransport(handler),
    )

    iterator = client.content_labels.add_labels("123", Label(prefix="my", name="label"))
    values = [item async for item in iterator]

    assert len(values) == 1
    assert requests
    assert requests[0].method == "POST"
    assert requests[0].url.params["start"] == "0"
    assert requests[0].url.params["limit"] == "25"
    assert requests[0].content.decode("utf-8") == '{"prefix":"my","name":"label"}'

    await client.aclose()
