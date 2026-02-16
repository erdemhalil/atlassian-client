from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic import BaseModel

from atlassian.core.pagination import AsyncPageIterator, PageIterator
from atlassian.core.resource import AsyncResource, Resource

from .pagination import ConfluencePage

if TYPE_CHECKING:
    from atlassian.core.async_client import AsyncBaseClient
    from atlassian.core.client import BaseClient

T = TypeVar("T", bound=BaseModel)


class ConfluenceAsyncResource(AsyncResource):
    """Async base resource with Confluence-style pagination."""

    def __init__(self, client: AsyncBaseClient) -> None:
        super().__init__(client)

    def _get_paged(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        model: type[T],
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[T]:
        page_model = ConfluencePage[model]  # type: ignore[valid-type]

        async def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "start": page_start, "limit": limit}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = await self._client._request("GET", path, params=merged)
            page = page_model.model_validate(response.json())
            if not page.has_next:
                return page.results, None
            return page.results, page.start + page.limit

        return AsyncPageIterator(fetch_page, start=start)


class ConfluenceResource(Resource):
    """Sync base resource with Confluence-style pagination."""

    def __init__(self, client: BaseClient) -> None:
        super().__init__(client)

    def _get_paged(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        model: type[T],
        start: int = 0,
        limit: int = 25,
    ) -> PageIterator[T]:
        page_model = ConfluencePage[model]  # type: ignore[valid-type]

        def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "start": page_start, "limit": limit}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = self._client._request("GET", path, params=merged)
            page = page_model.model_validate(response.json())
            if not page.has_next:
                return page.results, None
            return page.results, page.start + page.limit

        return PageIterator(fetch_page, start=start)
