"""Jira Data Center resource classes.

Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.
"""

from __future__ import annotations

from atlassian.core.pagination import AsyncPageIterator
from atlassian.jira.resource import AsyncJiraResource

from .endpoints import (
    ACKNOWLEDGE_ERRORS,
    ADD_ACTOR_USERS,
    ADD_ATTACHMENT,
    ADD_COMMENT,
    ADD_FIELD,
    ADD_FIELD_TO_DEFAULT_SCREEN,
    ADD_PROJECT_ASSOCIATIONS_TO_SCHEME,
    ADD_PROJECT_ROLE_ACTORS_TO_ROLE,
    ADD_SHARE_PERMISSION,
    ADD_TAB,
    ADD_USER_TO_APPLICATION_1,
    ADD_USER_TO_GROUP,
    ADD_VOTE,
    ADD_WATCHER_1,
    ADD_WORKLOG,
    APPLY_EMAIL_TEMPLATES,
    APPROVE_UPGRADE,
    ARCHIVE_ISSUE,
    ARCHIVE_ISSUES,
    ARCHIVE_PROJECT,
    ARE_METRICS_EXPOSED,
    ASSIGN,
    ASSIGN_PERMISSION_SCHEME,
    ASSIGN_PRIORITY_SCHEME,
    BULK_DELETE_CUSTOM_FIELDS,
    CAN_MOVE_SUB_TASK,
    CANCEL_UPGRADE,
    CHANGE_MY_PASSWORD,
    CHANGE_NODE_STATE_TO_OFFLINE,
    CHANGE_USER_PASSWORD,
    CREATE_AVATAR_FROM_TEMPORARY,
    CREATE_AVATAR_FROM_TEMPORARY_1,
    CREATE_AVATAR_FROM_TEMPORARY_2,
    CREATE_AVATAR_FROM_TEMPORARY_3,
    CREATE_AVATAR_FROM_TEMPORARY_4,
    CREATE_BOARD,
    CREATE_COMPONENT,
    CREATE_CUSTOM_FIELD,
    CREATE_DRAFT_FOR_PARENT,
    CREATE_FILTER,
    CREATE_GROUP,
    CREATE_INDEX_SNAPSHOT,
    CREATE_ISSUE,
    CREATE_ISSUE_LINK_TYPE,
    CREATE_ISSUE_TYPE,
    CREATE_ISSUE_TYPE_SCHEME,
    CREATE_ISSUES,
    CREATE_OR_UPDATE_REMOTE_ISSUE_LINK,
    CREATE_OR_UPDATE_REMOTE_VERSION_LINK,
    CREATE_OR_UPDATE_REMOTE_VERSION_LINK_1,
    CREATE_PERMISSION_GRANT,
    CREATE_PERMISSION_SCHEME,
    CREATE_PRIORITY_SCHEME,
    CREATE_PROJECT,
    CREATE_PROJECT_CATEGORY,
    CREATE_PROJECT_ROLE,
    CREATE_SCHEME,
    CREATE_SPRINT,
    CREATE_USER,
    CREATE_VERSION,
    CURRENT_USER,
    DEFAULT_COLUMNS,
    DEFAULT_COLUMNS_1,
    DELETE,
    DELETE_1,
    DELETE_ACTOR,
    DELETE_AVATAR,
    DELETE_AVATAR_1,
    DELETE_AVATAR_2,
    DELETE_BOARD,
    DELETE_COMMENT,
    DELETE_DEFAULT,
    DELETE_DRAFT_BY_ID,
    DELETE_DRAFT_DEFAULT,
    DELETE_DRAFT_ISSUE_TYPE,
    DELETE_DRAFT_WORKFLOW_MAPPING,
    DELETE_FILTER,
    DELETE_ISSUE,
    DELETE_ISSUE_LINK,
    DELETE_ISSUE_LINK_TYPE,
    DELETE_ISSUE_TYPE,
    DELETE_ISSUE_TYPE_1,
    DELETE_ISSUE_TYPE_SCHEME,
    DELETE_NODE,
    DELETE_PERMISSION_SCHEME,
    DELETE_PERMISSION_SCHEME_ENTITY,
    DELETE_PRIORITY_SCHEME,
    DELETE_PROJECT,
    DELETE_PROJECT_ROLE,
    DELETE_PROJECT_ROLE_ACTORS_FROM_ROLE,
    DELETE_PROPERTY,
    DELETE_PROPERTY_1,
    DELETE_PROPERTY_1_ITEMS_PROPERTIES,
    DELETE_PROPERTY_2,
    DELETE_PROPERTY_3,
    DELETE_PROPERTY_4,
    DELETE_PROPERTY_5,
    DELETE_PROPERTY_6,
    DELETE_REMOTE_ISSUE_LINK_BY_GLOBAL_ID,
    DELETE_REMOTE_ISSUE_LINK_BY_ID,
    DELETE_REMOTE_VERSION_LINK,
    DELETE_REMOTE_VERSION_LINKS_BY_VERSION_ID,
    DELETE_SCHEME,
    DELETE_SESSION,
    DELETE_SHARE_PERMISSION,
    DELETE_SPRINT,
    DELETE_TAB,
    DELETE_WORKFLOW_MAPPING,
    DELETE_WORKLOG,
    DO_TRANSITION,
    DOWNLOAD_EMAIL_TEMPLATES,
    EDIT_FILTER,
    EDIT_ISSUE,
    ESTIMATE_ISSUE_FOR_BOARD,
    EXPAND_FOR_HUMANS,
    EXPAND_FOR_MACHINES,
    FIND_ASSIGNABLE_USERS_1,
    FIND_BULK_ASSIGNABLE_USERS,
    FIND_GROUPS,
    FIND_USERS,
    FIND_USERS_AND_GROUPS,
    FIND_USERS_FOR_PICKER,
    FIND_USERS_WITH_ALL_PERMISSIONS,
    FIND_USERS_WITH_BROWSE_PERMISSION,
    FULLY_UPDATE_PROJECT_ROLE,
    GET_4,
    GET_A11Y_PERSONAL_SETTINGS,
    GET_ACCESSIBLE_PROJECT_TYPE_BY_KEY,
    GET_ADVANCED_SETTINGS,
    GET_ALL,
    GET_ALL_AVATARS,
    GET_ALL_AVATARS_1,
    GET_ALL_BOARDS,
    GET_ALL_FIELDS,
    GET_ALL_ISSUE_TYPE_SCHEMES,
    GET_ALL_NODES,
    GET_ALL_PERMISSIONS,
    GET_ALL_PROJECT_CATEGORIES,
    GET_ALL_PROJECT_TYPES,
    GET_ALL_PROJECTS,
    GET_ALL_SCREENS,
    GET_ALL_SPRINTS,
    GET_ALL_STATUSES,
    GET_ALL_SYSTEM_AVATARS,
    GET_ALL_TABS,
    GET_ALL_TERMINOLOGY_ENTRIES,
    GET_ALL_VERSIONS,
    GET_ALL_WORKFLOWS,
    GET_ALTERNATIVE_ISSUE_TYPES,
    GET_ASSIGNED_PERMISSION_SCHEME,
    GET_ASSIGNED_PRIORITY_SCHEME,
    GET_ASSOCIATED_PROJECTS,
    GET_ATTACHMENT,
    GET_ATTACHMENT_META,
    GET_AUTO_COMPLETE,
    GET_AVAILABLE_METRICS,
    GET_AVATARS,
    GET_BOARD,
    GET_BY_ID,
    GET_COMMENT,
    GET_COMMENTS,
    GET_COMPONENT,
    GET_COMPONENT_RELATED_ISSUES,
    GET_CONFIGURATION,
    GET_CONFIGURATION_1,
    GET_CREATE_ISSUE_META_FIELDS,
    GET_CREATE_ISSUE_META_PROJECT_ISSUE_TYPES,
    GET_CUSTOM_FIELD_OPTION,
    GET_CUSTOM_FIELD_OPTIONS,
    GET_CUSTOM_FIELDS,
    GET_DASHBOARD,
    GET_DEFAULT,
    GET_DEFAULT_SHARE_SCOPE,
    GET_DRAFT_BY_ID,
    GET_DRAFT_DEFAULT,
    GET_DRAFT_ISSUE_TYPE,
    GET_DRAFT_WORKFLOW,
    GET_DUPLICATED_USERS_COUNT,
    GET_DUPLICATED_USERS_MAPPING,
    GET_EDIT_ISSUE_META,
    GET_EMAIL_TYPES,
    GET_EPIC,
    GET_EPICS,
    GET_FAVOURITE_FILTERS,
    GET_FIELD_AUTO_COMPLETE_FOR_QUERY_STRING,
    GET_FIELDS,
    GET_FIELDS_TO_ADD,
    GET_FILTER,
    GET_IDS_OF_WORKLOGS_DELETED_SINCE,
    GET_IDS_OF_WORKLOGS_MODIFIED_SINCE,
    GET_INDEX_SUMMARY,
    GET_ISSUE_1_0_ISSUE,
    GET_ISSUE_2_ISSUE,
    GET_ISSUE_ALL_TYPES,
    GET_ISSUE_ESTIMATION_FOR_BOARD,
    GET_ISSUE_LINK,
    GET_ISSUE_LINK_TYPE,
    GET_ISSUE_LINK_TYPES,
    GET_ISSUE_NAVIGATOR_DEFAULT_COLUMNS,
    GET_ISSUE_PICKER_RESOURCE,
    GET_ISSUE_SECURITY_SCHEME,
    GET_ISSUE_SECURITY_SCHEME_1,
    GET_ISSUE_SECURITY_SCHEMES,
    GET_ISSUE_TYPE,
    GET_ISSUE_TYPE_1,
    GET_ISSUE_TYPE_SCHEME,
    GET_ISSUE_WATCHERS,
    GET_ISSUE_WORKLOG,
    GET_ISSUES_FOR_BACKLOG,
    GET_ISSUES_FOR_BOARD,
    GET_ISSUES_FOR_EPIC,
    GET_ISSUES_FOR_EPIC_1,
    GET_ISSUES_FOR_SPRINT,
    GET_ISSUES_FOR_SPRINT_1,
    GET_ISSUES_WITHOUT_EPIC,
    GET_ISSUES_WITHOUT_EPIC_1,
    GET_ISSUESECURITYLEVEL,
    GET_NOTIFICATION_SCHEME,
    GET_NOTIFICATION_SCHEME_1,
    GET_NOTIFICATION_SCHEMES,
    GET_PAGINATED_COMPONENTS,
    GET_PAGINATED_ISSUE_TYPES,
    GET_PAGINATED_RESOLUTIONS,
    GET_PAGINATED_STATUSES,
    GET_PAGINATED_VERSIONS,
    GET_PASSWORD_POLICY,
    GET_PERMISSION_SCHEME,
    GET_PERMISSION_SCHEME_GRANT,
    GET_PERMISSION_SCHEME_GRANTS,
    GET_PERMISSION_SCHEMES,
    GET_PERMISSIONS,
    GET_PINNED_COMMENTS,
    GET_PREFERENCE,
    GET_PRIORITIES,
    GET_PRIORITIES_1,
    GET_PRIORITY,
    GET_PRIORITY_SCHEME,
    GET_PRIORITY_SCHEMES,
    GET_PROGRESS,
    GET_PROGRESS_1,
    GET_PROGRESS_BULK,
    GET_PROJECT,
    GET_PROJECT_1,
    GET_PROJECT_CATEGORY_BY_ID,
    GET_PROJECT_COMPONENTS,
    GET_PROJECT_ROLE,
    GET_PROJECT_ROLE_ACTORS_FOR_ROLE,
    GET_PROJECT_ROLES,
    GET_PROJECT_ROLES_1,
    GET_PROJECT_ROLES_BY_ID,
    GET_PROJECT_TYPE_BY_KEY,
    GET_PROJECT_VERSIONS,
    GET_PROJECT_VERSIONS_PAGINATED,
    GET_PROJECTS,
    GET_PROPERTIES_KEYS,
    GET_PROPERTIES_KEYS_1,
    GET_PROPERTIES_KEYS_1_COMMENT_PROPERTIES,
    GET_PROPERTIES_KEYS_2,
    GET_PROPERTIES_KEYS_3,
    GET_PROPERTIES_KEYS_4,
    GET_PROPERTIES_KEYS_ITEMS_PROPERTIES,
    GET_PROPERTY,
    GET_PROPERTY_1,
    GET_PROPERTY_1_ITEMS_PROPERTIES,
    GET_PROPERTY_2,
    GET_PROPERTY_2_APPLICATION_PROPERTIES,
    GET_PROPERTY_3,
    GET_PROPERTY_4,
    GET_PROPERTY_5,
    GET_PROPERTY_6,
    GET_PROPERTY_KEYS,
    GET_REFINED_VELOCITY,
    GET_REINDEX_INFO,
    GET_REINDEX_PROGRESS,
    GET_REMOTE_ISSUE_LINK_BY_ID,
    GET_REMOTE_ISSUE_LINKS,
    GET_REMOTE_VERSION_LINK,
    GET_REMOTE_VERSION_LINKS,
    GET_REMOTE_VERSION_LINKS_BY_VERSION_ID,
    GET_RESOLUTION,
    GET_RESOLUTIONS,
    GET_SCHEME_ATTRIBUTE,
    GET_SECURITY_LEVELS_FOR_PROJECT,
    GET_SERVER_INFO,
    GET_SHARE_PERMISSION,
    GET_SHARE_PERMISSIONS,
    GET_SPRINT,
    GET_STATE,
    GET_STATUS,
    GET_STATUS_CATEGORIES,
    GET_STATUS_CATEGORY,
    GET_STATUSES,
    GET_SUB_TASKS,
    GET_TERMINOLOGY_ENTRY,
    GET_TRANSITIONS,
    GET_UPGRADE_RESULT,
    GET_USER,
    GET_USER_1,
    GET_USER_LIST,
    GET_USERS_FROM_GROUP,
    GET_VERSION,
    GET_VERSION_RELATED_ISSUES,
    GET_VERSION_UNRESOLVED_ISSUES,
    GET_VOTES,
    GET_WORKFLOW,
    GET_WORKFLOW_SCHEME_FOR_PROJECT,
    GET_WORKLOG,
    GET_WORKLOGS_FOR_IDS,
    IS_APP_MONITORING_ENABLED,
    IS_INDEX_SNAPSHOT_RUNNING,
    IS_IPD_MONITORING_ENABLED,
    LINK_ISSUES,
    LIST,
    LIST_INDEX_SNAPSHOT,
    LOGIN,
    LOGOUT,
    MERGE,
    MOVE_FIELD,
    MOVE_ISSUES_TO_BACKLOG,
    MOVE_ISSUES_TO_EPIC,
    MOVE_ISSUES_TO_SPRINT,
    MOVE_SUB_TASKS,
    MOVE_TAB,
    MOVE_VERSION,
    NOTIFY,
    PARTIAL_UPDATE_PROJECT_ROLE,
    PARTIALLY_UPDATE_EPIC,
    PARTIALLY_UPDATE_SPRINT,
    POLICY_CHECK_CREATE_USER,
    POLICY_CHECK_UPDATE_USER,
    PROCESS_REQUESTS,
    PUT_2,
    PUT_BULK,
    RANK_EPICS,
    RANK_ISSUES,
    REINDEX,
    REINDEX_ISSUES,
    RELEASE,
    REMOVE_ALL_PROJECT_ASSOCIATIONS,
    REMOVE_ATTACHMENT,
    REMOVE_FIELD,
    REMOVE_GROUP,
    REMOVE_ISSUES_FROM_EPIC,
    REMOVE_PREFERENCE,
    REMOVE_PROJECT_ASSOCIATION,
    REMOVE_PROJECT_CATEGORY,
    REMOVE_USER,
    REMOVE_USER_FROM_APPLICATION_1,
    REMOVE_USER_FROM_GROUP,
    REMOVE_VOTE,
    REMOVE_WATCHER_1,
    RENAME_TAB,
    REQUEST_CURRENT_INDEX_FROM_NODE,
    RESET_COLUMNS,
    RESET_COLUMNS_1,
    RESTORE_ISSUE,
    RESTORE_PROJECT,
    REVERT_EMAIL_TEMPLATES_TO_DEFAULT,
    RUN_UPGRADES_NOW,
    SCHEDULE_USER_ANONYMIZATION,
    SCHEDULE_USER_ANONYMIZATION_RERUN,
    SEARCH_1,
    SEARCH_FOR_PROJECTS,
    SEARCH_USING_SEARCH_REQUEST,
    SET_ACTORS,
    SET_APP_MONITORING_ENABLED,
    SET_APP_MONITORING_ENABLED_1,
    SET_BASE_URL,
    SET_COLUMNS_1,
    SET_COLUMNS_URL_ENCODED,
    SET_DEFAULT_SHARE_SCOPE,
    SET_DRAFT_ISSUE_TYPE,
    SET_ISSUE_NAVIGATOR_DEFAULT_COLUMNS_FORM,
    SET_ISSUE_TYPE,
    SET_PIN_COMMENT,
    SET_PREFERENCE,
    SET_PROJECT_ASSOCIATIONS_FOR_SCHEME,
    SET_PROPERTY,
    SET_PROPERTY_1,
    SET_PROPERTY_1_COMMENT_PROPERTIES,
    SET_PROPERTY_2,
    SET_PROPERTY_3,
    SET_PROPERTY_4,
    SET_PROPERTY_5,
    SET_PROPERTY_ITEMS_PROPERTIES,
    SET_PROPERTY_VIA_RESTFUL_TABLE,
    SET_READY_TO_UPGRADE,
    SET_REFINED_VELOCITY,
    SET_SCHEME_ATTRIBUTE,
    SET_TERMINOLOGY_ENTRIES,
    START,
    STOP,
    STORE_TEMPORARY_AVATAR,
    STORE_TEMPORARY_AVATAR_USING_MULTI_PART,
    STORE_TEMPORARY_AVATAR_USING_MULTI_PART_1,
    STORE_TEMPORARY_AVATAR_USING_MULTI_PART_2,
    STORE_TEMPORARY_AVATAR_USING_MULTI_PART_3,
    SWAP_SPRINT,
    UNASSIGN_PRIORITY_SCHEME,
    UNLOCK_ANONYMIZATION,
    UNMAP_ALL_SPRINTS,
    UNMAP_SPRINTS,
    UPDATE,
    UPDATE_COMMENT,
    UPDATE_COMPONENT,
    UPDATE_DEFAULT,
    UPDATE_DRAFT,
    UPDATE_DRAFT_DEFAULT,
    UPDATE_DRAFT_WORKFLOW_MAPPING,
    UPDATE_ISSUE_LINK_TYPE,
    UPDATE_ISSUE_TYPE,
    UPDATE_ISSUE_TYPE_SCHEME,
    UPDATE_PERMISSION_SCHEME,
    UPDATE_PRIORITY_SCHEME,
    UPDATE_PROJECT,
    UPDATE_PROJECT_AVATAR,
    UPDATE_PROJECT_CATEGORY,
    UPDATE_PROJECT_TYPE,
    UPDATE_REMOTE_ISSUE_LINK,
    UPDATE_SHOW_WHEN_EMPTY_INDICATOR,
    UPDATE_SPRINT,
    UPDATE_USER,
    UPDATE_USER_1,
    UPDATE_USER_AVATAR_1,
    UPDATE_VERSION,
    UPDATE_WORKFLOW_MAPPING,
    UPDATE_WORKLOG,
    UPLOAD_EMAIL_TEMPLATES,
    VALIDATE,
    VALIDATE_USER_ANONYMIZATION,
    VALIDATE_USER_ANONYMIZATION_RERUN,
)
from .models import (
    A11yPersonalSettingBean,
    ActorInputBean,
    ActorsMap,
    AddFieldBean,
    AddGroupBean,
    ApplicationRoleBean,
    AppMonitoringRestEntity,
    AssociateProjectsBean,
    AttachmentArchiveImpl,
    AttachmentBean,
    AttachmentJsonBean,
    AttachmentMetaBean,
    AuthParams,
    AuthSuccess,
    AutoCompleteResponseBean,
    AutoCompleteResultWrapper,
    AvatarBean,
    AvatarCroppingBean,
    BoardBean,
    BoardConfigBean,
    BoardCreateBean,
    BooleanSettingBean,
    BulkDeleteResponseBean,
    ClusterState,
    ColumnLayout,
    ColumnOptions,
    CommentJsonBean,
    ComponentBean,
    ComponentIssueCountsBean,
    ConfigurationBean,
    CreateMetaIssueTypeBean,
    CreateUpdateRoleRequestBean,
    CurrentUser,
    CustomFieldBean,
    CustomFieldDefinitionJsonBean,
    CustomFieldOptionBean,
    CustomFieldOptionsBean,
    DashboardBean,
    DefaultBean,
    DefaultShareScopeBean,
    DeleteAndReplaceVersionBean,
    EditMetaBean,
    EntityPropertiesKeysBean,
    EntityPropertyBean,
    EpicBean,
    EpicRankRequestBean,
    EpicUpdateBean,
    ErrorCollection,
    FieldBean,
    FieldEditBean,
    FieldMetaBean,
    FieldValueBean,
    FilePart,
    FilterBean,
    FilterPermissionBean,
    GroupBean,
    GroupSuggestionsBean,
    HumanReadableArchive,
    IdBean,
    IndexSnapshotBean,
    IndexSnapshotPromiseBean,
    IndexSnapshotStatusBean,
    IndexSummaryBean,
    IpdMonitoringRestEntity,
    IssueAssignRequestBean,
    IssueBean,
    IssueCreateResponse,
    IssueLinks,
    IssueLinkTypeJsonBean,
    IssueLinkTypesBean,
    IssuePickerResult,
    IssueRankRequestBean,
    IssueRefJsonBean,
    IssuesCreateResponse,
    IssueSubTaskMovePositionBean,
    IssuesUpdateBean,
    IssueTypeCreateBean,
    IssueTypeJsonBean,
    IssueTypeMappingBean,
    IssueTypeSchemeBean,
    IssueTypeSchemeCreateUpdateBean,
    IssueTypeSchemeListBean,
    IssueTypeUpdateBean,
    IssueTypeWithStatusJsonBean,
    IssueUpdateBean,
    LicenseValidationResults,
    LinkIssueRequestJsonBean,
    MoveFieldBean,
    NodeBean,
    NotificationJsonBean,
    NotificationSchemeBean,
    PageBean,
    PasswordBean,
    PasswordPolicyCreateUserBean,
    PasswordPolicyUpdateUserBean,
    PermissionGrantBean,
    PermissionGrantsBean,
    PermissionSchemeAttributeBean,
    PermissionSchemeBean,
    PermissionSchemesBean,
    PermissionsJsonBean,
    PinnedCommentJsonBean,
    PriorityJsonBean,
    PrioritySchemeBean,
    PrioritySchemeUpdateBean,
    ProjectBean,
    ProjectCategoryBean,
    ProjectCategoryJsonBean,
    ProjectIdentity,
    ProjectInputBean,
    ProjectJsonBean,
    ProjectPickerResultWrapper,
    ProjectRoleActorsBean,
    ProjectRoleActorsUpdateBean,
    ProjectRoleBean,
    ProjectTypeBean,
    ProjectUpdateBean,
    Property,
    PropertyBean,
    ReindexBean,
    ReindexRequestBean,
    RemoteEntityLinkJsonBean,
    RemoteEntityLinksJsonBean,
    RemoteIssueLinkBean,
    RemoteIssueLinkCreateOrUpdateRequest,
    ResolutionBean,
    ResolutionJsonBean,
    ScreenableFieldBean,
    ScreenableTabBean,
    SearchRequestBean,
    SecurityLevelJsonBean,
    SecurityListLevelJsonBean,
    SecuritySchemeJsonBean,
    SecuritySchemesJsonBean,
    ServerInfoBean,
    SharePermissionInputBean,
    SprintBean,
    SprintCreateBean,
    SprintSwapBean,
    StatusCategoryJsonBean,
    StatusJsonBean,
    StreamPageBean,
    StringList,
    TerminologyRequestBean,
    TerminologyResponseBean,
    TransitionsMetaBean,
    UnmapSprintsBean,
    UpdateUserToGroupBean,
    UpgradeResultBean,
    UserAnonymizationRequestBean,
    UserAnonymizationRerunRequestBean,
    UserAnonymizationValidationBean,
    UserBean,
    UserJsonBean,
    UserPickerResultsBean,
    UsersAndGroupsBean,
    UserWriteBean,
    VersionBean,
    VersionIssueCountsBean,
    VersionMoveBean,
    VersionUnresolvedIssueCountsBean,
    VoteBean,
    WatchersBean,
    WorkflowMappingBean,
    WorkflowSchemeBean,
    Worklog,
    WorklogChangeBean,
    WorklogIdsRequestBean,
)


class AsyncAgileResource(AsyncJiraResource):
    async def move_issues_to_backlog(self, body: IssueAssignRequestBean) -> None:
        """Update issues to move them to the backlog"""
        return await self._post(MOVE_ISSUES_TO_BACKLOG.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_all_boards(
        self,
        *,
        max_results: int | None = None,
        name: str | None = None,
        project_key_or_id: str | None = None,
        type_: StringList | None = None,
        start_at: int | None = None,
    ) -> BoardBean:
        """Get all boards"""
        return await self._get(
            GET_ALL_BOARDS.path,
            params={
                "maxResults": max_results,
                "name": name,
                "projectKeyOrId": project_key_or_id,
                "type": type_,
                "startAt": start_at,
            },
            model=BoardBean,
        )

    async def create_board(self, body: BoardCreateBean) -> BoardBean:
        """Create a new board"""
        return await self._post(
            CREATE_BOARD.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=BoardBean,
        )

    async def delete_board(self, board_id: int) -> None:
        """Delete the board"""
        return await self._delete(DELETE_BOARD.path.replace("{boardId}", str(board_id)))

    async def get_board(self, board_id: int) -> BoardBean:
        """Get a single board"""
        return await self._get(GET_BOARD.path.replace("{boardId}", str(board_id)), model=BoardBean)

    async def get_issues_for_backlog(
        self,
        board_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int | None = None,
    ) -> IssueBean:
        """Get all issues from the board's backlog"""
        return await self._get(
            GET_ISSUES_FOR_BACKLOG.path.replace("{boardId}", str(board_id)),
            params={
                "expand": expand,
                "jql": jql,
                "maxResults": max_results,
                "validateQuery": validate_query,
                "fields": fields,
                "startAt": start_at,
            },
            model=IssueBean,
        )

    async def get_configuration(self, board_id: int) -> BoardConfigBean:
        """Get the board configuration"""
        return await self._get(GET_CONFIGURATION.path.replace("{boardId}", str(board_id)), model=BoardConfigBean)

    async def get_epics(
        self,
        board_id: int,
        *,
        max_results: int | None = None,
        done: str | None = None,
        start_at: int | None = None,
    ) -> EpicBean:
        """Get all epics from the board"""
        return await self._get(
            GET_EPICS.path.replace("{boardId}", str(board_id)),
            params={"maxResults": max_results, "done": done, "startAt": start_at},
            model=EpicBean,
        )

    async def get_issues_without_epic(
        self,
        board_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int | None = None,
    ) -> IssueBean:
        """Get all issues without an epic"""
        return await self._get(
            GET_ISSUES_WITHOUT_EPIC.path.replace("{boardId}", str(board_id)),
            params={
                "expand": expand,
                "jql": jql,
                "maxResults": max_results,
                "validateQuery": validate_query,
                "fields": fields,
                "startAt": start_at,
            },
            model=IssueBean,
        )

    async def get_issues_for_epic(
        self,
        epic_id: int,
        board_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int | None = None,
    ) -> IssueBean:
        """Get all issues for a specific epic"""
        return await self._get(
            GET_ISSUES_FOR_EPIC.path.replace("{epicId}", str(epic_id)).replace("{boardId}", str(board_id)),
            params={
                "expand": expand,
                "jql": jql,
                "maxResults": max_results,
                "validateQuery": validate_query,
                "fields": fields,
                "startAt": start_at,
            },
            model=IssueBean,
        )

    async def get_issues_for_board(
        self,
        board_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int | None = None,
    ) -> IssueBean:
        """Get all issues from a board"""
        return await self._get(
            GET_ISSUES_FOR_BOARD.path.replace("{boardId}", str(board_id)),
            params={
                "expand": expand,
                "jql": jql,
                "maxResults": max_results,
                "validateQuery": validate_query,
                "fields": fields,
                "startAt": start_at,
            },
            model=IssueBean,
        )

    async def get_projects(
        self,
        board_id: int,
        *,
        max_results: int | None = None,
        start_at: int | None = None,
    ) -> ProjectJsonBean:
        """Get all projects associated with the board"""
        return await self._get(
            GET_PROJECTS.path.replace("{boardId}", str(board_id)),
            params={"maxResults": max_results, "startAt": start_at},
            model=ProjectJsonBean,
        )

    async def get_properties_keys(self, board_id: str) -> EntityPropertiesKeysBean:
        """Get all properties keys for a board"""
        return await self._get(
            GET_PROPERTIES_KEYS.path.replace("{boardId}", str(board_id)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property(self, property_key: str, board_id: str) -> None:
        """Delete a property from a board"""
        return await self._delete(
            DELETE_PROPERTY.path.replace("{propertyKey}", str(property_key)).replace("{boardId}", str(board_id)),
        )

    async def get_property(self, property_key: str, board_id: str) -> EntityPropertiesKeysBean:
        """Get a property from a board"""
        return await self._get(
            GET_PROPERTY.path.replace("{propertyKey}", str(property_key)).replace("{boardId}", str(board_id)),
            model=EntityPropertiesKeysBean,
        )

    async def set_property(self, property_key: str, board_id: str) -> EntityPropertiesKeysBean:
        """Update a board's property"""
        return await self._put(
            SET_PROPERTY.path.replace("{propertyKey}", str(property_key)).replace("{boardId}", str(board_id)),
            model=EntityPropertiesKeysBean,
        )

    async def get_refined_velocity(self, board_id: int) -> BooleanSettingBean:
        """Get the value of the refined velocity setting"""
        return await self._get(GET_REFINED_VELOCITY.path.replace("{boardId}", str(board_id)), model=BooleanSettingBean)

    async def set_refined_velocity(self, board_id: int, body: BooleanSettingBean) -> None:
        """Update the board's refined velocity setting"""
        return await self._put(
            SET_REFINED_VELOCITY.path.replace("{boardId}", str(board_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_all_sprints(
        self,
        board_id: int,
        *,
        max_results: int | None = None,
        state: StringList | None = None,
        start_at: int | None = None,
    ) -> SprintBean:
        """Get all sprints from a board"""
        return await self._get(
            GET_ALL_SPRINTS.path.replace("{boardId}", str(board_id)),
            params={"maxResults": max_results, "state": state, "startAt": start_at},
            model=SprintBean,
        )

    async def get_issues_for_sprint(
        self,
        sprint_id: int,
        board_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        max_results: int | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int | None = None,
    ) -> SprintBean:
        """Get all issues for a sprint"""
        return await self._get(
            GET_ISSUES_FOR_SPRINT.path.replace("{sprintId}", str(sprint_id)).replace("{boardId}", str(board_id)),
            params={
                "expand": expand,
                "jql": jql,
                "maxResults": max_results,
                "validateQuery": validate_query,
                "fields": fields,
                "startAt": start_at,
            },
            model=SprintBean,
        )

    async def get_all_versions(
        self,
        board_id: int,
        *,
        max_results: int | None = None,
        released: str | None = None,
        start_at: int | None = None,
    ) -> VersionBean:
        """Get all versions from a board"""
        return await self._get(
            GET_ALL_VERSIONS.path.replace("{boardId}", str(board_id)),
            params={"maxResults": max_results, "released": released, "startAt": start_at},
            model=VersionBean,
        )

    def get_issues_without_epic_1(
        self,
        *,
        expand: str | None = None,
        jql: str | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[IssueBean]:
        """Get issues without an epic"""
        return self._get_paged(
            GET_ISSUES_WITHOUT_EPIC_1.path,
            params={"expand": expand, "jql": jql, "validateQuery": validate_query, "fields": fields},
            model=IssueBean,
            items_field="issues",
            start_at=start_at,
            max_results=max_results,
        )

    async def remove_issues_from_epic(self, body: IssueAssignRequestBean) -> None:
        """Remove issues from any epic"""
        return await self._post(REMOVE_ISSUES_FROM_EPIC.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_epic(self, epic_id_or_key: str) -> EpicBean:
        """Get an epic by id or key"""
        return await self._get(GET_EPIC.path.replace("{epicIdOrKey}", str(epic_id_or_key)), model=EpicBean)

    async def partially_update_epic(self, epic_id_or_key: str, body: EpicUpdateBean) -> EpicBean:
        """Update an epic's details"""
        return await self._post(
            PARTIALLY_UPDATE_EPIC.path.replace("{epicIdOrKey}", str(epic_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=EpicBean,
        )

    def get_issues_for_epic_1(
        self,
        epic_id_or_key: str,
        *,
        expand: str | None = None,
        jql: str | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[IssueBean]:
        """Get issues for a specific epic"""
        return self._get_paged(
            GET_ISSUES_FOR_EPIC_1.path.replace("{epicIdOrKey}", str(epic_id_or_key)),
            params={"expand": expand, "jql": jql, "validateQuery": validate_query, "fields": fields},
            model=IssueBean,
            items_field="issues",
            start_at=start_at,
            max_results=max_results,
        )

    async def move_issues_to_epic(self, epic_id_or_key: str, body: IssueAssignRequestBean) -> None:
        """Move issues to a specific epic"""
        return await self._post(
            MOVE_ISSUES_TO_EPIC.path.replace("{epicIdOrKey}", str(epic_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def rank_epics(self, epic_id_or_key: str, body: EpicRankRequestBean) -> None:
        """Rank an epic relative to another"""
        return await self._put(
            RANK_EPICS.path.replace("{epicIdOrKey}", str(epic_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def create_sprint(self, body: SprintCreateBean) -> SprintBean:
        """Create a future sprint"""
        return await self._post(
            CREATE_SPRINT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SprintBean,
        )

    async def unmap_sprints(self, body: UnmapSprintsBean) -> None:
        """Unmap sprints from being synced"""
        return await self._put(UNMAP_SPRINTS.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def unmap_all_sprints(self) -> None:
        """Unmap all sprints from being synced"""
        return await self._put(UNMAP_ALL_SPRINTS.path)

    async def delete_sprint(self, sprint_id: int) -> None:
        """Delete a sprint"""
        return await self._delete(DELETE_SPRINT.path.replace("{sprintId}", str(sprint_id)))

    async def get_sprint(self, sprint_id: int) -> SprintBean:
        """Get sprint by id"""
        return await self._get(GET_SPRINT.path.replace("{sprintId}", str(sprint_id)), model=SprintBean)

    async def partially_update_sprint(self, sprint_id: int, body: SprintBean) -> SprintBean:
        """Partially update a sprint"""
        return await self._post(
            PARTIALLY_UPDATE_SPRINT.path.replace("{sprintId}", str(sprint_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SprintBean,
        )

    async def update_sprint(self, sprint_id: int, body: SprintBean) -> SprintBean:
        """Update a sprint fully"""
        return await self._put(
            UPDATE_SPRINT.path.replace("{sprintId}", str(sprint_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SprintBean,
        )

    def get_issues_for_sprint_1(
        self,
        sprint_id: int,
        *,
        expand: str | None = None,
        jql: str | None = None,
        validate_query: bool | None = None,
        fields: list[StringList] | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[IssueBean]:
        """Get all issues in a sprint"""
        return self._get_paged(
            GET_ISSUES_FOR_SPRINT_1.path.replace("{sprintId}", str(sprint_id)),
            params={"expand": expand, "jql": jql, "validateQuery": validate_query, "fields": fields},
            model=IssueBean,
            items_field="issues",
            start_at=start_at,
            max_results=max_results,
        )

    async def move_issues_to_sprint(self, sprint_id: int, body: IssueAssignRequestBean) -> None:
        """Move issues to a sprint"""
        return await self._post(
            MOVE_ISSUES_TO_SPRINT.path.replace("{sprintId}", str(sprint_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_properties_keys_1(self, sprint_id: str) -> EntityPropertiesKeysBean:
        """Get all properties keys for a sprint"""
        return await self._get(
            GET_PROPERTIES_KEYS_1.path.replace("{sprintId}", str(sprint_id)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_1(self, property_key: str, sprint_id: str) -> None:
        """Delete a sprint's property"""
        return await self._delete(
            DELETE_PROPERTY_1.path.replace("{propertyKey}", str(property_key)).replace("{sprintId}", str(sprint_id)),
        )

    async def get_property_1(self, property_key: str, sprint_id: str) -> EntityPropertyBean:
        """Get a property for a sprint"""
        return await self._get(
            GET_PROPERTY_1.path.replace("{propertyKey}", str(property_key)).replace("{sprintId}", str(sprint_id)),
            model=EntityPropertyBean,
        )

    async def set_property_1(self, property_key: str, sprint_id: str) -> None:
        """Update a sprint's property"""
        return await self._put(
            SET_PROPERTY_1.path.replace("{propertyKey}", str(property_key)).replace("{sprintId}", str(sprint_id)),
        )

    async def swap_sprint(self, sprint_id: int, body: SprintSwapBean) -> None:
        """Swap the position of two sprints"""
        return await self._post(
            SWAP_SPRINT.path.replace("{sprintId}", str(sprint_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )


class AsyncProjectResource(AsyncJiraResource):
    async def create_component(self, body: ComponentBean) -> ComponentBean:
        """Create component"""
        return await self._post(
            CREATE_COMPONENT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ComponentBean,
        )

    async def get_paginated_components(
        self,
        *,
        max_results: str | None = "100",
        query: str | None = None,
        project_ids: str | None = None,
        start_at: str | None = "0",
    ) -> PageBean:
        """Get paginated components"""
        return await self._get(
            GET_PAGINATED_COMPONENTS.path,
            params={"maxResults": max_results, "query": query, "projectIds": project_ids, "startAt": start_at},
            model=PageBean,
        )

    async def delete(self, id: str, *, move_issues_to: str | None = None) -> None:
        """Delete a project component"""
        return await self._delete(DELETE.path.replace("{id}", str(id)), params={"moveIssuesTo": move_issues_to})

    async def get_component(self, id: str) -> ComponentBean:
        """Get project component"""
        return await self._get(GET_COMPONENT.path.replace("{id}", str(id)), model=ComponentBean)

    async def update_component(self, id: str, body: ComponentBean) -> ComponentBean:
        """Update a component"""
        return await self._put(
            UPDATE_COMPONENT.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ComponentBean,
        )

    async def get_component_related_issues(self, id: str) -> ComponentIssueCountsBean:
        """Get component related issues"""
        return await self._get(
            GET_COMPONENT_RELATED_ISSUES.path.replace("{id}", str(id)),
            model=ComponentIssueCountsBean,
        )

    async def get_all_projects(
        self,
        *,
        include_archived: bool | None = None,
        expand: str | None = None,
        recent: int | None = None,
        browse_archive: bool | None = None,
    ) -> ProjectBean:
        """Get all visible projects"""
        return await self._get(
            GET_ALL_PROJECTS.path,
            params={
                "includeArchived": include_archived,
                "expand": expand,
                "recent": recent,
                "browseArchive": browse_archive,
            },
            model=ProjectBean,
        )

    async def create_project(self, body: ProjectInputBean) -> ProjectIdentity:
        """Create a new project"""
        return await self._post(
            CREATE_PROJECT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectIdentity,
        )

    async def get_all_project_types(self) -> ProjectTypeBean:
        """Get all project types"""
        return await self._get(GET_ALL_PROJECT_TYPES.path, model=ProjectTypeBean)

    async def get_project_type_by_key(self, project_type_key: str) -> ProjectTypeBean:
        """Get project type by key"""
        return await self._get(
            GET_PROJECT_TYPE_BY_KEY.path.replace("{projectTypeKey}", str(project_type_key)),
            model=ProjectTypeBean,
        )

    async def get_accessible_project_type_by_key(self, project_type_key: str) -> ProjectTypeBean:
        """Get project type by key"""
        return await self._get(
            GET_ACCESSIBLE_PROJECT_TYPE_BY_KEY.path.replace("{projectTypeKey}", str(project_type_key)),
            model=ProjectTypeBean,
        )

    async def delete_project(self, project_id_or_key: str) -> None:
        """Delete a project"""
        return await self._delete(DELETE_PROJECT.path.replace("{projectIdOrKey}", str(project_id_or_key)))

    async def get_project(self, project_id_or_key: str, *, expand: str | None = None) -> ProjectBean:
        """Get a project by ID or key"""
        return await self._get(
            GET_PROJECT.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            params={"expand": expand},
            model=ProjectBean,
        )

    async def update_project(
        self,
        project_id_or_key: str,
        body: ProjectUpdateBean,
        *,
        expand: str | None = None,
    ) -> ProjectBean:
        """Update a project"""
        return await self._put(
            UPDATE_PROJECT.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectBean,
        )

    async def archive_project(self, project_id_or_key: str) -> None:
        """Archive a project"""
        return await self._put(ARCHIVE_PROJECT.path.replace("{projectIdOrKey}", str(project_id_or_key)))

    async def create_avatar_from_temporary_2(self, project_id_or_key: str, body: AvatarCroppingBean) -> AvatarBean:
        """Create avatar from temporary"""
        return await self._post(
            CREATE_AVATAR_FROM_TEMPORARY_2.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarBean,
        )

    async def update_project_avatar(self, project_id_or_key: str, body: AvatarBean) -> None:
        """Update project avatar"""
        return await self._put(
            UPDATE_PROJECT_AVATAR.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def store_temporary_avatar_using_multi_part_1(
        self,
        project_id_or_key: str,
        body: FilePart,
    ) -> AvatarCroppingBean:
        """Store temporary avatar using multipart"""
        return await self._post(
            STORE_TEMPORARY_AVATAR_USING_MULTI_PART_1.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarCroppingBean,
        )

    async def delete_avatar(self, project_id_or_key: str, id: int) -> None:
        """Delete an avatar"""
        return await self._delete(
            DELETE_AVATAR.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace("{id}", str(id)),
        )

    async def get_all_avatars(self, project_id_or_key: str) -> AvatarBean:
        """Get all avatars for a project"""
        return await self._get(
            GET_ALL_AVATARS.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            model=AvatarBean,
        )

    async def get_project_components(self, project_id_or_key: str) -> ComponentBean:
        """Get project components"""
        return await self._get(
            GET_PROJECT_COMPONENTS.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            model=ComponentBean,
        )

    async def get_properties_keys_3(self, project_id_or_key: str) -> EntityPropertiesKeysBean:
        """Get keys of all properties for project"""
        return await self._get(
            GET_PROPERTIES_KEYS_3.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_5(self, property_key: str, project_id_or_key: str) -> None:
        """Delete property from project"""
        return await self._delete(
            DELETE_PROPERTY_5.path.replace("{propertyKey}", str(property_key)).replace(
                "{projectIdOrKey}", str(project_id_or_key)
            ),
        )

    async def get_property_5(self, property_key: str, project_id_or_key: str) -> EntityPropertyBean:
        """Get value of property from project"""
        return await self._get(
            GET_PROPERTY_5.path.replace("{propertyKey}", str(property_key)).replace(
                "{projectIdOrKey}", str(project_id_or_key)
            ),
            model=EntityPropertyBean,
        )

    async def set_property_4(self, property_key: str, project_id_or_key: str, body: PropertyBean) -> None:
        """Set value of specified project's property"""
        return await self._put(
            SET_PROPERTY_4.path.replace("{propertyKey}", str(property_key)).replace(
                "{projectIdOrKey}", str(project_id_or_key)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def restore_project(self, project_id_or_key: str) -> None:
        """Restore an archived project"""
        return await self._put(RESTORE_PROJECT.path.replace("{projectIdOrKey}", str(project_id_or_key)))

    async def get_project_roles(self, project_id_or_key: str) -> None:
        """Get all roles in project"""
        return await self._get(GET_PROJECT_ROLES.path.replace("{projectIdOrKey}", str(project_id_or_key)))

    async def delete_actor(
        self,
        project_id_or_key: str,
        id: int,
        *,
        user: str | None = None,
        group: str | None = None,
    ) -> None:
        """Delete actors from project role"""
        return await self._delete(
            DELETE_ACTOR.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace("{id}", str(id)),
            params={"user": user, "group": group},
        )

    async def get_project_role(self, project_id_or_key: str, id: int) -> ProjectRoleBean:
        """Get details for a project role"""
        return await self._get(
            GET_PROJECT_ROLE.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace("{id}", str(id)),
            model=ProjectRoleBean,
        )

    async def add_actor_users(self, project_id_or_key: str, id: int, body: ActorsMap) -> ProjectRoleBean:
        """Add actor to project role"""
        return await self._post(
            ADD_ACTOR_USERS.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleBean,
        )

    async def set_actors(self, project_id_or_key: str, id: int, body: ProjectRoleActorsUpdateBean) -> ProjectRoleBean:
        """Update project role with actors"""
        return await self._put(
            SET_ACTORS.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleBean,
        )

    async def get_all_statuses(self, project_id_or_key: str) -> IssueTypeWithStatusJsonBean:
        """Get all issue types with statuses for a project"""
        return await self._get(
            GET_ALL_STATUSES.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            model=IssueTypeWithStatusJsonBean,
        )

    async def update_project_type(self, project_id_or_key: str, new_project_type_key: str) -> ProjectBean:
        """Update project type"""
        return await self._put(
            UPDATE_PROJECT_TYPE.path.replace("{projectIdOrKey}", str(project_id_or_key)).replace(
                "{newProjectTypeKey}", str(new_project_type_key)
            ),
            model=ProjectBean,
        )

    async def get_project_versions_paginated(
        self,
        project_id_or_key: str,
        *,
        expand: str | None = None,
        max_results: int | None = None,
        order_by: str | None = None,
        start_at: int | None = None,
    ) -> PageBean:
        """Get paginated project versions"""
        return await self._get(
            GET_PROJECT_VERSIONS_PAGINATED.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            params={"expand": expand, "maxResults": max_results, "orderBy": order_by, "startAt": start_at},
            model=PageBean,
        )

    async def get_project_versions(self, project_id_or_key: str, *, expand: str | None = None) -> VersionBean:
        """Get project versions"""
        return await self._get(
            GET_PROJECT_VERSIONS.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            params={"expand": expand},
            model=VersionBean,
        )

    async def get_issue_security_scheme_1(self, project_key_or_id: str) -> SecuritySchemeJsonBean:
        """Get issue security scheme for project"""
        return await self._get(
            GET_ISSUE_SECURITY_SCHEME_1.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            model=SecuritySchemeJsonBean,
        )

    async def get_notification_scheme_1(
        self,
        project_key_or_id: str,
        *,
        expand: str | None = None,
    ) -> NotificationSchemeBean:
        """Get notification scheme associated with the project"""
        return await self._get(
            GET_NOTIFICATION_SCHEME_1.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            params={"expand": expand},
            model=NotificationSchemeBean,
        )

    async def get_assigned_permission_scheme(
        self,
        project_key_or_id: str,
        *,
        expand: str | None = None,
    ) -> PermissionSchemeBean:
        """Get assigned permission scheme"""
        return await self._get(
            GET_ASSIGNED_PERMISSION_SCHEME.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            params={"expand": expand},
            model=PermissionSchemeBean,
        )

    async def assign_permission_scheme(
        self,
        project_key_or_id: str,
        body: IdBean,
        *,
        expand: str | None = None,
    ) -> PermissionSchemeBean:
        """Assign permission scheme to project"""
        return await self._put(
            ASSIGN_PERMISSION_SCHEME.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PermissionSchemeBean,
        )

    async def get_assigned_priority_scheme(self, project_key_or_id: str) -> PrioritySchemeBean:
        """Get assigned priority scheme"""
        return await self._get(
            GET_ASSIGNED_PRIORITY_SCHEME.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            model=PrioritySchemeBean,
        )

    async def assign_priority_scheme(self, project_key_or_id: str, body: IdBean) -> PrioritySchemeBean:
        """Assign project with priority scheme"""
        return await self._put(
            ASSIGN_PRIORITY_SCHEME.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PrioritySchemeBean,
        )

    async def unassign_priority_scheme(self, scheme_id: int, project_key_or_id: str) -> PrioritySchemeBean:
        """Unassign project from priority scheme"""
        return await self._delete(
            UNASSIGN_PRIORITY_SCHEME.path.replace("{schemeId}", str(scheme_id)).replace(
                "{projectKeyOrId}", str(project_key_or_id)
            ),
            model=PrioritySchemeBean,
        )

    async def get_security_levels_for_project(self, project_key_or_id: str) -> SecurityListLevelJsonBean:
        """Get all security levels for project"""
        return await self._get(
            GET_SECURITY_LEVELS_FOR_PROJECT.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            model=SecurityListLevelJsonBean,
        )

    async def get_workflow_scheme_for_project(self, project_key_or_id: str) -> WorkflowSchemeBean:
        """Get workflow scheme for project"""
        return await self._get(
            GET_WORKFLOW_SCHEME_FOR_PROJECT.path.replace("{projectKeyOrId}", str(project_key_or_id)),
            model=WorkflowSchemeBean,
        )

    async def get_all_project_categories(self) -> ProjectCategoryJsonBean:
        """Get all project categories"""
        return await self._get(GET_ALL_PROJECT_CATEGORIES.path, model=ProjectCategoryJsonBean)

    async def create_project_category(self, body: ProjectCategoryBean) -> ProjectCategoryJsonBean:
        """Create project category"""
        return await self._post(
            CREATE_PROJECT_CATEGORY.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectCategoryJsonBean,
        )

    async def remove_project_category(self, id: int) -> None:
        """Delete project category"""
        return await self._delete(REMOVE_PROJECT_CATEGORY.path.replace("{id}", str(id)))

    async def get_project_category_by_id(self, id: int) -> ProjectCategoryJsonBean:
        """Get project category by ID"""
        return await self._get(GET_PROJECT_CATEGORY_BY_ID.path.replace("{id}", str(id)), model=ProjectCategoryJsonBean)

    async def update_project_category(self, id: int, body: ProjectCategoryBean) -> ProjectCategoryJsonBean:
        """Update project category"""
        return await self._put(
            UPDATE_PROJECT_CATEGORY.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectCategoryJsonBean,
        )

    async def search_for_projects(
        self,
        *,
        max_results: int | None = 0,
        query: str | None = "",
        allow_empty_query: bool | None = False,
    ) -> ProjectPickerResultWrapper:
        """Get projects matching query"""
        return await self._get(
            SEARCH_FOR_PROJECTS.path,
            params={"maxResults": max_results, "query": query, "allowEmptyQuery": allow_empty_query},
            model=ProjectPickerResultWrapper,
        )

    async def get_project_1(self, *, key: str | None = None) -> ErrorCollection:
        """Get project key validation"""
        return await self._get(GET_PROJECT_1.path, params={"key": key}, model=ErrorCollection)

    async def get_project_roles_1(self) -> ProjectRoleBean:
        """Get all project roles"""
        return await self._get(GET_PROJECT_ROLES_1.path, model=ProjectRoleBean)

    async def create_project_role(self, body: CreateUpdateRoleRequestBean) -> ProjectRoleBean:
        """Create a new project role"""
        return await self._post(
            CREATE_PROJECT_ROLE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleBean,
        )

    async def delete_project_role(self, id: int, *, swap: int | None = None) -> None:
        """Deletes a role"""
        return await self._delete(DELETE_PROJECT_ROLE.path.replace("{id}", str(id)), params={"swap": swap})

    async def get_project_roles_by_id(self, id: int) -> ProjectRoleBean:
        """Get a specific project role"""
        return await self._get(GET_PROJECT_ROLES_BY_ID.path.replace("{id}", str(id)), model=ProjectRoleBean)

    async def partial_update_project_role(self, id: int, body: CreateUpdateRoleRequestBean) -> ProjectRoleBean:
        """Partially updates a role's name or description"""
        return await self._post(
            PARTIAL_UPDATE_PROJECT_ROLE.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleBean,
        )

    async def fully_update_project_role(self, id: int, body: CreateUpdateRoleRequestBean) -> ProjectRoleBean:
        """Fully updates a role's name and description"""
        return await self._put(
            FULLY_UPDATE_PROJECT_ROLE.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleBean,
        )

    async def delete_project_role_actors_from_role(
        self,
        id: int,
        *,
        user: str | None = None,
        group: str | None = None,
    ) -> ProjectRoleActorsBean:
        """Removes default actor from a role"""
        return await self._delete(
            DELETE_PROJECT_ROLE_ACTORS_FROM_ROLE.path.replace("{id}", str(id)),
            params={"user": user, "group": group},
            model=ProjectRoleActorsBean,
        )

    async def get_project_role_actors_for_role(self, id: int) -> ProjectRoleActorsBean:
        """Get default actors for a role"""
        return await self._get(
            GET_PROJECT_ROLE_ACTORS_FOR_ROLE.path.replace("{id}", str(id)),
            model=ProjectRoleActorsBean,
        )

    async def add_project_role_actors_to_role(self, id: int, body: ActorInputBean) -> ProjectRoleActorsBean:
        """Adds default actors to a role"""
        return await self._post(
            ADD_PROJECT_ROLE_ACTORS_TO_ROLE.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ProjectRoleActorsBean,
        )

    async def get_paginated_versions(
        self,
        *,
        max_results: int | None = 100,
        query: str | None = "",
        project_ids: list[int] | None = None,
        start_at: int | None = 0,
    ) -> VersionBean:
        """Get paginated versions"""
        return await self._get(
            GET_PAGINATED_VERSIONS.path,
            params={"maxResults": max_results, "query": query, "projectIds": project_ids, "startAt": start_at},
            model=VersionBean,
        )

    async def create_version(self, body: VersionBean) -> VersionBean:
        """Create new version"""
        return await self._post(
            CREATE_VERSION.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=VersionBean,
        )

    async def get_remote_version_links(self, *, global_id: str | None = None) -> RemoteEntityLinksJsonBean:
        """Get remote version links by global ID"""
        return await self._get(
            GET_REMOTE_VERSION_LINKS.path,
            params={"globalId": global_id},
            model=RemoteEntityLinksJsonBean,
        )

    async def get_version(self, id: str, *, expand: str | None = None) -> VersionBean:
        """Get version details"""
        return await self._get(GET_VERSION.path.replace("{id}", str(id)), params={"expand": expand}, model=VersionBean)

    async def update_version(self, id: str, body: VersionBean) -> None:
        """Update version details"""
        return await self._put(
            UPDATE_VERSION.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def merge(self, move_issues_to: str, id: str) -> None:
        """Merge versions"""
        return await self._put(MERGE.path.replace("{moveIssuesTo}", str(move_issues_to)).replace("{id}", str(id)))

    async def move_version(self, id: str, body: VersionMoveBean) -> VersionBean:
        """Modify version's sequence"""
        return await self._post(
            MOVE_VERSION.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=VersionBean,
        )

    async def get_version_related_issues(self, id: str) -> VersionIssueCountsBean:
        """Get version related issues count"""
        return await self._get(GET_VERSION_RELATED_ISSUES.path.replace("{id}", str(id)), model=VersionIssueCountsBean)

    async def delete_1(self, id: str, body: DeleteAndReplaceVersionBean) -> None:
        """Delete version and replace values"""
        return await self._post(
            DELETE_1.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_version_unresolved_issues(self, id: str) -> VersionUnresolvedIssueCountsBean:
        """Get version unresolved issues count"""
        return await self._get(
            GET_VERSION_UNRESOLVED_ISSUES.path.replace("{id}", str(id)),
            model=VersionUnresolvedIssueCountsBean,
        )

    async def delete_remote_version_links_by_version_id(self, version_id: str) -> None:
        """Delete all remote version links for version"""
        return await self._delete(
            DELETE_REMOTE_VERSION_LINKS_BY_VERSION_ID.path.replace("{versionId}", str(version_id)),
        )

    async def get_remote_version_links_by_version_id(self, version_id: str) -> RemoteEntityLinksJsonBean:
        """Get remote version links by version ID"""
        return await self._get(
            GET_REMOTE_VERSION_LINKS_BY_VERSION_ID.path.replace("{versionId}", str(version_id)),
            model=RemoteEntityLinksJsonBean,
        )

    async def create_or_update_remote_version_link(self, version_id: str, body: RemoteEntityLinkJsonBean) -> None:
        """Create or update remote version link without global ID"""
        return await self._post(
            CREATE_OR_UPDATE_REMOTE_VERSION_LINK.path.replace("{versionId}", str(version_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def delete_remote_version_link(self, version_id: str, global_id: str) -> None:
        """Delete specific remote version link"""
        return await self._delete(
            DELETE_REMOTE_VERSION_LINK.path.replace("{versionId}", str(version_id)).replace(
                "{globalId}", str(global_id)
            ),
        )

    async def get_remote_version_link(self, version_id: str, global_id: str) -> RemoteEntityLinkJsonBean:
        """Get specific remote version link"""
        return await self._get(
            GET_REMOTE_VERSION_LINK.path.replace("{versionId}", str(version_id)).replace("{globalId}", str(global_id)),
            model=RemoteEntityLinkJsonBean,
        )

    async def create_or_update_remote_version_link_1(
        self,
        version_id: str,
        global_id: str,
        body: RemoteEntityLinkJsonBean,
    ) -> None:
        """Create or update remote version link with global ID"""
        return await self._post(
            CREATE_OR_UPDATE_REMOTE_VERSION_LINK_1.path.replace("{versionId}", str(version_id)).replace(
                "{globalId}", str(global_id)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )


class AsyncIssueResource(AsyncJiraResource):
    async def rank_issues(self, body: IssueRankRequestBean) -> None:
        """Rank issues before or after a given issue"""
        return await self._put(RANK_ISSUES.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_issue_1_0_issue(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        fields: list[StringList] | None = None,
        update_history: bool | None = None,
    ) -> IssueBean:
        """Get a single issue with Agile fields"""
        return await self._get(
            GET_ISSUE_1_0_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"expand": expand, "fields": fields, "updateHistory": update_history},
            model=IssueBean,
        )

    async def get_issue_estimation_for_board(
        self,
        issue_id_or_key: str,
        *,
        board_id: int | None = None,
    ) -> FieldValueBean:
        """Get the estimation of an issue for a board"""
        return await self._get(
            GET_ISSUE_ESTIMATION_FOR_BOARD.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"boardId": board_id},
            model=FieldValueBean,
        )

    async def estimate_issue_for_board(
        self,
        issue_id_or_key: str,
        body: FieldEditBean,
        *,
        board_id: int | None = None,
    ) -> FieldValueBean:
        """Update the estimation of an issue for a board"""
        return await self._put(
            ESTIMATE_ISSUE_FOR_BOARD.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"boardId": board_id},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=FieldValueBean,
        )

    async def get_attachment_meta(self) -> AttachmentMetaBean:
        """Get attachment capabilities"""
        return await self._get(GET_ATTACHMENT_META.path, model=AttachmentMetaBean)

    async def remove_attachment(self, id: str) -> None:
        """Delete an attachment from an issue"""
        return await self._delete(REMOVE_ATTACHMENT.path.replace("{id}", str(id)))

    async def get_attachment(self, id: str) -> AttachmentBean:
        """Get the meta-data for an attachment, including the URI of the actual attached file"""
        return await self._get(GET_ATTACHMENT.path.replace("{id}", str(id)), model=AttachmentBean)

    async def expand_for_humans(self, id: str) -> HumanReadableArchive:
        """Get human-readable attachment expansion"""
        return await self._get(EXPAND_FOR_HUMANS.path.replace("{id}", str(id)), model=HumanReadableArchive)

    async def expand_for_machines(self, id: str) -> AttachmentArchiveImpl:
        """Get raw attachment expansion"""
        return await self._get(EXPAND_FOR_MACHINES.path.replace("{id}", str(id)), model=AttachmentArchiveImpl)

    async def get_properties_keys_1(self, comment_id: str) -> EntityPropertiesKeysBean:
        """Get properties keys of a comment"""
        return await self._get(
            GET_PROPERTIES_KEYS_1_COMMENT_PROPERTIES.path.replace("{commentId}", str(comment_id)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_2(self, property_key: str, comment_id: str) -> None:
        """Delete a property from a comment"""
        return await self._delete(
            DELETE_PROPERTY_2.path.replace("{propertyKey}", str(property_key)).replace("{commentId}", str(comment_id)),
        )

    async def get_property_2(self, property_key: str, comment_id: str) -> EntityPropertyBean:
        """Get a property from a comment"""
        return await self._get(
            GET_PROPERTY_2.path.replace("{propertyKey}", str(property_key)).replace("{commentId}", str(comment_id)),
            model=EntityPropertyBean,
        )

    async def set_property_1(self, property_key: str, comment_id: str) -> None:
        """Set a property on a comment"""
        return await self._put(
            SET_PROPERTY_1_COMMENT_PROPERTIES.path.replace("{propertyKey}", str(property_key)).replace(
                "{commentId}", str(comment_id)
            ),
        )

    async def create_issue(self, body: IssueUpdateBean, *, update_history: bool | None = False) -> IssueCreateResponse:
        """Create an issue or sub-task from json"""
        return await self._post(
            CREATE_ISSUE.path,
            params={"updateHistory": update_history},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IssueCreateResponse,
        )

    async def archive_issues(self, *, notify_users: str | None = None) -> None:
        """Archive list of issues"""
        return await self._post(ARCHIVE_ISSUES.path, params={"notifyUsers": notify_users})

    async def create_issues(self, body: IssuesUpdateBean) -> IssuesCreateResponse:
        """Create an issue or sub-task from json - bulk operation."""
        return await self._post(
            CREATE_ISSUES.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IssuesCreateResponse,
        )

    async def get_create_issue_meta_project_issue_types(
        self,
        project_id_or_key: str,
        *,
        max_results: str | None = None,
        start_at: str | None = None,
    ) -> CreateMetaIssueTypeBean:
        """Get metadata for project issue types"""
        return await self._get(
            GET_CREATE_ISSUE_META_PROJECT_ISSUE_TYPES.path.replace("{projectIdOrKey}", str(project_id_or_key)),
            params={"maxResults": max_results, "startAt": start_at},
            model=CreateMetaIssueTypeBean,
        )

    async def get_create_issue_meta_fields(
        self,
        issue_type_id: str,
        project_id_or_key: str,
        *,
        max_results: str | None = None,
        start_at: str | None = None,
    ) -> FieldMetaBean:
        """Get metadata for issue types used for creating issues"""
        return await self._get(
            GET_CREATE_ISSUE_META_FIELDS.path.replace("{issueTypeId}", str(issue_type_id)).replace(
                "{projectIdOrKey}", str(project_id_or_key)
            ),
            params={"maxResults": max_results, "startAt": start_at},
            model=FieldMetaBean,
        )

    async def get_issue_picker_resource(
        self,
        *,
        current_project_id: str | None = None,
        query: str | None = None,
        current_issue_key: str | None = None,
        show_sub_tasks: str | None = None,
        current_jql: str | None = None,
        show_sub_task_parent: str | None = None,
    ) -> IssuePickerResult:
        """Get suggested issues for auto-completion"""
        return await self._get(
            GET_ISSUE_PICKER_RESOURCE.path,
            params={
                "currentProjectId": current_project_id,
                "query": query,
                "currentIssueKey": current_issue_key,
                "showSubTasks": show_sub_tasks,
                "currentJQL": current_jql,
                "showSubTaskParent": show_sub_task_parent,
            },
            model=IssuePickerResult,
        )

    async def delete_issue(self, issue_id_or_key: str, *, delete_subtasks: str | None = None) -> None:
        """Delete an issue"""
        return await self._delete(
            DELETE_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"deleteSubtasks": delete_subtasks},
        )

    async def get_issue_2_issue(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        fields: str | None = None,
        update_history: str | None = None,
        properties: str | None = None,
    ) -> IssueBean:
        """Get issue for key"""
        return await self._get(
            GET_ISSUE_2_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"expand": expand, "fields": fields, "updateHistory": update_history, "properties": properties},
            model=IssueBean,
        )

    async def edit_issue(self, issue_id_or_key: str, body: IssueUpdateBean, *, notify_users: str | None = None) -> None:
        """Edit an issue from a JSON representation"""
        return await self._put(
            EDIT_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"notifyUsers": notify_users},
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def archive_issue(self, issue_id_or_key: str, *, notify_users: str | None = None) -> None:
        """Archive an issue"""
        return await self._put(
            ARCHIVE_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"notifyUsers": notify_users},
        )

    async def assign(self, issue_id_or_key: str, body: UserBean) -> None:
        """Assign an issue to a user"""
        return await self._put(
            ASSIGN.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def add_attachment(self, issue_id_or_key: str) -> AttachmentJsonBean:
        """Add one or more attachments to an issue"""
        return await self._post(
            ADD_ATTACHMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=AttachmentJsonBean,
        )

    def get_comments(
        self,
        issue_id_or_key: str,
        *,
        expand: str | None = None,
        order_by: str | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[CommentJsonBean]:
        """Get comments for an issue"""
        return self._get_paged(
            GET_COMMENTS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"expand": expand, "orderBy": order_by},
            model=CommentJsonBean,
            items_field="comments",
            start_at=start_at,
            max_results=max_results,
        )

    async def add_comment(
        self,
        issue_id_or_key: str,
        body: CommentJsonBean,
        *,
        expand: str | None = None,
    ) -> CommentJsonBean:
        """Add a comment"""
        return await self._post(
            ADD_COMMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=CommentJsonBean,
        )

    async def delete_comment(self, issue_id_or_key: str, id: str) -> None:
        """Delete a comment"""
        return await self._delete(
            DELETE_COMMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
        )

    async def get_comment(self, issue_id_or_key: str, id: str, *, expand: str | None = None) -> CommentJsonBean:
        """Get a comment by id"""
        return await self._get(
            GET_COMMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
            params={"expand": expand},
            model=CommentJsonBean,
        )

    async def update_comment(
        self,
        issue_id_or_key: str,
        id: str,
        body: CommentJsonBean,
        *,
        expand: str | None = None,
    ) -> CommentJsonBean:
        """Update a comment"""
        return await self._put(
            UPDATE_COMMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=CommentJsonBean,
        )

    async def set_pin_comment(self, issue_id_or_key: str, id: str) -> None:
        """Pin a comment"""
        return await self._put(
            SET_PIN_COMMENT.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
        )

    async def get_edit_issue_meta(self, issue_id_or_key: str) -> EditMetaBean:
        """Get metadata for issue types used for editing issues"""
        return await self._get(
            GET_EDIT_ISSUE_META.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=EditMetaBean,
        )

    async def notify(self, issue_id_or_key: str, body: NotificationJsonBean) -> None:
        """Send notification to recipients"""
        return await self._post(
            NOTIFY.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_pinned_comments(self, issue_id_or_key: str) -> PinnedCommentJsonBean:
        """Get pinned comments for an issue"""
        return await self._get(
            GET_PINNED_COMMENTS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=PinnedCommentJsonBean,
        )

    async def get_properties_keys_2(self, issue_id_or_key: str) -> EntityPropertiesKeysBean:
        """Get keys of all properties for an issue"""
        return await self._get(
            GET_PROPERTIES_KEYS_2.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_3(self, property_key: str, issue_id_or_key: str) -> None:
        """Delete a property from an issue"""
        return await self._delete(
            DELETE_PROPERTY_3.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
        )

    async def get_property_3(self, property_key: str, issue_id_or_key: str) -> EntityPropertyBean:
        """Get the value of a specific property from an issue"""
        return await self._get(
            GET_PROPERTY_3.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
            model=EntityPropertyBean,
        )

    async def set_property_2(self, property_key: str, issue_id_or_key: str) -> None:
        """Update the value of a specific issue's property"""
        return await self._put(
            SET_PROPERTY_2.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
        )

    async def delete_remote_issue_link_by_global_id(self, issue_id_or_key: str, *, global_id: str) -> None:
        """Delete remote issue link"""
        return await self._delete(
            DELETE_REMOTE_ISSUE_LINK_BY_GLOBAL_ID.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"globalId": global_id},
        )

    async def get_remote_issue_links(
        self,
        issue_id_or_key: str,
        *,
        global_id: str | None = None,
    ) -> RemoteIssueLinkBean:
        """Get remote issue links for an issue"""
        return await self._get(
            GET_REMOTE_ISSUE_LINKS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"globalId": global_id},
            model=RemoteIssueLinkBean,
        )

    async def create_or_update_remote_issue_link(
        self,
        issue_id_or_key: str,
        body: RemoteIssueLinkCreateOrUpdateRequest,
    ) -> RemoteIssueLinkBean:
        """Create or update remote issue link"""
        return await self._post(
            CREATE_OR_UPDATE_REMOTE_ISSUE_LINK.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RemoteIssueLinkBean,
        )

    async def delete_remote_issue_link_by_id(self, link_id: str, issue_id_or_key: str) -> None:
        """Delete remote issue link by id"""
        return await self._delete(
            DELETE_REMOTE_ISSUE_LINK_BY_ID.path.replace("{linkId}", str(link_id)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
        )

    async def get_remote_issue_link_by_id(self, link_id: str, issue_id_or_key: str) -> RemoteIssueLinkBean:
        """Get a remote issue link by its id"""
        return await self._get(
            GET_REMOTE_ISSUE_LINK_BY_ID.path.replace("{linkId}", str(link_id)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
            model=RemoteIssueLinkBean,
        )

    async def update_remote_issue_link(
        self,
        link_id: str,
        issue_id_or_key: str,
        body: RemoteIssueLinkCreateOrUpdateRequest,
    ) -> None:
        """Update remote issue link"""
        return await self._put(
            UPDATE_REMOTE_ISSUE_LINK.path.replace("{linkId}", str(link_id)).replace(
                "{issueIdOrKey}", str(issue_id_or_key)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def restore_issue(self, issue_id_or_key: str, *, notify_users: str | None = None) -> None:
        """Restore an archived issue"""
        return await self._put(
            RESTORE_ISSUE.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"notifyUsers": notify_users},
        )

    async def get_sub_tasks(self, issue_id_or_key: str) -> IssueRefJsonBean:
        """Get an issue's subtask list"""
        return await self._get(
            GET_SUB_TASKS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=IssueRefJsonBean,
        )

    async def can_move_sub_task(self, issue_id_or_key: str) -> None:
        """Check if a subtask can be moved"""
        return await self._get(CAN_MOVE_SUB_TASK.path.replace("{issueIdOrKey}", str(issue_id_or_key)))

    async def move_sub_tasks(self, issue_id_or_key: str, body: IssueSubTaskMovePositionBean) -> None:
        """Reorder an issue's subtasks"""
        return await self._post(
            MOVE_SUB_TASKS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_transitions(self, issue_id_or_key: str, *, transition_id: str | None = None) -> TransitionsMetaBean:
        """Get list of transitions possible for an issue"""
        return await self._get(
            GET_TRANSITIONS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"transitionId": transition_id},
            model=TransitionsMetaBean,
        )

    async def do_transition(self, issue_id_or_key: str, body: IssueUpdateBean) -> None:
        """Perform a transition on an issue"""
        return await self._post(
            DO_TRANSITION.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def remove_vote(self, issue_id_or_key: str) -> None:
        """Remove vote from issue"""
        return await self._delete(REMOVE_VOTE.path.replace("{issueIdOrKey}", str(issue_id_or_key)))

    async def get_votes(self, issue_id_or_key: str) -> VoteBean:
        """Get votes for issue"""
        return await self._get(GET_VOTES.path.replace("{issueIdOrKey}", str(issue_id_or_key)), model=VoteBean)

    async def add_vote(self, issue_id_or_key: str) -> None:
        """Add vote to issue"""
        return await self._post(ADD_VOTE.path.replace("{issueIdOrKey}", str(issue_id_or_key)))

    async def remove_watcher_1(
        self,
        issue_id_or_key: str,
        *,
        user_name: str | None = None,
        username: str | None = None,
    ) -> None:
        """Delete watcher from issue"""
        return await self._delete(
            REMOVE_WATCHER_1.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"userName": user_name, "username": username},
        )

    async def get_issue_watchers(self, issue_id_or_key: str) -> WatchersBean:
        """Get list of watchers of issue"""
        return await self._get(
            GET_ISSUE_WATCHERS.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=WatchersBean,
        )

    async def add_watcher_1(self, issue_id_or_key: str, *, user_name: str | None = None) -> None:
        """Add a user as watcher"""
        return await self._post(
            ADD_WATCHER_1.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"userName": user_name},
        )

    def get_issue_worklog(
        self,
        issue_id_or_key: str,
        *,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[Worklog]:
        """Get worklogs for an issue"""
        return self._get_paged(
            GET_ISSUE_WORKLOG.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            model=Worklog,
            items_field="worklogs",
            start_at=start_at,
            max_results=max_results,
        )

    async def add_worklog(
        self,
        issue_id_or_key: str,
        body: Worklog,
        *,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
        reduce_by: str | None = None,
    ) -> Worklog:
        """Add a worklog entry"""
        return await self._post(
            ADD_WORKLOG.path.replace("{issueIdOrKey}", str(issue_id_or_key)),
            params={"newEstimate": new_estimate, "adjustEstimate": adjust_estimate, "reduceBy": reduce_by},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Worklog,
        )

    async def delete_worklog(
        self,
        issue_id_or_key: str,
        id: str,
        *,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
        increase_by: str | None = None,
    ) -> None:
        """Delete a worklog entry"""
        return await self._delete(
            DELETE_WORKLOG.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
            params={"newEstimate": new_estimate, "adjustEstimate": adjust_estimate, "increaseBy": increase_by},
        )

    async def get_worklog(self, issue_id_or_key: str, id: str) -> Worklog:
        """Get a worklog by id"""
        return await self._get(
            GET_WORKLOG.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
            model=Worklog,
        )

    async def update_worklog(
        self,
        issue_id_or_key: str,
        id: str,
        body: Worklog,
        *,
        new_estimate: str | None = None,
        adjust_estimate: str | None = None,
    ) -> Worklog:
        """Update a worklog entry"""
        return await self._put(
            UPDATE_WORKLOG.path.replace("{issueIdOrKey}", str(issue_id_or_key)).replace("{id}", str(id)),
            params={"newEstimate": new_estimate, "adjustEstimate": adjust_estimate},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Worklog,
        )

    async def link_issues(self, body: LinkIssueRequestJsonBean) -> None:
        """Create an issue link between two issues"""
        return await self._post(LINK_ISSUES.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def delete_issue_link(self, link_id: str) -> None:
        """Delete an issue link with the specified id"""
        return await self._delete(DELETE_ISSUE_LINK.path.replace("{linkId}", str(link_id)))

    async def get_issue_link(self, link_id: str) -> IssueLinks:
        """Get an issue link with the specified id"""
        return await self._get(GET_ISSUE_LINK.path.replace("{linkId}", str(link_id)), model=IssueLinks)

    async def get_issue_link_types(self) -> IssueLinkTypesBean:
        """Get list of available issue link types"""
        return await self._get(GET_ISSUE_LINK_TYPES.path, model=IssueLinkTypesBean)

    async def create_issue_link_type(self, body: IssueLinkTypeJsonBean) -> None:
        """Create a new issue link type"""
        return await self._post(CREATE_ISSUE_LINK_TYPE.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def delete_issue_link_type(self, issue_link_type_id: str) -> None:
        """Delete the specified issue link type"""
        return await self._delete(DELETE_ISSUE_LINK_TYPE.path.replace("{issueLinkTypeId}", str(issue_link_type_id)))

    async def get_issue_link_type(self, issue_link_type_id: str) -> IssueLinkTypeJsonBean:
        """Get information about an issue link type"""
        return await self._get(
            GET_ISSUE_LINK_TYPE.path.replace("{issueLinkTypeId}", str(issue_link_type_id)),
            model=IssueLinkTypeJsonBean,
        )

    async def update_issue_link_type(self, issue_link_type_id: str, body: IssueLinkTypeJsonBean) -> None:
        """Update the specified issue link type"""
        return await self._put(
            UPDATE_ISSUE_LINK_TYPE.path.replace("{issueLinkTypeId}", str(issue_link_type_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_auto_complete(self) -> AutoCompleteResponseBean:
        """Get auto complete data for JQL searches"""
        return await self._get(GET_AUTO_COMPLETE.path, model=AutoCompleteResponseBean)

    async def get_field_auto_complete_for_query_string(
        self,
        *,
        predicate_value: str | None = None,
        predicate_name: str | None = None,
        field_name: str | None = None,
        field_value: str | None = None,
    ) -> AutoCompleteResultWrapper:
        """Get auto complete suggestions for JQL search"""
        return await self._get(
            GET_FIELD_AUTO_COMPLETE_FOR_QUERY_STRING.path,
            params={
                "predicateValue": predicate_value,
                "predicateName": predicate_name,
                "fieldName": field_name,
                "fieldValue": field_value,
            },
            model=AutoCompleteResultWrapper,
        )

    def search_1(
        self,
        *,
        expand: StringList | None = None,
        jql: str | None = None,
        validate_query: bool | None = True,
        fields: list[StringList] | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[IssueBean]:
        """Get issues using JQL"""
        return self._get_paged(
            SEARCH_1.path,
            params={"expand": expand, "jql": jql, "validateQuery": validate_query, "fields": fields},
            model=IssueBean,
            items_field="issues",
            start_at=start_at,
            max_results=max_results,
        )

    def search_using_search_request(
        self,
        body: SearchRequestBean,
        *,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[IssueBean]:
        """Perform search with JQL"""
        return self._request_paged(
            "POST",
            SEARCH_USING_SEARCH_REQUEST.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IssueBean,
            items_field="issues",
            start_at=start_at,
            max_results=max_results,
        )

    def get_ids_of_worklogs_deleted_since(
        self,
        *,
        since: int | None = 0,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[WorklogChangeBean]:
        """Returns worklogs deleted since given time."""
        return self._get_paged(
            GET_IDS_OF_WORKLOGS_DELETED_SINCE.path,
            params={"since": since},
            model=WorklogChangeBean,
            items_field="values",
            start_at=start_at,
            max_results=max_results,
        )

    async def get_worklogs_for_ids(self, body: WorklogIdsRequestBean) -> Worklog:
        """Returns worklogs for given ids."""
        return await self._post(
            GET_WORKLOGS_FOR_IDS.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=Worklog,
        )

    def get_ids_of_worklogs_modified_since(
        self,
        *,
        since: int | None = 0,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[WorklogChangeBean]:
        """Returns worklogs updated since given time."""
        return self._get_paged(
            GET_IDS_OF_WORKLOGS_MODIFIED_SINCE.path,
            params={"since": since},
            model=WorklogChangeBean,
            items_field="values",
            start_at=start_at,
            max_results=max_results,
        )


class AsyncIssueMetaResource(AsyncJiraResource):
    async def get_custom_field_option(self, id: str) -> CustomFieldOptionBean:
        """Get custom field option by ID"""
        return await self._get(GET_CUSTOM_FIELD_OPTION.path.replace("{id}", str(id)), model=CustomFieldOptionBean)

    async def bulk_delete_custom_fields(self, *, ids: str) -> BulkDeleteResponseBean:
        """Delete custom fields in bulk"""
        return await self._delete(BULK_DELETE_CUSTOM_FIELDS.path, params={"ids": ids}, model=BulkDeleteResponseBean)

    async def get_custom_fields(
        self,
        *,
        sort_column: str | None = None,
        types: str | None = None,
        search: str | None = None,
        max_results: str | None = None,
        sort_order: str | None = None,
        screen_ids: str | None = None,
        last_value_update: str | None = None,
        project_ids: str | None = None,
        start_at: str | None = None,
    ) -> CustomFieldBean:
        """Get custom fields with pagination"""
        return await self._get(
            GET_CUSTOM_FIELDS.path,
            params={
                "sortColumn": sort_column,
                "types": types,
                "search": search,
                "maxResults": max_results,
                "sortOrder": sort_order,
                "screenIds": screen_ids,
                "lastValueUpdate": last_value_update,
                "projectIds": project_ids,
                "startAt": start_at,
            },
            model=CustomFieldBean,
        )

    async def get_custom_field_options(
        self,
        custom_field_id: str,
        *,
        max_results: str | None = None,
        issue_type_ids: str | None = None,
        query: str | None = None,
        page: str | None = None,
        project_ids: str | None = None,
    ) -> CustomFieldOptionsBean:
        """Get custom field options"""
        return await self._get(
            GET_CUSTOM_FIELD_OPTIONS.path.replace("{customFieldId}", str(custom_field_id)),
            params={
                "maxResults": max_results,
                "issueTypeIds": issue_type_ids,
                "query": query,
                "page": page,
                "projectIds": project_ids,
            },
            model=CustomFieldOptionsBean,
        )

    async def get_fields(self) -> FieldBean:
        """Get all fields, both System and Custom"""
        return await self._get(GET_FIELDS.path, model=FieldBean)

    async def create_custom_field(self, body: CustomFieldDefinitionJsonBean) -> FieldBean:
        """Create a custom field using a definition"""
        return await self._post(
            CREATE_CUSTOM_FIELD.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=FieldBean,
        )

    async def get_issue_all_types(self) -> IssueTypeJsonBean:
        """Get list of all issue types visible to user"""
        return await self._get(GET_ISSUE_ALL_TYPES.path, model=IssueTypeJsonBean)

    async def create_issue_type(self, body: IssueTypeCreateBean) -> None:
        """Create an issue type from JSON representation"""
        return await self._post(CREATE_ISSUE_TYPE.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_paginated_issue_types(
        self,
        *,
        max_results: int | None = 100,
        query: str | None = "",
        project_ids: list[int] | None = None,
        start_at: int | None = 0,
    ) -> IssueTypeJsonBean:
        """Get paginated list of filtered issue types"""
        return await self._get(
            GET_PAGINATED_ISSUE_TYPES.path,
            params={"maxResults": max_results, "query": query, "projectIds": project_ids, "startAt": start_at},
            model=IssueTypeJsonBean,
        )

    async def delete_issue_type_1(self, id: str, alternative_issue_type_id: str) -> None:
        """Delete specified issue type and migrate associated issues"""
        return await self._delete(
            DELETE_ISSUE_TYPE_1.path.replace("{id}", str(id)).replace(
                "{alternativeIssueTypeId}", str(alternative_issue_type_id)
            ),
        )

    async def get_issue_type_1(self, id: str) -> IssueTypeJsonBean:
        """Get full representation of issue type by id"""
        return await self._get(GET_ISSUE_TYPE_1.path.replace("{id}", str(id)), model=IssueTypeJsonBean)

    async def update_issue_type(self, id: str, body: IssueTypeUpdateBean) -> None:
        """Update specified issue type from JSON representation"""
        return await self._put(
            UPDATE_ISSUE_TYPE.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_alternative_issue_types(self, id: str) -> IssueTypeJsonBean:
        """Get list of alternative issue types for given id"""
        return await self._get(GET_ALTERNATIVE_ISSUE_TYPES.path.replace("{id}", str(id)), model=IssueTypeJsonBean)

    async def create_avatar_from_temporary_1(self, id: str, body: AvatarCroppingBean) -> AvatarBean:
        """Convert temporary avatar into a real avatar"""
        return await self._post(
            CREATE_AVATAR_FROM_TEMPORARY_1.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarBean,
        )

    async def store_temporary_avatar_using_multi_part(self, id: str, body: FilePart) -> AvatarCroppingBean:
        """Create temporary avatar using multipart for issue type"""
        return await self._post(
            STORE_TEMPORARY_AVATAR_USING_MULTI_PART.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarCroppingBean,
        )

    async def get_property_keys(self, issue_type_id: str) -> EntityPropertiesKeysBean:
        """Get all properties keys for issue type"""
        return await self._get(
            GET_PROPERTY_KEYS.path.replace("{issueTypeId}", str(issue_type_id)),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_4(self, property_key: str, issue_type_id: str) -> None:
        """Delete specified issue type's property"""
        return await self._delete(
            DELETE_PROPERTY_4.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueTypeId}", str(issue_type_id)
            ),
        )

    async def get_property_4(self, property_key: str, issue_type_id: str) -> EntityPropertyBean:
        """Get value of specified issue type's property"""
        return await self._get(
            GET_PROPERTY_4.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueTypeId}", str(issue_type_id)
            ),
            model=EntityPropertyBean,
        )

    async def set_property_3(self, property_key: str, issue_type_id: str, body: PropertyBean) -> None:
        """Update specified issue type's property"""
        return await self._put(
            SET_PROPERTY_3.path.replace("{propertyKey}", str(property_key)).replace(
                "{issueTypeId}", str(issue_type_id)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_all_issue_type_schemes(self) -> IssueTypeSchemeListBean:
        """Get list of all issue type schemes visible to user"""
        return await self._get(GET_ALL_ISSUE_TYPE_SCHEMES.path, model=IssueTypeSchemeListBean)

    async def create_issue_type_scheme(self, body: IssueTypeSchemeCreateUpdateBean) -> IssueTypeSchemeBean:
        """Create an issue type scheme from JSON representation"""
        return await self._post(
            CREATE_ISSUE_TYPE_SCHEME.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IssueTypeSchemeBean,
        )

    async def delete_issue_type_scheme(self, scheme_id: str) -> None:
        """Delete specified issue type scheme"""
        return await self._delete(DELETE_ISSUE_TYPE_SCHEME.path.replace("{schemeId}", str(scheme_id)))

    async def get_issue_type_scheme(self, scheme_id: str) -> IssueTypeSchemeBean:
        """Get full representation of issue type scheme by id"""
        return await self._get(
            GET_ISSUE_TYPE_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            model=IssueTypeSchemeBean,
        )

    async def update_issue_type_scheme(
        self,
        scheme_id: str,
        body: IssueTypeSchemeCreateUpdateBean,
    ) -> IssueTypeSchemeBean:
        """Update specified issue type scheme from JSON representation"""
        return await self._put(
            UPDATE_ISSUE_TYPE_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IssueTypeSchemeBean,
        )

    async def remove_all_project_associations(self, scheme_id: str) -> None:
        """Remove all project associations for specified scheme"""
        return await self._delete(REMOVE_ALL_PROJECT_ASSOCIATIONS.path.replace("{schemeId}", str(scheme_id)))

    async def get_associated_projects(self, scheme_id: str, *, expand: str | None = None) -> ProjectBean:
        """Get all of the associated projects for specified scheme"""
        return await self._get(
            GET_ASSOCIATED_PROJECTS.path.replace("{schemeId}", str(scheme_id)),
            params={"expand": expand},
            model=ProjectBean,
        )

    async def add_project_associations_to_scheme(self, scheme_id: str, body: AssociateProjectsBean) -> None:
        """Add project associations to scheme"""
        return await self._post(
            ADD_PROJECT_ASSOCIATIONS_TO_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def set_project_associations_for_scheme(self, scheme_id: str, body: AssociateProjectsBean) -> None:
        """Set project associations for scheme"""
        return await self._put(
            SET_PROJECT_ASSOCIATIONS_FOR_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def remove_project_association(self, proj_id_or_key: str, scheme_id: str) -> None:
        """Remove given project association for specified scheme"""
        return await self._delete(
            REMOVE_PROJECT_ASSOCIATION.path.replace("{projIdOrKey}", str(proj_id_or_key)).replace(
                "{schemeId}", str(scheme_id)
            ),
        )

    async def get_priorities(self) -> PriorityJsonBean:
        """Get all issue priorities"""
        return await self._get(GET_PRIORITIES.path, model=PriorityJsonBean)

    async def get_priorities_1(
        self,
        *,
        max_results: int | None = 100,
        query: str | None = "",
        project_ids: list[int] | None = None,
        start_at: int | None = 0,
    ) -> PriorityJsonBean:
        """Get paginated issue priorities"""
        return await self._get(
            GET_PRIORITIES_1.path,
            params={"maxResults": max_results, "query": query, "projectIds": project_ids, "startAt": start_at},
            model=PriorityJsonBean,
        )

    async def get_priority(self, id: str) -> PriorityJsonBean:
        """Get an issue priority by ID"""
        return await self._get(GET_PRIORITY.path.replace("{id}", str(id)), model=PriorityJsonBean)

    def get_priority_schemes(
        self,
        *,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[PrioritySchemeBean]:
        """Get all priority schemes"""
        return self._get_paged(
            GET_PRIORITY_SCHEMES.path,
            model=PrioritySchemeBean,
            items_field="schemes",
            start_at=start_at,
            max_results=max_results,
        )

    async def create_priority_scheme(self, body: PrioritySchemeUpdateBean) -> PrioritySchemeBean:
        """Create new priority scheme"""
        return await self._post(
            CREATE_PRIORITY_SCHEME.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PrioritySchemeBean,
        )

    async def delete_priority_scheme(self, scheme_id: int) -> None:
        """Delete a priority scheme"""
        return await self._delete(DELETE_PRIORITY_SCHEME.path.replace("{schemeId}", str(scheme_id)))

    async def get_priority_scheme(self, scheme_id: int) -> PrioritySchemeBean:
        """Get a priority scheme by ID"""
        return await self._get(GET_PRIORITY_SCHEME.path.replace("{schemeId}", str(scheme_id)), model=PrioritySchemeBean)

    async def update_priority_scheme(self, scheme_id: int, body: PrioritySchemeUpdateBean) -> PrioritySchemeBean:
        """Update a priority scheme"""
        return await self._put(
            UPDATE_PRIORITY_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PrioritySchemeBean,
        )

    async def get_resolutions(self) -> ResolutionJsonBean:
        """Get all resolutions"""
        return await self._get(GET_RESOLUTIONS.path, model=ResolutionJsonBean)

    async def get_paginated_resolutions(
        self,
        *,
        max_results: int | None = 100,
        query: str | None = "",
        start_at: int | None = 0,
    ) -> ResolutionBean:
        """Get paginated filtered resolutions"""
        return await self._get(
            GET_PAGINATED_RESOLUTIONS.path,
            params={"maxResults": max_results, "query": query, "startAt": start_at},
            model=ResolutionBean,
        )

    async def get_resolution(self, id: str) -> ResolutionJsonBean:
        """Get a resolution by ID"""
        return await self._get(GET_RESOLUTION.path.replace("{id}", str(id)), model=ResolutionJsonBean)

    async def get_all_screens(
        self,
        *,
        search: str | None = None,
        expand: str | None = None,
        max_results: str | None = None,
        start_at: str | None = None,
    ) -> None:
        """Get available field screens"""
        return await self._get(
            GET_ALL_SCREENS.path,
            params={"search": search, "expand": expand, "maxResults": max_results, "startAt": start_at},
        )

    async def add_field_to_default_screen(self, field_id: str) -> None:
        """Add field to default screen"""
        return await self._post(ADD_FIELD_TO_DEFAULT_SCREEN.path.replace("{fieldId}", str(field_id)))

    async def get_fields_to_add(self, screen_id: int) -> ScreenableFieldBean:
        """Get available fields for screen"""
        return await self._get(GET_FIELDS_TO_ADD.path.replace("{screenId}", str(screen_id)), model=ScreenableFieldBean)

    async def get_all_tabs(self, screen_id: int, *, project_key: str | None = None) -> ScreenableTabBean:
        """Get all tabs for a screen"""
        return await self._get(
            GET_ALL_TABS.path.replace("{screenId}", str(screen_id)),
            params={"projectKey": project_key},
            model=ScreenableTabBean,
        )

    async def add_tab(self, screen_id: int, body: ScreenableTabBean) -> ScreenableTabBean:
        """Create tab for a screen"""
        return await self._post(
            ADD_TAB.path.replace("{screenId}", str(screen_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ScreenableTabBean,
        )

    async def delete_tab(self, tab_id: int, screen_id: int) -> None:
        """Delete a tab from a screen"""
        return await self._delete(DELETE_TAB.path.replace("{tabId}", str(tab_id)).replace("{screenId}", str(screen_id)))

    async def rename_tab(self, tab_id: int, screen_id: int, body: ScreenableTabBean) -> ScreenableTabBean:
        """Rename a tab on a screen"""
        return await self._put(
            RENAME_TAB.path.replace("{tabId}", str(tab_id)).replace("{screenId}", str(screen_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ScreenableTabBean,
        )

    async def get_all_fields(
        self,
        tab_id: int,
        screen_id: int,
        *,
        project_key: str | None = None,
    ) -> ScreenableFieldBean:
        """Get all fields for a tab"""
        return await self._get(
            GET_ALL_FIELDS.path.replace("{tabId}", str(tab_id)).replace("{screenId}", str(screen_id)),
            params={"projectKey": project_key},
            model=ScreenableFieldBean,
        )

    async def add_field(self, tab_id: int, screen_id: int, body: AddFieldBean) -> ScreenableFieldBean:
        """Add field to a tab"""
        return await self._post(
            ADD_FIELD.path.replace("{tabId}", str(tab_id)).replace("{screenId}", str(screen_id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ScreenableFieldBean,
        )

    async def remove_field(self, tab_id: int, screen_id: int, id: str) -> None:
        """Remove field from tab"""
        return await self._delete(
            REMOVE_FIELD.path.replace("{tabId}", str(tab_id))
            .replace("{screenId}", str(screen_id))
            .replace("{id}", str(id)),
        )

    async def move_field(self, tab_id: int, screen_id: int, id: str, body: MoveFieldBean) -> None:
        """Move field on a tab"""
        return await self._post(
            MOVE_FIELD.path.replace("{tabId}", str(tab_id))
            .replace("{screenId}", str(screen_id))
            .replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def update_show_when_empty_indicator(self, tab_id: int, screen_id: int, new_value: bool, id: str) -> None:
        """Update 'showWhenEmptyIndicator' for a field"""
        return await self._put(
            UPDATE_SHOW_WHEN_EMPTY_INDICATOR.path.replace("{tabId}", str(tab_id))
            .replace("{screenId}", str(screen_id))
            .replace("{newValue}", str(new_value))
            .replace("{id}", str(id)),
        )

    async def move_tab(self, tab_id: int, screen_id: int, pos: int) -> None:
        """Move tab position"""
        return await self._post(
            MOVE_TAB.path.replace("{tabId}", str(tab_id))
            .replace("{screenId}", str(screen_id))
            .replace("{pos}", str(pos)),
        )

    async def get_statuses(self) -> StatusJsonBean:
        """Get all statuses"""
        return await self._get(GET_STATUSES.path, model=StatusJsonBean)

    async def get_paginated_statuses(
        self,
        *,
        issue_type_ids: list[str] | None = None,
        max_results: int | None = 100,
        query: str | None = "",
        project_ids: list[int] | None = None,
        start_at: int | None = 0,
    ) -> StatusJsonBean:
        """Get paginated filtered statuses"""
        return await self._get(
            GET_PAGINATED_STATUSES.path,
            params={
                "issueTypeIds": issue_type_ids,
                "maxResults": max_results,
                "query": query,
                "projectIds": project_ids,
                "startAt": start_at,
            },
            model=StatusJsonBean,
        )

    async def get_status(self, id_or_name: str) -> StatusJsonBean:
        """Get status by ID or name"""
        return await self._get(GET_STATUS.path.replace("{idOrName}", str(id_or_name)), model=StatusJsonBean)

    async def get_status_categories(
        self,
        *,
        request: str | None = None,
        uri_info: str | None = None,
    ) -> StatusCategoryJsonBean:
        """Get all status categories"""
        return await self._get(
            GET_STATUS_CATEGORIES.path,
            params={"request": request, "uriInfo": uri_info},
            model=StatusCategoryJsonBean,
        )

    async def get_status_category(self, id_or_key: str) -> StatusCategoryJsonBean:
        """Get status category by ID or key"""
        return await self._get(
            GET_STATUS_CATEGORY.path.replace("{idOrKey}", str(id_or_key)),
            model=StatusCategoryJsonBean,
        )

    async def get_all_workflows(self, *, workflow_name: str | None = None) -> None:
        """Get all workflows"""
        return await self._get(GET_ALL_WORKFLOWS.path, params={"workflowName": workflow_name})

    async def create_scheme(self, body: WorkflowSchemeBean) -> None:
        """Create a new workflow scheme"""
        return await self._post(CREATE_SCHEME.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def delete_scheme(self, id: int) -> None:
        """Delete the specified workflow scheme"""
        return await self._delete(DELETE_SCHEME.path.replace("{id}", str(id)))

    async def get_by_id(self, id: int, *, return_draft_if_exists: bool | None = False) -> WorkflowSchemeBean:
        """Get requested workflow scheme by ID"""
        return await self._get(
            GET_BY_ID.path.replace("{id}", str(id)),
            params={"returnDraftIfExists": return_draft_if_exists},
            model=WorkflowSchemeBean,
        )

    async def update(self, id: int, body: WorkflowSchemeBean) -> WorkflowSchemeBean:
        """Update a specified workflow scheme"""
        return await self._put(
            UPDATE.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def create_draft_for_parent(self, id: int) -> WorkflowSchemeBean:
        """Create a draft for a workflow scheme"""
        return await self._post(CREATE_DRAFT_FOR_PARENT.path.replace("{id}", str(id)), model=WorkflowSchemeBean)

    async def delete_default(self, id: int, *, update_draft_if_needed: bool | None = None) -> WorkflowSchemeBean:
        """Remove default workflow from a scheme"""
        return await self._delete(
            DELETE_DEFAULT.path.replace("{id}", str(id)),
            params={"updateDraftIfNeeded": update_draft_if_needed},
            model=WorkflowSchemeBean,
        )

    async def get_default(self, id: int, *, return_draft_if_exists: bool | None = False) -> WorkflowSchemeBean:
        """Get default workflow for a scheme"""
        return await self._get(
            GET_DEFAULT.path.replace("{id}", str(id)),
            params={"returnDraftIfExists": return_draft_if_exists},
            model=WorkflowSchemeBean,
        )

    async def update_default(self, id: int, body: DefaultBean) -> WorkflowSchemeBean:
        """Update default workflow for a scheme"""
        return await self._put(
            UPDATE_DEFAULT.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_draft_by_id(self, id: int) -> None:
        """Delete the specified draft workflow scheme"""
        return await self._delete(DELETE_DRAFT_BY_ID.path.replace("{id}", str(id)))

    async def get_draft_by_id(self, id: int) -> WorkflowSchemeBean:
        """Get requested draft workflow scheme by ID"""
        return await self._get(GET_DRAFT_BY_ID.path.replace("{id}", str(id)), model=WorkflowSchemeBean)

    async def update_draft(self, id: int, body: WorkflowSchemeBean) -> WorkflowSchemeBean:
        """Update a draft workflow scheme"""
        return await self._put(
            UPDATE_DRAFT.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_draft_default(self, id: int) -> WorkflowSchemeBean:
        """Remove default workflow from a draft scheme"""
        return await self._delete(DELETE_DRAFT_DEFAULT.path.replace("{id}", str(id)), model=WorkflowSchemeBean)

    async def get_draft_default(self, id: int) -> WorkflowSchemeBean:
        """Get default workflow for a draft scheme"""
        return await self._get(GET_DRAFT_DEFAULT.path.replace("{id}", str(id)), model=WorkflowSchemeBean)

    async def update_draft_default(self, id: int, body: DefaultBean) -> WorkflowSchemeBean:
        """Update default workflow for a draft scheme"""
        return await self._put(
            UPDATE_DRAFT_DEFAULT.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_draft_issue_type(self, issue_type: str, id: int) -> WorkflowSchemeBean:
        """Delete an issue type mapping from a draft scheme"""
        return await self._delete(
            DELETE_DRAFT_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            model=WorkflowSchemeBean,
        )

    async def get_draft_issue_type(self, issue_type: str, id: int) -> IssueTypeMappingBean:
        """Get issue type mapping for a draft scheme"""
        return await self._get(
            GET_DRAFT_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            model=IssueTypeMappingBean,
        )

    async def set_draft_issue_type(self, issue_type: str, id: int, body: IssueTypeMappingBean) -> WorkflowSchemeBean:
        """Set an issue type mapping for a draft scheme"""
        return await self._put(
            SET_DRAFT_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_draft_workflow_mapping(self, id: int, *, workflow_name: str | None = None) -> WorkflowSchemeBean:
        """Delete a workflow mapping from a draft scheme"""
        return await self._delete(
            DELETE_DRAFT_WORKFLOW_MAPPING.path.replace("{id}", str(id)),
            params={"workflowName": workflow_name},
            model=WorkflowSchemeBean,
        )

    async def get_draft_workflow(self, id: int, *, workflow_name: str | None = None) -> WorkflowSchemeBean:
        """Get draft workflow mappings"""
        return await self._get(
            GET_DRAFT_WORKFLOW.path.replace("{id}", str(id)),
            params={"workflowName": workflow_name},
            model=WorkflowSchemeBean,
        )

    async def update_draft_workflow_mapping(
        self,
        id: int,
        body: WorkflowMappingBean,
        *,
        workflow_name: str | None = None,
    ) -> WorkflowSchemeBean:
        """Update a workflow mapping in a draft scheme"""
        return await self._put(
            UPDATE_DRAFT_WORKFLOW_MAPPING.path.replace("{id}", str(id)),
            params={"workflowName": workflow_name},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_issue_type(
        self,
        issue_type: str,
        id: int,
        *,
        update_draft_if_needed: bool | None = None,
    ) -> WorkflowSchemeBean:
        """Delete an issue type mapping from a scheme"""
        return await self._delete(
            DELETE_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            params={"updateDraftIfNeeded": update_draft_if_needed},
            model=WorkflowSchemeBean,
        )

    async def get_issue_type(
        self,
        issue_type: str,
        id: int,
        *,
        return_draft_if_exists: bool | None = False,
    ) -> IssueTypeMappingBean:
        """Get issue type mapping for a scheme"""
        return await self._get(
            GET_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            params={"returnDraftIfExists": return_draft_if_exists},
            model=IssueTypeMappingBean,
        )

    async def set_issue_type(self, issue_type: str, id: int, body: IssueTypeMappingBean) -> WorkflowSchemeBean:
        """Set an issue type mapping for a scheme"""
        return await self._put(
            SET_ISSUE_TYPE.path.replace("{issueType}", str(issue_type)).replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )

    async def delete_workflow_mapping(
        self,
        id: int,
        *,
        update_draft_if_needed: bool | None = None,
        workflow_name: str | None = None,
    ) -> WorkflowSchemeBean:
        """Delete a workflow mapping from a scheme"""
        return await self._delete(
            DELETE_WORKFLOW_MAPPING.path.replace("{id}", str(id)),
            params={"updateDraftIfNeeded": update_draft_if_needed, "workflowName": workflow_name},
            model=WorkflowSchemeBean,
        )

    async def get_workflow(
        self,
        id: int,
        *,
        workflow_name: str | None = None,
        return_draft_if_exists: bool | None = False,
    ) -> WorkflowSchemeBean:
        """Get workflow mappings for a scheme"""
        return await self._get(
            GET_WORKFLOW.path.replace("{id}", str(id)),
            params={"workflowName": workflow_name, "returnDraftIfExists": return_draft_if_exists},
            model=WorkflowSchemeBean,
        )

    async def update_workflow_mapping(
        self,
        id: int,
        body: WorkflowMappingBean,
        *,
        workflow_name: str | None = None,
    ) -> WorkflowSchemeBean:
        """Update a workflow mapping in a scheme"""
        return await self._put(
            UPDATE_WORKFLOW_MAPPING.path.replace("{id}", str(id)),
            params={"workflowName": workflow_name},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=WorkflowSchemeBean,
        )


class AsyncPermissionSecurityResource(AsyncJiraResource):
    async def get_issue_security_schemes(self) -> SecuritySchemesJsonBean:
        """Get all issue security schemes"""
        return await self._get(GET_ISSUE_SECURITY_SCHEMES.path, model=SecuritySchemesJsonBean)

    async def get_issue_security_scheme(self, id: str) -> SecuritySchemeJsonBean:
        """Get specific issue security scheme by id"""
        return await self._get(GET_ISSUE_SECURITY_SCHEME.path.replace("{id}", str(id)), model=SecuritySchemeJsonBean)

    async def get_permissions(
        self,
        *,
        issue_id: str | None = None,
        project_key: str | None = None,
        issue_key: str | None = None,
        project_id: str | None = None,
    ) -> PermissionsJsonBean:
        """Get permissions for the logged in user"""
        return await self._get(
            GET_PERMISSIONS.path,
            params={"issueId": issue_id, "projectKey": project_key, "issueKey": issue_key, "projectId": project_id},
            model=PermissionsJsonBean,
        )

    async def get_notification_schemes(
        self,
        *,
        expand: str | None = None,
        max_results: int | None = None,
        start_at: int | None = None,
    ) -> PageBean:
        """Get paginated notification schemes"""
        return await self._get(
            GET_NOTIFICATION_SCHEMES.path,
            params={"expand": expand, "maxResults": max_results, "startAt": start_at},
            model=PageBean,
        )

    async def get_notification_scheme(self, id: int, *, expand: str | None = None) -> NotificationSchemeBean:
        """Get full notification scheme details"""
        return await self._get(
            GET_NOTIFICATION_SCHEME.path.replace("{id}", str(id)),
            params={"expand": expand},
            model=NotificationSchemeBean,
        )

    async def get_all_permissions(self) -> PermissionsJsonBean:
        """Get all permissions present in Jira instance"""
        return await self._get(GET_ALL_PERMISSIONS.path, model=PermissionsJsonBean)

    async def get_permission_schemes(self, *, expand: str | None = None) -> PermissionSchemesBean:
        """Get all permission schemes"""
        return await self._get(GET_PERMISSION_SCHEMES.path, params={"expand": expand}, model=PermissionSchemesBean)

    async def create_permission_scheme(
        self,
        body: PermissionSchemeBean,
        *,
        expand: str | None = None,
    ) -> PermissionSchemeBean:
        """Create a new permission scheme"""
        return await self._post(
            CREATE_PERMISSION_SCHEME.path,
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PermissionSchemeBean,
        )

    async def get_scheme_attribute(
        self,
        permission_scheme_id: int,
        attribute_key: str,
    ) -> PermissionSchemeAttributeBean:
        """Get scheme attribute by key"""
        return await self._get(
            GET_SCHEME_ATTRIBUTE.path.replace("{permissionSchemeId}", str(permission_scheme_id)).replace(
                "{attributeKey}", str(attribute_key)
            ),
            model=PermissionSchemeAttributeBean,
        )

    async def set_scheme_attribute(self, permission_scheme_id: int, key: str) -> None:
        """Update or insert a scheme attribute"""
        return await self._put(
            SET_SCHEME_ATTRIBUTE.path.replace("{permissionSchemeId}", str(permission_scheme_id)).replace(
                "{key}", str(key)
            ),
        )

    async def delete_permission_scheme(self, scheme_id: int) -> None:
        """Delete a permission scheme by ID"""
        return await self._delete(DELETE_PERMISSION_SCHEME.path.replace("{schemeId}", str(scheme_id)))

    async def get_permission_scheme(self, scheme_id: int, *, expand: str | None = None) -> PermissionSchemeBean:
        """Get a permission scheme by ID"""
        return await self._get(
            GET_PERMISSION_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            params={"expand": expand},
            model=PermissionSchemeBean,
        )

    async def update_permission_scheme(
        self,
        scheme_id: int,
        body: PermissionSchemeBean,
        *,
        expand: str | None = None,
    ) -> PermissionSchemeBean:
        """Update a permission scheme"""
        return await self._put(
            UPDATE_PERMISSION_SCHEME.path.replace("{schemeId}", str(scheme_id)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PermissionSchemeBean,
        )

    async def get_permission_scheme_grants(self, scheme_id: int, *, expand: str | None = None) -> PermissionGrantsBean:
        """Get all permission grants of a scheme"""
        return await self._get(
            GET_PERMISSION_SCHEME_GRANTS.path.replace("{schemeId}", str(scheme_id)),
            params={"expand": expand},
            model=PermissionGrantsBean,
        )

    async def create_permission_grant(
        self,
        scheme_id: int,
        body: PermissionGrantBean,
        *,
        expand: str | None = None,
    ) -> PermissionGrantBean:
        """Create a permission grant in a scheme"""
        return await self._post(
            CREATE_PERMISSION_GRANT.path.replace("{schemeId}", str(scheme_id)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=PermissionGrantBean,
        )

    async def delete_permission_scheme_entity(self, permission_id: int, scheme_id: int) -> None:
        """Delete a permission grant from a scheme"""
        return await self._delete(
            DELETE_PERMISSION_SCHEME_ENTITY.path.replace("{permissionId}", str(permission_id)).replace(
                "{schemeId}", str(scheme_id)
            ),
        )

    async def get_permission_scheme_grant(
        self,
        permission_id: int,
        scheme_id: int,
        *,
        expand: str | None = None,
    ) -> PermissionGrantBean:
        """Get a permission grant by ID"""
        return await self._get(
            GET_PERMISSION_SCHEME_GRANT.path.replace("{permissionId}", str(permission_id)).replace(
                "{schemeId}", str(scheme_id)
            ),
            params={"expand": expand},
            model=PermissionGrantBean,
        )

    async def get_issuesecuritylevel(self, id: str) -> SecurityLevelJsonBean:
        """Get a security level by ID"""
        return await self._get(GET_ISSUESECURITYLEVEL.path.replace("{id}", str(id)), model=SecurityLevelJsonBean)


class AsyncUserResource(AsyncJiraResource):
    async def get_all(self) -> ApplicationRoleBean:
        """Get all application roles in the system"""
        return await self._get(GET_ALL.path, model=ApplicationRoleBean)

    async def put_bulk(self, body: ApplicationRoleBean) -> ApplicationRoleBean:
        """Update application roles"""
        return await self._put(
            PUT_BULK.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ApplicationRoleBean,
        )

    async def get_4(self, key: str) -> ApplicationRoleBean:
        """Get application role by key"""
        return await self._get(GET_4.path.replace("{key}", str(key)), model=ApplicationRoleBean)

    async def put_2(self, key: str, body: ApplicationRoleBean) -> ApplicationRoleBean:
        """Update application role"""
        return await self._put(
            PUT_2.path.replace("{key}", str(key)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ApplicationRoleBean,
        )

    async def find_users_and_groups(
        self,
        *,
        issue_type_id: str | None = None,
        max_results: str | None = None,
        query: str | None = None,
        show_avatar: str | None = None,
        project_id: str | None = None,
        field_id: str | None = None,
    ) -> UsersAndGroupsBean:
        """Get users and groups matching query with highlighting"""
        return await self._get(
            FIND_USERS_AND_GROUPS.path,
            params={
                "issueTypeId": issue_type_id,
                "maxResults": max_results,
                "query": query,
                "showAvatar": show_avatar,
                "projectId": project_id,
                "fieldId": field_id,
            },
            model=UsersAndGroupsBean,
        )

    async def remove_preference(self, *, key: str | None = None) -> None:
        """Delete user preference"""
        return await self._delete(REMOVE_PREFERENCE.path, params={"key": key})

    async def get_preference(self, *, key: str | None = None) -> None:
        """Get user preference by key"""
        return await self._get(GET_PREFERENCE.path, params={"key": key})

    async def set_preference(self, *, key: str | None = None) -> None:
        """Update user preference"""
        return await self._put(SET_PREFERENCE.path, params={"key": key})

    async def get_user(self) -> UserBean:
        """Get currently logged user"""
        return await self._get(GET_USER.path, model=UserBean)

    async def update_user(self, body: UserWriteBean) -> UserWriteBean:
        """Update currently logged user"""
        return await self._put(
            UPDATE_USER.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=UserWriteBean,
        )

    async def change_my_password(self, body: PasswordBean) -> None:
        """Update caller password"""
        return await self._put(CHANGE_MY_PASSWORD.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def remove_user(self, *, key: str | None = None, username: str | None = None) -> None:
        """Delete user"""
        return await self._delete(REMOVE_USER.path, params={"key": key, "username": username})

    async def get_user_1(
        self,
        *,
        include_deleted: bool | None = False,
        key: str | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Get user by username or key"""
        return await self._get(
            GET_USER_1.path,
            params={"includeDeleted": include_deleted, "key": key, "username": username},
            model=UserBean,
        )

    async def create_user(self, body: UserWriteBean) -> UserWriteBean:
        """Create new user"""
        return await self._post(
            CREATE_USER.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=UserWriteBean,
        )

    async def update_user_1(
        self,
        body: UserWriteBean,
        *,
        key: str | None = None,
        username: str | None = None,
    ) -> UserWriteBean:
        """Update user details"""
        return await self._put(
            UPDATE_USER_1.path,
            params={"key": key, "username": username},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=UserWriteBean,
        )

    async def get_a11y_personal_settings(self) -> A11yPersonalSettingBean:
        """Get available accessibility personal settings"""
        return await self._get(GET_A11Y_PERSONAL_SETTINGS.path, model=A11yPersonalSettingBean)

    async def validate_user_anonymization(self, *, expand: str | None = None, user_key: str | None = None) -> None:
        """Get validation for user anonymization"""
        return await self._get(VALIDATE_USER_ANONYMIZATION.path, params={"expand": expand, "userKey": user_key})

    async def schedule_user_anonymization(self, body: UserAnonymizationRequestBean) -> None:
        """Schedule user anonymization"""
        return await self._post(
            SCHEDULE_USER_ANONYMIZATION.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_progress_1(self, *, task_id: int | None = None) -> None:
        """Get user anonymization progress"""
        return await self._get(GET_PROGRESS_1.path, params={"taskId": task_id})

    async def validate_user_anonymization_rerun(
        self,
        *,
        expand: str | None = None,
        old_user_key: str | None = None,
        old_user_name: str | None = None,
        user_key: str | None = None,
    ) -> UserAnonymizationValidationBean:
        """Get validation for user anonymization rerun"""
        return await self._get(
            VALIDATE_USER_ANONYMIZATION_RERUN.path,
            params={"expand": expand, "oldUserKey": old_user_key, "oldUserName": old_user_name, "userKey": user_key},
            model=UserAnonymizationValidationBean,
        )

    async def schedule_user_anonymization_rerun(self, body: UserAnonymizationRerunRequestBean) -> None:
        """Schedule user anonymization rerun"""
        return await self._post(
            SCHEDULE_USER_ANONYMIZATION_RERUN.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def unlock_anonymization(self) -> None:
        """Delete stale user anonymization task"""
        return await self._delete(UNLOCK_ANONYMIZATION.path)

    async def remove_user_from_application_1(
        self,
        *,
        application_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Remove user from application"""
        return await self._delete(
            REMOVE_USER_FROM_APPLICATION_1.path,
            params={"applicationKey": application_key, "username": username},
        )

    async def add_user_to_application_1(
        self,
        *,
        application_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Add user to application"""
        return await self._post(
            ADD_USER_TO_APPLICATION_1.path,
            params={"applicationKey": application_key, "username": username},
        )

    async def find_bulk_assignable_users(
        self,
        *,
        max_results: int | None = 50,
        project_keys: str | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Find bulk assignable users"""
        return await self._get(
            FIND_BULK_ASSIGNABLE_USERS.path,
            params={"maxResults": max_results, "projectKeys": project_keys, "username": username},
            model=UserBean,
        )

    async def find_assignable_users_1(
        self,
        *,
        issue_key: str | None = None,
        max_results: int | None = 50,
        project: str | None = None,
        action_descriptor_id: int | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Find assignable users by username"""
        return await self._get(
            FIND_ASSIGNABLE_USERS_1.path,
            params={
                "issueKey": issue_key,
                "maxResults": max_results,
                "project": project,
                "actionDescriptorId": action_descriptor_id,
                "username": username,
            },
            model=UserBean,
        )

    async def create_avatar_from_temporary_4(
        self,
        body: AvatarCroppingBean,
        *,
        username: str | None = None,
    ) -> AvatarBean:
        """Create avatar from temporary"""
        return await self._post(
            CREATE_AVATAR_FROM_TEMPORARY_4.path,
            params={"username": username},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarBean,
        )

    async def update_user_avatar_1(self, body: AvatarBean, *, username: str | None = None) -> AvatarBean:
        """Update user avatar"""
        return await self._put(
            UPDATE_USER_AVATAR_1.path,
            params={"username": username},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarBean,
        )

    async def store_temporary_avatar_using_multi_part_3(self, *, username: str | None = None) -> AvatarCroppingBean:
        """Store temporary avatar using multipart"""
        return await self._post(
            STORE_TEMPORARY_AVATAR_USING_MULTI_PART_3.path,
            params={"username": username},
            model=AvatarCroppingBean,
        )

    async def delete_avatar_2(self, id: int, *, username: str | None = None) -> None:
        """Delete avatar"""
        return await self._delete(DELETE_AVATAR_2.path.replace("{id}", str(id)), params={"username": username})

    async def get_all_avatars_1(self, *, username: str | None = None) -> AvatarBean:
        """Get all avatars for user"""
        return await self._get(GET_ALL_AVATARS_1.path, params={"username": username}, model=AvatarBean)

    async def reset_columns(self, *, username: str | None = None) -> None:
        """Reset default columns to system default"""
        return await self._delete(RESET_COLUMNS.path, params={"username": username})

    async def default_columns(self, *, username: str | None = None) -> ColumnOptions:
        """Get default columns for user"""
        return await self._get(DEFAULT_COLUMNS.path, params={"username": username}, model=ColumnOptions)

    async def set_columns_url_encoded(self) -> None:
        """Set default columns for user"""
        return await self._put(SET_COLUMNS_URL_ENCODED.path)

    async def get_duplicated_users_count(self, *, flush: bool | None = None) -> UserBean:
        """Get duplicated users count"""
        return await self._get(GET_DUPLICATED_USERS_COUNT.path, params={"flush": flush}, model=UserBean)

    async def get_duplicated_users_mapping(self, *, flush: bool | None = None) -> AvatarBean:
        """Get duplicated users mapping"""
        return await self._get(GET_DUPLICATED_USERS_MAPPING.path, params={"flush": flush}, model=AvatarBean)

    async def get_user_list(self, *, cursor: int | None = None, max_results: int | None = 2000) -> StreamPageBean:
        """List all users"""
        return await self._get(
            GET_USER_LIST.path,
            params={"cursor": cursor, "maxResults": max_results},
            model=StreamPageBean,
        )

    async def change_user_password(
        self,
        body: PasswordBean,
        *,
        key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Update user password"""
        return await self._put(
            CHANGE_USER_PASSWORD.path,
            params={"key": key, "username": username},
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def find_users_with_all_permissions(
        self,
        *,
        project_key: str | None = None,
        issue_key: str | None = None,
        max_results: int | None = None,
        permissions: str | None = None,
        start_at: int | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Find users with all specified permissions"""
        return await self._get(
            FIND_USERS_WITH_ALL_PERMISSIONS.path,
            params={
                "projectKey": project_key,
                "issueKey": issue_key,
                "maxResults": max_results,
                "permissions": permissions,
                "startAt": start_at,
                "username": username,
            },
            model=UserBean,
        )

    async def find_users_for_picker(
        self,
        *,
        max_results: int | None = None,
        query: str | None = None,
        exclude: list[str] | None = None,
        show_avatar: bool | None = None,
    ) -> UserPickerResultsBean:
        """Find users for picker by query"""
        return await self._get(
            FIND_USERS_FOR_PICKER.path,
            params={"maxResults": max_results, "query": query, "exclude": exclude, "showAvatar": show_avatar},
            model=UserPickerResultsBean,
        )

    async def get_properties_keys_4(self, *, user_key: str | None = None, username: str | None = None) -> None:
        """Get keys of all properties for a user"""
        return await self._get(GET_PROPERTIES_KEYS_4.path, params={"userKey": user_key, "username": username})

    async def delete_property_6(
        self,
        property_key: str,
        *,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Delete a specified user's property"""
        return await self._delete(
            DELETE_PROPERTY_6.path.replace("{propertyKey}", str(property_key)),
            params={"userKey": user_key, "username": username},
        )

    async def get_property_6(
        self,
        property_key: str,
        *,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Get the value of a specified user's property"""
        return await self._get(
            GET_PROPERTY_6.path.replace("{propertyKey}", str(property_key)),
            params={"userKey": user_key, "username": username},
        )

    async def set_property_5(
        self,
        property_key: str,
        *,
        user_key: str | None = None,
        username: str | None = None,
    ) -> None:
        """Set the value of a specified user's property"""
        return await self._put(
            SET_PROPERTY_5.path.replace("{propertyKey}", str(property_key)),
            params={"userKey": user_key, "username": username},
        )

    async def find_users(
        self,
        *,
        include_inactive: bool | None = None,
        max_results: int | None = None,
        include_active: bool | None = None,
        start_at: int | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Find users by username"""
        return await self._get(
            FIND_USERS.path,
            params={
                "includeInactive": include_inactive,
                "maxResults": max_results,
                "includeActive": include_active,
                "startAt": start_at,
                "username": username,
            },
            model=UserBean,
        )

    async def delete_session(self, username: str) -> None:
        """Delete user session"""
        return await self._delete(DELETE_SESSION.path.replace("{username}", str(username)))

    async def find_users_with_browse_permission(
        self,
        *,
        project_key: str | None = None,
        issue_key: str | None = None,
        max_results: int | None = None,
        username: str | None = None,
    ) -> UserBean:
        """Find users with browse permission"""
        return await self._get(
            FIND_USERS_WITH_BROWSE_PERMISSION.path,
            params={"projectKey": project_key, "issueKey": issue_key, "maxResults": max_results, "username": username},
            model=UserBean,
        )


class AsyncGroupResource(AsyncJiraResource):
    async def remove_group(self, *, groupname: str, swap_group: str | None = None) -> None:
        """Delete a specified group"""
        return await self._delete(REMOVE_GROUP.path, params={"groupname": groupname, "swapGroup": swap_group})

    async def create_group(self, body: AddGroupBean) -> GroupBean:
        """Create a group with given parameters"""
        return await self._post(
            CREATE_GROUP.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=GroupBean,
        )

    async def get_users_from_group(
        self,
        groupname: str,
        *,
        include_inactive_users: str | None = None,
        max_results: str | None = None,
        start_at: str | None = None,
    ) -> UserJsonBean:
        """Get users from a specified group"""
        return await self._get(
            GET_USERS_FROM_GROUP.path.replace("{groupname}", str(groupname)),
            params={"includeInactiveUsers": include_inactive_users, "maxResults": max_results, "startAt": start_at},
            model=UserJsonBean,
        )

    async def remove_user_from_group(self, *, groupname: str, username: str) -> None:
        """Remove a user from a specified group"""
        return await self._delete(REMOVE_USER_FROM_GROUP.path, params={"groupname": groupname, "username": username})

    async def add_user_to_group(self, body: UpdateUserToGroupBean, *, groupname: str) -> GroupBean:
        """Add a user to a specified group"""
        return await self._post(
            ADD_USER_TO_GROUP.path,
            params={"groupname": groupname},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=GroupBean,
        )

    async def find_groups(
        self,
        *,
        max_results: str | None = None,
        query: str | None = None,
        exclude: str | None = None,
        user_name: str | None = None,
    ) -> GroupSuggestionsBean:
        """Get groups matching a query"""
        return await self._get(
            FIND_GROUPS.path,
            params={"maxResults": max_results, "query": query, "exclude": exclude, "userName": user_name},
            model=GroupSuggestionsBean,
        )


class AsyncAvatarResource(AsyncJiraResource):
    async def get_all_system_avatars(self, type_: str) -> AvatarBean:
        """Get all system avatars"""
        return await self._get(GET_ALL_SYSTEM_AVATARS.path.replace("{type}", str(type_)), model=AvatarBean)

    async def store_temporary_avatar(
        self,
        type_: str,
        *,
        filename: str | None = None,
        size: str | None = None,
    ) -> AvatarCroppingBean:
        """Create temporary avatar"""
        return await self._post(
            STORE_TEMPORARY_AVATAR.path.replace("{type}", str(type_)),
            params={"filename": filename, "size": size},
            model=AvatarCroppingBean,
        )

    async def create_avatar_from_temporary(self, type_: str, body: AvatarCroppingBean) -> None:
        """Update avatar cropping"""
        return await self._post(
            CREATE_AVATAR_FROM_TEMPORARY.path.replace("{type}", str(type_)),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_avatars(self, type_: str, owning_object_id: str) -> AvatarBean:
        """Get all avatars for a type and owner"""
        return await self._get(
            GET_AVATARS.path.replace("{type}", str(type_)).replace("{owningObjectId}", str(owning_object_id)),
            model=AvatarBean,
        )

    async def create_avatar_from_temporary_3(
        self,
        type_: str,
        owning_object_id: str,
        body: AvatarCroppingBean,
    ) -> AvatarBean:
        """Create avatar from temporary"""
        return await self._post(
            CREATE_AVATAR_FROM_TEMPORARY_3.path.replace("{type}", str(type_)).replace(
                "{owningObjectId}", str(owning_object_id)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarBean,
        )

    async def delete_avatar_1(self, id: int, type_: str, owning_object_id: str) -> None:
        """Delete avatar by ID"""
        return await self._delete(
            DELETE_AVATAR_1.path.replace("{id}", str(id))
            .replace("{type}", str(type_))
            .replace("{owningObjectId}", str(owning_object_id)),
        )

    async def store_temporary_avatar_using_multi_part_2(
        self,
        type_: str,
        owning_object_id: str,
        body: FilePart,
    ) -> AvatarCroppingBean:
        """Create temporary avatar using multipart upload"""
        return await self._post(
            STORE_TEMPORARY_AVATAR_USING_MULTI_PART_2.path.replace("{type}", str(type_)).replace(
                "{owningObjectId}", str(owning_object_id)
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AvatarCroppingBean,
        )


class AsyncDashboardFilterResource(AsyncJiraResource):
    def list(
        self,
        *,
        filter: str | None = None,
        start_at: int = 0,
        max_results: int = 50,
    ) -> AsyncPageIterator[DashboardBean]:
        """Get all dashboards with optional filtering"""
        return self._get_paged(
            LIST.path,
            params={"filter": filter},
            model=DashboardBean,
            items_field="dashboards",
            start_at=start_at,
            max_results=max_results,
        )

    async def get_properties_keys(self, item_id: str, dashboard_id: str) -> EntityPropertiesKeysBean:
        """Get all properties keys for a dashboard item"""
        return await self._get(
            GET_PROPERTIES_KEYS_ITEMS_PROPERTIES.path.replace("{itemId}", str(item_id)).replace(
                "{dashboardId}", str(dashboard_id)
            ),
            model=EntityPropertiesKeysBean,
        )

    async def delete_property_1(self, property_key: str, item_id: str, dashboard_id: str) -> None:
        """Delete a property from a dashboard item"""
        return await self._delete(
            DELETE_PROPERTY_1_ITEMS_PROPERTIES.path.replace("{propertyKey}", str(property_key))
            .replace("{itemId}", str(item_id))
            .replace("{dashboardId}", str(dashboard_id)),
        )

    async def get_property_1(self, property_key: str, item_id: str, dashboard_id: str) -> EntityPropertyBean:
        """Get a property from a dashboard item"""
        return await self._get(
            GET_PROPERTY_1_ITEMS_PROPERTIES.path.replace("{propertyKey}", str(property_key))
            .replace("{itemId}", str(item_id))
            .replace("{dashboardId}", str(dashboard_id)),
            model=EntityPropertyBean,
        )

    async def set_property(self, property_key: str, item_id: str, dashboard_id: str) -> None:
        """Set a property on a dashboard item"""
        return await self._put(
            SET_PROPERTY_ITEMS_PROPERTIES.path.replace("{propertyKey}", str(property_key))
            .replace("{itemId}", str(item_id))
            .replace("{dashboardId}", str(dashboard_id)),
        )

    async def get_dashboard(self, id: str) -> DashboardBean:
        """Get a single dashboard by ID"""
        return await self._get(GET_DASHBOARD.path.replace("{id}", str(id)), model=DashboardBean)

    async def create_filter(self, body: FilterBean, *, expand: StringList | None = None) -> FilterBean:
        """Create a new filter"""
        return await self._post(
            CREATE_FILTER.path,
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=FilterBean,
        )

    async def get_default_share_scope(self) -> DefaultShareScopeBean:
        """Get default share scope"""
        return await self._get(GET_DEFAULT_SHARE_SCOPE.path, model=DefaultShareScopeBean)

    async def set_default_share_scope(self, body: DefaultShareScopeBean) -> DefaultShareScopeBean:
        """Set default share scope"""
        return await self._put(
            SET_DEFAULT_SHARE_SCOPE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=DefaultShareScopeBean,
        )

    async def get_favourite_filters(self, *, expand: StringList | None = None) -> FilterBean:
        """Get favourite filters"""
        return await self._get(GET_FAVOURITE_FILTERS.path, params={"expand": expand}, model=FilterBean)

    async def delete_filter(self, id: str) -> None:
        """Delete a filter"""
        return await self._delete(DELETE_FILTER.path.replace("{id}", str(id)))

    async def get_filter(self, id: str, *, expand: StringList | None = None) -> FilterBean:
        """Get a filter by ID"""
        return await self._get(GET_FILTER.path.replace("{id}", str(id)), params={"expand": expand}, model=FilterBean)

    async def edit_filter(self, id: str, body: FilterBean, *, expand: StringList | None = None) -> FilterBean:
        """Update an existing filter"""
        return await self._put(
            EDIT_FILTER.path.replace("{id}", str(id)),
            params={"expand": expand},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=FilterBean,
        )

    async def reset_columns_1(self, id: str) -> None:
        """Reset columns for filter"""
        return await self._delete(RESET_COLUMNS_1.path.replace("{id}", str(id)))

    async def default_columns_1(self, id: str) -> ColumnLayout:
        """Get default columns for filter"""
        return await self._get(DEFAULT_COLUMNS_1.path.replace("{id}", str(id)), model=ColumnLayout)

    async def set_columns_1(self, id: str) -> None:
        """Set default columns for filter"""
        return await self._put(SET_COLUMNS_1.path.replace("{id}", str(id)))

    async def get_share_permissions(self, id: str) -> FilterPermissionBean:
        """Get all share permissions of filter"""
        return await self._get(GET_SHARE_PERMISSIONS.path.replace("{id}", str(id)), model=FilterPermissionBean)

    async def add_share_permission(self, id: str, body: SharePermissionInputBean) -> FilterPermissionBean:
        """Add share permissions to filter"""
        return await self._post(
            ADD_SHARE_PERMISSION.path.replace("{id}", str(id)),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=FilterPermissionBean,
        )

    async def delete_share_permission(self, permission_id: str, id: str, permission_id_2: int) -> None:
        """Remove share permissions from filter"""
        return await self._delete(
            DELETE_SHARE_PERMISSION.path.replace("{permissionId}", str(permission_id))
            .replace("{id}", str(id))
            .replace("{permission-id}", str(permission_id_2)),
        )

    async def get_share_permission(self, permission_id: str, id: str) -> FilterPermissionBean:
        """Get a single share permission of filter"""
        return await self._get(
            GET_SHARE_PERMISSION.path.replace("{permissionId}", str(permission_id)).replace("{id}", str(id)),
            model=FilterPermissionBean,
        )


class AsyncSystemResource(AsyncJiraResource):
    async def get_property(self, *, permission_level: str, key_filter: str | None = None, key: str) -> Property:
        """Get an application property by key"""
        return await self._get(
            GET_PROPERTY_2_APPLICATION_PROPERTIES.path,
            params={"permissionLevel": permission_level, "keyFilter": key_filter, "key": key},
            model=Property,
        )

    async def get_advanced_settings(self) -> Property:
        """Get all advanced settings properties"""
        return await self._get(GET_ADVANCED_SETTINGS.path, model=Property)

    async def set_property_via_restful_table(self, id: str) -> Property:
        """Update an application property"""
        return await self._put(SET_PROPERTY_VIA_RESTFUL_TABLE.path.replace("{id}", str(id)), model=Property)

    async def get_configuration_1(self) -> ConfigurationBean:
        """Get Jira configuration details"""
        return await self._get(GET_CONFIGURATION_1.path, model=ConfigurationBean)

    async def download_email_templates(self) -> None:
        """Get email templates as zip file"""
        return await self._get(DOWNLOAD_EMAIL_TEMPLATES.path)

    async def upload_email_templates(self) -> None:
        """Update email templates with zip file"""
        return await self._post(UPLOAD_EMAIL_TEMPLATES.path)

    async def apply_email_templates(self) -> None:
        """Update email templates with previously uploaded pack"""
        return await self._post(APPLY_EMAIL_TEMPLATES.path)

    async def revert_email_templates_to_default(self) -> None:
        """Update email templates to default"""
        return await self._post(REVERT_EMAIL_TEMPLATES_TO_DEFAULT.path)

    async def get_email_types(self) -> None:
        """Get email types for templates"""
        return await self._get(GET_EMAIL_TYPES.path)

    async def validate(self) -> LicenseValidationResults:
        """Validate a Jira license"""
        return await self._post(VALIDATE.path, model=LicenseValidationResults)

    async def get_server_info(self) -> ServerInfoBean:
        """Get general information about the current Jira server"""
        return await self._get(GET_SERVER_INFO.path, model=ServerInfoBean)

    async def set_base_url(self) -> None:
        """Update base URL for Jira instance"""
        return await self._put(SET_BASE_URL.path)

    async def get_issue_navigator_default_columns(self) -> ColumnOptions:
        """Get default system columns for issue navigator"""
        return await self._get(GET_ISSUE_NAVIGATOR_DEFAULT_COLUMNS.path, model=ColumnOptions)

    async def set_issue_navigator_default_columns_form(self) -> None:
        """Set default system columns for issue navigator using form"""
        return await self._put(SET_ISSUE_NAVIGATOR_DEFAULT_COLUMNS_FORM.path)

    async def get_all_terminology_entries(self) -> TerminologyResponseBean:
        """Get all defined names for 'epic' and 'sprint'"""
        return await self._get(GET_ALL_TERMINOLOGY_ENTRIES.path, model=TerminologyResponseBean)

    async def set_terminology_entries(self, body: TerminologyRequestBean) -> None:
        """Update epic/sprint names from original to new"""
        return await self._post(SET_TERMINOLOGY_ENTRIES.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_terminology_entry(self, original_name: str) -> TerminologyResponseBean:
        """Get epic or sprint name by original name"""
        return await self._get(
            GET_TERMINOLOGY_ENTRY.path.replace("{originalName}", str(original_name)),
            model=TerminologyResponseBean,
        )


class AsyncOperationsResource(AsyncJiraResource):
    async def request_current_index_from_node(self, node_id: str) -> None:
        """Request node index snapshot"""
        return await self._put(REQUEST_CURRENT_INDEX_FROM_NODE.path.replace("{nodeId}", str(node_id)))

    async def delete_node(self, node_id: str) -> None:
        """Delete a cluster node"""
        return await self._delete(DELETE_NODE.path.replace("{nodeId}", str(node_id)))

    async def change_node_state_to_offline(self, node_id: str) -> None:
        """Update node state to offline"""
        return await self._put(CHANGE_NODE_STATE_TO_OFFLINE.path.replace("{nodeId}", str(node_id)))

    async def get_all_nodes(self) -> NodeBean:
        """Get all cluster nodes"""
        return await self._get(GET_ALL_NODES.path, model=NodeBean)

    async def approve_upgrade(self) -> None:
        """Approve cluster upgrade"""
        return await self._post(APPROVE_UPGRADE.path)

    async def cancel_upgrade(self) -> None:
        """Cancel cluster upgrade"""
        return await self._post(CANCEL_UPGRADE.path)

    async def acknowledge_errors(self) -> None:
        """Retry cluster upgrade"""
        return await self._post(ACKNOWLEDGE_ERRORS.path)

    async def set_ready_to_upgrade(self) -> None:
        """Start cluster upgrade"""
        return await self._post(SET_READY_TO_UPGRADE.path)

    async def get_state(self) -> ClusterState:
        """Get cluster upgrade state"""
        return await self._get(GET_STATE.path, model=ClusterState)

    async def list_index_snapshot(self) -> IndexSnapshotBean:
        """Get list of available index snapshots"""
        return await self._get(LIST_INDEX_SNAPSHOT.path, model=IndexSnapshotBean)

    async def create_index_snapshot(self) -> IndexSnapshotPromiseBean:
        """Create index snapshot if not in progress"""
        return await self._post(CREATE_INDEX_SNAPSHOT.path, model=IndexSnapshotPromiseBean)

    async def is_index_snapshot_running(self) -> IndexSnapshotStatusBean:
        """Get index snapshot creation status"""
        return await self._get(IS_INDEX_SNAPSHOT_RUNNING.path, model=IndexSnapshotStatusBean)

    async def get_index_summary(self) -> IndexSummaryBean:
        """Get index condition summary"""
        return await self._get(GET_INDEX_SUMMARY.path, model=IndexSummaryBean)

    async def is_app_monitoring_enabled(self) -> AppMonitoringRestEntity:
        """Get App Monitoring status"""
        return await self._get(IS_APP_MONITORING_ENABLED.path, model=AppMonitoringRestEntity)

    async def set_app_monitoring_enabled(self, body: AppMonitoringRestEntity) -> None:
        """Update App Monitoring status"""
        return await self._post(SET_APP_MONITORING_ENABLED.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def is_ipd_monitoring_enabled(self) -> IpdMonitoringRestEntity:
        """Get if IPD Monitoring is enabled"""
        return await self._get(IS_IPD_MONITORING_ENABLED.path, model=IpdMonitoringRestEntity)

    async def set_app_monitoring_enabled_1(self, body: IpdMonitoringRestEntity) -> None:
        """Update IPD Monitoring status"""
        return await self._post(
            SET_APP_MONITORING_ENABLED_1.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def are_metrics_exposed(self) -> None:
        """Check if JMX metrics are being exposed"""
        return await self._get(ARE_METRICS_EXPOSED.path)

    async def get_available_metrics(self) -> None:
        """Get the available JMX metrics"""
        return await self._get(GET_AVAILABLE_METRICS.path)

    async def start(self) -> None:
        """Start exposing JMX metrics"""
        return await self._post(START.path)

    async def stop(self) -> None:
        """Stop exposing JMX metrics"""
        return await self._post(STOP.path)

    async def get_reindex_info(self, *, task_id: int | None = None) -> ReindexBean:
        """Get reindex information"""
        return await self._get(GET_REINDEX_INFO.path, params={"taskId": task_id}, model=ReindexBean)

    async def reindex(
        self,
        *,
        index_change_history: bool | None = False,
        type_: str | None = None,
        index_worklogs: bool | None = False,
        index_comments: bool | None = False,
    ) -> ReindexBean:
        """Start a reindex operation"""
        return await self._post(
            REINDEX.path,
            params={
                "indexChangeHistory": index_change_history,
                "type": type_,
                "indexWorklogs": index_worklogs,
                "indexComments": index_comments,
            },
            model=ReindexBean,
        )

    async def reindex_issues(
        self,
        *,
        issue_id: list[str] | None = None,
        index_change_history: bool | None = False,
        index_worklogs: bool | None = False,
        index_comments: bool | None = False,
    ) -> ReindexBean:
        """Reindex individual issues"""
        return await self._post(
            REINDEX_ISSUES.path,
            params={
                "issueId": issue_id,
                "indexChangeHistory": index_change_history,
                "indexWorklogs": index_worklogs,
                "indexComments": index_comments,
            },
            model=ReindexBean,
        )

    async def get_reindex_progress(self, *, task_id: int | None = None) -> ReindexBean:
        """Get reindex progress"""
        return await self._get(GET_REINDEX_PROGRESS.path, params={"taskId": task_id}, model=ReindexBean)

    async def process_requests(self) -> None:
        """Execute pending reindex requests"""
        return await self._post(PROCESS_REQUESTS.path)

    async def get_progress_bulk(self, *, request_id: list[int] | None = None) -> ReindexRequestBean:
        """Get progress of multiple reindex requests"""
        return await self._get(GET_PROGRESS_BULK.path, params={"requestId": request_id}, model=ReindexRequestBean)

    async def get_progress(self, request_id: int) -> ReindexRequestBean:
        """Get progress of a single reindex request"""
        return await self._get(GET_PROGRESS.path.replace("{requestId}", str(request_id)), model=ReindexRequestBean)

    async def get_upgrade_result(self) -> UpgradeResultBean:
        """Get result of the last upgrade task"""
        return await self._get(GET_UPGRADE_RESULT.path, model=UpgradeResultBean)

    async def run_upgrades_now(self) -> None:
        """Run pending upgrade tasks"""
        return await self._post(RUN_UPGRADES_NOW.path)


class AsyncAuthResource(AsyncJiraResource):
    async def get_password_policy(self, *, has_old_password: bool | None = False) -> None:
        """Get current password policy requirements"""
        return await self._get(GET_PASSWORD_POLICY.path, params={"hasOldPassword": has_old_password})

    async def policy_check_create_user(self, body: PasswordPolicyCreateUserBean) -> None:
        """Get reasons for password policy disallowance on user creation"""
        return await self._post(POLICY_CHECK_CREATE_USER.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def policy_check_update_user(self, body: PasswordPolicyUpdateUserBean) -> None:
        """Get reasons for password policy disallowance on user password update"""
        return await self._post(POLICY_CHECK_UPDATE_USER.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def logout(self) -> None:
        """Delete current user session"""
        return await self._delete(LOGOUT.path)

    async def current_user(self) -> CurrentUser:
        """Get current user session information"""
        return await self._get(CURRENT_USER.path, model=CurrentUser)

    async def login(self, body: AuthParams) -> AuthSuccess:
        """Create new user session"""
        return await self._post(LOGIN.path, json=body.model_dump(by_alias=True, exclude_none=True), model=AuthSuccess)

    async def release(self) -> None:
        """Invalidate the current WebSudo session"""
        return await self._delete(RELEASE.path)
