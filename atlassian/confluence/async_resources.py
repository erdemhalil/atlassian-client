"""Confluence Data Center resource classes.

Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.
"""

from __future__ import annotations

from atlassian.confluence.resource import ConfluenceAsyncResource
from atlassian.core.pagination import AsyncPageIterator

from .endpoints import (
    ADD,
    ADD_CONTENT_WATCHER,
    ADD_LABELS,
    ADD_SPACE_WATCH,
    ARCHIVE,
    BY_OPERATION,
    CANCEL_ALL_QUEUED_JOBS,
    CANCEL_JOB,
    CHANGE_PASSWORD,
    CHANGE_PASSWORD_1,
    CHILDREN,
    CHILDREN_OF_TYPE,
    COMMENTS_OF_CONTENT,
    CONTENTS,
    CONTENTS_WITH_TYPE,
    CONTENTS_WITH_TYPE_1,
    CONVERT,
    CREATE,
    CREATE_1,
    CREATE_2,
    CREATE_3,
    CREATE_4,
    CREATE_ATTACHMENTS,
    CREATE_CONTENT,
    CREATE_PERSONAL_SPACE,
    CREATE_PERSONAL_SPACE_1,
    CREATE_PRIVATE_SPACE,
    CREATE_SITE_BACKUP_JOB,
    CREATE_SITE_RESTORE_JOB,
    CREATE_SITE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE,
    CREATE_SPACE,
    CREATE_SPACE_BACKUP_JOB,
    CREATE_SPACE_RESTORE_JOB,
    CREATE_SPACE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE,
    CREATE_USER,
    CREATE_WEBHOOK,
    DELETE,
    DELETE_1,
    DELETE_2,
    DELETE_3,
    DELETE_4,
    DELETE_5,
    DELETE_6,
    DELETE_CONTENT_HISTORY,
    DELETE_LABEL,
    DELETE_LABEL_WITH_QUERY_PARAM,
    DELETE_WEBHOOK,
    DESCENDANTS,
    DESCENDANTS_OF_TYPE,
    DISABLE,
    DOWNLOAD_BACKUP_FILE,
    ENABLE,
    FIND_ALL,
    FIND_BY_KEY,
    FIND_JOBS,
    FIND_WEBHOOKS,
    FOR_OPERATION,
    GET,
    GET_1,
    GET_ACCESS_MODE_STATUS,
    GET_ACTIVE_USERS,
    GET_ALL_GLOBAL_PERMISSIONS,
    GET_ALL_SPACE_PERMISSIONS,
    GET_ANONYMOUS,
    GET_ATTACHMENTS,
    GET_AUDIT_RECORDS,
    GET_CLUSTER_NODE_STATUSES,
    GET_COLOR_SCHEME_TYPE,
    GET_CONTENT,
    GET_CONTENT_BY_ID,
    GET_CURRENT,
    GET_DEFAULT_COLOR_SCHEME,
    GET_FILES,
    GET_GLOBAL_COLOR_SCHEME,
    GET_GROUP,
    GET_GROUPS,
    GET_GROUPS_1,
    GET_HISTORY,
    GET_JOB,
    GET_LATEST_INVOCATION,
    GET_MACRO_BODY_BY_HASH,
    GET_MACRO_BODY_BY_MACRO_ID,
    GET_MEMBERS,
    GET_NESTED_GROUP_MEMBERS,
    GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS,
    GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS_1,
    GET_PERMISSIONS_GRANTED_TO_GROUP,
    GET_PERMISSIONS_GRANTED_TO_GROUP_1,
    GET_PERMISSIONS_GRANTED_TO_UNLICENSED_USERS,
    GET_PERMISSIONS_GRANTED_TO_USER,
    GET_PERMISSIONS_GRANTED_TO_USER_1,
    GET_SPACE_COLOR_SCHEME,
    GET_STATISTICS,
    GET_STATISTICS_SUMMARY,
    GET_TASK,
    GET_TASKS,
    GET_USER,
    GET_USERS,
    GET_WEBHOOK,
    GRANT_PERMISSIONS_TO_ANONYMOUS_USERS,
    GRANT_PERMISSIONS_TO_ANONYMOUS_USERS_1,
    GRANT_PERMISSIONS_TO_GROUP,
    GRANT_PERMISSIONS_TO_GROUP_1,
    GRANT_PERMISSIONS_TO_UNLICENSED_USERS,
    GRANT_PERMISSIONS_TO_USER,
    GRANT_PERMISSIONS_TO_USER_1,
    INDEX,
    INDEX_1,
    INDEX_2,
    INDEX_3,
    INDEX_4,
    IS_WATCHING_CONTENT,
    IS_WATCHING_SPACE,
    LABELS,
    LABELS_1,
    MOVE,
    POPULAR,
    POPULAR_1,
    PUBLISH_LEGACY_DRAFT,
    PUBLISH_SHARED_DRAFT,
    RECENT,
    RECENT_1,
    RELATED,
    RELATED_1,
    RELEVANT_VIEW_RESTRICTIONS,
    REMOVE_ATTACHMENT,
    REMOVE_ATTACHMENT_VERSION,
    REMOVE_CATEGORY,
    REMOVE_CONTENT_WATCHER,
    REMOVE_SPACE_WATCH,
    RESET_GLOBAL_COLOR_SCHEME,
    RESET_SPACE_COLOR_SCHEME,
    RESTORE,
    REVOKE_PERMISSIONS_FROM_ANONYMOUS_USER,
    REVOKE_PERMISSIONS_FROM_ANONYMOUS_USERS,
    REVOKE_PERMISSIONS_FROM_GROUP,
    REVOKE_PERMISSIONS_FROM_GROUP_1,
    REVOKE_PERMISSIONS_FROM_UNLICENSED_USERS,
    REVOKE_PERMISSIONS_FROM_USER,
    REVOKE_PERMISSIONS_FROM_USER_1,
    SCAN_CONTENT,
    SEARCH,
    SEARCH_1,
    SET_PERMISSIONS,
    SET_PERMISSIONS_1,
    SPACE,
    SPACES,
    TEST_WEBHOOK,
    TRASH,
    UPDATE,
    UPDATE_1,
    UPDATE_2,
    UPDATE_3,
    UPDATE_4,
    UPDATE_5,
    UPDATE_COLOR_SCHEME,
    UPDATE_COLOR_SCHEME_TYPE,
    UPDATE_DATA,
    UPDATE_RESTRICTIONS,
    UPDATE_SPACE_COLOR_SCHEME,
    UPDATE_USER,
    UPDATE_USER_1,
    UPDATE_WEBHOOK,
)
from .models import (
    ColorSchemeThemeBasedModel,
    Content,
    ContentBody,
    ContentWatch,
    Credentials,
    DetailedInvocation,
    ExampleMultipartFormData,
    FileInfo,
    GlobalPermission,
    Group,
    History,
    InstanceMetrics,
    JobDetails,
    JsonContentProperty,
    JsonSpaceProperty,
    Label,
    LongTaskStatus,
    LongTaskSubmission,
    MacroInstance,
    MockAttachmentRequest,
    MockRestrictionsResponse,
    NodeStatus,
    OperationRestriction,
    PasswordChangeDetails,
    Person,
    PersonalSpaceDetailsForCreation,
    RestInvocationHistory,
    RestWebhook,
    SearchResult,
    ServerInformation,
    SiteBackupJobDetails,
    SiteBackupSettings,
    SiteRestoreJobDetails,
    SiteRestoreSettings,
    Space,
    SpaceBackupJobDetails,
    SpaceBackupSettings,
    SpaceColorSchemeTypeModel,
    SpacePermission,
    SpaceRestoreJobDetails,
    SpaceRestoreSettings,
    SpaceWatch,
    User,
    UserDetailsForCreation,
    UserDetailsForUpdate,
    UserKey,
    Webhook,
)


class AsyncContentResource(ConfluenceAsyncResource):
    def get_content(
        self,
        *,
        space_key: str | None = None,
        expand: str | None = None,
        posting_day: str | None = None,
        ids: str | None = None,
        title: str | None = None,
        type_: str | None = None,
        status: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get content"""
        return self._get_paged(
            GET_CONTENT.path,
            params={
                "spaceKey": space_key,
                "expand": expand,
                "postingDay": posting_day,
                "ids": ids,
                "title": title,
                "type": type_,
                "status": status,
            },
            model=Content,
            start=start,
            limit=limit,
        )

    async def create_content(self, body: Content, *, expand: str | None = None, status: str | None = None) -> Content:
        """Create content"""
        return await self._post(
            CREATE_CONTENT.path,
            params={"expand": expand, "status": status},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def publish_legacy_draft(
        self,
        draft_id: str,
        body: Content,
        *,
        expand: str | None = None,
        status: str | None = None,
    ) -> Content:
        """Publish legacy draft"""
        return await self._post(
            PUBLISH_LEGACY_DRAFT.path.replace("{draftId}", str(draft_id)),
            params={"expand": expand, "status": status},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def publish_shared_draft(
        self,
        draft_id: str,
        body: Content,
        *,
        expand: str | None = None,
        status: str | None = None,
    ) -> Content:
        """Publish shared draft"""
        return await self._put(
            PUBLISH_SHARED_DRAFT.path.replace("{draftId}", str(draft_id)),
            params={"expand": expand, "status": status},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def scan_content(
        self,
        *,
        cursor: str | None = None,
        space_key: str | None = None,
        expand: str | None = None,
        limit: str | None = None,
        type_: str | None = None,
        status: str | None = None,
    ) -> None:
        """Scan content by space key"""
        return await self._get(
            SCAN_CONTENT.path,
            params={
                "cursor": cursor,
                "spaceKey": space_key,
                "expand": expand,
                "limit": limit,
                "type": type_,
                "status": status,
            },
        )

    def search(
        self,
        *,
        cqlcontext: str | None = None,
        expand: str | None = None,
        cql: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Search content using CQL"""
        return self._get_paged(
            SEARCH.path,
            params={"cqlcontext": cqlcontext, "expand": expand, "cql": cql},
            model=Content,
            start=start,
            limit=limit,
        )

    async def update_2(
        self,
        content_id: str,
        body: Content,
        *,
        async_reconciliation: bool | None = False,
        conflict_policy: str | None = None,
        status: str | None = None,
    ) -> Content:
        """Update content"""
        return await self._put(
            UPDATE_2.path.replace("{contentId}", str(content_id)),
            params={"asyncReconciliation": async_reconciliation, "conflictPolicy": conflict_policy, "status": status},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    def index(self, content_id: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[User]:
        """Fetch users watching a given content"""
        return self._get_paged(INDEX.path.replace("{contentId}", str(content_id)), model=User, start=start, limit=limit)

    async def delete_3(self, id: str, *, status: str | None = None) -> None:
        """Delete content"""
        return await self._delete(DELETE_3.path.replace("{id}", str(id)), params={"status": status})

    async def get_content_by_id(
        self,
        id: str,
        *,
        expand: str | None = None,
        version: str | None = None,
        status: str | None = None,
    ) -> Content:
        """Get content by ID"""
        return await self._get(
            GET_CONTENT_BY_ID.path.replace("{id}", str(id)),
            params={"expand": expand, "version": version, "status": status},
            model=Content,
        )

    async def get_history(self, id: str, *, expand: str | None = None) -> History:
        """Get history of content"""
        return await self._get(GET_HISTORY.path.replace("{id}", str(id)), params={"expand": expand}, model=History)

    async def get_macro_body_by_hash(self, id: str, version: str, hash: str) -> MacroInstance:
        """Get macro body by hash"""
        return await self._get(
            GET_MACRO_BODY_BY_HASH.path.replace("{id}", str(id))
            .replace("{version}", str(version))
            .replace("{hash}", str(hash)),
            model=MacroInstance,
        )

    async def get_macro_body_by_macro_id(self, macro_id: str, id: str, version: str) -> MacroInstance:
        """Get macro body by macro ID"""
        return await self._get(
            GET_MACRO_BODY_BY_MACRO_ID.path.replace("{macroId}", str(macro_id))
            .replace("{id}", str(id))
            .replace("{version}", str(version)),
            model=MacroInstance,
        )

    async def delete_content_history(self, id: str, version_number: str) -> None:
        """Delete content history"""
        return await self._delete(
            DELETE_CONTENT_HISTORY.path.replace("{id}", str(id)).replace("{versionNumber}", str(version_number)),
        )

    async def convert(self, to: str, body: ContentBody, *, expand: str | None = None) -> ContentBody:
        """Convert body representation"""
        return await self._post(
            CONVERT.path.replace("{to}", str(to)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ContentBody,
        )


class AsyncContentLabelsResource(ConfluenceAsyncResource):
    async def delete_label_with_query_param(self, id: str, *, name: str | None = None) -> None:
        """Delete label with query param"""
        return await self._delete(DELETE_LABEL_WITH_QUERY_PARAM.path.replace("{id}", str(id)), params={"name": name})

    def labels(
        self,
        id: str,
        *,
        prefix: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Label]:
        """Get labels"""
        return self._get_paged(
            LABELS.path.replace("{id}", str(id)),
            params={"prefix": prefix},
            model=Label,
            start=start,
            limit=limit,
        )

    def add_labels(self, id: str, body: Label, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Add Labels"""
        return self._request_paged(
            "POST",
            ADD_LABELS.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Label,
            start=start,
            limit=limit,
        )

    async def delete_label(self, id: str, label: str) -> None:
        """Delete label"""
        return await self._delete(DELETE_LABEL.path.replace("{id}", str(id)).replace("{label}", str(label)))


class AsyncContentPropertyResource(ConfluenceAsyncResource):
    def find_all(
        self,
        id: str,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[JsonContentProperty]:
        """Find all content properties"""
        return self._get_paged(
            FIND_ALL.path.replace("{id}", str(id)),
            params={"expand": expand},
            model=JsonContentProperty,
            start=start,
            limit=limit,
        )

    async def create_1(self, id: str, body: JsonContentProperty) -> JsonContentProperty:
        """Create a content property"""
        return await self._post(
            CREATE_1.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=JsonContentProperty,
        )

    async def delete_2(self, id: str, key: str) -> None:
        """Delete content property"""
        return await self._delete(DELETE_2.path.replace("{id}", str(id)).replace("{key}", str(key)))

    async def find_by_key(
        self,
        id: str,
        key: str,
        *,
        expand: str | None = None,
        limit: str | None = None,
    ) -> JsonContentProperty:
        """Find content property by key"""
        return await self._get(
            FIND_BY_KEY.path.replace("{id}", str(id)).replace("{key}", str(key)),
            params={"expand": expand, "limit": limit},
            model=JsonContentProperty,
        )

    async def create_2(self, id: str, key: str, body: JsonContentProperty) -> None:
        """POST /rest/api/content/{id}/property/{key}"""
        return await self._post(
            CREATE_2.path.replace("{id}", str(id)).replace("{key}", str(key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def update_1(
        self,
        id: str,
        key: str,
        body: JsonContentProperty,
        *,
        expand: str | None = None,
    ) -> JsonContentProperty:
        """Update content property"""
        return await self._put(
            UPDATE_1.path.replace("{id}", str(id)).replace("{key}", str(key)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=JsonContentProperty,
        )


class AsyncContentRestrictionsResource(ConfluenceAsyncResource):
    def update_restrictions(
        self,
        id: str,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[OperationRestriction]:
        """Update restrictions"""
        return self._request_paged(
            "PUT",
            UPDATE_RESTRICTIONS.path.replace("{id}", str(id)),
            params={"expand": expand},
            model=OperationRestriction,
            start=start,
            limit=limit,
        )

    async def by_operation(self, id: str, *, expand: str | None = None) -> MockRestrictionsResponse:
        """Get all restrictions by Operation"""
        return await self._get(
            BY_OPERATION.path.replace("{id}", str(id)),
            params={"expand": expand},
            model=MockRestrictionsResponse,
        )

    async def for_operation(
        self,
        operation_key: str,
        id: str,
        *,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
    ) -> OperationRestriction:
        """Get all restrictions for given operation"""
        return await self._get(
            FOR_OPERATION.path.replace("{operationKey}", str(operation_key)).replace("{id}", str(id)),
            params={"expand": expand, "limit": limit, "start": start},
            model=OperationRestriction,
        )

    async def relevant_view_restrictions(
        self,
        id: str,
        *,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
    ) -> MockRestrictionsResponse:
        """Get all view restriction both direct and inherited."""
        return await self._get(
            RELEVANT_VIEW_RESTRICTIONS.path.replace("{id}", str(id)),
            params={"expand": expand, "limit": limit, "start": start},
            model=MockRestrictionsResponse,
        )


class AsyncContentDescendantResource(ConfluenceAsyncResource):
    def descendants(
        self,
        id: str,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get Descendants"""
        return self._get_paged(
            DESCENDANTS.path.replace("{id}", str(id)),
            params={"expand": expand},
            model=Content,
            start=start,
            limit=limit,
        )

    def descendants_of_type(
        self,
        id: str,
        type_: str,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get descendants of type"""
        return self._get_paged(
            DESCENDANTS_OF_TYPE.path.replace("{id}", str(id)).replace("{type}", str(type_)),
            params={"expand": expand},
            model=Content,
            start=start,
            limit=limit,
        )


class AsyncChildContentResource(ConfluenceAsyncResource):
    def children(
        self,
        id: str,
        *,
        expand: str | None = None,
        parent_version: int | None = 0,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get children of content"""
        return self._get_paged(
            CHILDREN.path.replace("{id}", str(id)),
            params={"expand": expand, "parentVersion": parent_version},
            model=Content,
            start=start,
            limit=limit,
        )

    def comments_of_content(
        self,
        id: str,
        *,
        expand: str | None = None,
        depth: str | None = None,
        location: str | None = None,
        parent_version: int | None = 0,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get comments of content"""
        return self._get_paged(
            COMMENTS_OF_CONTENT.path.replace("{id}", str(id)),
            params={"expand": expand, "depth": depth, "location": location, "parentVersion": parent_version},
            model=Content,
            start=start,
            limit=limit,
        )

    def children_of_type(
        self,
        id: str,
        type_: str,
        *,
        expand: str | None = None,
        parent_version: int | None = 0,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get children of content by type"""
        return self._get_paged(
            CHILDREN_OF_TYPE.path.replace("{id}", str(id)).replace("{type}", str(type_)),
            params={"expand": expand, "parentVersion": parent_version},
            model=Content,
            start=start,
            limit=limit,
        )


class AsyncAttachmentsResource(ConfluenceAsyncResource):
    def get_attachments(
        self,
        id: str,
        *,
        expand: str | None = None,
        filename: str | None = None,
        media_type: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get attachment"""
        return self._get_paged(
            GET_ATTACHMENTS.path.replace("{id}", str(id)),
            params={"expand": expand, "filename": filename, "mediaType": media_type},
            model=Content,
            start=start,
            limit=limit,
        )

    async def create_attachments(
        self,
        id: str,
        body: MockAttachmentRequest,
        *,
        expand: str | None = None,
        allow_duplicated: str | None = None,
        status: str | None = None,
    ) -> Content:
        """Create attachments"""
        return await self._post(
            CREATE_ATTACHMENTS.path.replace("{id}", str(id)),
            params={"expand": expand, "allowDuplicated": allow_duplicated, "status": status},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def remove_attachment(self, attachment_id: str, id: str) -> None:
        """Remove attachment"""
        return await self._delete(
            REMOVE_ATTACHMENT.path.replace("{attachmentId}", str(attachment_id)).replace("{id}", str(id)),
        )

    async def update(self, attachment_id: str, id: str, body: Content) -> Content:
        """Update non-binary data of an Attachment"""
        return await self._put(
            UPDATE.path.replace("{attachmentId}", str(attachment_id)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def update_data(self, attachment_id: str, id: str, body: MockAttachmentRequest) -> Content:
        """Update binary data of an attachment"""
        return await self._post(
            UPDATE_DATA.path.replace("{attachmentId}", str(attachment_id)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Content,
        )

    async def move(
        self,
        attachment_id: str,
        id: str,
        *,
        new_name: str | None = None,
        new_content_id: str | None = None,
    ) -> None:
        """Move attachment"""
        return await self._post(
            MOVE.path.replace("{attachmentId}", str(attachment_id)).replace("{id}", str(id)),
            params={"newName": new_name, "newContentId": new_content_id},
        )

    async def remove_attachment_version(self, attachment_id: str, id: str, version: int) -> None:
        """Remove attachment version"""
        return await self._delete(
            REMOVE_ATTACHMENT_VERSION.path.replace("{attachmentId}", str(attachment_id))
            .replace("{id}", str(id))
            .replace("{version}", str(version)),
        )


class AsyncSpaceResource(ConfluenceAsyncResource):
    def spaces(
        self,
        *,
        space_key_single: str | None = None,
        label: str | None = None,
        favourite: str | None = None,
        type_: str | None = None,
        space_key: str | None = None,
        space_id: list[str] | None = None,
        expand: str | None = None,
        has_retention_policy: str | None = None,
        space_keys: str | None = None,
        content_label: str | None = None,
        space_ids: str | None = None,
        status: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Space]:
        """Get spaces by key"""
        return self._get_paged(
            SPACES.path,
            params={
                "spaceKeySingle": space_key_single,
                "label": label,
                "favourite": favourite,
                "type": type_,
                "spaceKey": space_key,
                "spaceId": space_id,
                "expand": expand,
                "hasRetentionPolicy": has_retention_policy,
                "spaceKeys": space_keys,
                "contentLabel": content_label,
                "spaceIds": space_ids,
                "status": status,
            },
            model=Space,
            start=start,
            limit=limit,
        )

    async def create_space(self, body: Space) -> Space:
        """Creates a new Space."""
        return await self._post(CREATE_SPACE.path, json=body.model_dump(by_alias=True, exclude_none=True), model=Space)

    async def create_private_space(self, body: Space) -> Space:
        """Create private space"""
        return await self._post(
            CREATE_PRIVATE_SPACE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Space,
        )

    async def create_personal_space_1(self, body: PersonalSpaceDetailsForCreation) -> Space:
        """Creates the personal Space for self."""
        return await self._post(
            CREATE_PERSONAL_SPACE_1.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Space,
        )

    async def delete_5(self, space_key: str) -> LongTaskSubmission:
        """Delete Space"""
        return await self._delete(DELETE_5.path.replace("{spaceKey}", str(space_key)), model=LongTaskSubmission)

    async def space(self, space_key: str, *, expand: str | None = None) -> Space:
        """Get space"""
        return await self._get(SPACE.path.replace("{spaceKey}", str(space_key)), params={"expand": expand}, model=Space)

    async def update_4(self, space_key: str, body: Space) -> Space:
        """Update Space"""
        return await self._put(
            UPDATE_4.path.replace("{spaceKey}", str(space_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Space,
        )

    async def archive(self, space_key: str) -> None:
        """Archive space"""
        return await self._put(ARCHIVE.path.replace("{spaceKey}", str(space_key)))

    def contents(
        self,
        space_key: str,
        *,
        expand: str | None = None,
        depth: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get contents in space"""
        return self._get_paged(
            CONTENTS.path.replace("{spaceKey}", str(space_key)),
            params={"expand": expand, "depth": depth},
            model=Content,
            start=start,
            limit=limit,
        )

    def contents_with_type_1(
        self,
        space_key: str,
        type_: str,
        *,
        expand: str | None = None,
        depth: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Content]:
        """Get contents by type"""
        return self._get_paged(
            CONTENTS_WITH_TYPE_1.path.replace("{spaceKey}", str(space_key)).replace("{type}", str(type_)),
            params={"expand": expand, "depth": depth},
            model=Content,
            start=start,
            limit=limit,
        )

    async def restore(self, space_key: str) -> None:
        """Restore space"""
        return await self._put(RESTORE.path.replace("{spaceKey}", str(space_key)))

    async def trash(self, space_key: str) -> None:
        """Remove all trash contents"""
        return await self._delete(TRASH.path.replace("{spaceKey}", str(space_key)))

    async def contents_with_type(
        self,
        space_key: str,
        *,
        cursor: str | None = None,
        expand: str | None = None,
        limit: str | None = None,
    ) -> None:
        """Get trash contents of space"""
        return await self._get(
            CONTENTS_WITH_TYPE.path.replace("{spaceKey}", str(space_key)),
            params={"cursor": cursor, "expand": expand, "limit": limit},
        )

    def index_4(self, space_key: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[User]:
        """Fetch users watching space"""
        return self._get_paged(INDEX_4.path.replace("{spaceKey}", str(space_key)), model=User, start=start, limit=limit)


class AsyncSpaceLabelResource(ConfluenceAsyncResource):
    def index_3(self, space_key: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Fetch all labels"""
        return self._get_paged(
            INDEX_3.path.replace("{spaceKey}", str(space_key)),
            model=Label,
            start=start,
            limit=limit,
        )

    def popular_1(self, space_key: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Get popular labels"""
        return self._get_paged(
            POPULAR_1.path.replace("{spaceKey}", str(space_key)),
            model=Label,
            start=start,
            limit=limit,
        )

    def recent_1(self, space_key: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Get recent labels"""
        return self._get_paged(
            RECENT_1.path.replace("{spaceKey}", str(space_key)),
            model=Label,
            start=start,
            limit=limit,
        )

    def related_1(
        self,
        space_key: str,
        label_name: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Label]:
        """Get related labels"""
        return self._get_paged(
            RELATED_1.path.replace("{spaceKey}", str(space_key)).replace("{labelName}", str(label_name)),
            model=Label,
            start=start,
            limit=limit,
        )


class AsyncSpacePermissionsResource(ConfluenceAsyncResource):
    async def get_all_space_permissions(self, space_key: str) -> SpacePermission:
        """Get all space permissions"""
        return await self._get(
            GET_ALL_SPACE_PERMISSIONS.path.replace("{spaceKey}", str(space_key)),
            model=SpacePermission,
        )

    async def set_permissions_1(self, space_key: str) -> None:
        """Set permissions to multiple users/groups/anonymous user in the given space"""
        return await self._post(SET_PERMISSIONS_1.path.replace("{spaceKey}", str(space_key)))

    async def get_permissions_granted_to_anonymous_users_1(self, space_key: str) -> SpacePermission:
        """Gets the permissions granted to an anonymous user in a space"""
        return await self._get(
            GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS_1.path.replace("{spaceKey}", str(space_key)),
            model=SpacePermission,
        )

    async def grant_permissions_to_anonymous_users_1(self, space_key: str) -> None:
        """Grants space permissions to anonymous user"""
        return await self._put(GRANT_PERMISSIONS_TO_ANONYMOUS_USERS_1.path.replace("{spaceKey}", str(space_key)))

    async def revoke_permissions_from_anonymous_user(self, space_key: str) -> None:
        """Revoke space permissions from anonymous user"""
        return await self._put(REVOKE_PERMISSIONS_FROM_ANONYMOUS_USER.path.replace("{spaceKey}", str(space_key)))

    async def get_permissions_granted_to_group_1(self, space_key: str, group_name: str) -> SpacePermission:
        """Gets the permissions granted to a group in a space"""
        return await self._get(
            GET_PERMISSIONS_GRANTED_TO_GROUP_1.path.replace("{spaceKey}", str(space_key)).replace(
                "{groupName}", str(group_name)
            ),
            model=SpacePermission,
        )

    async def grant_permissions_to_group_1(self, space_key: str, group_name: str) -> None:
        """Grants space permissions to a group"""
        return await self._put(
            GRANT_PERMISSIONS_TO_GROUP_1.path.replace("{spaceKey}", str(space_key)).replace(
                "{groupName}", str(group_name)
            ),
        )

    async def revoke_permissions_from_group_1(self, space_key: str, group_name: str) -> None:
        """Revoke space permissions from a group"""
        return await self._put(
            REVOKE_PERMISSIONS_FROM_GROUP_1.path.replace("{spaceKey}", str(space_key)).replace(
                "{groupName}", str(group_name)
            ),
        )

    async def get_permissions_granted_to_user_1(self, space_key: str, user_key: str) -> SpacePermission:
        """Gets the permissions granted to a user in a space"""
        return await self._get(
            GET_PERMISSIONS_GRANTED_TO_USER_1.path.replace("{spaceKey}", str(space_key)).replace(
                "{userKey}", str(user_key)
            ),
            model=SpacePermission,
        )

    async def grant_permissions_to_user_1(self, space_key: str, user_key: str) -> None:
        """Grants space permissions to a user"""
        return await self._put(
            GRANT_PERMISSIONS_TO_USER_1.path.replace("{spaceKey}", str(space_key)).replace("{userKey}", str(user_key)),
        )

    async def revoke_permissions_from_user_1(self, space_key: str, user_key: str) -> None:
        """Revoke space permissions from a user"""
        return await self._put(
            REVOKE_PERMISSIONS_FROM_USER_1.path.replace("{spaceKey}", str(space_key)).replace(
                "{userKey}", str(user_key)
            ),
        )


class AsyncSpacePropertyResource(ConfluenceAsyncResource):
    def get_1(
        self,
        space_key: str,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[JsonSpaceProperty]:
        """Get space properties"""
        return self._get_paged(
            GET_1.path.replace("{spaceKey}", str(space_key)),
            params={"expand": expand},
            model=JsonSpaceProperty,
            start=start,
            limit=limit,
        )

    async def create_3(self, space_key: str, body: JsonSpaceProperty) -> JsonSpaceProperty:
        """Create a space property"""
        return await self._post(
            CREATE_3.path.replace("{spaceKey}", str(space_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=JsonSpaceProperty,
        )

    async def delete_4(self, space_key: str, key: str) -> None:
        """Delete space property"""
        return await self._delete(DELETE_4.path.replace("{spaceKey}", str(space_key)).replace("{key}", str(key)))

    async def get(
        self,
        space_key: str,
        key: str,
        *,
        expand: str | None = None,
        limit: str | None = None,
        start: str | None = None,
    ) -> JsonSpaceProperty:
        """Get space property by key"""
        return await self._get(
            GET.path.replace("{spaceKey}", str(space_key)).replace("{key}", str(key)),
            params={"expand": expand, "limit": limit, "start": start},
            model=JsonSpaceProperty,
        )

    async def create_4(self, space_key: str, key: str, body: JsonSpaceProperty) -> JsonSpaceProperty:
        """Create a space property with a specific key"""
        return await self._post(
            CREATE_4.path.replace("{spaceKey}", str(space_key)).replace("{key}", str(key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=JsonSpaceProperty,
        )

    async def update_3(self, space_key: str, key: str, body: JsonSpaceProperty) -> JsonSpaceProperty:
        """Update space property"""
        return await self._put(
            UPDATE_3.path.replace("{spaceKey}", str(space_key)).replace("{key}", str(key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=JsonSpaceProperty,
        )


class AsyncSpaceColorSchemeResource(ConfluenceAsyncResource):
    async def get_space_color_scheme(self, space_key: str) -> ColorSchemeThemeBasedModel:
        """Get Space color scheme"""
        return await self._get(
            GET_SPACE_COLOR_SCHEME.path.replace("{spaceKey}", str(space_key)),
            model=ColorSchemeThemeBasedModel,
        )

    async def update_space_color_scheme(
        self,
        space_key: str,
        body: ColorSchemeThemeBasedModel,
    ) -> ColorSchemeThemeBasedModel:
        """Update Space color scheme"""
        return await self._put(
            UPDATE_SPACE_COLOR_SCHEME.path.replace("{spaceKey}", str(space_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ColorSchemeThemeBasedModel,
        )

    async def reset_space_color_scheme(self, space_key: str) -> ColorSchemeThemeBasedModel:
        """Reset Space color scheme"""
        return await self._put(
            RESET_SPACE_COLOR_SCHEME.path.replace("{spaceKey}", str(space_key)),
            model=ColorSchemeThemeBasedModel,
        )

    async def get_color_scheme_type(self, space_key: str) -> SpaceColorSchemeTypeModel:
        """Get Space color scheme type"""
        return await self._get(
            GET_COLOR_SCHEME_TYPE.path.replace("{spaceKey}", str(space_key)),
            model=SpaceColorSchemeTypeModel,
        )

    async def update_color_scheme_type(
        self,
        space_key: str,
        body: SpaceColorSchemeTypeModel,
    ) -> SpaceColorSchemeTypeModel:
        """Update Space color scheme type"""
        return await self._put(
            UPDATE_COLOR_SCHEME_TYPE.path.replace("{spaceKey}", str(space_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SpaceColorSchemeTypeModel,
        )


class AsyncGroupResource(ConfluenceAsyncResource):
    def get_groups(self, *, expand: str | None = "", start: int = 0, limit: int = 25) -> AsyncPageIterator[Group]:
        """Get groups"""
        return self._get_paged(GET_GROUPS.path, params={"expand": expand}, model=Group, start=start, limit=limit)

    async def get_group(self, group_name: str, *, expand: str | None = None) -> Group:
        """Get group by name"""
        return await self._get(
            GET_GROUP.path.replace("{groupName}", str(group_name)),
            params={"expand": expand},
            model=Group,
        )

    def get_nested_group_members(
        self,
        group_name: Group,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Group]:
        """Get group members of group"""
        return self._get_paged(
            GET_NESTED_GROUP_MEMBERS.path.replace("{groupName}", str(group_name)),
            params={"expand": expand},
            model=Group,
            start=start,
            limit=limit,
        )

    def get_members(
        self,
        group_name: Group,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Person]:
        """Get members of group"""
        return self._get_paged(
            GET_MEMBERS.path.replace("{groupName}", str(group_name)),
            params={"expand": expand},
            model=Person,
            start=start,
            limit=limit,
        )

    async def delete_6(self, group_name: str, username: str) -> None:
        """Delete user group"""
        return await self._delete(
            DELETE_6.path.replace("{groupName}", str(group_name)).replace("{username}", str(username)),
        )

    async def update_5(self, group_name: str, username: str) -> None:
        """Update user group"""
        return await self._put(
            UPDATE_5.path.replace("{groupName}", str(group_name)).replace("{username}", str(username)),
        )


class AsyncUserResource(ConfluenceAsyncResource):
    async def get_user(
        self,
        *,
        expand: str | None = None,
        key: str | None = None,
        username: str | None = None,
    ) -> Person:
        """Get user"""
        return await self._get(GET_USER.path, params={"expand": expand, "key": key, "username": username}, model=Person)

    async def get_anonymous(self, *, expand: str | None = None) -> Person:
        """Get information about anonymous user type"""
        return await self._get(GET_ANONYMOUS.path, params={"expand": expand}, model=Person)

    async def get_current(self, *, expand: str | None = None) -> Person:
        """Get current user"""
        return await self._get(GET_CURRENT.path, params={"expand": expand}, model=Person)

    async def update_user_1(self, body: UserDetailsForUpdate) -> None:
        """Update details of the current user"""
        return await self._put(UPDATE_USER_1.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def change_password_1(self, body: PasswordChangeDetails) -> None:
        """Change password"""
        return await self._post(CHANGE_PASSWORD_1.path, json=body.model_dump(by_alias=True, exclude_none=True))

    def get_users(self, *, expand: str | None = None, start: int = 0, limit: int = 25) -> AsyncPageIterator[Person]:
        """Get registered users"""
        return self._get_paged(GET_USERS.path, params={"expand": expand}, model=Person, start=start, limit=limit)

    def get_groups_1(
        self,
        *,
        expand: str | None = None,
        key: str | None = None,
        username: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Person]:
        """Get groups"""
        return self._get_paged(
            GET_GROUPS_1.path,
            params={"expand": expand, "key": key, "username": username},
            model=Person,
            start=start,
            limit=limit,
        )


class AsyncUserWatchResource(ConfluenceAsyncResource):
    async def remove_content_watcher(
        self,
        content_id: str,
        *,
        key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Remove content watcher"""
        return await self._delete(
            REMOVE_CONTENT_WATCHER.path.replace("{contentId}", str(content_id)),
            params={"key": key, "username": username},
        )

    async def is_watching_content(
        self,
        content_id: str,
        *,
        key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Get information about content watcher"""
        return await self._get(
            IS_WATCHING_CONTENT.path.replace("{contentId}", str(content_id)),
            params={"key": key, "username": username},
        )

    async def add_content_watcher(
        self,
        content_id: str,
        *,
        key: str | None = None,
        username: str | None = None,
    ) -> ContentWatch:
        """Add content watcher"""
        return await self._post(
            ADD_CONTENT_WATCHER.path.replace("{contentId}", str(content_id)),
            params={"key": key, "username": username},
            model=ContentWatch,
        )

    async def remove_space_watch(
        self,
        space_key: str,
        *,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Remove space watcher"""
        return await self._delete(
            REMOVE_SPACE_WATCH.path.replace("{spaceKey}", str(space_key)),
            params={"contentType": content_type, "key": key, "username": username},
        )

    async def is_watching_space(
        self,
        space_key: str,
        *,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Get information about space watcher"""
        return await self._get(
            IS_WATCHING_SPACE.path.replace("{spaceKey}", str(space_key)),
            params={"contentType": content_type, "key": key, "username": username},
        )

    async def add_space_watch(
        self,
        space_key: str,
        *,
        content_type: str | None = None,
        key: str | None = None,
        username: str | None = None,
    ) -> SpaceWatch:
        """Add space watcher"""
        return await self._post(
            ADD_SPACE_WATCH.path.replace("{spaceKey}", str(space_key)),
            params={"contentType": content_type, "key": key, "username": username},
            model=SpaceWatch,
        )


class AsyncSearchResource(ConfluenceAsyncResource):
    def search_1(
        self,
        *,
        cqlcontext: str | None = None,
        expand: str | None = None,
        include_archived_spaces: str | None = None,
        excerpt: str | None = None,
        cql: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[SearchResult]:
        """Search for entities in confluence"""
        return self._get_paged(
            SEARCH_1.path,
            params={
                "cqlcontext": cqlcontext,
                "expand": expand,
                "includeArchivedSpaces": include_archived_spaces,
                "excerpt": excerpt,
                "cql": cql,
            },
            model=SearchResult,
            start=start,
            limit=limit,
        )


class AsyncLabelResource(ConfluenceAsyncResource):
    def labels_1(
        self,
        *,
        space_key: str | None = None,
        owner: str | None = None,
        namespace: str | None = None,
        label_name: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Label]:
        """Get list of labels matching the given label name, namespace, space (via space key) or owner."""
        return self._get_paged(
            LABELS_1.path,
            params={"spaceKey": space_key, "owner": owner, "namespace": namespace, "labelName": label_name},
            model=Label,
            start=start,
            limit=limit,
        )

    def popular(self, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Get most popular labels"""
        return self._get_paged(POPULAR.path, model=Label, start=start, limit=limit)

    def recent(self, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Get recently used labels"""
        return self._get_paged(RECENT.path, model=Label, start=start, limit=limit)

    def related(self, label_name: str, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[Label]:
        """Get related labels."""
        return self._get_paged(
            RELATED.path.replace("{labelName}", str(label_name)),
            model=Label,
            start=start,
            limit=limit,
        )


class AsyncLongTaskResource(ConfluenceAsyncResource):
    def get_tasks(
        self,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[LongTaskStatus]:
        """Get tasks"""
        return self._get_paged(
            GET_TASKS.path,
            params={"expand": expand},
            model=LongTaskStatus,
            start=start,
            limit=limit,
        )

    async def get_task(self, id: str, *, expand: str | None = None) -> LongTaskStatus:
        """Get task by ID"""
        return await self._get(GET_TASK.path.replace("{id}", str(id)), params={"expand": expand}, model=LongTaskStatus)


class AsyncBackupRestoreResource(ConfluenceAsyncResource):
    async def create_site_backup_job(self, body: SiteBackupSettings) -> SiteBackupJobDetails:
        """Create site backup job"""
        return await self._post(
            CREATE_SITE_BACKUP_JOB.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SiteBackupJobDetails,
        )

    async def create_space_backup_job(self, body: SpaceBackupSettings) -> SpaceBackupJobDetails:
        """Create space backup job"""
        return await self._post(
            CREATE_SPACE_BACKUP_JOB.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SpaceBackupJobDetails,
        )

    async def find_jobs(
        self,
        *,
        owner: str | None = None,
        space_key: str | None = None,
        from_date: str | None = None,
        job_states: str | None = None,
        to_date: str | None = None,
        job_operation: str | None = None,
        limit: str | None = None,
        job_scope: str | None = None,
    ) -> JobDetails:
        """Find jobs by filters"""
        return await self._get(
            FIND_JOBS.path,
            params={
                "owner": owner,
                "spaceKey": space_key,
                "fromDate": from_date,
                "jobStates": job_states,
                "toDate": to_date,
                "jobOperation": job_operation,
                "limit": limit,
                "jobScope": job_scope,
            },
            model=JobDetails,
        )

    async def cancel_all_queued_jobs(self) -> None:
        """Cancel all queued jobs"""
        return await self._put(CANCEL_ALL_QUEUED_JOBS.path)

    async def get_job(self, job_id: str) -> JobDetails:
        """Get job by ID"""
        return await self._get(GET_JOB.path.replace("{jobId}", str(job_id)), model=JobDetails)

    async def cancel_job(self, job_id: str) -> JobDetails:
        """Cancel job"""
        return await self._put(CANCEL_JOB.path.replace("{jobId}", str(job_id)), model=JobDetails)

    async def download_backup_file(self, job_id: str) -> JobDetails:
        """Download backup file"""
        return await self._get(DOWNLOAD_BACKUP_FILE.path.replace("{jobId}", str(job_id)), model=JobDetails)

    async def get_files(self, *, job_scope: str | None = None) -> FileInfo:
        """Get files in restore directory"""
        return await self._get(GET_FILES.path, params={"jobScope": job_scope}, model=FileInfo)

    async def create_site_restore_job(self, body: SiteRestoreSettings) -> SiteRestoreJobDetails:
        """Create site restore job"""
        return await self._post(
            CREATE_SITE_RESTORE_JOB.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SiteRestoreJobDetails,
        )

    async def create_site_restore_job_for_uploaded_backup_file(
        self,
        body: ExampleMultipartFormData,
    ) -> SiteRestoreJobDetails:
        """Create site restore job for upload backup file"""
        return await self._post(
            CREATE_SITE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SiteRestoreJobDetails,
        )

    async def create_space_restore_job(self, body: SpaceRestoreSettings) -> SpaceRestoreJobDetails:
        """Create space restore job"""
        return await self._post(
            CREATE_SPACE_RESTORE_JOB.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SpaceRestoreJobDetails,
        )

    async def create_space_restore_job_for_uploaded_backup_file(
        self,
        body: ExampleMultipartFormData,
    ) -> SpaceRestoreJobDetails:
        """Create space restore job for upload backup file"""
        return await self._post(
            CREATE_SPACE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SpaceRestoreJobDetails,
        )


class AsyncWebhooksResource(ConfluenceAsyncResource):
    def find_webhooks(
        self,
        *,
        event: str | None = None,
        statistics: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestWebhook]:
        """Find webhooks"""
        return self._get_paged(
            FIND_WEBHOOKS.path,
            params={"event": event, "statistics": statistics},
            model=RestWebhook,
            start=start,
            limit=limit,
        )

    async def create_webhook(self, body: RestWebhook) -> Webhook:
        """Create webhook"""
        return await self._post(
            CREATE_WEBHOOK.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Webhook,
        )

    async def test_webhook(self, *, url: str) -> None:
        """Test webhook"""
        return await self._post(TEST_WEBHOOK.path, params={"url": url})

    async def delete_webhook(self, webhook_id: str) -> None:
        """Delete webhook"""
        return await self._delete(DELETE_WEBHOOK.path.replace("{webhookId}", str(webhook_id)))

    async def get_webhook(self, webhook_id: str, *, statistics: bool | None = False) -> RestWebhook:
        """Get webhook"""
        return await self._get(
            GET_WEBHOOK.path.replace("{webhookId}", str(webhook_id)),
            params={"statistics": statistics},
            model=RestWebhook,
        )

    async def update_webhook(self, webhook_id: str, body: RestWebhook) -> RestWebhook:
        """Update webhook"""
        return await self._put(
            UPDATE_WEBHOOK.path.replace("{webhookId}", str(webhook_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhook,
        )

    async def get_latest_invocation(
        self,
        webhook_id: str,
        *,
        outcomes: str | None = None,
        event: str | None = None,
        outcome: list[str] | None = None,
    ) -> DetailedInvocation:
        """Get latest invocations"""
        return await self._get(
            GET_LATEST_INVOCATION.path.replace("{webhookId}", str(webhook_id)),
            params={"outcomes": outcomes, "event": event, "outcome": outcome},
            model=DetailedInvocation,
        )

    async def get_statistics(self, webhook_id: str, *, event: str | None = None) -> RestInvocationHistory:
        """Get statistic"""
        return await self._get(
            GET_STATISTICS.path.replace("{webhookId}", str(webhook_id)),
            params={"event": event},
            model=RestInvocationHistory,
        )

    async def get_statistics_summary(self, webhook_id: str) -> RestInvocationHistory:
        """Get statistics summary"""
        return await self._get(
            GET_STATISTICS_SUMMARY.path.replace("{webhookId}", str(webhook_id)),
            model=RestInvocationHistory,
        )


class AsyncGlobalPermissionsResource(ConfluenceAsyncResource):
    async def get_all_global_permissions(self) -> GlobalPermission:
        """Get global permissions"""
        return await self._get(GET_ALL_GLOBAL_PERMISSIONS.path, model=GlobalPermission)

    async def set_permissions(self) -> None:
        """Set global permissions to multiple users/groups"""
        return await self._put(SET_PERMISSIONS.path)

    async def get_permissions_granted_to_anonymous_users(self) -> GlobalPermission:
        """Gets the permissions granted to an anonymous user"""
        return await self._get(GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS.path, model=GlobalPermission)

    async def grant_permissions_to_anonymous_users(self) -> None:
        """Grants global permissions to anonymous users"""
        return await self._put(GRANT_PERMISSIONS_TO_ANONYMOUS_USERS.path)

    async def revoke_permissions_from_anonymous_users(self) -> None:
        """Revoke global permissions from anonymous users"""
        return await self._put(REVOKE_PERMISSIONS_FROM_ANONYMOUS_USERS.path)

    async def get_permissions_granted_to_group(self, group_name: str) -> GlobalPermission:
        """Gets global permissions granted to a group"""
        return await self._get(
            GET_PERMISSIONS_GRANTED_TO_GROUP.path.replace("{groupName}", str(group_name)),
            model=GlobalPermission,
        )

    async def grant_permissions_to_group(self, group_name: str) -> None:
        """Grants global permissions to a group"""
        return await self._put(GRANT_PERMISSIONS_TO_GROUP.path.replace("{groupName}", str(group_name)))

    async def revoke_permissions_from_group(self, group_name: str) -> None:
        """Revoke global permissions from a group"""
        return await self._put(REVOKE_PERMISSIONS_FROM_GROUP.path.replace("{groupName}", str(group_name)))

    async def get_permissions_granted_to_unlicensed_users(self) -> GlobalPermission:
        """Gets the permissions granted to an unlicensed users"""
        return await self._get(GET_PERMISSIONS_GRANTED_TO_UNLICENSED_USERS.path, model=GlobalPermission)

    async def grant_permissions_to_unlicensed_users(self) -> None:
        """Grants global permissions to unlicensed users"""
        return await self._put(GRANT_PERMISSIONS_TO_UNLICENSED_USERS.path)

    async def revoke_permissions_from_unlicensed_users(self) -> None:
        """Revoke global permissions from unlicensed users"""
        return await self._put(REVOKE_PERMISSIONS_FROM_UNLICENSED_USERS.path)

    async def get_permissions_granted_to_user(self, user: str) -> GlobalPermission:
        """Gets global permissions granted to a user"""
        return await self._get(
            GET_PERMISSIONS_GRANTED_TO_USER.path.replace("{user}", str(user)),
            model=GlobalPermission,
        )

    async def grant_permissions_to_user(self, user: str) -> None:
        """Grants global permissions to a user"""
        return await self._put(GRANT_PERMISSIONS_TO_USER.path.replace("{user}", str(user)))

    async def revoke_permissions_from_user(self, user: str) -> None:
        """Revoke global permissions from a user"""
        return await self._put(REVOKE_PERMISSIONS_FROM_USER.path.replace("{user}", str(user)))


class AsyncGlobalColorSchemeResource(ConfluenceAsyncResource):
    async def get_global_color_scheme(self) -> ColorSchemeThemeBasedModel:
        """Get global color scheme"""
        return await self._get(GET_GLOBAL_COLOR_SCHEME.path, model=ColorSchemeThemeBasedModel)

    async def update_color_scheme(self, body: ColorSchemeThemeBasedModel) -> ColorSchemeThemeBasedModel:
        """Set global color scheme"""
        return await self._put(
            UPDATE_COLOR_SCHEME.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ColorSchemeThemeBasedModel,
        )

    async def get_default_color_scheme(self) -> ColorSchemeThemeBasedModel:
        """Get default global color scheme"""
        return await self._get(GET_DEFAULT_COLOR_SCHEME.path, model=ColorSchemeThemeBasedModel)

    async def reset_global_color_scheme(self) -> ColorSchemeThemeBasedModel:
        """Reset global color scheme"""
        return await self._put(RESET_GLOBAL_COLOR_SCHEME.path, model=ColorSchemeThemeBasedModel)


class AsyncCategoryResource(ConfluenceAsyncResource):
    async def remove_category(self, space_key: str, category_name: str) -> None:
        """Remove a category from a space"""
        return await self._delete(
            REMOVE_CATEGORY.path.replace("{spaceKey}", str(space_key)).replace("{categoryName}", str(category_name)),
        )

    async def add(self, space_key: str, label_name: str) -> None:
        """Add a category to a space"""
        return await self._post(ADD.path.replace("{spaceKey}", str(space_key)).replace("{labelName}", str(label_name)))


class AsyncAccessModeResource(ConfluenceAsyncResource):
    async def get_access_mode_status(self) -> None:
        """Get access mode status"""
        return await self._get(GET_ACCESS_MODE_STATUS.path)


class AsyncServerInfoResource(ConfluenceAsyncResource):
    async def index_1(self) -> InstanceMetrics:
        """Get instance metrics"""
        return await self._get(INDEX_1.path, model=InstanceMetrics)

    async def index_2(self) -> ServerInformation:
        """Get server information"""
        return await self._get(INDEX_2.path, model=ServerInformation)


class AsyncAdminResource(ConfluenceAsyncResource):
    async def create(self, body: Group) -> Group:
        """Create group"""
        return await self._post(CREATE.path, json=body.model_dump(by_alias=True, exclude_none=True), model=Group)

    async def delete(self, group_name: str) -> None:
        """Delete group"""
        return await self._delete(DELETE.path.replace("{groupName}", str(group_name)))

    async def create_personal_space(self, username: str, body: PersonalSpaceDetailsForCreation) -> Space:
        """Creates personal Space for a User."""
        return await self._post(
            CREATE_PERSONAL_SPACE.path.replace("{username}", str(username)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Space,
        )

    async def create_user(self, body: UserDetailsForCreation) -> UserKey:
        """Create user"""
        return await self._post(CREATE_USER.path, json=body.model_dump(by_alias=True, exclude_none=True), model=UserKey)

    async def delete_1(self, username: str) -> LongTaskSubmission:
        """Delete user"""
        return await self._delete(DELETE_1.path.replace("{username}", str(username)), model=LongTaskSubmission)

    async def update_user(self, username: str, body: UserDetailsForUpdate) -> None:
        """Update user"""
        return await self._put(
            UPDATE_USER.path.replace("{username}", str(username)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def disable(self, username: str) -> None:
        """Disable user"""
        return await self._put(DISABLE.path.replace("{username}", str(username)))

    async def enable(self, username: str) -> None:
        """Enable user"""
        return await self._put(ENABLE.path.replace("{username}", str(username)))

    async def change_password(self, username: str, body: Credentials) -> None:
        """Change password"""
        return await self._post(
            CHANGE_PASSWORD.path.replace("{username}", str(username)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    def get_active_users(
        self,
        *,
        expand: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[Person]:
        """Get active users"""
        return self._get_paged(GET_ACTIVE_USERS.path, params={"expand": expand}, model=Person, start=start, limit=limit)

    async def get_audit_records(self) -> None:
        """GET /rest/api/audit"""
        return await self._get(GET_AUDIT_RECORDS.path)

    def get_cluster_node_statuses(self, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[NodeStatus]:
        """Get node statuses in a cluster"""
        return self._get_paged(GET_CLUSTER_NODE_STATUSES.path, model=NodeStatus, start=start, limit=limit)
