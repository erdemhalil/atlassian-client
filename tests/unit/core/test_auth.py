from __future__ import annotations

import base64

import httpx

from atlassian.core.auth import BasicAuth, TokenAuth


def test_basic_auth_sets_authorization_header() -> None:
    request = httpx.Request("GET", "https://example.test")

    auth = BasicAuth(username="alice", password="secret")
    updated = auth.apply(request)

    expected_token = base64.b64encode(b"alice:secret").decode("ascii")
    assert updated.headers["Authorization"] == f"Basic {expected_token}"


def test_token_auth_sets_bearer_header() -> None:
    request = httpx.Request("GET", "https://example.test")

    auth = TokenAuth(token="pat-123")
    updated = auth.apply(request)

    assert updated.headers["Authorization"] == "Bearer pat-123"
