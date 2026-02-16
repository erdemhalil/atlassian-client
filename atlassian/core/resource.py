from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic import BaseModel

from .pagination import AsyncPageIterator, Page, PageIterator

if TYPE_CHECKING:
    from .async_client import AsyncBaseClient
    from .client import BaseClient

T = TypeVar("T", bound=BaseModel)


class AsyncResource:
    def __init__(self, client: AsyncBaseClient) -> None:
        self._client = client

    async def _get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request("GET", path, params=params, headers=headers)
        return self._deserialize(response, model)

    def _get_paged(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        model: type[T],
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[T]:
        """Return an async iterator that auto-paginates through all results."""
        page_model = Page[model]  # type: ignore[valid-type]

        async def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "start": page_start, "limit": limit}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = await self._client._request("GET", path, params=merged)
            page = page_model.model_validate(response.json())
            if page.is_last_page:
                return page.values, None
            next_start = (
                page.next_page_start
                if page.next_page_start is not None
                else page.start + page.limit
            )
            return page.values, next_start

        return AsyncPageIterator(fetch_page, start=start)

    async def _post(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request(
            "POST",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    async def _put(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request(
            "PUT",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    async def _delete(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request("DELETE", path, params=params, headers=headers)
        return self._deserialize(response, model)

    async def _patch(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request(
            "PATCH",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    @staticmethod
    def _deserialize(response: Any, model: type[BaseModel] | None) -> Any:
        if model is None:
            return response

        payload = response.json()
        return model.model_validate(payload)


class Resource:
    """Synchronous base class for resource namespaces."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client

    def _get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = self._client._request("GET", path, params=params, headers=headers)
        return self._deserialize(response, model)

    def _get_paged(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        model: type[T],
        start: int = 0,
        limit: int = 25,
    ) -> PageIterator[T]:
        """Return a sync iterator that auto-paginates through all results."""
        page_model = Page[model]  # type: ignore[valid-type]

        def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "start": page_start, "limit": limit}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = self._client._request("GET", path, params=merged)
            page = page_model.model_validate(response.json())
            if page.is_last_page:
                return page.values, None
            next_start = (
                page.next_page_start
                if page.next_page_start is not None
                else page.start + page.limit
            )
            return page.values, next_start

        return PageIterator(fetch_page, start=start)

    def _post(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = self._client._request(
            "POST",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    def _put(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = self._client._request(
            "PUT",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    def _delete(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = self._client._request("DELETE", path, params=params, headers=headers)
        return self._deserialize(response, model)

    def _patch(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = self._client._request(
            "PATCH",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    @staticmethod
    def _deserialize(response: Any, model: type[BaseModel] | None) -> Any:
        if model is None:
            return response

        payload = response.json()
        return model.model_validate(payload)
