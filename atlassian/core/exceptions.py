from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


@dataclass(slots=True)
class AtlassianError(Exception):
    message: str
    status_code: int | None = None
    response: Any = None

    def __str__(self) -> str:
        if self.status_code is None:
            return self.message
        return f"{self.status_code}: {self.message}"


class HttpError(AtlassianError):
    pass


class AuthenticationError(AtlassianError):
    pass


class ForbiddenError(AtlassianError):
    pass


class NotFoundError(AtlassianError):
    pass


class ConflictError(AtlassianError):
    pass


class ServerError(AtlassianError):
    pass


class ValidationError(AtlassianError):
    pass


@dataclass(slots=True)
class RateLimitError(AtlassianError):
    retry_after: float | None = None


def _extract_message(response: httpx.Response) -> tuple[str, Any]:
    try:
        payload = response.json()
    except ValueError:
        payload = response.text

    if isinstance(payload, dict):
        errors = payload.get("errors")
        if isinstance(errors, list) and errors:
            first = errors[0]
            if isinstance(first, dict):
                message = first.get("message")
                if isinstance(message, str) and message:
                    return message, payload
        message = payload.get("message")
        if isinstance(message, str) and message:
            return message, payload

    if isinstance(payload, str) and payload:
        return payload, payload

    return f"HTTP {response.status_code} error", payload


def raise_for_status(response: httpx.Response) -> None:
    status_code = response.status_code
    if status_code < 400:
        return

    message, payload = _extract_message(response)

    if status_code == 401:
        raise AuthenticationError(message=message, status_code=status_code, response=payload)
    if status_code == 403:
        raise ForbiddenError(message=message, status_code=status_code, response=payload)
    if status_code == 404:
        raise NotFoundError(message=message, status_code=status_code, response=payload)
    if status_code == 409:
        raise ConflictError(message=message, status_code=status_code, response=payload)
    if status_code == 429:
        retry_after_raw = response.headers.get("Retry-After")
        retry_after = float(retry_after_raw) if retry_after_raw is not None else None
        raise RateLimitError(
            message=message,
            status_code=status_code,
            response=payload,
            retry_after=retry_after,
        )
    if status_code >= 500:
        raise ServerError(message=message, status_code=status_code, response=payload)
    if status_code == 422:
        raise ValidationError(message=message, status_code=status_code, response=payload)

    raise HttpError(message=message, status_code=status_code, response=payload)
