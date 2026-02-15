from __future__ import annotations

from typing import Any, Literal, overload

from atlassian.core.pagination import AsyncPageIterator, Page
from atlassian.core.resource import AsyncResource

from .endpoints import PROJECTS_LIST


class AsyncProjectsResource(AsyncResource):
    @overload
    async def list(
        self,
        *,
        start: int = 0,
        limit: int = 25,
        paginate: Literal[True] = True,
    ) -> AsyncPageIterator[dict[str, Any]]: ...

    @overload
    async def list(
        self,
        *,
        start: int = 0,
        limit: int = 25,
        paginate: Literal[False],
    ) -> Page[dict[str, Any]]: ...

    async def list(
        self,
        *,
        start: int = 0,
        limit: int = 25,
        paginate: bool = True,
    ) -> AsyncPageIterator[dict[str, Any]] | Page[dict[str, Any]]:
        async def fetch_page(page_start: int) -> Page[dict[str, Any]]:
            page_model = Page[dict[str, Any]]
            return await self._get(
                PROJECTS_LIST.path,
                params={"start": page_start, "limit": limit},
                model=page_model,
            )

        if paginate:
            return AsyncPageIterator(fetch_page, start=start)
        return await fetch_page(start)


class AsyncRepositoriesResource(AsyncResource):
    pass


class AsyncPullRequestsResource(AsyncResource):
    pass


class AsyncAccessTokensResource(AsyncResource):
    pass


class AsyncSshKeysResource(AsyncResource):
    pass


class AsyncBuildsResource(AsyncResource):
    pass


class AsyncPermissionsResource(AsyncResource):
    pass


class AsyncSecurityResource(AsyncResource):
    pass


class AsyncAdminResource(AsyncResource):
    pass


class AsyncDashboardResource(AsyncResource):
    pass


class AsyncMirroringResource(AsyncResource):
    pass


class AsyncJiraIntegrationResource(AsyncResource):
    pass


class AsyncMarkupResource(AsyncResource):
    pass
