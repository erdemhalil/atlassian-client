from __future__ import annotations

import httpx

from atlassian.core.async_client import AsyncBaseClient
from atlassian.core.auth import AuthBase, BasicAuth, TokenAuth

from .async_resources import (
    AsyncAccessTokensResource,
    AsyncAdminResource,
    AsyncBuildsResource,
    AsyncDashboardResource,
    AsyncJiraIntegrationResource,
    AsyncMarkupResource,
    AsyncMirroringResource,
    AsyncPermissionsResource,
    AsyncProjectsResource,
    AsyncPullRequestsResource,
    AsyncRepositoriesResource,
    AsyncSecurityResource,
    AsyncSshKeysResource,
)


class AsyncBitBucketClient(AsyncBaseClient):
    def __init__(
        self,
        *,
        url: str,
        username: str | None = None,
        password: str | None = None,
        token: str | None = None,
        auth: AuthBase | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
        verify_ssl: bool = True,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        resolved_auth = self._resolve_auth(
            username=username,
            password=password,
            token=token,
            auth=auth,
        )

        super().__init__(
            base_url=url,
            auth=resolved_auth,
            timeout=timeout,
            max_retries=max_retries,
            retry_backoff_factor=retry_backoff_factor,
            verify_ssl=verify_ssl,
            transport=transport,
        )

        self._projects: AsyncProjectsResource | None = None
        self._repositories: AsyncRepositoriesResource | None = None
        self._pull_requests: AsyncPullRequestsResource | None = None
        self._access_tokens: AsyncAccessTokensResource | None = None
        self._ssh_keys: AsyncSshKeysResource | None = None
        self._builds: AsyncBuildsResource | None = None
        self._permissions: AsyncPermissionsResource | None = None
        self._security: AsyncSecurityResource | None = None
        self._admin: AsyncAdminResource | None = None
        self._dashboard: AsyncDashboardResource | None = None
        self._mirroring: AsyncMirroringResource | None = None
        self._jira_integration: AsyncJiraIntegrationResource | None = None
        self._markup: AsyncMarkupResource | None = None

    @staticmethod
    def _resolve_auth(
        *,
        username: str | None,
        password: str | None,
        token: str | None,
        auth: AuthBase | None,
    ) -> AuthBase | None:
        if auth is not None and any(value is not None for value in (username, password, token)):
            raise ValueError("Provide either auth or username/password/token, not both.")

        if token is not None and any(value is not None for value in (username, password)):
            raise ValueError("Token authentication cannot be combined with username/password.")

        if (username is None) != (password is None):
            raise ValueError("Both username and password must be provided together.")

        if auth is not None:
            return auth
        if token is not None:
            return TokenAuth(token)
        if username is not None and password is not None:
            return BasicAuth(username, password)
        return None

    @property
    def projects(self) -> AsyncProjectsResource:
        if self._projects is None:
            self._projects = AsyncProjectsResource(self)
        return self._projects

    @property
    def repositories(self) -> AsyncRepositoriesResource:
        if self._repositories is None:
            self._repositories = AsyncRepositoriesResource(self)
        return self._repositories

    @property
    def pull_requests(self) -> AsyncPullRequestsResource:
        if self._pull_requests is None:
            self._pull_requests = AsyncPullRequestsResource(self)
        return self._pull_requests

    @property
    def access_tokens(self) -> AsyncAccessTokensResource:
        if self._access_tokens is None:
            self._access_tokens = AsyncAccessTokensResource(self)
        return self._access_tokens

    @property
    def ssh_keys(self) -> AsyncSshKeysResource:
        if self._ssh_keys is None:
            self._ssh_keys = AsyncSshKeysResource(self)
        return self._ssh_keys

    @property
    def builds(self) -> AsyncBuildsResource:
        if self._builds is None:
            self._builds = AsyncBuildsResource(self)
        return self._builds

    @property
    def permissions(self) -> AsyncPermissionsResource:
        if self._permissions is None:
            self._permissions = AsyncPermissionsResource(self)
        return self._permissions

    @property
    def security(self) -> AsyncSecurityResource:
        if self._security is None:
            self._security = AsyncSecurityResource(self)
        return self._security

    @property
    def admin(self) -> AsyncAdminResource:
        if self._admin is None:
            self._admin = AsyncAdminResource(self)
        return self._admin

    @property
    def dashboard(self) -> AsyncDashboardResource:
        if self._dashboard is None:
            self._dashboard = AsyncDashboardResource(self)
        return self._dashboard

    @property
    def mirroring(self) -> AsyncMirroringResource:
        if self._mirroring is None:
            self._mirroring = AsyncMirroringResource(self)
        return self._mirroring

    @property
    def jira_integration(self) -> AsyncJiraIntegrationResource:
        if self._jira_integration is None:
            self._jira_integration = AsyncJiraIntegrationResource(self)
        return self._jira_integration

    @property
    def markup(self) -> AsyncMarkupResource:
        if self._markup is None:
            self._markup = AsyncMarkupResource(self)
        return self._markup
