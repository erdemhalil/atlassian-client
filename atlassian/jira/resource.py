from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from urllib.parse import parse_qsl, urlparse

from pydantic import BaseModel

from atlassian.core.pagination import AsyncPageIterator, PageIterator
from atlassian.core.resource import AsyncResource, Resource

if TYPE_CHECKING:
    from atlassian.core.async_client import AsyncBaseClient
    from atlassian.core.client import BaseClient

T = TypeVar("T", bound=BaseModel)


def _parse_next_target(next_link: str, *, base_path: str) -> tuple[str, dict[str, str]]:
    parsed = urlparse(next_link)
    target_path = parsed.path or next_link
    normalized_base = base_path.rstrip("/") or "/"
    if normalized_base != "/" and target_path.startswith(f"{normalized_base}/"):
        target_path = target_path[len(normalized_base) :]
    target_params = dict(parse_qsl(parsed.query, keep_blank_values=True))
    return target_path, target_params


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
        next_targets: dict[int, tuple[str, dict[str, str]]] = {}
        base_path = str(self._client._client.base_url.path)

        async def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            if page_start in next_targets:
                target_path, target_params = next_targets.pop(page_start)
                response = await self._client._request(method, target_path, params=target_params, json=json)
            else:
                merged: dict[str, Any] = {**(params or {}), "startAt": page_start, "maxResults": max_results}
                merged = {k: v for k, v in merged.items() if v is not None}
                response = await self._client._request(method, path, params=merged, json=json)
            payload = response.json()

            raw_items = payload.get(items_field) or []
            items = [model.model_validate(item) for item in raw_items]

            if payload.get("isLast") is True or payload.get("isLastPage") is True:
                return items, None

            next_link = payload.get("nextPage") or payload.get("next")
            if isinstance(next_link, str) and next_link:
                target_path, target_params = _parse_next_target(next_link, base_path=base_path)
                token = page_start + 1
                while token in next_targets:
                    token += 1
                next_targets[token] = (target_path, target_params)
                return items, token

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
        next_targets: dict[int, tuple[str, dict[str, str]]] = {}
        base_path = str(self._client._client.base_url.path)

        def fetch_page(page_start: int) -> tuple[list[T], int | None]:
            if page_start in next_targets:
                target_path, target_params = next_targets.pop(page_start)
                response = self._client._request(method, target_path, params=target_params, json=json)
            else:
                merged: dict[str, Any] = {**(params or {}), "startAt": page_start, "maxResults": max_results}
                merged = {k: v for k, v in merged.items() if v is not None}
                response = self._client._request(method, path, params=merged, json=json)
            payload = response.json()

            raw_items = payload.get(items_field) or []
            items = [model.model_validate(item) for item in raw_items]

            if payload.get("isLast") is True or payload.get("isLastPage") is True:
                return items, None

            next_link = payload.get("nextPage") or payload.get("next")
            if isinstance(next_link, str) and next_link:
                target_path, target_params = _parse_next_target(next_link, base_path=base_path)
                token = page_start + 1
                while token in next_targets:
                    token += 1
                next_targets[token] = (target_path, target_params)
                return items, token

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
