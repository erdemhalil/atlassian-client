from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic import BaseModel

from atlassian.core.pagination import AsyncPageIterator, PageIterator
from atlassian.core.resource import AsyncResource, Resource

if TYPE_CHECKING:
    from atlassian.core.async_client import AsyncBaseClient
    from atlassian.core.client import BaseClient

T = TypeVar("T", bound=BaseModel)


class AsyncJiraResource(AsyncResource):
    """Async base resource with Jira-style pagination."""

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
        items_field: str = "values",
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> AsyncPageIterator[T]:
        resolved_start = start_at if start_at is not None else start
        resolved_max = max_results if max_results is not None else limit
        return self._request_paged(
            "GET",
            path,
            params=params,
            model=model,
            items_field=items_field,
            start_at=resolved_start,
            max_results=resolved_max,
        )

    def _request_paged(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        model: type[T],
        items_field: str,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[T]:
        async def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "startAt": page_start, "maxResults": max_results}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = await self._client._request(method, path, params=merged, json=json)
            payload = response.json()

            raw_items = payload.get(items_field) or []
            items = [model.model_validate(item) for item in raw_items]

            if payload.get("isLast") is True or payload.get("isLastPage") is True:
                return items, None

            page_max = payload.get("maxResults")
            current_max = page_max if isinstance(page_max, int) and page_max > 0 else max_results

            next_start = page_start + current_max

            total = payload.get("total")
            if isinstance(total, int):
                if next_start >= total:
                    return items, None
                return items, next_start

            if len(items) < current_max:
                return items, None

            return items, next_start

        return AsyncPageIterator(fetch_page, start=start_at)


class JiraResource(Resource):
    """Sync base resource with Jira-style pagination."""

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
        items_field: str = "values",
        start_at: int | None = None,
        max_results: int | None = None,
    ) -> PageIterator[T]:
        resolved_start = start_at if start_at is not None else start
        resolved_max = max_results if max_results is not None else limit
        return self._request_paged(
            "GET",
            path,
            params=params,
            model=model,
            items_field=items_field,
            start_at=resolved_start,
            max_results=resolved_max,
        )

    def _request_paged(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        model: type[T],
        items_field: str,
        start_at: int = 0,
        max_results: int = 50,
    ) -> PageIterator[T]:
        def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            merged: dict[str, Any] = {**(params or {}), "startAt": page_start, "maxResults": max_results}
            merged = {k: v for k, v in merged.items() if v is not None}
            response = self._client._request(method, path, params=merged, json=json)
            payload = response.json()

            raw_items = payload.get(items_field) or []
            items = [model.model_validate(item) for item in raw_items]

            if payload.get("isLast") is True or payload.get("isLastPage") is True:
                return items, None

            page_max = payload.get("maxResults")
            current_max = page_max if isinstance(page_max, int) and page_max > 0 else max_results

            next_start = page_start + current_max

            total = payload.get("total")
            if isinstance(total, int):
                if next_start >= total:
                    return items, None
                return items, next_start

            if len(items) < current_max:
                return items, None

            return items, next_start

        return PageIterator(fetch_page, start=start_at)
