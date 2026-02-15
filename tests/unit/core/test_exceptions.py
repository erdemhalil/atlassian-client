from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime

import httpx
import pytest

from atlassian.core.exceptions import (
    AuthenticationError,
    ConflictError,
    ForbiddenError,
    HttpError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_status,
)


def _response(
    status_code: int,
    body: dict | str,
    headers: dict[str, str] | None = None,
) -> httpx.Response:
    request = httpx.Request("GET", "https://example.test")
    if isinstance(body, dict):
        return httpx.Response(status_code, json=body, headers=headers, request=request)
    return httpx.Response(status_code, text=body, headers=headers, request=request)


@pytest.mark.parametrize(
    ("status_code", "exc_type"),
    [
        (401, AuthenticationError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, ValidationError),
        (500, ServerError),
        (418, HttpError),
    ],
)
def test_raise_for_status_maps_exceptions(status_code: int, exc_type: type[Exception]) -> None:
    response = _response(status_code, {"errors": [{"message": "boom"}]})

    with pytest.raises(exc_type, match="boom"):
        raise_for_status(response)


def test_raise_for_status_uses_retry_after_for_rate_limit() -> None:
    response = _response(
        429,
        {"errors": [{"message": "too many requests"}]},
        headers={"Retry-After": "3"},
    )

    with pytest.raises(RateLimitError) as exc_info:
        raise_for_status(response)

    assert exc_info.value.retry_after == 3.0


def test_raise_for_status_parses_retry_after_http_date() -> None:
    future = datetime(2099, 1, 1, tzinfo=timezone.utc)
    response = _response(
        429,
        {"errors": [{"message": "too many requests"}]},
        headers={"Retry-After": format_datetime(future, usegmt=True)},
    )

    with pytest.raises(RateLimitError) as exc_info:
        raise_for_status(response)

    assert exc_info.value.retry_after is not None
    assert exc_info.value.retry_after > 0


def test_raise_for_status_ignores_invalid_retry_after() -> None:
    response = _response(
        429,
        {"errors": [{"message": "too many requests"}]},
        headers={"Retry-After": "tomorrow"},
    )

    with pytest.raises(RateLimitError) as exc_info:
        raise_for_status(response)

    assert exc_info.value.retry_after is None


def test_raise_for_status_noop_for_success() -> None:
    response = _response(200, {"ok": True})

    raise_for_status(response)
