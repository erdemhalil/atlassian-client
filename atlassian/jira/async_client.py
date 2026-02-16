from __future__ import annotations

import httpx

from atlassian.core.async_client import AsyncBaseClient
from atlassian.core.auth import AuthBase, BasicAuth, TokenAuth

from .async_resources import (
    AsyncAgileResource,
    AsyncAuthResource,
    AsyncAvatarResource,
    AsyncDashboardFilterResource,
    AsyncGroupResource,
    AsyncIssueMetaResource,
    AsyncIssueResource,
    AsyncOperationsResource,
    AsyncPermissionSecurityResource,
    AsyncProjectResource,
    AsyncSystemResource,
    AsyncUserResource,
)


class AsyncJiraClient(AsyncBaseClient):
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
        normalized_url = self._normalize_url(url)
        resolved_auth = self._resolve_auth(
            username=username,
            password=password,
            token=token,
            auth=auth,
        )

        super().__init__(
            base_url=normalized_url,
            auth=resolved_auth,
            timeout=timeout,
            max_retries=max_retries,
            retry_backoff_factor=retry_backoff_factor,
            verify_ssl=verify_ssl,
            transport=transport,
        )

        self._agile: AsyncAgileResource | None = None
        self._project: AsyncProjectResource | None = None
        self._issue: AsyncIssueResource | None = None
        self._issue_meta: AsyncIssueMetaResource | None = None
        self._permission_security: AsyncPermissionSecurityResource | None = None
        self._user: AsyncUserResource | None = None
        self._group: AsyncGroupResource | None = None
        self._avatar: AsyncAvatarResource | None = None
        self._dashboard_filter: AsyncDashboardFilterResource | None = None
        self._system: AsyncSystemResource | None = None
        self._operations: AsyncOperationsResource | None = None
        self._authentication: AsyncAuthResource | None = None

    @staticmethod
    def _normalize_url(url: str) -> str:
        stripped = url.rstrip("/")
        if stripped.endswith("/rest"):
            return stripped
        return f"{stripped}/rest"

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
    def agile(self) -> AsyncAgileResource:
        if self._agile is None:
            self._agile = AsyncAgileResource(self)
        return self._agile

    @property
    def project(self) -> AsyncProjectResource:
        if self._project is None:
            self._project = AsyncProjectResource(self)
        return self._project

    @property
    def issue(self) -> AsyncIssueResource:
        if self._issue is None:
            self._issue = AsyncIssueResource(self)
        return self._issue

    @property
    def issue_meta(self) -> AsyncIssueMetaResource:
        if self._issue_meta is None:
            self._issue_meta = AsyncIssueMetaResource(self)
        return self._issue_meta

    @property
    def permission_security(self) -> AsyncPermissionSecurityResource:
        if self._permission_security is None:
            self._permission_security = AsyncPermissionSecurityResource(self)
        return self._permission_security

    @property
    def user(self) -> AsyncUserResource:
        if self._user is None:
            self._user = AsyncUserResource(self)
        return self._user

    @property
    def group(self) -> AsyncGroupResource:
        if self._group is None:
            self._group = AsyncGroupResource(self)
        return self._group

    @property
    def avatar(self) -> AsyncAvatarResource:
        if self._avatar is None:
            self._avatar = AsyncAvatarResource(self)
        return self._avatar

    @property
    def dashboard_filter(self) -> AsyncDashboardFilterResource:
        if self._dashboard_filter is None:
            self._dashboard_filter = AsyncDashboardFilterResource(self)
        return self._dashboard_filter

    @property
    def system(self) -> AsyncSystemResource:
        if self._system is None:
            self._system = AsyncSystemResource(self)
        return self._system

    @property
    def operations(self) -> AsyncOperationsResource:
        if self._operations is None:
            self._operations = AsyncOperationsResource(self)
        return self._operations

    @property
    def authentication(self) -> AsyncAuthResource:
        if self._authentication is None:
            self._authentication = AsyncAuthResource(self)
        return self._authentication
