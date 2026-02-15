from __future__ import annotations

import asyncio
from collections.abc import Mapping
from typing import Any

import httpx

from .auth import AuthBase
from .exceptions import raise_for_status


class AsyncBaseClient:
    def __init__(
        self,
        *,
        base_url: str,
        auth: AuthBase | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
        verify_ssl: bool = True,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.auth = auth
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            verify=verify_ssl,
            transport=transport,
        )

    async def __aenter__(self) -> AsyncBaseClient:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._client.aclose()

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
        for attempt in range(self.max_retries + 1):
            request = self._client.build_request(
                method,
                path,
                params=params,
                json=json,
                data=data,
                headers=headers,
            )
            if self.auth is not None:
                request = await self.auth.apply(request)

            response = await self._client.send(request)
            if not self._is_retryable(response.status_code):
                break

            if attempt >= self.max_retries:
                break

            backoff = self.retry_backoff_factor * (2**attempt)
            await asyncio.sleep(backoff)

        raise_for_status(response)
        return response

    @staticmethod
    def _is_retryable(status_code: int) -> bool:
        return status_code == 429 or status_code >= 500
