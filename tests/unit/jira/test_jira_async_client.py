from __future__ import annotations

import json

import httpx
import pytest

from atlassian.core.auth import BasicAuth, TokenAuth
from atlassian.core.pagination import AsyncPageIterator
from atlassian.jira.async_client import AsyncJiraClient
from atlassian.jira.async_resources import AsyncIssueResource
from atlassian.jira.models import SearchRequestBean


def test_async_jira_client_builds_basic_auth() -> None:
    client = AsyncJiraClient(url="https://jira.example.com", username="u", password="p")

    assert isinstance(client.auth, BasicAuth)


def test_async_jira_client_builds_token_auth() -> None:
    client = AsyncJiraClient(url="https://jira.example.com", token="pat")

    assert isinstance(client.auth, TokenAuth)


def test_async_jira_client_rejects_invalid_auth_combination() -> None:
    with pytest.raises(ValueError):
        AsyncJiraClient(
            url="https://jira.example.com",
            token="pat",
            username="u",
            password="p",
        )


def test_jira_namespace_is_lazy_resource() -> None:
    client = AsyncJiraClient(url="https://jira.example.com")

    resource = client.issue

    assert isinstance(resource, AsyncIssueResource)
    assert resource is client.issue


def test_async_jira_client_normalizes_url_with_rest_suffix() -> None:
    client = AsyncJiraClient(url="https://jira.example.com")

    assert str(client._client.base_url) == "https://jira.example.com/rest/"


def test_async_jira_client_keeps_existing_rest_suffix() -> None:
    client = AsyncJiraClient(url="https://jira.example.com/rest")

    assert str(client._client.base_url) == "https://jira.example.com/rest/"


@pytest.mark.asyncio
async def test_jira_get_pagination_returns_items_and_uses_start_at() -> None:
    requests: list[httpx.Request] = []
    payloads = [
        {
            "issues": [{"id": "10001"}, {"id": "10002"}],
            "startAt": 0,
            "maxResults": 2,
            "total": 3,
        },
        {
            "issues": [{"id": "10003"}],
            "startAt": 2,
            "maxResults": 2,
            "total": 3,
        },
    ]
    call_index = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        payload = payloads[call_index["value"]]
        call_index["value"] += 1
        return httpx.Response(200, json=payload)

    client = AsyncJiraClient(url="https://jira.example.com", transport=httpx.MockTransport(handler))

    iterator = client.agile.get_issues_without_epic_1(max_results=2)
    assert isinstance(iterator, AsyncPageIterator)

    values = [item async for item in iterator]

    assert [item.id for item in values] == ["10001", "10002", "10003"]
    assert len(requests) == 2
    assert requests[0].method == "GET"
    assert requests[0].url.params["startAt"] == "0"
    assert requests[0].url.params["maxResults"] == "2"
    assert requests[1].url.params["startAt"] == "2"
    assert requests[1].url.params["maxResults"] == "2"

    await client.aclose()


@pytest.mark.asyncio
async def test_jira_post_pagination_uses_method_and_request_body() -> None:
    requests: list[httpx.Request] = []
    payloads = [
        {
            "issues": [{"id": "20001"}, {"id": "20002"}],
            "startAt": 0,
            "maxResults": 2,
            "total": 3,
        },
        {
            "issues": [{"id": "20003"}],
            "startAt": 2,
            "maxResults": 2,
            "total": 3,
        },
    ]
    call_index = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        payload = payloads[call_index["value"]]
        call_index["value"] += 1
        return httpx.Response(200, json=payload)

    client = AsyncJiraClient(url="https://jira.example.com", transport=httpx.MockTransport(handler))

    iterator = client.issue.search_using_search_request(SearchRequestBean(jql="project = DEMO"), max_results=2)
    assert isinstance(iterator, AsyncPageIterator)

    values = [item async for item in iterator]

    assert [item.id for item in values] == ["20001", "20002", "20003"]
    assert len(requests) == 2
    assert requests[0].method == "POST"
    assert requests[0].url.params["startAt"] == "0"
    assert requests[0].url.params["maxResults"] == "2"
    assert json.loads(requests[0].content.decode("utf-8"))["jql"] == "project = DEMO"

    await client.aclose()
