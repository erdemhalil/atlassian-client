from __future__ import annotations

import httpx

from atlassian.core.async_client import AsyncBaseClient
from atlassian.core.auth import AuthBase, BasicAuth, TokenAuth

from .async_resources import (
    AsyncAccessModeResource,
    AsyncAdminResource,
    AsyncAttachmentsResource,
    AsyncBackupRestoreResource,
    AsyncCategoryResource,
    AsyncChildContentResource,
    AsyncContentDescendantResource,
    AsyncContentLabelsResource,
    AsyncContentPropertyResource,
    AsyncContentResource,
    AsyncContentRestrictionsResource,
    AsyncGlobalColorSchemeResource,
    AsyncGlobalPermissionsResource,
    AsyncGroupResource,
    AsyncLabelResource,
    AsyncLongTaskResource,
    AsyncSearchResource,
    AsyncServerInfoResource,
    AsyncSpaceColorSchemeResource,
    AsyncSpaceLabelResource,
    AsyncSpacePermissionsResource,
    AsyncSpacePropertyResource,
    AsyncSpaceResource,
    AsyncUserResource,
    AsyncUserWatchResource,
    AsyncWebhooksResource,
)


class ConfluenceContentGroup(AsyncContentResource):
    def __init__(self, owner: AsyncConfluenceClient) -> None:
        super().__init__(owner)
        self._owner = owner

    @property
    def labels(self) -> AsyncContentLabelsResource:
        return self._owner.content_labels

    @property
    def props(self) -> AsyncContentPropertyResource:
        return self._owner.content_property

    @property
    def restrictions(self) -> AsyncContentRestrictionsResource:
        return self._owner.content_restrictions

    @property
    def descendant(self) -> AsyncContentDescendantResource:
        return self._owner.content_descendant

    @property
    def child(self) -> AsyncChildContentResource:
        return self._owner.child_content

    @property
    def children(self) -> AsyncChildContentResource:
        return self._owner.child_content

    @property
    def attachments(self) -> AsyncAttachmentsResource:
        return self._owner.attachments


class ConfluenceSpaceGroup(AsyncSpaceResource):
    def __init__(self, owner: AsyncConfluenceClient) -> None:
        super().__init__(owner)
        self._owner = owner

    @property
    def labels(self) -> AsyncSpaceLabelResource:
        return self._owner.space_label

    @property
    def permissions(self) -> AsyncSpacePermissionsResource:
        return self._owner.space_permissions

    @property
    def props(self) -> AsyncSpacePropertyResource:
        return self._owner.space_property

    @property
    def color_scheme(self) -> AsyncSpaceColorSchemeResource:
        return self._owner.space_color_scheme

    @property
    def colors(self) -> AsyncSpaceColorSchemeResource:
        return self._owner.space_color_scheme


class AsyncConfluenceClient(AsyncBaseClient):
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

        self._content: ConfluenceContentGroup | None = None
        self._content_labels: AsyncContentLabelsResource | None = None
        self._content_property: AsyncContentPropertyResource | None = None
        self._content_restrictions: AsyncContentRestrictionsResource | None = None
        self._content_descendant: AsyncContentDescendantResource | None = None
        self._child_content: AsyncChildContentResource | None = None
        self._attachments: AsyncAttachmentsResource | None = None
        self._space: ConfluenceSpaceGroup | None = None
        self._space_label: AsyncSpaceLabelResource | None = None
        self._space_permissions: AsyncSpacePermissionsResource | None = None
        self._space_property: AsyncSpacePropertyResource | None = None
        self._space_color_scheme: AsyncSpaceColorSchemeResource | None = None
        self._group: AsyncGroupResource | None = None
        self._user: AsyncUserResource | None = None
        self._user_watch: AsyncUserWatchResource | None = None
        self._search: AsyncSearchResource | None = None
        self._label: AsyncLabelResource | None = None
        self._long_task: AsyncLongTaskResource | None = None
        self._backup_restore: AsyncBackupRestoreResource | None = None
        self._webhooks: AsyncWebhooksResource | None = None
        self._global_permissions: AsyncGlobalPermissionsResource | None = None
        self._global_color_scheme: AsyncGlobalColorSchemeResource | None = None
        self._category: AsyncCategoryResource | None = None
        self._access_mode: AsyncAccessModeResource | None = None
        self._server_info: AsyncServerInfoResource | None = None
        self._admin: AsyncAdminResource | None = None

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
    def content(self) -> ConfluenceContentGroup:
        if self._content is None:
            self._content = ConfluenceContentGroup(self)
        return self._content

    @property
    def content_labels(self) -> AsyncContentLabelsResource:
        if self._content_labels is None:
            self._content_labels = AsyncContentLabelsResource(self)
        return self._content_labels

    @property
    def content_property(self) -> AsyncContentPropertyResource:
        if self._content_property is None:
            self._content_property = AsyncContentPropertyResource(self)
        return self._content_property

    @property
    def content_restrictions(self) -> AsyncContentRestrictionsResource:
        if self._content_restrictions is None:
            self._content_restrictions = AsyncContentRestrictionsResource(self)
        return self._content_restrictions

    @property
    def content_descendant(self) -> AsyncContentDescendantResource:
        if self._content_descendant is None:
            self._content_descendant = AsyncContentDescendantResource(self)
        return self._content_descendant

    @property
    def child_content(self) -> AsyncChildContentResource:
        if self._child_content is None:
            self._child_content = AsyncChildContentResource(self)
        return self._child_content

    @property
    def attachments(self) -> AsyncAttachmentsResource:
        if self._attachments is None:
            self._attachments = AsyncAttachmentsResource(self)
        return self._attachments

    @property
    def space(self) -> ConfluenceSpaceGroup:
        if self._space is None:
            self._space = ConfluenceSpaceGroup(self)
        return self._space

    @property
    def space_label(self) -> AsyncSpaceLabelResource:
        if self._space_label is None:
            self._space_label = AsyncSpaceLabelResource(self)
        return self._space_label

    @property
    def space_permissions(self) -> AsyncSpacePermissionsResource:
        if self._space_permissions is None:
            self._space_permissions = AsyncSpacePermissionsResource(self)
        return self._space_permissions

    @property
    def space_property(self) -> AsyncSpacePropertyResource:
        if self._space_property is None:
            self._space_property = AsyncSpacePropertyResource(self)
        return self._space_property

    @property
    def space_color_scheme(self) -> AsyncSpaceColorSchemeResource:
        if self._space_color_scheme is None:
            self._space_color_scheme = AsyncSpaceColorSchemeResource(self)
        return self._space_color_scheme

    @property
    def group(self) -> AsyncGroupResource:
        if self._group is None:
            self._group = AsyncGroupResource(self)
        return self._group

    @property
    def user(self) -> AsyncUserResource:
        if self._user is None:
            self._user = AsyncUserResource(self)
        return self._user

    @property
    def user_watch(self) -> AsyncUserWatchResource:
        if self._user_watch is None:
            self._user_watch = AsyncUserWatchResource(self)
        return self._user_watch

    @property
    def search(self) -> AsyncSearchResource:
        if self._search is None:
            self._search = AsyncSearchResource(self)
        return self._search

    @property
    def label(self) -> AsyncLabelResource:
        if self._label is None:
            self._label = AsyncLabelResource(self)
        return self._label

    @property
    def long_task(self) -> AsyncLongTaskResource:
        if self._long_task is None:
            self._long_task = AsyncLongTaskResource(self)
        return self._long_task

    @property
    def tasks(self) -> AsyncLongTaskResource:
        return self.long_task

    @property
    def backup_restore(self) -> AsyncBackupRestoreResource:
        if self._backup_restore is None:
            self._backup_restore = AsyncBackupRestoreResource(self)
        return self._backup_restore

    @property
    def backup(self) -> AsyncBackupRestoreResource:
        return self.backup_restore

    @property
    def webhooks(self) -> AsyncWebhooksResource:
        if self._webhooks is None:
            self._webhooks = AsyncWebhooksResource(self)
        return self._webhooks

    @property
    def global_permissions(self) -> AsyncGlobalPermissionsResource:
        if self._global_permissions is None:
            self._global_permissions = AsyncGlobalPermissionsResource(self)
        return self._global_permissions

    @property
    def global_color_scheme(self) -> AsyncGlobalColorSchemeResource:
        if self._global_color_scheme is None:
            self._global_color_scheme = AsyncGlobalColorSchemeResource(self)
        return self._global_color_scheme

    @property
    def colors(self) -> AsyncGlobalColorSchemeResource:
        return self.global_color_scheme

    @property
    def category(self) -> AsyncCategoryResource:
        if self._category is None:
            self._category = AsyncCategoryResource(self)
        return self._category

    @property
    def access_mode(self) -> AsyncAccessModeResource:
        if self._access_mode is None:
            self._access_mode = AsyncAccessModeResource(self)
        return self._access_mode

    @property
    def server_info(self) -> AsyncServerInfoResource:
        if self._server_info is None:
            self._server_info = AsyncServerInfoResource(self)
        return self._server_info

    @property
    def info(self) -> AsyncServerInfoResource:
        return self.server_info

    @property
    def admin(self) -> AsyncAdminResource:
        if self._admin is None:
            self._admin = AsyncAdminResource(self)
        return self._admin
