"""Bitbucket Data Center async resource classes.

Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.
"""

from __future__ import annotations

from typing import Any

from atlassian.core.pagination import AsyncPageIterator
from atlassian.core.resource import AsyncResource

from .endpoints import (
    ACCEPT,
    ADD,
    ADD_ANNOTATIONS,
    ADD_BUILD_STATUS,
    ADD_DEFAULT_TASK,
    ADD_DEFAULT_TASK_1,
    ADD_EXEMPT_REPO,
    ADD_FOR_PROJECT,
    ADD_FOR_REPOSITORY,
    ADD_GROUP_TO_USER,
    ADD_IDP,
    ADD_KEY,
    ADD_LABEL,
    ADD_SSH_KEY,
    ADD_USER_TO_GROUP,
    ADD_USER_TO_GROUPS,
    ADD_USERS_TO_GROUP,
    ANALYTICS_SETTINGS,
    APPLY_SUGGESTION,
    APPROVE,
    ASSIGN_PARTICIPANT_ROLE,
    AUTHENTICATE,
    AUTHENTICATE_MIRRORING_AUTHENTICATE,
    AUTHENTICATE_WITH_RECOVERY_CODE,
    BULK_ADD_EXEMPT_REPOSITORIES,
    BULK_ADD_EXEMPT_REPOSITORIES_1,
    CAN_MERGE,
    CAN_REBASE,
    CANCEL_AUTO_MERGE,
    CANCEL_EXPORT_JOB,
    CANCEL_IMPORT_JOB,
    CANCEL_MESH_MIGRATION_JOB,
    CLEAR_DEFAULT_BRANCH,
    CLEAR_SENDER_ADDRESS,
    CLEAR_USER_CAPTCHA_CHALLENGE,
    COMPLETE_AUTHENTICATION_CHANGE,
    COMPLETE_ENFORCED_ENROLLMENT,
    COMPLETE_VOLUNTARY_ENROLLMENT,
    CONNECTIVITY,
    CREATE,
    CREATE_1,
    CREATE_2,
    CREATE_3,
    CREATE_ACCESS_TOKEN,
    CREATE_ACCESS_TOKEN_1,
    CREATE_ACCESS_TOKEN_2,
    CREATE_ALLOWLIST_RULE,
    CREATE_ALLOWLIST_RULE_1,
    CREATE_BRANCH,
    CREATE_BRANCH_FOR_REPOSITORY,
    CREATE_CERTIFICATE,
    CREATE_COMMENT,
    CREATE_COMMENT_1,
    CREATE_COMMENT_2,
    CREATE_GROUP,
    CREATE_HOOK_SCRIPT,
    CREATE_ISSUE,
    CREATE_OR_UPDATE_DEPLOYMENT,
    CREATE_PROJECT,
    CREATE_PULL_REQUEST_CONDITION,
    CREATE_PULL_REQUEST_CONDITION_1,
    CREATE_REPOSITORY,
    CREATE_REQUIRED_BUILDS_MERGE_CHECK,
    CREATE_RESTRICTIONS,
    CREATE_RESTRICTIONS_1,
    CREATE_RULE,
    CREATE_RULE_1,
    CREATE_RULE_2,
    CREATE_TAG,
    CREATE_TAG_FOR_REPOSITORY,
    CREATE_USER,
    CREATE_WEBHOOK,
    CREATE_WEBHOOK_1,
    DECLINE,
    DELETE,
    DELETE_1,
    DELETE_2,
    DELETE_3,
    DELETE_4,
    DELETE_5,
    DELETE_6,
    DELETE_7,
    DELETE_8,
    DELETE_9,
    DELETE_A_CODE_INSIGHTS_REPORT,
    DELETE_ALL_DEFAULT_TASKS,
    DELETE_ALL_DEFAULT_TASKS_1,
    DELETE_ALLOWLIST_RULE,
    DELETE_ALLOWLIST_RULE_1,
    DELETE_ANNOTATIONS,
    DELETE_ATTACHMENT,
    DELETE_ATTACHMENT_METADATA,
    DELETE_AUTO_DECLINE_SETTINGS,
    DELETE_AUTO_DECLINE_SETTINGS_1,
    DELETE_AVATAR,
    DELETE_BANNER,
    DELETE_BRANCH,
    DELETE_BY_ID,
    DELETE_BY_ID_1,
    DELETE_BY_ID_2,
    DELETE_CERTIFICATE,
    DELETE_COMMENT,
    DELETE_COMMENT_1,
    DELETE_COMMENT_2,
    DELETE_DEFAULT_TASK,
    DELETE_DEFAULT_TASK_1,
    DELETE_EXEMPT_REPO,
    DELETE_FOR_USER,
    DELETE_GROUP,
    DELETE_HOOK_SCRIPT,
    DELETE_KEY,
    DELETE_MAIL_CONFIG,
    DELETE_MIRRORING_REQUEST,
    DELETE_PREFERRED_MIRROR_ID,
    DELETE_PROJECT,
    DELETE_PULL_REQUEST_CONDITION,
    DELETE_PULL_REQUEST_CONDITION_1,
    DELETE_REPOSITORY,
    DELETE_REPOSITORY_HOOK,
    DELETE_REQUIRED_BUILDS_MERGE_CHECK,
    DELETE_RESTRICTION,
    DELETE_RESTRICTION_1,
    DELETE_RULE,
    DELETE_RULE_1,
    DELETE_RULE_2,
    DELETE_SSH_KEY,
    DELETE_SSH_KEYS,
    DELETE_TAG,
    DELETE_USER,
    DELETE_WEBHOOK,
    DELETE_WEBHOOK_1,
    DISABLE_HOOK,
    DISABLE_HOOK_1,
    DISCARD_REVIEW,
    DISMISS_RETENTION_CONFIG_REVIEW_NOTIFICATION,
    EDIT_ALLOWLIST_RULE,
    EDIT_ALLOWLIST_RULE_1,
    EDIT_FILE,
    EDIT_RULE,
    EDIT_RULE_1,
    EDIT_RULE_2,
    ELEVATE_PERMISSIONS_WITH_PASSWORD,
    ELEVATE_PERMISSIONS_WITH_RECOVERY_CODE,
    ELEVATE_PERMISSIONS_WITH_TOTP,
    ENABLE_HOOK,
    ENABLE_HOOK_1,
    END_ROLLING_UPGRADE,
    ERASE_USER,
    FIND_BRANCHES,
    FIND_BY_COMMIT,
    FIND_EXEMPT_REPOS_BY_PROJECT,
    FIND_EXEMPT_REPOS_BY_SCOPE,
    FIND_GROUPS_FOR_USER,
    FIND_OTHER_GROUPS_FOR_USER,
    FIND_USERS_IN_GROUP,
    FIND_USERS_NOT_IN_GROUP,
    FIND_WEBHOOKS,
    FIND_WEBHOOKS_1,
    FINISH_REVIEW,
    FORK_REPOSITORY,
    GET,
    GET_1,
    GET_2,
    GET_3,
    GET_4,
    GET_5,
    GET_6,
    GET_7,
    GET_A_CODE_INSIGHTS_REPORT,
    GET_ACTIVE_MESH_MIGRATION_SUMMARY,
    GET_ACTIVITIES,
    GET_ALL,
    GET_ALL_ACCESS_TOKENS,
    GET_ALL_ACCESS_TOKENS_1,
    GET_ALL_ACCESS_TOKENS_2,
    GET_ALL_CERTIFICATES,
    GET_ALL_CONTENT_HASHES,
    GET_ALL_LABELS_FOR_REPOSITORY,
    GET_ALL_MESH_MIGRATION_SUMMARIES,
    GET_ALL_RATE_LIMIT_SETTINGS,
    GET_ALL_REGISTERED_MESH_NODES,
    GET_ALL_REPOS_FOR_PROJECT,
    GET_ALLOWLIST_RULE,
    GET_ALLOWLIST_RULE_1,
    GET_ANNOTATIONS,
    GET_ANNOTATIONS_1,
    GET_APPLICATION_PROPERTIES,
    GET_ARCHIVE,
    GET_ATTACHMENT,
    GET_ATTACHMENT_METADATA,
    GET_AUTO_DECLINE_SETTINGS,
    GET_AUTO_DECLINE_SETTINGS_1,
    GET_AUTO_MERGE_REQUEST,
    GET_AVATAR,
    GET_BANNER,
    GET_BRANCHES,
    GET_BUILD_STATUS,
    GET_BUILD_STATUS_STATS,
    GET_BY_ID,
    GET_BY_ID_1,
    GET_BY_ID_2,
    GET_CAPABILITIES,
    GET_CAPABILITIES_1,
    GET_CAPTCHA_DATA,
    GET_CHANGES,
    GET_CHANGES_1,
    GET_COMMENT,
    GET_COMMENT_1,
    GET_COMMENT_2,
    GET_COMMENTS,
    GET_COMMENTS_1,
    GET_COMMENTS_2,
    GET_COMMIT,
    GET_COMMIT_MESSAGE_SUGGESTION,
    GET_COMMITS,
    GET_COMMITS_1,
    GET_COMMITS_BUILDS,
    GET_COMMITS_BY_ISSUE_KEY,
    GET_CONFIG,
    GET_CONFIGURATIONS,
    GET_CONFIGURATIONS_1,
    GET_CONTENT,
    GET_CONTENT_1,
    GET_CONTENT_HASH_BY_ID,
    GET_CONTROL_PLANE_PUBLIC_KEY,
    GET_DEFAULT_BRANCH,
    GET_DEFAULT_BRANCH_1,
    GET_DEFAULT_BRANCH_2,
    GET_DEFAULT_TASKS,
    GET_DEFAULT_TASKS_1,
    GET_DIFF_STATS_SUMMARY,
    GET_DIFF_STATS_SUMMARY_1,
    GET_DIFF_STATS_SUMMARY_2,
    GET_ELEVATED_PERMISSION_STATUS,
    GET_ENHANCED_ENTITY_LINK_FOR_PROJECT,
    GET_EXPORT_JOB,
    GET_EXPORT_JOB_MESSAGES,
    GET_FARM_NODES,
    GET_FOR_PROJECT,
    GET_FOR_PROJECTS,
    GET_FOR_REPOSITORIES,
    GET_FOR_REPOSITORY,
    GET_FOR_REPOSITORY_1,
    GET_FORKED_REPOSITORIES,
    GET_GLOBAL_SETTINGS,
    GET_GROUPS,
    GET_GROUPS_1,
    GET_GROUPS_WITH_ANY_PERMISSION,
    GET_GROUPS_WITH_ANY_PERMISSION_1,
    GET_GROUPS_WITH_ANY_PERMISSION_2,
    GET_GROUPS_WITHOUT_ANY_PERMISSION,
    GET_GROUPS_WITHOUT_ANY_PERMISSION_1,
    GET_GROUPS_WITHOUT_ANY_PERMISSION_2,
    GET_HISTORY,
    GET_HOOK_SCRIPT,
    GET_IDP,
    GET_IDPS,
    GET_IMPORT_JOB,
    GET_IMPORT_JOB_MESSAGES,
    GET_INFORMATION,
    GET_ISSUE_KEYS_FOR_PULL_REQUEST,
    GET_JIT_PROVISIONED_USERS,
    GET_KEYS_FOR_USER,
    GET_LABEL,
    GET_LABELABLES,
    GET_LABELS,
    GET_LATEST_INVOCATION,
    GET_LATEST_INVOCATION_1,
    GET_LEVEL,
    GET_LOGIN_OPTIONS,
    GET_MAIL_CONFIG,
    GET_MERGE_BASE,
    GET_MERGE_BASE_1,
    GET_MERGE_CONFIG,
    GET_MESH_MIGRATION_JOB,
    GET_MESH_MIGRATION_JOB_MESSAGES,
    GET_MESH_MIGRATION_JOB_SUMMARY,
    GET_MIRROR,
    GET_MIRROR_MODE,
    GET_MIRROR_SETTINGS,
    GET_MIRRORED_PROJECTS,
    GET_MIRRORED_REPOSITORY,
    GET_MIRRORING_REQUEST,
    GET_MULTIPLE_BUILD_STATUS_STATS,
    GET_OUT_OF_SYNC_REPOSITORIES,
    GET_PAGE,
    GET_PAGE_OF_REQUIRED_BUILDS_MERGE_CHECKS,
    GET_PREFERRED_MIRROR_ID,
    GET_PROJECT,
    GET_PROJECT_AVATAR,
    GET_PROJECT_BY_ID,
    GET_PROJECTS,
    GET_PULL_REQUEST_CONDITIONS,
    GET_PULL_REQUEST_CONDITIONS_1,
    GET_PULL_REQUEST_COUNT,
    GET_PULL_REQUEST_SETTINGS,
    GET_PULL_REQUEST_SETTINGS_1,
    GET_PULL_REQUEST_SUGGESTIONS,
    GET_PULL_REQUESTS,
    GET_PULL_REQUESTS_1,
    GET_PULL_REQUESTS_2,
    GET_REF_CHANGE_ACTIVITY,
    GET_REF_CHANGES_QUEUE,
    GET_REF_CHANGES_QUEUE_COUNT,
    GET_REGISTERED_MESH_NODE_BY_ID,
    GET_RELATED_REPOSITORIES,
    GET_REPO_SYNC_STATUS,
    GET_REPO_SYNC_STATUS_1,
    GET_REPORTS,
    GET_REPOSITORIES,
    GET_REPOSITORIES_1,
    GET_REPOSITORIES_RECENTLY_ACCESSED,
    GET_REPOSITORY,
    GET_REPOSITORY_ARCHIVE_POLICY,
    GET_REPOSITORY_DELETE_POLICY,
    GET_REPOSITORY_HOOK,
    GET_REPOSITORY_HOOK_1,
    GET_REPOSITORY_HOOKS,
    GET_REPOSITORY_HOOKS_1,
    GET_REPOSITORY_LOCK_OWNER,
    GET_REPOSITORY_LOCK_OWNERS,
    GET_REPOSITORY_MIRRORS,
    GET_RESTRICTION,
    GET_RESTRICTION_1,
    GET_RESTRICTIONS,
    GET_RESTRICTIONS_1,
    GET_REVIEW,
    GET_REVIEWER_GROUP,
    GET_REVIEWER_GROUP_1,
    GET_REVIEWER_GROUPS,
    GET_REVIEWER_GROUPS_1,
    GET_REVIEWERS,
    GET_ROOT_LEVEL,
    GET_RULE,
    GET_RULE_1,
    GET_RULE_2,
    GET_SENDER_ADDRESS,
    GET_SETTINGS,
    GET_SETTINGS_1,
    GET_SETTINGS_2,
    GET_SSH_KEY,
    GET_SSH_KEYS,
    GET_SSH_KEYS_FOR_PROJECT,
    GET_SSO_MANAGEMENT_STATUS,
    GET_STATISTICS,
    GET_STATISTICS_1,
    GET_STATISTICS_SUMMARY,
    GET_STATISTICS_SUMMARY_1,
    GET_STATUS,
    GET_STATUS_PROJECTS_REPOS,
    GET_SUPPORT_ZIP,
    GET_SUPPORT_ZIPS,
    GET_SUPPORTED_KEY_TYPES,
    GET_SYNCHRONIZATION_PROGRESS,
    GET_SYSTEM_SIGNING_CONFIGURATION,
    GET_TAG,
    GET_TAGS,
    GET_UPSTREAM_SERVER,
    GET_USER,
    GET_USER_DIRECTORIES,
    GET_USER_SETTINGS,
    GET_USERS,
    GET_USERS_1,
    GET_USERS_2,
    GET_USERS_WITH_ANY_PERMISSION,
    GET_USERS_WITH_ANY_PERMISSION_1,
    GET_USERS_WITH_ANY_PERMISSION_2,
    GET_USERS_WITHOUT_ANY_PERMISSION,
    GET_USERS_WITHOUT_PERMISSION,
    GET_USERS_WITHOUT_PERMISSION_1,
    GET_WEBHOOK,
    GET_WEBHOOK_1,
    HAS_ALL_USER_PERMISSION,
    IS_REPO_EXEMPT,
    LIST_MIRRORS,
    LIST_PARTICIPANTS,
    LIST_REQUESTS,
    MERGE,
    MODIFY_ALL_USER_PERMISSION,
    PREVIEW,
    PREVIEW_EXPORT,
    PREVIEW_MESH_MIGRATION,
    PUBLISH_EVENT,
    PUT,
    REACT,
    REACT_1,
    READ,
    REBASE,
    REGISTER,
    REGISTER_NEW_MESH_NODE,
    REJECT,
    REMOVE,
    REMOVE_CONFIGURATION,
    REMOVE_CONFIGURATION_1,
    REMOVE_GROUP_FROM_USER,
    REMOVE_IDP,
    REMOVE_LABEL,
    REMOVE_USER_FROM_GROUP,
    RENAME_USER,
    REOPEN,
    RETRY_CREATE_REPOSITORY,
    REVOKE_FOR_PROJECT,
    REVOKE_FOR_REPOSITORY,
    REVOKE_MANY,
    REVOKE_PERMISSIONS,
    REVOKE_PERMISSIONS_1,
    REVOKE_PERMISSIONS_FOR_GROUP,
    REVOKE_PERMISSIONS_FOR_GROUP_1,
    REVOKE_PERMISSIONS_FOR_GROUP_2,
    REVOKE_PERMISSIONS_FOR_USER,
    REVOKE_PERMISSIONS_FOR_USER_1,
    REVOKE_PERMISSIONS_FOR_USER_2,
    ROTATE_RECOVER_CODE,
    SAVE_ATTACHMENT_METADATA,
    SEARCH,
    SEARCH_1,
    SEARCH_2,
    SEARCH_3,
    SEARCH_4,
    SEARCH_ALLOWLIST_RULE,
    SEARCH_MESH_MIGRATION_REPOS,
    SEARCH_PERMISSIONS,
    SEARCH_PERMISSIONS_1,
    SEARCH_WEBHOOKS,
    SET,
    SET_1,
    SET_2,
    SET_3,
    SET_A_CODE_INSIGHTS_REPORT,
    SET_ANNOTATION,
    SET_AUTO_DECLINE_SETTINGS,
    SET_AUTO_DECLINE_SETTINGS_1,
    SET_BANNER,
    SET_CONFIGURATION,
    SET_CONFIGURATION_1,
    SET_DEFAULT_BRANCH,
    SET_DEFAULT_BRANCH_1,
    SET_DEFAULT_BRANCH_2,
    SET_ENABLED,
    SET_LEVEL,
    SET_MAIL_CONFIG,
    SET_MERGE_CONFIG,
    SET_MIRROR_MODE,
    SET_MIRROR_SETTINGS,
    SET_PERMISSION_FOR_GROUP,
    SET_PERMISSION_FOR_GROUPS,
    SET_PERMISSION_FOR_GROUPS_1,
    SET_PERMISSION_FOR_USER,
    SET_PERMISSION_FOR_USERS,
    SET_PERMISSION_FOR_USERS_1,
    SET_PREFERRED_MIRROR_ID,
    SET_REPOSITORY_ARCHIVE_POLICY,
    SET_REPOSITORY_DELETE_POLICY,
    SET_ROOT_LEVEL,
    SET_SENDER_ADDRESS,
    SET_SETTINGS,
    SET_SETTINGS_1,
    SET_SETTINGS_2,
    SSH_SETTINGS,
    START_ENFORCED_ENROLLMENT,
    START_ENROLLMENT_UPDATE,
    START_EXPORT,
    START_IMPORT,
    START_MESH_MIGRATION,
    START_MIRRORING_PROJECT,
    START_MIRRORING_PROJECTS,
    START_ROLLING_UPGRADE,
    START_VOLUNTARY_ENROLLMENT,
    STOP_MIRRORING_PROJECT,
    STREAM,
    STREAM_1,
    STREAM_CHANGES,
    STREAM_CHANGES_1,
    STREAM_COMMITS,
    STREAM_CONTRIBUTING,
    STREAM_DIFF,
    STREAM_DIFF_1,
    STREAM_DIFF_2,
    STREAM_FILES,
    STREAM_FILES_1,
    STREAM_LICENSE,
    STREAM_PATCH,
    STREAM_PATCH_1,
    STREAM_RAW,
    STREAM_RAW_DIFF,
    STREAM_RAW_DIFF_1,
    STREAM_RAW_DIFF_2,
    STREAM_README,
    SYNCHRONIZE,
    TEST_WEBHOOK,
    TEST_WEBHOOK_1,
    TRY_AUTO_MERGE,
    UN_REACT,
    UN_REACT_1,
    UNASSIGN_PARTICIPANT_ROLE,
    UNASSIGN_PARTICIPANT_ROLE_1,
    UNENROLL,
    UNENROLL_USER,
    UNWATCH,
    UNWATCH_1,
    UNWATCH_2,
    UPDATE,
    UPDATE_1,
    UPDATE_2,
    UPDATE_ACCESS_TOKEN,
    UPDATE_ACCESS_TOKEN_1,
    UPDATE_ACCESS_TOKEN_2,
    UPDATE_CERTIFICATE_REVOCATION_LIST_ENTRIES,
    UPDATE_COMMENT,
    UPDATE_COMMENT_1,
    UPDATE_COMMENT_2,
    UPDATE_CONFIG,
    UPDATE_DEFAULT_TASK,
    UPDATE_DEFAULT_TASK_1,
    UPDATE_GLOBAL_SETTINGS,
    UPDATE_HOOK_SCRIPT,
    UPDATE_IDP,
    UPDATE_LICENSE,
    UPDATE_MESH_NODE,
    UPDATE_PERMISSION,
    UPDATE_PERMISSION_1,
    UPDATE_PROJECT,
    UPDATE_PULL_REQUEST_CONDITION,
    UPDATE_PULL_REQUEST_CONDITION_1,
    UPDATE_PULL_REQUEST_SETTINGS,
    UPDATE_PULL_REQUEST_SETTINGS_1,
    UPDATE_REPOSITORY,
    UPDATE_REQUIRED_BUILDS_MERGE_CHECK,
    UPDATE_SETTINGS,
    UPDATE_STATUS,
    UPDATE_SYSTEM_SIGNING_CONFIGURATION,
    UPDATE_USER_DETAILS,
    UPDATE_USER_DETAILS_1,
    UPDATE_USER_PASSWORD,
    UPDATE_USER_PASSWORD_1,
    UPDATE_WEBHOOK,
    UPDATE_WEBHOOK_1,
    UPGRADE,
    UPLOAD_AVATAR,
    UPLOAD_AVATAR_1,
    VALIDATE_ERASABLE,
    VERIFY_CODE,
    WATCH,
    WATCH_1,
    WATCH_2,
    WITHDRAW_APPROVAL,
)
from .models import (
    AdminPasswordUpdate,
    AuthenticationEntity,
    AuthenticationResponse,
    BasicAuthConfigEntity,
    CaptchaDataEntity,
    ConversationDTO,
    EnrichedRepository,
    ExampleAvatarMultipartFormData,
    ExampleCertificateMultipartFormData,
    ExampleFiles,
    ExampleMultipartFormData,
    ExamplePostMultipartFormData,
    ExamplePreviewMigration,
    ExamplePutMultipartFormData,
    ExampleSettings,
    ExampleSettingsMap,
    FileListResource,
    GroupAndUsers,
    GroupPickerContext,
    IdpConfigEntity,
    JitUserEntity,
    RestAccessToken,
    RestAccessTokenRequest,
    RestAggregateRejectCounter,
    RestAnalyticsSettings,
    RestAnnouncementBanner,
    RestApplicationProperties,
    RestApplicationUser,
    RestApplicationUserWithPermissions,
    RestApplySuggestionRequest,
    RestAttachmentMetadata,
    RestAuthenticationRequest,
    RestAutoDeclineSettings,
    RestAutoDeclineSettingsRequest,
    RestAutoMergeProcessingResult,
    RestAutoMergeProjectSettingsRequest,
    RestAutoMergeRequest,
    RestAutoMergeRestrictedSettings,
    RestAutoMergeSettingsRequest,
    RestBitbucketLicense,
    RestBranch,
    RestBranchCreateRequest,
    RestBranchDeleteRequest,
    RestBuildCapabilities,
    RestBuildStats,
    RestBuildStatus,
    RestBuildStatusSetRequest,
    RestBulkAddInsightAnnotationRequest,
    RestBulkUserRateLimitSettingsUpdateRequest,
    RestChange,
    RestChangeset,
    RestClusterInformation,
    RestClusterNode,
    RestComment,
    RestCommentJiraIssue,
    RestCommit,
    RestCommitMessageSuggestion,
    RestCreateBranchRequest,
    RestCreateTagRequest,
    RestDefaultReviewersRequest,
    RestDefaultTask,
    RestDefaultTaskRequest,
    RestDeployment,
    RestDeploymentSetRequest,
    RestDetailedGroup,
    RestDetailedInvocation,
    RestDetailedUser,
    RestDiff,
    RestDiffStatsSummary,
    RestEnhancedEntityLink,
    RestErasedUser,
    RestExportRequest,
    RestGitTagCreateRequest,
    RestGpgKey,
    RestHookScript,
    RestHookScriptConfig,
    RestHookScriptTriggers,
    RestImportRequest,
    RestInsightAnnotationsResponse,
    RestInsightReport,
    RestInvocationHistory,
    RestJiraIssue,
    RestJob,
    RestJobMessage,
    RestLabel,
    RestLabelable,
    RestLogLevel,
    RestMailConfiguration,
    RestMarkup,
    RestMeshConnectivityReport,
    RestMeshMigrationRequest,
    RestMeshMigrationSummary,
    RestMeshNode,
    RestMigrationRepository,
    RestMinimalRef,
    RestMirroredRepository,
    RestMirroredRepositoryDescriptor,
    RestMirroringRequest,
    RestMirrorRepositorySynchronizationStatus,
    RestMirrorServer,
    RestMirrorUpgradeRequest,
    RestMultipleBuildStats,
    RestNamedLink,
    RestPermitted,
    RestPermittedGroup,
    RestPermittedUser,
    RestProject,
    RestProjectSettingsRestriction,
    RestProjectSettingsRestrictionRequest,
    RestPullRequest,
    RestPullRequestActivity,
    RestPullRequestAssignParticipantRoleRequest,
    RestPullRequestAssignStatusRequest,
    RestPullRequestCondition,
    RestPullRequestDeclineRequest,
    RestPullRequestDeleteRequest,
    RestPullRequestFinishReviewRequest,
    RestPullRequestMergeability,
    RestPullRequestMergeConfig,
    RestPullRequestMergeRequest,
    RestPullRequestParticipant,
    RestPullRequestRebaseability,
    RestPullRequestRebaseRequest,
    RestPullRequestRebaseResult,
    RestPullRequestReopenRequest,
    RestPullRequestSettings,
    RestPullRequestSuggestion,
    RestRateLimitSettings,
    RestRawAccessToken,
    RestRefRestriction,
    RestRefSyncQueue,
    RestRefSyncRequest,
    RestRefSyncStatus,
    RestRejectedRef,
    RestRepository,
    RestRepositoryHook,
    RestRepositoryLockOwner,
    RestRepositoryMirrorEvent,
    RestRepositoryPolicy,
    RestRepositoryPullRequestSettings,
    RestRepositoryRefChangeActivity,
    RestRequiredBuildCondition,
    RestRequiredBuildConditionSetRequest,
    RestReviewerGroup,
    RestRollingUpgradeState,
    RestScopesExample,
    RestSecretScanningAllowlistRule,
    RestSecretScanningAllowlistRuleSetRequest,
    RestSecretScanningRule,
    RestSecretScanningRuleSetRequest,
    RestSetInsightReportRequest,
    RestSingleAddInsightAnnotationRequest,
    RestSshAccessKey,
    RestSshKey,
    RestSshKeySettings,
    RestSshSettings,
    RestSyncProgress,
    RestSystemSigningConfiguration,
    RestTag,
    RestUpstreamServer,
    RestUpstreamSettings,
    RestUserDirectory,
    RestUserRateLimitSettings,
    RestUserRateLimitSettingsUpdateRequest,
    RestUserReaction,
    RestWebhook,
    RestWebhookCredentials,
    RestWebhookRequestResponse,
    RestX509Certificate,
    SsoConfigEntity,
    SsoManagementStatusDTO,
    StatusDTO,
    TotpCodeVerificationDTO,
    TotpElevationRestDTO,
    TotpRecoveryCodeAuthenticationDTO,
    TotpRecoveryCodeDTO,
    TotpUserEnrollmentDTO,
    UserAndGroups,
    UserPasswordUpdate,
    UserPickerContext,
    UserRename,
    UserUpdate,
    UserUpdateWithCredentials,
)


class AsyncProjectsResource(AsyncResource):
    async def get_avatar(self, hook_key: str, *, version: str | None = None) -> None:
        """Get project avatar"""
        return await self._get(GET_AVATAR.path.format(hookKey=hook_key), params={"version": version})

    def get_projects(
        self,
        *,
        name: str | None = None,
        permission: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestProject]:
        """Get projects"""
        return self._get_paged(
            GET_PROJECTS.path,
            params={"name": name, "permission": permission},
            model=RestProject,
            start=start,
            limit=limit,
        )

    async def create_project(self, body: RestProject) -> RestProject:
        """Create a new project"""
        return await self._post(
            CREATE_PROJECT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestProject,
        )

    async def delete_project(self, project_key: str) -> None:
        """Delete project"""
        return await self._delete(DELETE_PROJECT.path.format(projectKey=project_key))

    async def get_project(self, project_key: str) -> RestProject:
        """Get a project"""
        return await self._get(GET_PROJECT.path.format(projectKey=project_key), model=RestProject)

    async def update_project(self, project_key: str, body: RestProject) -> RestProject:
        """Update project"""
        return await self._put(
            UPDATE_PROJECT.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestProject,
        )

    async def get_project_avatar(self, project_key: str, *, s: str | None = None) -> None:
        """Get avatar for project"""
        return await self._get(GET_PROJECT_AVATAR.path.format(projectKey=project_key), params={"s": s})

    async def upload_avatar(self, project_key: str, body: ExampleAvatarMultipartFormData) -> None:
        """Update project avatar"""
        return await self._post(
            UPLOAD_AVATAR.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    def get_configurations(
        self,
        project_key: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestHookScriptConfig]:
        """Get configured hook scripts"""
        return self._get_paged(
            GET_CONFIGURATIONS.path.format(projectKey=project_key),
            model=RestHookScriptConfig,
            start=start,
            limit=limit,
        )

    async def remove_configuration(self, project_key: str, script_id: str) -> None:
        """Remove a hook script"""
        return await self._delete(REMOVE_CONFIGURATION.path.format(projectKey=project_key, scriptId=script_id))

    async def set_configuration(
        self,
        project_key: str,
        script_id: str,
        body: RestHookScriptTriggers,
    ) -> RestHookScriptConfig:
        """Create/update a hook script"""
        return await self._put(
            SET_CONFIGURATION.path.format(projectKey=project_key, scriptId=script_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestHookScriptConfig,
        )

    async def revoke_permissions(self, project_key: str, *, user: str | None = None, group: str | None = None) -> None:
        """Revoke project permissions"""
        return await self._delete(
            REVOKE_PERMISSIONS.path.format(projectKey=project_key),
            params={"user": user, "group": group},
        )

    async def revoke_permissions_for_group_1(self, project_key: str, *, name: str | None = None) -> None:
        """Revoke group project permission"""
        return await self._delete(
            REVOKE_PERMISSIONS_FOR_GROUP_1.path.format(projectKey=project_key),
            params={"name": name},
        )

    def get_groups_with_any_permission_1(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedGroup]:
        """Get groups with permission to project"""
        return self._get_paged(
            GET_GROUPS_WITH_ANY_PERMISSION_1.path.format(projectKey=project_key),
            params={"filter": filter},
            model=RestPermittedGroup,
            start=start,
            limit=limit,
        )

    async def set_permission_for_groups_1(
        self,
        project_key: str,
        *,
        name: str | None = None,
        permission: str | None = None,
    ) -> None:
        """Update group project permission"""
        return await self._put(
            SET_PERMISSION_FOR_GROUPS_1.path.format(projectKey=project_key),
            params={"name": name, "permission": permission},
        )

    def get_groups_without_any_permission_1(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedGroup]:
        """Get groups without project permission"""
        return self._get_paged(
            GET_GROUPS_WITHOUT_ANY_PERMISSION_1.path.format(projectKey=project_key),
            params={"filter": filter},
            model=RestDetailedGroup,
            start=start,
            limit=limit,
        )

    async def search_permissions(
        self,
        project_key: str,
        *,
        permission: str | None = None,
        filter_text: str | None = None,
        type_: str | None = None,
    ) -> None:
        """Search project permissions"""
        return await self._get(
            SEARCH_PERMISSIONS.path.format(projectKey=project_key),
            params={"permission": permission, "filterText": filter_text, "type": type_},
        )

    async def revoke_permissions_for_user_1(self, project_key: str, *, name: str | None = None) -> None:
        """Revoke user project permission"""
        return await self._delete(
            REVOKE_PERMISSIONS_FOR_USER_1.path.format(projectKey=project_key),
            params={"name": name},
        )

    def get_users_with_any_permission_1(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedUser]:
        """Get users with permission to project"""
        return self._get_paged(
            GET_USERS_WITH_ANY_PERMISSION_1.path.format(projectKey=project_key),
            params={"filter": filter},
            model=RestPermittedUser,
            start=start,
            limit=limit,
        )

    async def set_permission_for_users_1(
        self,
        project_key: str,
        *,
        name: str | None = None,
        permission: str | None = None,
    ) -> None:
        """Update user project permission"""
        return await self._put(
            SET_PERMISSION_FOR_USERS_1.path.format(projectKey=project_key),
            params={"name": name, "permission": permission},
        )

    def get_users_without_permission(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestApplicationUser]:
        """Get users without project permission"""
        return self._get_paged(
            GET_USERS_WITHOUT_PERMISSION.path.format(projectKey=project_key),
            params={"filter": filter},
            model=RestApplicationUser,
            start=start,
            limit=limit,
        )

    async def has_all_user_permission(self, project_key: str, permission: str) -> RestPermitted:
        """Check default project permission"""
        return await self._get(
            HAS_ALL_USER_PERMISSION.path.format(projectKey=project_key, permission=permission),
            model=RestPermitted,
        )

    async def modify_all_user_permission(self, project_key: str, permission: str, *, allow: str | None = None) -> None:
        """Grant project permission"""
        return await self._post(
            MODIFY_ALL_USER_PERMISSION.path.format(projectKey=project_key, permission=permission),
            params={"allow": allow},
        )

    def get_repositories(
        self,
        project_key: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Get repositories for project"""
        return self._get_paged(
            GET_REPOSITORIES.path.format(projectKey=project_key),
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def create_repository(self, project_key: str, body: RestRepository) -> RestRepository:
        """Create repository"""
        return await self._post(
            CREATE_REPOSITORY.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepository,
        )

    async def delete_repository(self, project_key: str, repository_slug: str) -> None:
        """Delete repository"""
        return await self._delete(DELETE_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug))

    async def get_repository(self, project_key: str, repository_slug: str) -> RestRepository:
        """Get repository"""
        return await self._get(
            GET_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepository,
        )

    async def fork_repository(self, project_key: str, repository_slug: str, body: RestRepository) -> RestRepository:
        """Fork repository"""
        return await self._post(
            FORK_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepository,
        )

    async def update_repository(self, project_key: str, repository_slug: str, body: RestRepository) -> RestRepository:
        """Update repository"""
        return await self._put(
            UPDATE_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepository,
        )

    async def stream_contributing(
        self,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        markup: str | None = None,
        html_escape: str | None = None,
        include_heading_id: str | None = None,
        hardwrap: str | None = None,
    ) -> None:
        """Get repository contributing guidelines"""
        return await self._get(
            STREAM_CONTRIBUTING.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "at": at,
                "markup": markup,
                "htmlEscape": html_escape,
                "includeHeadingId": include_heading_id,
                "hardwrap": hardwrap,
            },
        )

    async def get_default_branch_2(self, project_key: str, repository_slug: str) -> RestMinimalRef:
        """Get repository default branch"""
        return await self._get(
            GET_DEFAULT_BRANCH_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestMinimalRef,
        )

    async def set_default_branch_2(self, project_key: str, repository_slug: str, body: RestBranch) -> None:
        """Update default branch for repository"""
        return await self._put(
            SET_DEFAULT_BRANCH_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    def get_forked_repositories(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Get repository forks"""
        return self._get_paged(
            GET_FORKED_REPOSITORIES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def stream_license(
        self,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        markup: str | None = None,
        html_escape: str | None = None,
        include_heading_id: str | None = None,
        hardwrap: str | None = None,
    ) -> None:
        """Get repository license"""
        return await self._get(
            STREAM_LICENSE.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "at": at,
                "markup": markup,
                "htmlEscape": html_escape,
                "includeHeadingId": include_heading_id,
                "hardwrap": hardwrap,
            },
        )

    async def stream_readme(
        self,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        markup: str | None = None,
        html_escape: str | None = None,
        include_heading_id: str | None = None,
        hardwrap: str | None = None,
    ) -> None:
        """Get repository readme"""
        return await self._get(
            STREAM_README.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "at": at,
                "markup": markup,
                "htmlEscape": html_escape,
                "includeHeadingId": include_heading_id,
                "hardwrap": hardwrap,
            },
        )

    async def retry_create_repository(self, project_key: str, repository_slug: str) -> RestRepository:
        """Retry repository creation"""
        return await self._post(
            RETRY_CREATE_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepository,
        )

    def get_related_repositories(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Get related repository"""
        return self._get_paged(
            GET_RELATED_REPOSITORIES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def delete_9(
        self,
        project_key: str,
        *,
        namespace: str,
        component_key: str | None = None,
        feature_key: str,
    ) -> None:
        """Stop enforcing project restriction"""
        return await self._delete(
            DELETE_9.path.format(projectKey=project_key),
            params={"namespace": namespace, "componentKey": component_key, "featureKey": feature_key},
        )

    async def get_7(
        self,
        project_key: str,
        *,
        namespace: str,
        component_key: str | None = None,
        feature_key: str,
    ) -> RestProjectSettingsRestriction:
        """Get enforcing project setting"""
        return await self._get(
            GET_7.path.format(projectKey=project_key),
            params={"namespace": namespace, "componentKey": component_key, "featureKey": feature_key},
            model=RestProjectSettingsRestriction,
        )

    async def create_3(
        self,
        project_key: str,
        body: RestProjectSettingsRestrictionRequest,
    ) -> RestProjectSettingsRestriction:
        """Enforce project restriction"""
        return await self._post(
            CREATE_3.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestProjectSettingsRestriction,
        )

    def get_all(
        self,
        project_key: str,
        *,
        namespace: str,
        feature_key: str,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestProjectSettingsRestriction]:
        """Get all enforcing project settings"""
        return self._get_paged(
            GET_ALL.path.format(projectKey=project_key),
            params={"namespace": namespace, "featureKey": feature_key},
            model=RestProjectSettingsRestriction,
            start=start,
            limit=limit,
        )

    async def delete_auto_decline_settings(self, project_key: str) -> None:
        """Delete auto decline settings"""
        return await self._delete(DELETE_AUTO_DECLINE_SETTINGS.path.format(projectKey=project_key))

    async def get_auto_decline_settings(self, project_key: str) -> RestAutoDeclineSettings:
        """Get auto decline settings"""
        return await self._get(
            GET_AUTO_DECLINE_SETTINGS.path.format(projectKey=project_key),
            model=RestAutoDeclineSettings,
        )

    async def set_auto_decline_settings(
        self,
        project_key: str,
        body: RestAutoDeclineSettingsRequest,
    ) -> RestAutoDeclineSettings:
        """Create/Update auto decline settings"""
        return await self._put(
            SET_AUTO_DECLINE_SETTINGS.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAutoDeclineSettings,
        )

    async def delete_4(self, project_key: str) -> None:
        """Delete pull request auto-merge settings"""
        return await self._delete(DELETE_4.path.format(projectKey=project_key))

    async def get_4(self, project_key: str) -> RestAutoMergeRestrictedSettings:
        """Get pull request auto-merge settings"""
        return await self._get(GET_4.path.format(projectKey=project_key), model=RestAutoMergeRestrictedSettings)

    async def set(self, project_key: str, body: RestAutoMergeProjectSettingsRequest) -> RestAutoMergeRestrictedSettings:
        """Create or update the pull request auto-merge settings"""
        return await self._put(
            SET.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAutoMergeRestrictedSettings,
        )

    def get_repository_hooks(
        self,
        project_key: str,
        *,
        type_: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepositoryHook]:
        """Get repository hooks"""
        return self._get_paged(
            GET_REPOSITORY_HOOKS.path.format(projectKey=project_key),
            params={"type": type_},
            model=RestRepositoryHook,
            start=start,
            limit=limit,
        )

    async def get_repository_hook(self, project_key: str, hook_key: str) -> RestRepositoryHook:
        """Get a repository hook"""
        return await self._get(
            GET_REPOSITORY_HOOK.path.format(projectKey=project_key, hookKey=hook_key),
            model=RestRepositoryHook,
        )

    async def disable_hook(self, project_key: str, hook_key: str) -> RestRepositoryHook:
        """Disable repository hook"""
        return await self._delete(
            DISABLE_HOOK.path.format(projectKey=project_key, hookKey=hook_key),
            model=RestRepositoryHook,
        )

    async def enable_hook(self, project_key: str, hook_key: str) -> RestRepositoryHook:
        """Enable repository hook"""
        return await self._put(
            ENABLE_HOOK.path.format(projectKey=project_key, hookKey=hook_key),
            model=RestRepositoryHook,
        )

    async def get_settings(self, project_key: str, hook_key: str) -> ExampleSettings:
        """Get repository hook settings"""
        return await self._get(
            GET_SETTINGS.path.format(projectKey=project_key, hookKey=hook_key),
            model=ExampleSettings,
        )

    async def set_settings(self, project_key: str, hook_key: str, body: ExampleSettings) -> ExampleSettings:
        """Update repository hook settings"""
        return await self._put(
            SET_SETTINGS.path.format(projectKey=project_key, hookKey=hook_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ExampleSettings,
        )

    async def get_pull_request_settings(self, project_key: str, scm_id: str) -> RestPullRequestSettings:
        """Get merge strategy"""
        return await self._get(
            GET_PULL_REQUEST_SETTINGS.path.format(projectKey=project_key, scmId=scm_id),
            model=RestPullRequestSettings,
        )

    async def update_pull_request_settings(
        self,
        project_key: str,
        scm_id: str,
        body: RestPullRequestSettings,
    ) -> RestPullRequestSettings:
        """Update merge strategy"""
        return await self._post(
            UPDATE_PULL_REQUEST_SETTINGS.path.format(projectKey=project_key, scmId=scm_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestSettings,
        )

    async def find_webhooks(
        self,
        project_key: str,
        *,
        event: str | None = None,
        statistics: bool | None = None,
    ) -> None:
        """Find webhooks"""
        return await self._get(
            FIND_WEBHOOKS.path.format(projectKey=project_key),
            params={"event": event, "statistics": statistics},
        )

    async def create_webhook(self, project_key: str, body: RestWebhook) -> RestWebhook:
        """Create webhook"""
        return await self._post(
            CREATE_WEBHOOK.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhook,
        )

    async def test_webhook(
        self,
        project_key: str,
        body: RestWebhookCredentials,
        *,
        webhook_id: int | None = None,
        ssl_verification_required: bool | None = True,
        url: str | None = None,
    ) -> RestWebhookRequestResponse:
        """Test webhook"""
        return await self._post(
            TEST_WEBHOOK.path.format(projectKey=project_key),
            params={"webhookId": webhook_id, "sslVerificationRequired": ssl_verification_required, "url": url},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhookRequestResponse,
        )

    async def delete_webhook(self, project_key: str, webhook_id: str) -> None:
        """Delete webhook"""
        return await self._delete(DELETE_WEBHOOK.path.format(projectKey=project_key, webhookId=webhook_id))

    async def get_webhook(self, project_key: str, webhook_id: str, *, statistics: str | None = None) -> RestWebhook:
        """Get webhook"""
        return await self._get(
            GET_WEBHOOK.path.format(projectKey=project_key, webhookId=webhook_id),
            params={"statistics": statistics},
            model=RestWebhook,
        )

    async def update_webhook(self, project_key: str, webhook_id: str, body: RestWebhook) -> RestWebhook:
        """Update webhook"""
        return await self._put(
            UPDATE_WEBHOOK.path.format(projectKey=project_key, webhookId=webhook_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhook,
        )

    async def get_latest_invocation(
        self,
        project_key: str,
        webhook_id: str,
        *,
        event: str | None = None,
        outcome: str | None = None,
    ) -> RestDetailedInvocation:
        """Get last webhook invocation details"""
        return await self._get(
            GET_LATEST_INVOCATION.path.format(projectKey=project_key, webhookId=webhook_id),
            params={"event": event, "outcome": outcome},
            model=RestDetailedInvocation,
        )

    async def get_statistics(
        self,
        project_key: str,
        webhook_id: str,
        *,
        event: str | None = None,
    ) -> RestInvocationHistory:
        """Get webhook statistics"""
        return await self._get(
            GET_STATISTICS.path.format(projectKey=project_key, webhookId=webhook_id),
            params={"event": event},
            model=RestInvocationHistory,
        )

    async def get_statistics_summary(self, project_key: str, webhook_id: str) -> RestInvocationHistory:
        """Get webhook statistics summary"""
        return await self._get(
            GET_STATISTICS_SUMMARY.path.format(projectKey=project_key, webhookId=webhook_id),
            model=RestInvocationHistory,
        )

    def get_restrictions(
        self,
        project_key: str,
        *,
        matcher_type: str | None = None,
        matcher_id: str | None = None,
        type_: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRefRestriction]:
        """Search for ref restrictions"""
        return self._get_paged(
            GET_RESTRICTIONS.path.format(projectKey=project_key),
            params={"matcherType": matcher_type, "matcherId": matcher_id, "type": type_},
            model=RestRefRestriction,
            start=start,
            limit=limit,
        )

    async def create_restrictions(self, project_key: str) -> RestRefRestriction:
        """Create multiple ref restrictions"""
        return await self._post(CREATE_RESTRICTIONS.path.format(projectKey=project_key), model=RestRefRestriction)

    async def delete_restriction(self, project_key: str, id: str) -> None:
        """Delete a ref restriction"""
        return await self._delete(DELETE_RESTRICTION.path.format(projectKey=project_key, id=id))

    async def get_restriction(self, project_key: str, id: str) -> RestRefRestriction:
        """Get a ref restriction"""
        return await self._get(GET_RESTRICTION.path.format(projectKey=project_key, id=id), model=RestRefRestriction)

    async def delete_all_default_tasks(self, project_key: str) -> None:
        """Deletes all default tasks for the project"""
        return await self._delete(DELETE_ALL_DEFAULT_TASKS.path.format(projectKey=project_key))

    def get_default_tasks(
        self,
        project_key: str,
        *,
        markup: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDefaultTask]:
        """Get a page of default tasks"""
        return self._get_paged(
            GET_DEFAULT_TASKS.path.format(projectKey=project_key),
            params={"markup": markup},
            model=RestDefaultTask,
            start=start,
            limit=limit,
        )

    async def add_default_task(self, project_key: str, body: RestDefaultTaskRequest) -> RestDefaultTask:
        """Add a default task"""
        return await self._post(
            ADD_DEFAULT_TASK.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDefaultTask,
        )

    async def delete_default_task(self, project_key: str, task_id: str) -> None:
        """Delete a specific default task"""
        return await self._delete(DELETE_DEFAULT_TASK.path.format(projectKey=project_key, taskId=task_id))

    async def update_default_task(
        self,
        project_key: str,
        task_id: str,
        body: RestDefaultTaskRequest,
    ) -> RestDefaultTask:
        """Update a default task"""
        return await self._put(
            UPDATE_DEFAULT_TASK.path.format(projectKey=project_key, taskId=task_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDefaultTask,
        )


class AsyncRepositoriesResource(AsyncResource):
    def get_repositories_recently_accessed(
        self,
        *,
        permission: str | None = "REPO_READ",
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Get recently accessed repositories"""
        return self._get_paged(
            GET_REPOSITORIES_RECENTLY_ACCESSED.path,
            params={"permission": permission},
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def get_archive(
        self,
        project_key: str,
        repository_slug: str,
        *,
        path: str | None = None,
        filename: str | None = None,
        at: str | None = None,
        prefix: str | None = None,
        format: str | None = None,
    ) -> None:
        """Stream archive of repository"""
        return await self._get(
            GET_ARCHIVE.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"path": path, "filename": filename, "at": at, "prefix": prefix, "format": format},
        )

    async def delete_attachment(self, project_key: str, attachment_id: str, repository_slug: str) -> None:
        """Delete an attachment"""
        return await self._delete(
            DELETE_ATTACHMENT.path.format(
                projectKey=project_key, attachmentId=attachment_id, repositorySlug=repository_slug
            ),
        )

    async def get_attachment(self, project_key: str, attachment_id: str, repository_slug: str) -> None:
        """Get an attachment"""
        return await self._get(
            GET_ATTACHMENT.path.format(
                projectKey=project_key, attachmentId=attachment_id, repositorySlug=repository_slug
            ),
        )

    async def delete_attachment_metadata(self, project_key: str, attachment_id: str, repository_slug: str) -> None:
        """Delete attachment metadata"""
        return await self._delete(
            DELETE_ATTACHMENT_METADATA.path.format(
                projectKey=project_key, attachmentId=attachment_id, repositorySlug=repository_slug
            ),
        )

    async def get_attachment_metadata(
        self,
        project_key: str,
        attachment_id: str,
        repository_slug: str,
    ) -> RestAttachmentMetadata:
        """Get attachment metadata"""
        return await self._get(
            GET_ATTACHMENT_METADATA.path.format(
                projectKey=project_key, attachmentId=attachment_id, repositorySlug=repository_slug
            ),
            model=RestAttachmentMetadata,
        )

    async def save_attachment_metadata(self, project_key: str, attachment_id: str, repository_slug: str) -> None:
        """Save attachment metadata"""
        return await self._put(
            SAVE_ATTACHMENT_METADATA.path.format(
                projectKey=project_key, attachmentId=attachment_id, repositorySlug=repository_slug
            ),
        )

    def get_branches(
        self,
        project_key: str,
        repository_slug: str,
        *,
        boost_matches: bool | None = None,
        context: str | None = None,
        order_by: str | None = None,
        details: bool | None = None,
        filter_text: str | None = None,
        base: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestBranch]:
        """Find branches"""
        return self._get_paged(
            GET_BRANCHES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "boostMatches": boost_matches,
                "context": context,
                "orderBy": order_by,
                "details": details,
                "filterText": filter_text,
                "base": base,
            },
            model=RestBranch,
            start=start,
            limit=limit,
        )

    async def create_branch_for_repository(
        self,
        project_key: str,
        repository_slug: str,
        body: RestCreateBranchRequest,
    ) -> RestBranch:
        """Create branch"""
        return await self._post(
            CREATE_BRANCH_FOR_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestBranch,
        )

    async def get_default_branch_1(self, project_key: str, repository_slug: str) -> RestBranch:
        """Get default branch

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._get(
            GET_DEFAULT_BRANCH_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestBranch,
        )

    async def set_default_branch_1(self, project_key: str, repository_slug: str, body: RestBranch) -> None:
        """Update default branch

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._put(
            SET_DEFAULT_BRANCH_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_content(
        self,
        project_key: str,
        repository_slug: str,
        *,
        no_content: str | None = None,
        at: str | None = None,
        size: str | None = None,
        blame: str | None = None,
        type_: str | None = None,
    ) -> None:
        """Get file content at revision"""
        return await self._get(
            GET_CONTENT.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"noContent": no_content, "at": at, "size": size, "blame": blame, "type": type_},
        )

    async def get_content_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        no_content: str | None = None,
        at: str | None = None,
        size: str | None = None,
        blame: str | None = None,
        type_: str | None = None,
    ) -> None:
        """Get file content"""
        return await self._get(
            GET_CONTENT_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={"noContent": no_content, "at": at, "size": size, "blame": blame, "type": type_},
        )

    async def edit_file(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        body: ExampleMultipartFormData,
    ) -> RestCommit:
        """Edit file"""
        return await self._put(
            EDIT_FILE.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestCommit,
        )

    def get_changes_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        until: str | None = None,
        since: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestChange]:
        """Get changes made in commit"""
        return self._get_paged(
            GET_CHANGES_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"until": until, "since": since},
            model=RestChange,
            start=start,
            limit=limit,
        )

    def get_commits(
        self,
        project_key: str,
        repository_slug: str,
        *,
        avatar_scheme: str | None = None,
        path: str | None = None,
        with_counts: str | None = None,
        follow_renames: str | None = None,
        until: str | None = None,
        avatar_size: str | None = None,
        since: str | None = None,
        merges: str | None = None,
        ignore_missing: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestCommit]:
        """Get commits"""
        return self._get_paged(
            GET_COMMITS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "avatarScheme": avatar_scheme,
                "path": path,
                "withCounts": with_counts,
                "followRenames": follow_renames,
                "until": until,
                "avatarSize": avatar_size,
                "since": since,
                "merges": merges,
                "ignoreMissing": ignore_missing,
            },
            model=RestCommit,
            start=start,
            limit=limit,
        )

    async def get_commit(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        path: str | None = None,
    ) -> RestCommit:
        """Get commit by ID"""
        return await self._get(
            GET_COMMIT.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"path": path},
            model=RestCommit,
        )

    def get_changes(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        with_comments: str | None = None,
        since: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestChange]:
        """Get changes in commit"""
        return self._get_paged(
            GET_CHANGES.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"withComments": with_comments, "since": since},
            model=RestChange,
            start=start,
            limit=limit,
        )

    def get_comments(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        path: str | None = None,
        since: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestComment]:
        """Search for commit comments"""
        return self._get_paged(
            GET_COMMENTS.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"path": path, "since": since},
            model=RestComment,
            start=start,
            limit=limit,
        )

    async def create_comment(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        body: RestComment,
        *,
        since: str | None = None,
    ) -> RestComment:
        """Add a new commit comment"""
        return await self._post(
            CREATE_COMMENT.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"since": since},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def delete_comment(
        self,
        project_key: str,
        comment_id: str,
        commit_id: str,
        repository_slug: str,
        *,
        version: str | None = None,
    ) -> None:
        """Delete a commit comment"""
        return await self._delete(
            DELETE_COMMENT.path.format(
                projectKey=project_key, commentId=comment_id, commitId=commit_id, repositorySlug=repository_slug
            ),
            params={"version": version},
        )

    async def get_comment(self, project_key: str, comment_id: str, commit_id: str, repository_slug: str) -> RestComment:
        """Get a commit comment"""
        return await self._get(
            GET_COMMENT.path.format(
                projectKey=project_key, commentId=comment_id, commitId=commit_id, repositorySlug=repository_slug
            ),
            model=RestComment,
        )

    async def update_comment(
        self,
        project_key: str,
        comment_id: str,
        commit_id: str,
        repository_slug: str,
        body: RestComment,
    ) -> RestComment:
        """Update a commit comment"""
        return await self._put(
            UPDATE_COMMENT.path.format(
                projectKey=project_key, commentId=comment_id, commitId=commit_id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def get_diff_stats_summary(
        self,
        path: str,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        src_path: str | None = None,
        auto_src_path: str | None = None,
        whitespace: str | None = None,
        since: str | None = None,
    ) -> RestDiffStatsSummary:
        """Get diff stats summary between revisions"""
        return await self._get(
            GET_DIFF_STATS_SUMMARY.path.format(
                path=path, projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug
            ),
            params={"srcPath": src_path, "autoSrcPath": auto_src_path, "whitespace": whitespace, "since": since},
            model=RestDiffStatsSummary,
        )

    async def stream_diff(
        self,
        commit_id: str,
        repository_slug: str,
        path: str,
        project_key: str,
        *,
        src_path: str | None = None,
        avatar_size: str | None = None,
        filter: str | None = None,
        avatar_scheme: str | None = None,
        context_lines: str | None = None,
        auto_src_path: str | None = None,
        whitespace: str | None = None,
        with_comments: str | None = None,
        since: str | None = None,
    ) -> RestDiff:
        """Get diff between revisions"""
        return await self._get(
            STREAM_DIFF.path.format(
                commitId=commit_id, repositorySlug=repository_slug, path=path, projectKey=project_key
            ),
            params={
                "srcPath": src_path,
                "avatarSize": avatar_size,
                "filter": filter,
                "avatarScheme": avatar_scheme,
                "contextLines": context_lines,
                "autoSrcPath": auto_src_path,
                "whitespace": whitespace,
                "withComments": with_comments,
                "since": since,
            },
            model=RestDiff,
        )

    async def get_merge_base(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        other_commit_id: str | None = None,
    ) -> RestCommit:
        """Get the common ancestor between two commits"""
        return await self._get(
            GET_MERGE_BASE.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"otherCommitId": other_commit_id},
            model=RestCommit,
        )

    async def unwatch(self, project_key: str, commit_id: str, repository_slug: str) -> None:
        """Stop watching commit"""
        return await self._delete(
            UNWATCH.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
        )

    async def watch(self, project_key: str, commit_id: str, repository_slug: str) -> None:
        """Watch commit"""
        return await self._post(
            WATCH.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
        )

    def stream_changes(
        self,
        project_key: str,
        repository_slug: str,
        *,
        from_repo: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestChange]:
        """Compare commits"""
        return self._get_paged(
            STREAM_CHANGES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"fromRepo": from_repo, "from": from_, "to": to},
            model=RestChange,
            start=start,
            limit=limit,
        )

    def stream_commits(
        self,
        project_key: str,
        repository_slug: str,
        *,
        from_repo: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestCommit]:
        """Get accessible commits"""
        return self._get_paged(
            STREAM_COMMITS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"fromRepo": from_repo, "from": from_, "to": to},
            model=RestCommit,
            start=start,
            limit=limit,
        )

    async def get_diff_stats_summary_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        from_repo: str | None = None,
        src_path: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        whitespace: str | None = None,
    ) -> RestDiff:
        """Retrieve the diff stats summary between commits"""
        return await self._get(
            GET_DIFF_STATS_SUMMARY_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={"fromRepo": from_repo, "srcPath": src_path, "from": from_, "to": to, "whitespace": whitespace},
            model=RestDiff,
        )

    async def stream_diff_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        context_lines: str | None = None,
        from_repo: str | None = None,
        src_path: str | None = None,
        from_: str | None = None,
        to: str | None = None,
        whitespace: str | None = None,
    ) -> RestDiff:
        """Get diff between commits"""
        return await self._get(
            STREAM_DIFF_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={
                "contextLines": context_lines,
                "fromRepo": from_repo,
                "srcPath": src_path,
                "from": from_,
                "to": to,
                "whitespace": whitespace,
            },
            model=RestDiff,
        )

    async def stream_raw_diff(
        self,
        project_key: str,
        repository_slug: str,
        *,
        context_lines: str | None = None,
        src_path: str | None = None,
        until: str | None = None,
        whitespace: str | None = None,
        since: str | None = None,
    ) -> None:
        """Get raw diff for path"""
        return await self._get(
            STREAM_RAW_DIFF.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "contextLines": context_lines,
                "srcPath": src_path,
                "until": until,
                "whitespace": whitespace,
                "since": since,
            },
        )

    async def stream_raw_diff_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        context_lines: str | None = None,
        src_path: str | None = None,
        until: str | None = None,
        whitespace: str | None = None,
        since: str | None = None,
    ) -> None:
        """Get raw diff for path"""
        return await self._get(
            STREAM_RAW_DIFF_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={
                "contextLines": context_lines,
                "srcPath": src_path,
                "until": until,
                "whitespace": whitespace,
                "since": since,
            },
        )

    def stream_files(
        self,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[FileListResource]:
        """Get files in directory"""
        return self._get_paged(
            STREAM_FILES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"at": at},
            model=FileListResource,
            start=start,
            limit=limit,
        )

    def stream_files_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[FileListResource]:
        """Get files in directory"""
        return self._get_paged(
            STREAM_FILES_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={"at": at},
            model=FileListResource,
            start=start,
            limit=limit,
        )

    def get_configurations_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestHookScriptConfig]:
        """Get hook scripts"""
        return self._get_paged(
            GET_CONFIGURATIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestHookScriptConfig,
            start=start,
            limit=limit,
        )

    async def remove_configuration_1(self, project_key: str, script_id: str, repository_slug: str) -> None:
        """Remove a hook script"""
        return await self._delete(
            REMOVE_CONFIGURATION_1.path.format(
                projectKey=project_key, scriptId=script_id, repositorySlug=repository_slug
            ),
        )

    async def set_configuration_1(
        self,
        project_key: str,
        script_id: str,
        repository_slug: str,
        body: RestHookScriptTriggers,
    ) -> RestHookScriptConfig:
        """Create/update a hook script"""
        return await self._put(
            SET_CONFIGURATION_1.path.format(projectKey=project_key, scriptId=script_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestHookScriptConfig,
        )

    async def get_all_labels_for_repository(self, project_key: str, repository_slug: str) -> RestLabel:
        """Get repository labels"""
        return await self._get(
            GET_ALL_LABELS_FOR_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestLabel,
        )

    async def add_label(self, project_key: str, repository_slug: str, body: RestLabel) -> RestLabel:
        """Add repository label"""
        return await self._post(
            ADD_LABEL.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestLabel,
        )

    async def remove_label(self, project_key: str, label_name: str, repository_slug: str) -> None:
        """Remove repository label"""
        return await self._delete(
            REMOVE_LABEL.path.format(projectKey=project_key, labelName=label_name, repositorySlug=repository_slug),
        )

    async def stream(self, project_key: str, repository_slug: str, *, at: str | None = None) -> ExampleFiles:
        """Stream files"""
        return await self._get(
            STREAM.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"at": at},
            model=ExampleFiles,
        )

    async def stream_1(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
    ) -> ExampleFiles:
        """Stream files with last modified commit in path"""
        return await self._get(
            STREAM_1.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={"at": at},
            model=ExampleFiles,
        )

    async def stream_patch(
        self,
        project_key: str,
        repository_slug: str,
        *,
        until: str | None = None,
        all_ancestors: str | None = None,
        since: str | None = None,
    ) -> None:
        """Get patch content at revision"""
        return await self._get(
            STREAM_PATCH.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"until": until, "allAncestors": all_ancestors, "since": since},
        )

    async def stream_raw(
        self,
        path: str,
        project_key: str,
        repository_slug: str,
        *,
        at: str | None = None,
        markup: str | None = None,
        html_escape: str | None = None,
        include_heading_id: str | None = None,
        hardwrap: str | None = None,
    ) -> None:
        """Get raw content of a file at revision"""
        return await self._get(
            STREAM_RAW.path.format(path=path, projectKey=project_key, repositorySlug=repository_slug),
            params={
                "at": at,
                "markup": markup,
                "htmlEscape": html_escape,
                "includeHeadingId": include_heading_id,
                "hardwrap": hardwrap,
            },
        )

    def get_ref_change_activity(
        self,
        project_key: str,
        repository_slug: str,
        *,
        ref: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepositoryRefChangeActivity]:
        """Get ref change activity"""
        return self._get_paged(
            GET_REF_CHANGE_ACTIVITY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"ref": ref},
            model=RestRepositoryRefChangeActivity,
            start=start,
            limit=limit,
        )

    def find_branches(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter_text: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMinimalRef]:
        """Get branches with ref change activities for repository"""
        return self._get_paged(
            FIND_BRANCHES.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filterText": filter_text},
            model=RestMinimalRef,
            start=start,
            limit=limit,
        )

    async def delete_auto_decline_settings_1(self, project_key: str, repository_slug: str) -> None:
        """Delete auto decline settings"""
        return await self._delete(
            DELETE_AUTO_DECLINE_SETTINGS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
        )

    async def get_auto_decline_settings_1(self, project_key: str, repository_slug: str) -> RestAutoDeclineSettings:
        """Get auto decline settings"""
        return await self._get(
            GET_AUTO_DECLINE_SETTINGS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestAutoDeclineSettings,
        )

    async def set_auto_decline_settings_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestAutoDeclineSettingsRequest,
    ) -> RestAutoDeclineSettings:
        """Create auto decline settings"""
        return await self._put(
            SET_AUTO_DECLINE_SETTINGS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAutoDeclineSettings,
        )

    async def delete_5(self, project_key: str, repository_slug: str) -> None:
        """Delete pull request auto-merge settings"""
        return await self._delete(DELETE_5.path.format(projectKey=project_key, repositorySlug=repository_slug))

    async def get_5(self, project_key: str, repository_slug: str) -> RestAutoMergeRestrictedSettings:
        """Get pull request auto-merge settings"""
        return await self._get(
            GET_5.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestAutoMergeRestrictedSettings,
        )

    async def set_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestAutoMergeSettingsRequest,
    ) -> RestAutoMergeRestrictedSettings:
        """Create or update the pull request auto-merge settings"""
        return await self._put(
            SET_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAutoMergeRestrictedSettings,
        )

    def get_repository_hooks_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        type_: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepositoryHook]:
        """Get repository hooks"""
        return self._get_paged(
            GET_REPOSITORY_HOOKS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"type": type_},
            model=RestRepositoryHook,
            start=start,
            limit=limit,
        )

    async def delete_repository_hook(self, project_key: str, hook_key: str, repository_slug: str) -> None:
        """Delete repository hook"""
        return await self._delete(
            DELETE_REPOSITORY_HOOK.path.format(
                projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug
            ),
        )

    async def get_repository_hook_1(self, project_key: str, hook_key: str, repository_slug: str) -> RestRepositoryHook:
        """Get repository hook"""
        return await self._get(
            GET_REPOSITORY_HOOK_1.path.format(projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug),
            model=RestRepositoryHook,
        )

    async def disable_hook_1(self, project_key: str, hook_key: str, repository_slug: str) -> RestRepositoryHook:
        """Disable repository hook"""
        return await self._delete(
            DISABLE_HOOK_1.path.format(projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug),
            model=RestRepositoryHook,
        )

    async def enable_hook_1(self, project_key: str, hook_key: str, repository_slug: str) -> RestRepositoryHook:
        """Enable repository hook"""
        return await self._put(
            ENABLE_HOOK_1.path.format(projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug),
            model=RestRepositoryHook,
        )

    async def get_settings_1(self, project_key: str, hook_key: str, repository_slug: str) -> ExampleSettings:
        """Get repository hook settings"""
        return await self._get(
            GET_SETTINGS_1.path.format(projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug),
            model=ExampleSettings,
        )

    async def set_settings_1(
        self,
        project_key: str,
        hook_key: str,
        repository_slug: str,
        body: ExampleSettings,
    ) -> ExampleSettings:
        """Update repository hook settings"""
        return await self._put(
            SET_SETTINGS_1.path.format(projectKey=project_key, hookKey=hook_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ExampleSettings,
        )

    async def get_pull_request_settings_1(
        self,
        project_key: str,
        repository_slug: str,
    ) -> RestRepositoryPullRequestSettings:
        """Get pull request settings"""
        return await self._get(
            GET_PULL_REQUEST_SETTINGS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepositoryPullRequestSettings,
        )

    async def update_pull_request_settings_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestRepositoryPullRequestSettings,
    ) -> RestRepositoryPullRequestSettings:
        """Update pull request settings"""
        return await self._post(
            UPDATE_PULL_REQUEST_SETTINGS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepositoryPullRequestSettings,
        )

    def get_tags(
        self,
        project_key: str,
        repository_slug: str,
        *,
        order_by: str | None = None,
        filter_text: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestTag]:
        """Find tag"""
        return self._get_paged(
            GET_TAGS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"orderBy": order_by, "filterText": filter_text},
            model=RestTag,
            start=start,
            limit=limit,
        )

    async def create_tag_for_repository(
        self,
        project_key: str,
        repository_slug: str,
        body: RestCreateTagRequest,
    ) -> RestTag:
        """Create tag"""
        return await self._post(
            CREATE_TAG_FOR_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestTag,
        )

    async def get_tag(self, project_key: str, name: str, repository_slug: str) -> RestTag:
        """Get tag"""
        return await self._get(
            GET_TAG.path.format(projectKey=project_key, name=name, repositorySlug=repository_slug),
            model=RestTag,
        )

    async def unwatch_2(self, project_key: str, repository_slug: str) -> None:
        """Stop watching repository"""
        return await self._delete(UNWATCH_2.path.format(projectKey=project_key, repositorySlug=repository_slug))

    async def watch_2(self, project_key: str, repository_slug: str, body: RestRepository) -> None:
        """Watch repository"""
        return await self._post(
            WATCH_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def find_webhooks_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        event: str | None = None,
        statistics: bool | None = None,
    ) -> None:
        """Find webhooks"""
        return await self._get(
            FIND_WEBHOOKS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"event": event, "statistics": statistics},
        )

    async def create_webhook_1(self, project_key: str, repository_slug: str, body: RestWebhook) -> RestWebhook:
        """Create webhook"""
        return await self._post(
            CREATE_WEBHOOK_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhook,
        )

    async def search_webhooks(
        self,
        project_key: str,
        repository_slug: str,
        *,
        scope_type: str | None = None,
        event: str | None = None,
        statistics: bool | None = None,
    ) -> None:
        """Search webhooks"""
        return await self._get(
            SEARCH_WEBHOOKS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"scopeType": scope_type, "event": event, "statistics": statistics},
        )

    async def test_webhook_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestWebhookCredentials,
        *,
        webhook_id: int | None = None,
        ssl_verification_required: str | None = None,
        url: str | None = None,
    ) -> RestWebhookRequestResponse:
        """Test webhook"""
        return await self._post(
            TEST_WEBHOOK_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"webhookId": webhook_id, "sslVerificationRequired": ssl_verification_required, "url": url},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhookRequestResponse,
        )

    async def delete_webhook_1(self, project_key: str, webhook_id: str, repository_slug: str) -> None:
        """Delete webhook"""
        return await self._delete(
            DELETE_WEBHOOK_1.path.format(projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug),
        )

    async def get_webhook_1(
        self,
        project_key: str,
        webhook_id: str,
        repository_slug: str,
        *,
        statistics: str | None = None,
    ) -> RestWebhook:
        """Get webhook"""
        return await self._get(
            GET_WEBHOOK_1.path.format(projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug),
            params={"statistics": statistics},
            model=RestWebhook,
        )

    async def update_webhook_1(
        self,
        project_key: str,
        webhook_id: str,
        repository_slug: str,
        body: RestWebhook,
    ) -> RestWebhook:
        """Update webhook"""
        return await self._put(
            UPDATE_WEBHOOK_1.path.format(projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestWebhook,
        )

    async def get_latest_invocation_1(
        self,
        project_key: str,
        webhook_id: str,
        repository_slug: str,
        *,
        event: str | None = None,
        outcome: str | None = None,
    ) -> RestDetailedInvocation:
        """Get last webhook invocation details"""
        return await self._get(
            GET_LATEST_INVOCATION_1.path.format(
                projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug
            ),
            params={"event": event, "outcome": outcome},
            model=RestDetailedInvocation,
        )

    async def get_statistics_1(
        self,
        project_key: str,
        webhook_id: str,
        repository_slug: str,
        *,
        event: str | None = None,
    ) -> RestInvocationHistory:
        """Get webhook statistics"""
        return await self._get(
            GET_STATISTICS_1.path.format(projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug),
            params={"event": event},
            model=RestInvocationHistory,
        )

    async def get_statistics_summary_1(
        self,
        project_key: str,
        webhook_id: str,
        repository_slug: str,
    ) -> RestInvocationHistory:
        """Get webhook statistics summary"""
        return await self._get(
            GET_STATISTICS_SUMMARY_1.path.format(
                projectKey=project_key, webhookId=webhook_id, repositorySlug=repository_slug
            ),
            model=RestInvocationHistory,
        )

    def get_repositories_1(
        self,
        *,
        archived: str | None = None,
        projectname: str | None = None,
        projectkey: str | None = None,
        visibility: str | None = None,
        name: str | None = None,
        permission: str | None = None,
        state: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Search for repositories"""
        return self._get_paged(
            GET_REPOSITORIES_1.path,
            params={
                "archived": archived,
                "projectname": projectname,
                "projectkey": projectkey,
                "visibility": visibility,
                "name": name,
                "permission": permission,
                "state": state,
            },
            model=RestRepository,
            start=start,
            limit=limit,
        )

    def get_restrictions_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        matcher_type: str | None = None,
        matcher_id: str | None = None,
        type_: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRefRestriction]:
        """Search for ref restrictions"""
        return self._get_paged(
            GET_RESTRICTIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"matcherType": matcher_type, "matcherId": matcher_id, "type": type_},
            model=RestRefRestriction,
            start=start,
            limit=limit,
        )

    async def create_restrictions_1(self, project_key: str, repository_slug: str) -> RestRefRestriction:
        """Create multiple ref restrictions"""
        return await self._post(
            CREATE_RESTRICTIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRefRestriction,
        )

    async def delete_restriction_1(self, project_key: str, id: str, repository_slug: str) -> None:
        """Delete a ref restriction"""
        return await self._delete(
            DELETE_RESTRICTION_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
        )

    async def get_restriction_1(self, project_key: str, id: str, repository_slug: str) -> RestRefRestriction:
        """Get a ref restriction"""
        return await self._get(
            GET_RESTRICTION_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestRefRestriction,
        )

    async def delete_branch(self, project_key: str, repository_slug: str, body: RestBranchDeleteRequest) -> None:
        """Delete branch"""
        return await self._delete(DELETE_BRANCH.path.format(projectKey=project_key, repositorySlug=repository_slug))

    async def create_branch(self, project_key: str, repository_slug: str, body: RestBranchCreateRequest) -> RestBranch:
        """Create branch"""
        return await self._post(
            CREATE_BRANCH.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestBranch,
        )

    def find_by_commit(
        self,
        project_key: str,
        commit_id: Any,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMinimalRef]:
        """Get branch"""
        return self._get_paged(
            FIND_BY_COMMIT.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            model=RestMinimalRef,
            start=start,
            limit=limit,
        )

    async def un_react(
        self,
        project_key: str,
        comment_id: str,
        commit_id: str,
        emoticon: str,
        repository_slug: str,
    ) -> None:
        """Remove a reaction from comment"""
        return await self._delete(
            UN_REACT.path.format(
                projectKey=project_key,
                commentId=comment_id,
                commitId=commit_id,
                emoticon=emoticon,
                repositorySlug=repository_slug,
            ),
        )

    async def react(
        self,
        project_key: str,
        comment_id: str,
        commit_id: str,
        emoticon: str,
        repository_slug: str,
    ) -> RestUserReaction:
        """React to a comment"""
        return await self._put(
            REACT.path.format(
                projectKey=project_key,
                commentId=comment_id,
                commitId=commit_id,
                emoticon=emoticon,
                repositorySlug=repository_slug,
            ),
            model=RestUserReaction,
        )

    async def delete_all_default_tasks_1(self, project_key: str, repository_slug: str) -> None:
        """Deletes all default tasks for the repository"""
        return await self._delete(
            DELETE_ALL_DEFAULT_TASKS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
        )

    def get_default_tasks_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        markup: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDefaultTask]:
        """Get a page of default tasks"""
        return self._get_paged(
            GET_DEFAULT_TASKS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"markup": markup},
            model=RestDefaultTask,
            start=start,
            limit=limit,
        )

    async def add_default_task_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestDefaultTaskRequest,
    ) -> RestDefaultTask:
        """Add a default task"""
        return await self._post(
            ADD_DEFAULT_TASK_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDefaultTask,
        )

    async def delete_default_task_1(self, project_key: str, repository_slug: str, task_id: str) -> None:
        """Delete a specific default task"""
        return await self._delete(
            DELETE_DEFAULT_TASK_1.path.format(projectKey=project_key, repositorySlug=repository_slug, taskId=task_id),
        )

    async def update_default_task_1(
        self,
        project_key: str,
        repository_slug: str,
        task_id: str,
        body: RestDefaultTaskRequest,
    ) -> RestDefaultTask:
        """Update a default task"""
        return await self._put(
            UPDATE_DEFAULT_TASK_1.path.format(projectKey=project_key, repositorySlug=repository_slug, taskId=task_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDefaultTask,
        )

    async def create_tag(self, project_key: str, repository_slug: str, body: RestGitTagCreateRequest) -> RestTag:
        """Create tag"""
        return await self._post(
            CREATE_TAG.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestTag,
        )

    async def delete_tag(self, project_key: str, name: str, repository_slug: str) -> None:
        """Delete tag"""
        return await self._delete(
            DELETE_TAG.path.format(projectKey=project_key, name=name, repositorySlug=repository_slug),
        )

    async def get_status(self, project_key: str, repository_slug: str, *, at: str | None = None) -> RestRefSyncStatus:
        """Get synchronization status"""
        return await self._get(
            GET_STATUS_PROJECTS_REPOS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"at": at},
            model=RestRefSyncStatus,
        )

    async def set_enabled(self, project_key: str, repository_slug: str, body: RestRefSyncStatus) -> RestRefSyncStatus:
        """Disable synchronization"""
        return await self._post(
            SET_ENABLED.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRefSyncStatus,
        )

    async def synchronize(self, project_key: str, repository_slug: str, body: RestRefSyncRequest) -> RestRejectedRef:
        """Manual synchronization"""
        return await self._post(
            SYNCHRONIZE.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRejectedRef,
        )


class AsyncPullRequestsResource(AsyncResource):
    async def get_merge_config(self, scm_id: str) -> RestPullRequestMergeConfig:
        """Get merge strategies"""
        return await self._get(GET_MERGE_CONFIG.path.format(scmId=scm_id), model=RestPullRequestMergeConfig)

    async def set_merge_config(self, scm_id: str, body: RestPullRequestSettings) -> RestPullRequestMergeConfig:
        """Update merge strategies"""
        return await self._post(
            SET_MERGE_CONFIG.path.format(scmId=scm_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestMergeConfig,
        )

    def get_pull_requests(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequest]:
        """Get repository pull requests containing commit"""
        return self._get_paged(
            GET_PULL_REQUESTS.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            model=RestPullRequest,
            start=start,
            limit=limit,
        )

    def search(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        role: str | None = None,
        direction: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestApplicationUser]:
        """Search pull request participants"""
        return self._get_paged(
            SEARCH.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter, "role": role, "direction": direction},
            model=RestApplicationUser,
            start=start,
            limit=limit,
        )

    def get_page(
        self,
        project_key: str,
        repository_slug: str,
        *,
        with_attributes: str | None = None,
        at: str | None = None,
        with_properties: str | None = None,
        draft: str | None = None,
        filter_text: str | None = None,
        state: str | None = None,
        order: str | None = None,
        direction: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequest]:
        """Get pull requests for repository"""
        return self._get_paged(
            GET_PAGE.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "withAttributes": with_attributes,
                "at": at,
                "withProperties": with_properties,
                "draft": draft,
                "filterText": filter_text,
                "state": state,
                "order": order,
                "direction": direction,
            },
            model=RestPullRequest,
            start=start,
            limit=limit,
        )

    async def create(self, project_key: str, repository_slug: str, body: RestPullRequest) -> RestPullRequest:
        """Create pull request"""
        return await self._post(
            CREATE.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequest,
        )

    async def delete_3(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestDeleteRequest,
    ) -> None:
        """Delete pull request"""
        return await self._delete(
            DELETE_3.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
        )

    async def get_3(self, project_key: str, pull_request_id: str, repository_slug: str) -> RestPullRequest:
        """Get pull request"""
        return await self._get(
            GET_3.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            model=RestPullRequest,
        )

    async def update(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequest,
    ) -> RestPullRequest:
        """Update pull request metadata"""
        return await self._put(
            UPDATE.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequest,
        )

    async def stream_raw_diff_2(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        context_lines: str | None = None,
        whitespace: str | None = None,
    ) -> None:
        """Stream raw pull request diff"""
        return await self._get(
            STREAM_RAW_DIFF_2.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"contextLines": context_lines, "whitespace": whitespace},
        )

    async def stream_patch_1(self, project_key: str, pull_request_id: str, repository_slug: str) -> None:
        """Stream pull request as patch"""
        return await self._get(
            STREAM_PATCH_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
        )

    def get_activities(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        from_type: str | None = None,
        from_id: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequestActivity]:
        """Get pull request activity"""
        return self._get_paged(
            GET_ACTIVITIES.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"fromType": from_type, "fromId": from_id},
            model=RestPullRequestActivity,
            start=start,
            limit=limit,
        )

    async def withdraw_approval(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestPullRequestParticipant:
        """Unapprove pull request

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._delete(
            WITHDRAW_APPROVAL.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestPullRequestParticipant,
        )

    async def approve(self, project_key: str, pull_request_id: str, repository_slug: str) -> RestPullRequestParticipant:
        """Approve pull request

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(
            APPROVE.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            model=RestPullRequestParticipant,
        )

    async def cancel_auto_merge(self, project_key: str, pull_request_id: str, repository_slug: str) -> None:
        """Cancel auto-merge for pull request"""
        return await self._delete(
            CANCEL_AUTO_MERGE.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
        )

    async def get_auto_merge_request(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestAutoMergeRequest:
        """Get auto-merge request for pull request"""
        return await self._get(
            GET_AUTO_MERGE_REQUEST.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestAutoMergeRequest,
        )

    async def try_auto_merge(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestAutoMergeProcessingResult:
        """Auto-merge pull request"""
        return await self._post(
            TRY_AUTO_MERGE.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestAutoMergeProcessingResult,
        )

    def get_comments_1(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        count: str | None = None,
        state: list[str] | None = None,
        states: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestComment]:
        """Search pull request comments"""
        return self._get_paged(
            GET_COMMENTS_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"count": count, "state": state, "states": states},
            model=RestComment,
            start=start,
            limit=limit,
        )

    async def create_comment_1(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestComment,
    ) -> RestComment:
        """Add new blocker comment"""
        return await self._post(
            CREATE_COMMENT_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def delete_comment_1(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        version: str | None = None,
    ) -> None:
        """Delete pull request comment"""
        return await self._delete(
            DELETE_COMMENT_1.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            params={"version": version},
        )

    async def get_comment_1(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestComment:
        """Get pull request comment"""
        return await self._get(
            GET_COMMENT_1.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            model=RestComment,
        )

    async def update_comment_1(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestComment,
    ) -> RestComment:
        """Update pull request comment"""
        return await self._put(
            UPDATE_COMMENT_1.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def stream_changes_1(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        since_id: str | None = None,
        change_scope: str | None = None,
        until_id: str | None = None,
        with_comments: str | None = None,
        start: float | None = None,
        limit: float | None = None,
    ) -> RestChange:
        """Gets pull request changes"""
        return await self._get(
            STREAM_CHANGES_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={
                "sinceId": since_id,
                "changeScope": change_scope,
                "untilId": until_id,
                "withComments": with_comments,
                "start": start,
                "limit": limit,
            },
            model=RestChange,
        )

    def get_comments_2(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        path: str,
        from_hash: str | None = None,
        anchor_state: str | None = None,
        diff_type: list[str] | None = None,
        to_hash: str | None = None,
        state: list[str] | None = None,
        diff_types: str | None = None,
        states: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestComment]:
        """Get pull request comments for path"""
        return self._get_paged(
            GET_COMMENTS_2.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={
                "path": path,
                "fromHash": from_hash,
                "anchorState": anchor_state,
                "diffType": diff_type,
                "toHash": to_hash,
                "state": state,
                "diffTypes": diff_types,
                "states": states,
            },
            model=RestComment,
            start=start,
            limit=limit,
        )

    async def create_comment_2(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestComment,
    ) -> RestComment:
        """Add pull request comment"""
        return await self._post(
            CREATE_COMMENT_2.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def delete_comment_2(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        version: str | None = None,
    ) -> None:
        """Delete a pull request comment"""
        return await self._delete(
            DELETE_COMMENT_2.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            params={"version": version},
        )

    async def get_comment_2(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestComment:
        """Get a pull request comment"""
        return await self._get(
            GET_COMMENT_2.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            model=RestComment,
        )

    async def update_comment_2(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestComment,
    ) -> RestComment:
        """Update pull request comment"""
        return await self._put(
            UPDATE_COMMENT_2.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestComment,
        )

    async def apply_suggestion(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestApplySuggestionRequest,
    ) -> None:
        """Apply pull request suggestion"""
        return await self._post(
            APPLY_SUGGESTION.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_commit_message_suggestion(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestCommitMessageSuggestion:
        """Get commit message suggestion"""
        return await self._get(
            GET_COMMIT_MESSAGE_SUGGESTION.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestCommitMessageSuggestion,
        )

    def get_commits_1(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        avatar_scheme: str | None = None,
        with_counts: str | None = None,
        avatar_size: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestCommit]:
        """Get pull request commits"""
        return self._get_paged(
            GET_COMMITS_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"avatarScheme": avatar_scheme, "withCounts": with_counts, "avatarSize": avatar_size},
            model=RestCommit,
            start=start,
            limit=limit,
        )

    async def decline(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestDeclineRequest,
        *,
        version: str | None = None,
    ) -> RestPullRequest:
        """Decline pull request"""
        return await self._post(
            DECLINE.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            params={"version": version},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequest,
        )

    async def get_diff_stats_summary_2(
        self,
        path: str,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        since_id: str | None = None,
        src_path: str | None = None,
        until_id: str | None = None,
        whitespace: str | None = None,
    ) -> RestDiffStatsSummary:
        """Get diff stats summary for pull request"""
        return await self._get(
            GET_DIFF_STATS_SUMMARY_2.path.format(
                path=path, projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"sinceId": since_id, "srcPath": src_path, "untilId": until_id, "whitespace": whitespace},
            model=RestDiffStatsSummary,
        )

    async def stream_diff_2(
        self,
        path: str,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        avatar_scheme: str | None = None,
        context_lines: str | None = None,
        since_id: str | None = None,
        src_path: str | None = None,
        diff_type: str | None = None,
        until_id: str | None = None,
        whitespace: str | None = None,
        with_comments: str | None = None,
        avatar_size: str | None = None,
    ) -> RestDiff:
        """Stream a diff within a pull request"""
        return await self._get(
            STREAM_DIFF_2.path.format(
                path=path, projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={
                "avatarScheme": avatar_scheme,
                "contextLines": context_lines,
                "sinceId": since_id,
                "srcPath": src_path,
                "diffType": diff_type,
                "untilId": until_id,
                "whitespace": whitespace,
                "withComments": with_comments,
                "avatarSize": avatar_size,
            },
            model=RestDiff,
        )

    async def can_merge(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestPullRequestMergeability:
        """Test if pull request can be merged"""
        return await self._get(
            CAN_MERGE.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestPullRequestMergeability,
        )

    async def merge(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestMergeRequest,
        *,
        version: str | None = None,
    ) -> RestPullRequest:
        """Merge pull request"""
        return await self._post(
            MERGE.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            params={"version": version},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequest,
        )

    async def get_merge_base_1(self, project_key: str, pull_request_id: str, repository_slug: str) -> RestCommit:
        """Get the common ancestor between the latest commits of the source and target branches of the pull request"""
        return await self._get(
            GET_MERGE_BASE_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestCommit,
        )

    async def unassign_participant_role_1(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        username: str | None = None,
    ) -> None:
        """Unassign pull request participant

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._delete(
            UNASSIGN_PARTICIPANT_ROLE_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"username": username},
        )

    def list_participants(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequestParticipant]:
        """Get pull request participants"""
        return self._get_paged(
            LIST_PARTICIPANTS.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestPullRequestParticipant,
            start=start,
            limit=limit,
        )

    async def assign_participant_role(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestAssignParticipantRoleRequest,
    ) -> RestPullRequestParticipant:
        """Assign pull request participant role"""
        return await self._post(
            ASSIGN_PARTICIPANT_ROLE.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestParticipant,
        )

    async def unassign_participant_role(
        self,
        project_key: str,
        user_slug: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> None:
        """Unassign pull request participant"""
        return await self._delete(
            UNASSIGN_PARTICIPANT_ROLE.path.format(
                projectKey=project_key,
                userSlug=user_slug,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
        )

    async def update_status(
        self,
        project_key: str,
        user_slug: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestAssignStatusRequest,
        *,
        version: str | None = None,
    ) -> RestPullRequestParticipant:
        """Change pull request status"""
        return await self._put(
            UPDATE_STATUS.path.format(
                projectKey=project_key,
                userSlug=user_slug,
                pullRequestId=pull_request_id,
                repositorySlug=repository_slug,
            ),
            params={"version": version},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestParticipant,
        )

    async def reopen(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestReopenRequest,
        *,
        version: str | None = None,
    ) -> RestPullRequest:
        """Re-open pull request"""
        return await self._post(
            REOPEN.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            params={"version": version},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequest,
        )

    async def discard_review(self, project_key: str, pull_request_id: str, repository_slug: str) -> None:
        """Discard pull request review"""
        return await self._delete(
            DISCARD_REVIEW.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
        )

    def get_review(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestComment]:
        """Get pull request comment thread"""
        return self._get_paged(
            GET_REVIEW.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestComment,
            start=start,
            limit=limit,
        )

    async def finish_review(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestFinishReviewRequest,
        *,
        version: str | None = None,
    ) -> None:
        """Complete pull request review"""
        return await self._put(
            FINISH_REVIEW.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            params={"version": version},
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def unwatch_1(self, project_key: str, pull_request_id: str, repository_slug: str) -> None:
        """Stop watching pull request"""
        return await self._delete(
            UNWATCH_1.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
        )

    async def watch_1(self, project_key: str, pull_request_id: str, repository_slug: str) -> None:
        """Watch pull request"""
        return await self._post(
            WATCH_1.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
        )

    def get_reviewer_groups_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestReviewerGroup]:
        """Get all reviewer groups"""
        return self._get_paged(
            GET_REVIEWER_GROUPS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestReviewerGroup,
            start=start,
            limit=limit,
        )

    async def create_2(self, project_key: str, repository_slug: str, body: RestReviewerGroup) -> RestReviewerGroup:
        """Create reviewer group"""
        return await self._post(
            CREATE_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestReviewerGroup,
        )

    async def delete_7(self, project_key: str, id: str, repository_slug: str) -> None:
        """Delete reviewer group"""
        return await self._delete(DELETE_7.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug))

    async def get_reviewer_group_1(self, project_key: str, id: str, repository_slug: str) -> RestReviewerGroup:
        """Get reviewer group"""
        return await self._get(
            GET_REVIEWER_GROUP_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestReviewerGroup,
        )

    async def update_2(
        self,
        project_key: str,
        id: str,
        repository_slug: str,
        body: RestReviewerGroup,
    ) -> RestReviewerGroup:
        """Update reviewer group attributes"""
        return await self._put(
            UPDATE_2.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestReviewerGroup,
        )

    async def get_users(self, project_key: str, id: str, repository_slug: str) -> RestApplicationUser:
        """Get reviewer group users"""
        return await self._get(
            GET_USERS.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestApplicationUser,
        )

    def get_reviewer_groups(
        self,
        project_key: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestReviewerGroup]:
        """Get all reviewer groups"""
        return self._get_paged(
            GET_REVIEWER_GROUPS.path.format(projectKey=project_key),
            model=RestReviewerGroup,
            start=start,
            limit=limit,
        )

    async def create_1(self, project_key: str, body: RestReviewerGroup) -> RestReviewerGroup:
        """Create reviewer group"""
        return await self._post(
            CREATE_1.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestReviewerGroup,
        )

    async def delete_6(self, project_key: str, id: str) -> None:
        """Delete reviewer group"""
        return await self._delete(DELETE_6.path.format(projectKey=project_key, id=id))

    async def get_reviewer_group(self, project_key: str, id: str) -> RestReviewerGroup:
        """Get reviewer group"""
        return await self._get(GET_REVIEWER_GROUP.path.format(projectKey=project_key, id=id), model=RestReviewerGroup)

    async def update_1(self, project_key: str, id: str, body: RestReviewerGroup) -> RestReviewerGroup:
        """Update reviewer group attributes"""
        return await self._put(
            UPDATE_1.path.format(projectKey=project_key, id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestReviewerGroup,
        )

    async def un_react_1(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        emoticon: str,
        repository_slug: str,
    ) -> None:
        """Remove a reaction from a PR comment"""
        return await self._delete(
            UN_REACT_1.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                emoticon=emoticon,
                repositorySlug=repository_slug,
            ),
        )

    async def react_1(
        self,
        project_key: str,
        comment_id: str,
        pull_request_id: str,
        emoticon: str,
        repository_slug: str,
    ) -> RestUserReaction:
        """React to a PR comment"""
        return await self._put(
            REACT_1.path.format(
                projectKey=project_key,
                commentId=comment_id,
                pullRequestId=pull_request_id,
                emoticon=emoticon,
                repositorySlug=repository_slug,
            ),
            model=RestUserReaction,
        )

    async def create_pull_request_condition(
        self,
        project_key: str,
        body: RestDefaultReviewersRequest,
    ) -> RestPullRequestCondition:
        """Create default reviewer"""
        return await self._post(
            CREATE_PULL_REQUEST_CONDITION.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestCondition,
        )

    async def delete_pull_request_condition(self, project_key: str, id: str) -> None:
        """Remove default reviewer"""
        return await self._delete(DELETE_PULL_REQUEST_CONDITION.path.format(projectKey=project_key, id=id))

    async def update_pull_request_condition(
        self,
        project_key: str,
        id: str,
        body: RestDefaultReviewersRequest,
    ) -> RestPullRequestCondition:
        """Update the default reviewer"""
        return await self._put(
            UPDATE_PULL_REQUEST_CONDITION.path.format(projectKey=project_key, id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestCondition,
        )

    async def get_pull_request_conditions(self, project_key: str) -> RestPullRequestCondition:
        """Get default reviewers"""
        return await self._get(
            GET_PULL_REQUEST_CONDITIONS.path.format(projectKey=project_key),
            model=RestPullRequestCondition,
        )

    async def create_pull_request_condition_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestDefaultReviewersRequest,
    ) -> RestPullRequestCondition:
        """Create default reviewers condition"""
        return await self._post(
            CREATE_PULL_REQUEST_CONDITION_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestCondition,
        )

    async def delete_pull_request_condition_1(self, project_key: str, id: int, repository_slug: str) -> None:
        """Delete a default reviewer condition"""
        return await self._delete(
            DELETE_PULL_REQUEST_CONDITION_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
        )

    async def update_pull_request_condition_1(
        self,
        project_key: str,
        id: str,
        repository_slug: str,
    ) -> RestPullRequestCondition:
        """Update a default reviewer condition"""
        return await self._put(
            UPDATE_PULL_REQUEST_CONDITION_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestPullRequestCondition,
        )

    async def get_pull_request_conditions_1(self, project_key: str, repository_slug: str) -> RestPullRequestCondition:
        """Get configured default reviewers"""
        return await self._get(
            GET_PULL_REQUEST_CONDITIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestPullRequestCondition,
        )

    async def get_reviewers(
        self,
        project_key: str,
        repository_slug: str,
        *,
        target_repo_id: str | None = None,
        source_repo_id: str | None = None,
        source_ref_id: str | None = None,
        target_ref_id: str | None = None,
    ) -> RestPullRequestCondition:
        """Get required reviewers for PR creation"""
        return await self._get(
            GET_REVIEWERS.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "targetRepoId": target_repo_id,
                "sourceRepoId": source_repo_id,
                "sourceRefId": source_ref_id,
                "targetRefId": target_ref_id,
            },
            model=RestPullRequestCondition,
        )

    async def can_rebase(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestPullRequestRebaseability:
        """Check PR rebase precondition"""
        return await self._get(
            CAN_REBASE.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestPullRequestRebaseability,
        )

    async def rebase(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
        body: RestPullRequestRebaseRequest,
    ) -> RestPullRequestRebaseResult:
        """Rebase pull request"""
        return await self._post(
            REBASE.path.format(projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestPullRequestRebaseResult,
        )


class AsyncAuthenticationResource(AsyncResource):
    def get_all_access_tokens(
        self,
        project_key: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestAccessToken]:
        """Get project HTTP tokens"""
        return self._get_paged(
            GET_ALL_ACCESS_TOKENS.path.format(projectKey=project_key),
            model=RestAccessToken,
            start=start,
            limit=limit,
        )

    async def create_access_token(self, project_key: str, body: RestAccessTokenRequest) -> RestRawAccessToken:
        """Create project HTTP token"""
        return await self._put(
            CREATE_ACCESS_TOKEN.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRawAccessToken,
        )

    def get_all_access_tokens_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestAccessToken]:
        """Get repository HTTP tokens"""
        return self._get_paged(
            GET_ALL_ACCESS_TOKENS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestAccessToken,
            start=start,
            limit=limit,
        )

    async def create_access_token_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestAccessTokenRequest,
    ) -> RestRawAccessToken:
        """Create repository HTTP token"""
        return await self._put(
            CREATE_ACCESS_TOKEN_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRawAccessToken,
        )

    async def delete_by_id_1(self, project_key: str, token_id: str, repository_slug: str) -> None:
        """Delete a HTTP token"""
        return await self._delete(
            DELETE_BY_ID_1.path.format(projectKey=project_key, tokenId=token_id, repositorySlug=repository_slug),
        )

    async def get_by_id_1(self, project_key: str, token_id: str, repository_slug: str) -> RestAccessToken:
        """Get HTTP token by ID"""
        return await self._get(
            GET_BY_ID_1.path.format(projectKey=project_key, tokenId=token_id, repositorySlug=repository_slug),
            model=RestAccessToken,
        )

    async def update_access_token_1(
        self,
        project_key: str,
        token_id: str,
        repository_slug: str,
        body: RestAccessTokenRequest,
    ) -> RestAccessToken:
        """Update HTTP token"""
        return await self._post(
            UPDATE_ACCESS_TOKEN_1.path.format(projectKey=project_key, tokenId=token_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAccessToken,
        )

    async def delete_by_id(self, project_key: str, token_id: str) -> None:
        """Delete a HTTP token"""
        return await self._delete(DELETE_BY_ID.path.format(projectKey=project_key, tokenId=token_id))

    async def get_by_id(self, project_key: str, token_id: str) -> RestAccessToken:
        """Get HTTP token by ID"""
        return await self._get(GET_BY_ID.path.format(projectKey=project_key, tokenId=token_id), model=RestAccessToken)

    async def update_access_token(
        self,
        project_key: str,
        token_id: str,
        body: RestAccessTokenRequest,
    ) -> RestAccessToken:
        """Update HTTP token"""
        return await self._post(
            UPDATE_ACCESS_TOKEN.path.format(projectKey=project_key, tokenId=token_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAccessToken,
        )

    def get_all_access_tokens_2(
        self,
        user_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestAccessToken]:
        """Get personal HTTP tokens"""
        return self._get_paged(
            GET_ALL_ACCESS_TOKENS_2.path.format(userSlug=user_slug),
            model=RestAccessToken,
            start=start,
            limit=limit,
        )

    async def create_access_token_2(self, user_slug: str, body: RestAccessTokenRequest) -> RestRawAccessToken:
        """Create personal HTTP token"""
        return await self._put(
            CREATE_ACCESS_TOKEN_2.path.format(userSlug=user_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRawAccessToken,
        )

    async def delete_by_id_2(self, token_id: str, user_slug: str) -> None:
        """Delete a HTTP token"""
        return await self._delete(DELETE_BY_ID_2.path.format(tokenId=token_id, userSlug=user_slug))

    async def get_by_id_2(self, token_id: str, user_slug: str) -> RestAccessToken:
        """Get HTTP token by ID"""
        return await self._get(GET_BY_ID_2.path.format(tokenId=token_id, userSlug=user_slug), model=RestAccessToken)

    async def update_access_token_2(
        self,
        token_id: str,
        user_slug: str,
        body: RestAccessTokenRequest,
    ) -> RestAccessToken:
        """Update HTTP token"""
        return await self._post(
            UPDATE_ACCESS_TOKEN_2.path.format(tokenId=token_id, userSlug=user_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestAccessToken,
        )

    async def get_idps(self, *, start: float | None = None, limit: float | None = None) -> None:
        """Get all configured IdPs"""
        return await self._get(GET_IDPS.path, params={"start": start, "limit": limit})

    async def add_idp(self, body: IdpConfigEntity) -> IdpConfigEntity:
        """Create IdP configuration"""
        return await self._post(
            ADD_IDP.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IdpConfigEntity,
        )

    async def remove_idp(self, id: str) -> IdpConfigEntity:
        """Delete IdP configuration"""
        return await self._delete(REMOVE_IDP.path.format(id=id), model=IdpConfigEntity)

    async def get_idp(self, id: str) -> IdpConfigEntity:
        """Get IdP configuration"""
        return await self._get(GET_IDP.path.format(id=id), model=IdpConfigEntity)

    async def update_idp(self, id: str, body: IdpConfigEntity) -> IdpConfigEntity:
        """Update IdP configuration"""
        return await self._patch(
            UPDATE_IDP.path.format(id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=IdpConfigEntity,
        )

    async def get_jit_provisioned_users(self) -> JitUserEntity:
        """Get all JIT provisioned users"""
        return await self._get(GET_JIT_PROVISIONED_USERS.path, model=JitUserEntity)

    async def get_login_options(self, *, start: float | None = None, limit: float | None = None) -> None:
        """Get available login options"""
        return await self._get(GET_LOGIN_OPTIONS.path, params={"start": start, "limit": limit})

    async def get_config(self) -> SsoConfigEntity:
        """Get SSO configuration"""
        return await self._get(GET_CONFIG.path, model=SsoConfigEntity)

    async def update_config(self, body: SsoConfigEntity) -> SsoConfigEntity:
        """Update SSO configuration"""
        return await self._patch(
            UPDATE_CONFIG.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=SsoConfigEntity,
        )

    async def get(self) -> BasicAuthConfigEntity:
        """Get basic auth configuration"""
        return await self._get(GET.path, model=BasicAuthConfigEntity)

    async def put(self, body: BasicAuthConfigEntity) -> None:
        """Update basic auth configuration"""
        return await self._put(PUT.path, json=body.model_dump(by_alias=True, exclude_none=True))

    def get_for_repository_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        effective: str | None = None,
        minimum_permission: str | None = None,
        permission: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSshAccessKey]:
        """Get repository SSH keys"""
        return self._get_paged(
            GET_FOR_REPOSITORY_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={
                "filter": filter,
                "effective": effective,
                "minimumPermission": minimum_permission,
                "permission": permission,
            },
            model=RestSshAccessKey,
            start=start,
            limit=limit,
        )

    async def add_for_repository(
        self,
        project_key: str,
        repository_slug: str,
        body: RestSshAccessKey,
    ) -> RestSshAccessKey:
        """Add repository SSH key"""
        return await self._post(
            ADD_FOR_REPOSITORY.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSshAccessKey,
        )

    async def revoke_for_repository(self, project_key: str, key_id: str, repository_slug: str) -> None:
        """Revoke repository SSH key"""
        return await self._delete(
            REVOKE_FOR_REPOSITORY.path.format(projectKey=project_key, keyId=key_id, repositorySlug=repository_slug),
        )

    async def get_for_repository(self, project_key: str, key_id: str, repository_slug: str) -> RestSshAccessKey:
        """Get repository SSH key"""
        return await self._get(
            GET_FOR_REPOSITORY.path.format(projectKey=project_key, keyId=key_id, repositorySlug=repository_slug),
            model=RestSshAccessKey,
        )

    async def update_permission_1(
        self,
        project_key: str,
        key_id: str,
        permission: str,
        repository_slug: str,
    ) -> RestSshAccessKey:
        """Update repository SSH key permission"""
        return await self._put(
            UPDATE_PERMISSION_1.path.format(
                projectKey=project_key, keyId=key_id, permission=permission, repositorySlug=repository_slug
            ),
            model=RestSshAccessKey,
        )

    def get_ssh_keys_for_project(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        permission: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSshAccessKey]:
        """Get SSH key"""
        return self._get_paged(
            GET_SSH_KEYS_FOR_PROJECT.path.format(projectKey=project_key),
            params={"filter": filter, "permission": permission},
            model=RestSshAccessKey,
            start=start,
            limit=limit,
        )

    async def add_for_project(self, project_key: str, body: RestSshAccessKey) -> RestSshAccessKey:
        """Add project SSH key"""
        return await self._post(
            ADD_FOR_PROJECT.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSshAccessKey,
        )

    async def revoke_for_project(self, project_key: str, key_id: str) -> None:
        """Revoke project SSH key"""
        return await self._delete(REVOKE_FOR_PROJECT.path.format(projectKey=project_key, keyId=key_id))

    async def get_for_project(self, project_key: str, key_id: str) -> RestSshAccessKey:
        """Get project SSH key"""
        return await self._get(
            GET_FOR_PROJECT.path.format(projectKey=project_key, keyId=key_id),
            model=RestSshAccessKey,
        )

    async def update_permission(self, project_key: str, key_id: str, permission: str) -> RestSshAccessKey:
        """Update project SSH key permission"""
        return await self._put(
            UPDATE_PERMISSION.path.format(projectKey=project_key, keyId=key_id, permission=permission),
            model=RestSshAccessKey,
        )

    async def revoke_many(self, key_id: str) -> None:
        """Revoke project SSH key"""
        return await self._delete(REVOKE_MANY.path.format(keyId=key_id))

    async def get_for_projects(self, key_id: int) -> None:
        """Get project SSH keys"""
        return await self._get(GET_FOR_PROJECTS.path.format(keyId=key_id))

    async def get_for_repositories(self, key_id: str, *, with_restrictions: str | None = None) -> None:
        """Get repository SSH key"""
        return await self._get(
            GET_FOR_REPOSITORIES.path.format(keyId=key_id),
            params={"withRestrictions": with_restrictions},
        )

    async def delete_ssh_keys(self, *, user_name: str | None = None, user: str | None = None) -> None:
        """Delete all user SSH key"""
        return await self._delete(DELETE_SSH_KEYS.path, params={"userName": user_name, "user": user})

    def get_ssh_keys(
        self,
        *,
        user_name: str | None = None,
        user: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSshKey]:
        """Get SSH keys for user"""
        return self._get_paged(
            GET_SSH_KEYS.path,
            params={"userName": user_name, "user": user},
            model=RestSshKey,
            start=start,
            limit=limit,
        )

    async def add_ssh_key(self, *, user: Any | None = None) -> RestSshKey:
        """Add SSH key for user"""
        return await self._post(ADD_SSH_KEY.path, params={"user": user}, model=RestSshKey)

    async def delete_ssh_key(self, key_id: str) -> None:
        """Remove SSH key"""
        return await self._delete(DELETE_SSH_KEY.path.format(keyId=key_id))

    async def get_ssh_key(self, key_id: str) -> RestSshKey:
        """Get SSH key for user by keyId"""
        return await self._get(GET_SSH_KEY.path.format(keyId=key_id), model=RestSshKey)

    async def ssh_settings(self) -> RestSshSettings:
        """Get SSH settings"""
        return await self._get(SSH_SETTINGS.path, model=RestSshSettings)

    async def authenticate(self, body: AuthenticationEntity) -> AuthenticationResponse:
        """Authenticate with 2SV"""
        return await self._post(
            AUTHENTICATE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AuthenticationResponse,
        )

    async def get_captcha_data(self) -> CaptchaDataEntity:
        """Get CAPTCHA challenge"""
        return await self._get(GET_CAPTCHA_DATA.path, model=CaptchaDataEntity)

    async def authenticate_with_recovery_code(self, body: TotpRecoveryCodeAuthenticationDTO) -> AuthenticationResponse:
        """Authenticate using recovery code"""
        return await self._post(
            AUTHENTICATE_WITH_RECOVERY_CODE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=AuthenticationResponse,
        )

    async def verify_code(self, body: TotpCodeVerificationDTO) -> None:
        """Authenticate using TOTP code"""
        return await self._post(VERIFY_CODE.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_elevated_permission_status(self, *, action_type: str | None = None) -> None:
        """Get elevated session status"""
        return await self._get(GET_ELEVATED_PERMISSION_STATUS.path, params={"actionType": action_type})

    async def elevate_permissions_with_password(
        self,
        body: TotpElevationRestDTO,
        *,
        action_type: str | None = None,
    ) -> None:
        """Create elevated session with password"""
        return await self._post(
            ELEVATE_PERMISSIONS_WITH_PASSWORD.path,
            params={"actionType": action_type},
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def elevate_permissions_with_recovery_code(
        self,
        body: TotpRecoveryCodeDTO,
        *,
        action_type: str | None = None,
    ) -> TotpRecoveryCodeDTO:
        """Create elevated session with recovery code"""
        return await self._post(
            ELEVATE_PERMISSIONS_WITH_RECOVERY_CODE.path,
            params={"actionType": action_type},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=TotpRecoveryCodeDTO,
        )

    async def elevate_permissions_with_totp(
        self,
        body: TotpElevationRestDTO,
        *,
        action_type: str | None = None,
    ) -> None:
        """Create elevated session with TOTP"""
        return await self._post(
            ELEVATE_PERMISSIONS_WITH_TOTP.path,
            params={"actionType": action_type},
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_sso_management_status(self) -> SsoManagementStatusDTO:
        """Get SSO management status"""
        return await self._get(GET_SSO_MANAGEMENT_STATUS.path, model=SsoManagementStatusDTO)

    async def get_status(self) -> StatusDTO:
        """Get two-step verification status"""
        return await self._get(GET_STATUS.path, model=StatusDTO)

    async def complete_enforced_enrollment(self, body: TotpCodeVerificationDTO) -> TotpRecoveryCodeDTO:
        """Complete enforced enrollment in 2SV"""
        return await self._post(
            COMPLETE_ENFORCED_ENROLLMENT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=TotpRecoveryCodeDTO,
        )

    async def complete_authentication_change(self, body: TotpCodeVerificationDTO) -> TotpUserEnrollmentDTO:
        """Complete authentication app update for 2SV"""
        return await self._post(
            COMPLETE_AUTHENTICATION_CHANGE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=TotpUserEnrollmentDTO,
        )

    async def complete_voluntary_enrollment(self, body: TotpCodeVerificationDTO) -> TotpUserEnrollmentDTO:
        """Complete voluntary enrollment in 2SV"""
        return await self._post(
            COMPLETE_VOLUNTARY_ENROLLMENT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=TotpUserEnrollmentDTO,
        )

    async def rotate_recover_code(self) -> TotpRecoveryCodeDTO:
        """Rotate recovery code"""
        return await self._post(ROTATE_RECOVER_CODE.path, model=TotpRecoveryCodeDTO)

    async def start_enforced_enrollment(self, body: ConversationDTO) -> TotpUserEnrollmentDTO:
        """Start enforced enrollment in 2SV"""
        return await self._post(
            START_ENFORCED_ENROLLMENT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=TotpUserEnrollmentDTO,
        )

    async def start_enrollment_update(self) -> TotpUserEnrollmentDTO:
        """Start authentication app update for 2SV"""
        return await self._post(START_ENROLLMENT_UPDATE.path, model=TotpUserEnrollmentDTO)

    async def start_voluntary_enrollment(self) -> TotpUserEnrollmentDTO:
        """Start voluntary enrollment in 2SV"""
        return await self._post(START_VOLUNTARY_ENROLLMENT.path, model=TotpUserEnrollmentDTO)

    async def unenroll(self) -> None:
        """Uneroll current user from two-step verification"""
        return await self._delete(UNENROLL.path)

    async def unenroll_user(self, user_name: str, body: TotpElevationRestDTO) -> None:
        """Unenroll specific user from two-step verification"""
        return await self._delete(UNENROLL_USER.path.format(userName=user_name))


class AsyncBuildsResource(AsyncResource):
    async def get_capabilities(self) -> RestBuildCapabilities:
        """Get build capabilities"""
        return await self._get(GET_CAPABILITIES.path, model=RestBuildCapabilities)

    async def get_capabilities_1(self) -> None:
        """Get deployment capabilities"""
        return await self._get(GET_CAPABILITIES_1.path)

    async def delete(self, project_key: str, commit_id: str, repository_slug: str, *, key: str) -> None:
        """Delete a specific build status"""
        return await self._delete(
            DELETE.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"key": key},
        )

    async def get(self, project_key: str, commit_id: str, repository_slug: str, *, key: str) -> RestBuildStatus:
        """Get a specific build status"""
        return await self._get(
            GET_COMMITS_BUILDS.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"key": key},
            model=RestBuildStatus,
        )

    async def add(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        body: RestBuildStatusSetRequest,
    ) -> None:
        """Store a build status"""
        return await self._post(
            ADD.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def delete_1(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        deployment_sequence_number: str | None = None,
        key: str | None = None,
        environment_key: str | None = None,
    ) -> None:
        """Delete a deployment"""
        return await self._delete(
            DELETE_1.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={
                "deploymentSequenceNumber": deployment_sequence_number,
                "key": key,
                "environmentKey": environment_key,
            },
        )

    async def get_1(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        deployment_sequence_number: str | None = None,
        key: str | None = None,
        environment_key: str | None = None,
    ) -> RestDeployment:
        """Get a deployment"""
        return await self._get(
            GET_1.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={
                "deploymentSequenceNumber": deployment_sequence_number,
                "key": key,
                "environmentKey": environment_key,
            },
            model=RestDeployment,
        )

    async def create_or_update_deployment(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        body: RestDeploymentSetRequest,
    ) -> RestDeployment:
        """Create or update a deployment"""
        return await self._post(
            CREATE_OR_UPDATE_DEPLOYMENT.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDeployment,
        )

    async def get_multiple_build_status_stats(self) -> RestMultipleBuildStats:
        """Get build status statistics for multiple commits

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(GET_MULTIPLE_BUILD_STATUS_STATS.path, model=RestMultipleBuildStats)

    async def get_build_status_stats(self, commit_id: str, *, include_unique: bool | None = None) -> RestBuildStats:
        """Get build status statistics for commit

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._get(
            GET_BUILD_STATUS_STATS.path.format(commitId=commit_id),
            params={"includeUnique": include_unique},
            model=RestBuildStats,
        )

    def get_build_status(
        self,
        commit_id: str,
        *,
        order_by: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestBuildStatus]:
        """Get build statuses for commit

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return self._get_paged(
            GET_BUILD_STATUS.path.format(commitId=commit_id),
            params={"orderBy": order_by},
            model=RestBuildStatus,
            start=start,
            limit=limit,
        )

    async def add_build_status(self, commit_id: str, body: RestBuildStatus) -> None:
        """Create build status for commit

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(
            ADD_BUILD_STATUS.path.format(commitId=commit_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_annotations_1(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        severity: str | None = None,
        path: str | None = None,
        external_id: str | None = None,
        type_: str | None = None,
        key: str | None = None,
    ) -> RestInsightAnnotationsResponse:
        """Get Code Insights annotations for a commit"""
        return await self._get(
            GET_ANNOTATIONS_1.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            params={"severity": severity, "path": path, "externalId": external_id, "type": type_, "key": key},
            model=RestInsightAnnotationsResponse,
        )

    def get_reports(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestInsightReport]:
        """Get all Code Insights reports for a commit"""
        return self._get_paged(
            GET_REPORTS.path.format(projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug),
            model=RestInsightReport,
            start=start,
            limit=limit,
        )

    async def delete_a_code_insights_report(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
    ) -> None:
        """Delete a Code Insights report"""
        return await self._delete(
            DELETE_A_CODE_INSIGHTS_REPORT.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
        )

    async def get_a_code_insights_report(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
    ) -> RestInsightReport:
        """Get a Code Insights report"""
        return await self._get(
            GET_A_CODE_INSIGHTS_REPORT.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
            model=RestInsightReport,
        )

    async def set_a_code_insights_report(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
        body: RestSetInsightReportRequest,
    ) -> RestInsightReport:
        """Create a Code Insights report"""
        return await self._put(
            SET_A_CODE_INSIGHTS_REPORT.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestInsightReport,
        )

    async def delete_annotations(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
        *,
        external_id: str | None = None,
    ) -> None:
        """Delete Code Insights annotations"""
        return await self._delete(
            DELETE_ANNOTATIONS.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
            params={"externalId": external_id},
        )

    async def get_annotations(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
    ) -> RestInsightAnnotationsResponse:
        """Get Code Insights annotations for a report"""
        return await self._get(
            GET_ANNOTATIONS.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
            model=RestInsightAnnotationsResponse,
        )

    async def add_annotations(
        self,
        project_key: str,
        commit_id: str,
        repository_slug: str,
        key: str,
        body: RestBulkAddInsightAnnotationRequest,
    ) -> None:
        """Add Code Insights annotations"""
        return await self._post(
            ADD_ANNOTATIONS.path.format(
                projectKey=project_key, commitId=commit_id, repositorySlug=repository_slug, key=key
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def set_annotation(
        self,
        project_key: str,
        external_id: str,
        commit_id: str,
        repository_slug: str,
        key: str,
        body: RestSingleAddInsightAnnotationRequest,
    ) -> None:
        """Create or replace a Code Insights annotation"""
        return await self._put(
            SET_ANNOTATION.path.format(
                projectKey=project_key,
                externalId=external_id,
                commitId=commit_id,
                repositorySlug=repository_slug,
                key=key,
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def create_required_builds_merge_check(
        self,
        project_key: str,
        repository_slug: str,
        body: RestRequiredBuildConditionSetRequest,
    ) -> RestRequiredBuildCondition:
        """Create a required builds merge check"""
        return await self._post(
            CREATE_REQUIRED_BUILDS_MERGE_CHECK.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRequiredBuildCondition,
        )

    async def delete_required_builds_merge_check(self, project_key: str, id: int, repository_slug: str) -> None:
        """Delete a required builds merge check"""
        return await self._delete(
            DELETE_REQUIRED_BUILDS_MERGE_CHECK.path.format(
                projectKey=project_key, id=id, repositorySlug=repository_slug
            ),
        )

    async def update_required_builds_merge_check(
        self,
        project_key: str,
        id: int,
        repository_slug: str,
        body: RestRequiredBuildConditionSetRequest,
    ) -> RestRequiredBuildCondition:
        """Update a required builds merge check"""
        return await self._put(
            UPDATE_REQUIRED_BUILDS_MERGE_CHECK.path.format(
                projectKey=project_key, id=id, repositorySlug=repository_slug
            ),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRequiredBuildCondition,
        )

    def get_page_of_required_builds_merge_checks(
        self,
        project_key: str,
        repository_slug: str,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRequiredBuildCondition]:
        """Get required builds merge checks"""
        return self._get_paged(
            GET_PAGE_OF_REQUIRED_BUILDS_MERGE_CHECKS.path.format(
                projectKey=project_key, repositorySlug=repository_slug
            ),
            model=RestRequiredBuildCondition,
            start=start,
            limit=limit,
        )


class AsyncPermissionsResource(AsyncResource):
    async def delete_group(self, *, name: str) -> RestDetailedGroup:
        """Remove group"""
        return await self._delete(DELETE_GROUP.path, params={"name": name}, model=RestDetailedGroup)

    def get_groups_1(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedGroup]:
        """Get groups"""
        return self._get_paged(
            GET_GROUPS_1.path,
            params={"filter": filter},
            model=RestDetailedGroup,
            start=start,
            limit=limit,
        )

    async def create_group(self, *, name: str) -> RestDetailedGroup:
        """Create group"""
        return await self._post(CREATE_GROUP.path, params={"name": name}, model=RestDetailedGroup)

    async def add_user_to_group(self, body: UserPickerContext) -> None:
        """Add user to group

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(ADD_USER_TO_GROUP.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def add_users_to_group(self, body: GroupAndUsers) -> None:
        """Add multiple users to group"""
        return await self._post(ADD_USERS_TO_GROUP.path, json=body.model_dump(by_alias=True, exclude_none=True))

    def find_users_in_group(
        self,
        *,
        filter: str | None = None,
        context: str,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedUser]:
        """Get group members"""
        return self._get_paged(
            FIND_USERS_IN_GROUP.path,
            params={"filter": filter, "context": context},
            model=RestDetailedUser,
            start=start,
            limit=limit,
        )

    def find_users_not_in_group(
        self,
        *,
        filter: str | None = None,
        context: str,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedUser]:
        """Get members not in group"""
        return self._get_paged(
            FIND_USERS_NOT_IN_GROUP.path,
            params={"filter": filter, "context": context},
            model=RestDetailedUser,
            start=start,
            limit=limit,
        )

    async def remove_user_from_group(self, body: UserPickerContext) -> None:
        """Remove user from group

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(REMOVE_USER_FROM_GROUP.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def revoke_permissions_for_group(self, *, name: str) -> None:
        """Revoke all global permissions for group"""
        return await self._delete(REVOKE_PERMISSIONS_FOR_GROUP.path, params={"name": name})

    def get_groups_with_any_permission(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedGroup]:
        """Get groups with a global permission"""
        return self._get_paged(
            GET_GROUPS_WITH_ANY_PERMISSION.path,
            params={"filter": filter},
            model=RestPermittedGroup,
            start=start,
            limit=limit,
        )

    async def set_permission_for_groups(self, *, name: list[str], permission: str) -> None:
        """Update global permission for group"""
        return await self._put(SET_PERMISSION_FOR_GROUPS.path, params={"name": name, "permission": permission})

    def get_groups_without_any_permission(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedGroup]:
        """Get groups with no global permission"""
        return self._get_paged(
            GET_GROUPS_WITHOUT_ANY_PERMISSION.path,
            params={"filter": filter},
            model=RestDetailedGroup,
            start=start,
            limit=limit,
        )

    async def revoke_permissions_for_user(self, *, name: str) -> None:
        """Revoke all global permissions for user"""
        return await self._delete(REVOKE_PERMISSIONS_FOR_USER.path, params={"name": name})

    def get_users_with_any_permission(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedGroup]:
        """Get users with a global permission"""
        return self._get_paged(
            GET_USERS_WITH_ANY_PERMISSION.path,
            params={"filter": filter},
            model=RestPermittedGroup,
            start=start,
            limit=limit,
        )

    async def set_permission_for_users(self, *, name: list[str], permission: str) -> None:
        """Update global permission for user"""
        return await self._put(SET_PERMISSION_FOR_USERS.path, params={"name": name, "permission": permission})

    def get_users_without_any_permission(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestApplicationUser]:
        """Get users with no global permission"""
        return self._get_paged(
            GET_USERS_WITHOUT_ANY_PERMISSION.path,
            params={"filter": filter},
            model=RestApplicationUser,
            start=start,
            limit=limit,
        )

    async def get_user_directories(self, *, include_inactive: str | None = None) -> RestUserDirectory:
        """Get directories"""
        return await self._get(
            GET_USER_DIRECTORIES.path,
            params={"includeInactive": include_inactive},
            model=RestUserDirectory,
        )

    async def delete_user(self, *, name: str) -> RestDetailedUser:
        """Remove user"""
        return await self._delete(DELETE_USER.path, params={"name": name}, model=RestDetailedUser)

    def get_users_1(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedUser]:
        """Get users"""
        return self._get_paged(
            GET_USERS_1.path,
            params={"filter": filter},
            model=RestDetailedUser,
            start=start,
            limit=limit,
        )

    async def create_user(
        self,
        *,
        email_address: str,
        password: str | None = None,
        add_to_default_group: bool | None = True,
        display_name: str,
        name: str,
        notify: bool | None = None,
    ) -> None:
        """Create user"""
        return await self._post(
            CREATE_USER.path,
            params={
                "emailAddress": email_address,
                "password": password,
                "addToDefaultGroup": add_to_default_group,
                "displayName": display_name,
                "name": name,
                "notify": notify,
            },
        )

    async def update_user_details(self, body: UserUpdate) -> RestDetailedUser:
        """Update user details"""
        return await self._put(
            UPDATE_USER_DETAILS.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDetailedUser,
        )

    async def add_group_to_user(self, body: GroupPickerContext) -> None:
        """Add user to group

        .. deprecated::
            This endpoint is deprecated in the Bitbucket Data Center API.
        """
        return await self._post(ADD_GROUP_TO_USER.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def add_user_to_groups(self, body: UserAndGroups) -> None:
        """Add user to groups"""
        return await self._post(ADD_USER_TO_GROUPS.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def clear_user_captcha_challenge(self, *, name: str) -> None:
        """Clear CAPTCHA for user"""
        return await self._delete(CLEAR_USER_CAPTCHA_CHALLENGE.path, params={"name": name})

    async def update_user_password(self, body: AdminPasswordUpdate) -> None:
        """Set password for user"""
        return await self._put(UPDATE_USER_PASSWORD.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def validate_erasable(self, *, name: str) -> None:
        """Check user removal"""
        return await self._get(VALIDATE_ERASABLE.path, params={"name": name})

    async def erase_user(self, *, name: str) -> RestErasedUser:
        """Erase user information"""
        return await self._post(ERASE_USER.path, params={"name": name}, model=RestErasedUser)

    def find_groups_for_user(
        self,
        *,
        filter: str | None = None,
        context: str,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedUser]:
        """Get groups for user"""
        return self._get_paged(
            FIND_GROUPS_FOR_USER.path,
            params={"filter": filter, "context": context},
            model=RestDetailedUser,
            start=start,
            limit=limit,
        )

    def find_other_groups_for_user(
        self,
        *,
        filter: str | None = None,
        context: str,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedGroup]:
        """Find other groups for user"""
        return self._get_paged(
            FIND_OTHER_GROUPS_FOR_USER.path,
            params={"filter": filter, "context": context},
            model=RestDetailedGroup,
            start=start,
            limit=limit,
        )

    async def remove_group_from_user(self, body: GroupPickerContext) -> None:
        """Remove user from group"""
        return await self._post(REMOVE_GROUP_FROM_USER.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def rename_user(self, body: UserRename) -> RestDetailedUser:
        """Rename user"""
        return await self._post(
            RENAME_USER.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestDetailedUser,
        )

    async def get_groups(
        self,
        *,
        filter: str | None = None,
        start: float | None = None,
        limit: float | None = None,
    ) -> None:
        """Get group names"""
        return await self._get(GET_GROUPS.path, params={"filter": filter, "start": start, "limit": limit})

    async def revoke_permissions_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        user: str | None = None,
        group: str | None = None,
    ) -> None:
        """Revoke all repository permissions for users and groups"""
        return await self._delete(
            REVOKE_PERMISSIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"user": user, "group": group},
        )

    async def revoke_permissions_for_group_2(self, project_key: str, repository_slug: str, *, name: str) -> None:
        """Revoke group repository permission"""
        return await self._delete(
            REVOKE_PERMISSIONS_FOR_GROUP_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"name": name},
        )

    def get_groups_with_any_permission_2(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedGroup]:
        """Get groups with permission to repository"""
        return self._get_paged(
            GET_GROUPS_WITH_ANY_PERMISSION_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter},
            model=RestPermittedGroup,
            start=start,
            limit=limit,
        )

    async def set_permission_for_group(
        self,
        project_key: str,
        repository_slug: str,
        *,
        name: list[str],
        permission: str,
    ) -> None:
        """Update group repository permission"""
        return await self._put(
            SET_PERMISSION_FOR_GROUP.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"name": name, "permission": permission},
        )

    def get_groups_without_any_permission_2(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestDetailedGroup]:
        """Get groups without repository permission"""
        return self._get_paged(
            GET_GROUPS_WITHOUT_ANY_PERMISSION_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter},
            model=RestDetailedGroup,
            start=start,
            limit=limit,
        )

    async def search_permissions_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        permission: str | None = None,
        filter_text: str | None = None,
        type_: str | None = None,
    ) -> None:
        """Search repository permissions"""
        return await self._get(
            SEARCH_PERMISSIONS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"permission": permission, "filterText": filter_text, "type": type_},
        )

    async def revoke_permissions_for_user_2(self, project_key: str, repository_slug: str, *, name: str) -> None:
        """Revoke user repository permission"""
        return await self._delete(
            REVOKE_PERMISSIONS_FOR_USER_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"name": name},
        )

    def get_users_with_any_permission_2(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPermittedUser]:
        """Get users with permission to repository"""
        return self._get_paged(
            GET_USERS_WITH_ANY_PERMISSION_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter},
            model=RestPermittedUser,
            start=start,
            limit=limit,
        )

    async def set_permission_for_user(
        self,
        project_key: str,
        repository_slug: str,
        *,
        name: list[str],
        permission: str,
    ) -> None:
        """Update user repository permission"""
        return await self._put(
            SET_PERMISSION_FOR_USER.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"name": name, "permission": permission},
        )

    def get_users_without_permission_1(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestApplicationUser]:
        """Get users without repository permission"""
        return self._get_paged(
            GET_USERS_WITHOUT_PERMISSION_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter},
            model=RestApplicationUser,
            start=start,
            limit=limit,
        )


class AsyncSecurityResource(AsyncResource):
    def search_2(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSecretScanningAllowlistRule]:
        """Find repository secret scanning allowlist rules"""
        return self._get_paged(
            SEARCH_2.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter, "order": order},
            model=RestSecretScanningAllowlistRule,
            start=start,
            limit=limit,
        )

    async def create_allowlist_rule_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestSecretScanningAllowlistRuleSetRequest,
    ) -> RestSecretScanningAllowlistRule:
        """Create repository secret scanning allowlist rule"""
        return await self._post(
            CREATE_ALLOWLIST_RULE_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningAllowlistRule,
        )

    async def delete_allowlist_rule_1(self, project_key: str, id: str, repository_slug: str) -> None:
        """Delete a repository secret scanning allowlist rule"""
        return await self._delete(
            DELETE_ALLOWLIST_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
        )

    async def get_allowlist_rule_1(
        self,
        project_key: str,
        id: str,
        repository_slug: str,
    ) -> RestSecretScanningAllowlistRule:
        """Get a repository secret scanning allowlist rule"""
        return await self._get(
            GET_ALLOWLIST_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestSecretScanningAllowlistRule,
        )

    async def edit_allowlist_rule_1(
        self,
        project_key: str,
        id: str,
        repository_slug: str,
        body: RestSecretScanningAllowlistRuleSetRequest,
    ) -> RestSecretScanningAllowlistRule:
        """Edit an existing repository secret scanning allowlist rule"""
        return await self._put(
            EDIT_ALLOWLIST_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningAllowlistRule,
        )

    async def delete_exempt_repo(self) -> None:
        """Delete an exempt repository"""
        return await self._delete(DELETE_EXEMPT_REPO.path)

    async def is_repo_exempt(self) -> None:
        """Get whether a repository is exempt"""
        return await self._get(IS_REPO_EXEMPT.path)

    async def add_exempt_repo(self) -> None:
        """Exempt a repo from secret scanning"""
        return await self._put(ADD_EXEMPT_REPO.path)

    def search_3(
        self,
        project_key: str,
        repository_slug: str,
        *,
        filter: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSecretScanningRule]:
        """Find repository secret scanning rules"""
        return self._get_paged(
            SEARCH_3.path.format(projectKey=project_key, repositorySlug=repository_slug),
            params={"filter": filter, "order": order},
            model=RestSecretScanningRule,
            start=start,
            limit=limit,
        )

    async def create_rule_1(
        self,
        project_key: str,
        repository_slug: str,
        body: RestSecretScanningRuleSetRequest,
    ) -> RestSecretScanningRule:
        """Create repository secret scanning rule"""
        return await self._post(
            CREATE_RULE_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    async def delete_rule_1(self, project_key: str, id: str, repository_slug: str) -> None:
        """Delete a repository secret scanning rule"""
        return await self._delete(
            DELETE_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
        )

    async def get_rule_1(self, project_key: str, id: str, repository_slug: str) -> RestSecretScanningRule:
        """Get a repository secret scanning rule"""
        return await self._get(
            GET_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            model=RestSecretScanningRule,
        )

    async def edit_rule_1(
        self,
        project_key: str,
        id: str,
        repository_slug: str,
        body: RestSecretScanningRuleSetRequest,
    ) -> RestSecretScanningRule:
        """Edit an existing repository secret scanning rule"""
        return await self._put(
            EDIT_RULE_1.path.format(projectKey=project_key, id=id, repositorySlug=repository_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    def search_allowlist_rule(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSecretScanningAllowlistRule]:
        """Find project secret scanning allowlist rules"""
        return self._get_paged(
            SEARCH_ALLOWLIST_RULE.path.format(projectKey=project_key),
            params={"filter": filter, "order": order},
            model=RestSecretScanningAllowlistRule,
            start=start,
            limit=limit,
        )

    async def create_allowlist_rule(
        self,
        project_key: str,
        body: RestSecretScanningAllowlistRuleSetRequest,
    ) -> RestSecretScanningAllowlistRule:
        """Create project secret scanning allowlist rule"""
        return await self._post(
            CREATE_ALLOWLIST_RULE.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningAllowlistRule,
        )

    async def delete_allowlist_rule(self, project_key: str, id: str) -> None:
        """Delete a project secret scanning allowlist rule"""
        return await self._delete(DELETE_ALLOWLIST_RULE.path.format(projectKey=project_key, id=id))

    async def get_allowlist_rule(self, project_key: str, id: str) -> RestSecretScanningAllowlistRule:
        """Get a project secret scanning allowlist rule"""
        return await self._get(
            GET_ALLOWLIST_RULE.path.format(projectKey=project_key, id=id),
            model=RestSecretScanningAllowlistRule,
        )

    async def edit_allowlist_rule(
        self,
        project_key: str,
        id: str,
        body: RestSecretScanningAllowlistRuleSetRequest,
    ) -> RestSecretScanningAllowlistRule:
        """Edit an existing project secret scanning allowlist rule"""
        return await self._put(
            EDIT_ALLOWLIST_RULE.path.format(projectKey=project_key, id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningAllowlistRule,
        )

    def find_exempt_repos_by_project(
        self,
        *,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Find repos exempt from secret scanning for a project"""
        return self._get_paged(
            FIND_EXEMPT_REPOS_BY_PROJECT.path,
            params={"order": order},
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def bulk_add_exempt_repositories_1(self) -> None:
        """Bulk exempt repos from secret scanning"""
        return await self._post(BULK_ADD_EXEMPT_REPOSITORIES_1.path)

    def search_1(
        self,
        project_key: str,
        *,
        filter: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSecretScanningRule]:
        """Find project secret scanning rules"""
        return self._get_paged(
            SEARCH_1.path.format(projectKey=project_key),
            params={"filter": filter, "order": order},
            model=RestSecretScanningRule,
            start=start,
            limit=limit,
        )

    async def create_rule(self, project_key: str, body: RestSecretScanningRuleSetRequest) -> RestSecretScanningRule:
        """Create project secret scanning rule"""
        return await self._post(
            CREATE_RULE.path.format(projectKey=project_key),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    async def delete_rule(self, project_key: str, id: str) -> None:
        """Delete a project secret scanning rule"""
        return await self._delete(DELETE_RULE.path.format(projectKey=project_key, id=id))

    async def get_rule(self, project_key: str, id: str) -> RestSecretScanningRule:
        """Get a project secret scanning rule"""
        return await self._get(GET_RULE.path.format(projectKey=project_key, id=id), model=RestSecretScanningRule)

    async def edit_rule(
        self,
        project_key: str,
        id: str,
        body: RestSecretScanningRuleSetRequest,
    ) -> RestSecretScanningRule:
        """Edit an existing project secret scanning rule"""
        return await self._put(
            EDIT_RULE.path.format(projectKey=project_key, id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    def find_exempt_repos_by_scope(
        self,
        *,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestRepository]:
        """Find all repos exempt from secret scan"""
        return self._get_paged(
            FIND_EXEMPT_REPOS_BY_SCOPE.path,
            params={"order": order},
            model=RestRepository,
            start=start,
            limit=limit,
        )

    async def bulk_add_exempt_repositories(self) -> None:
        """Bulk exempt repos from secret scanning"""
        return await self._post(BULK_ADD_EXEMPT_REPOSITORIES.path)

    def search_4(
        self,
        *,
        filter: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestSecretScanningRule]:
        """Find global secret scanning rules"""
        return self._get_paged(
            SEARCH_4.path,
            params={"filter": filter, "order": order},
            model=RestSecretScanningRule,
            start=start,
            limit=limit,
        )

    async def create_rule_2(self, body: RestSecretScanningRuleSetRequest) -> RestSecretScanningRule:
        """Create global secret scanning rule"""
        return await self._post(
            CREATE_RULE_2.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    async def delete_rule_2(self, id: str) -> None:
        """Delete a global secret scanning rule"""
        return await self._delete(DELETE_RULE_2.path.format(id=id))

    async def get_rule_2(self, id: str) -> RestSecretScanningRule:
        """Get a global secret scanning rule"""
        return await self._get(GET_RULE_2.path.format(id=id), model=RestSecretScanningRule)

    async def edit_rule_2(self, id: str, body: RestSecretScanningRuleSetRequest) -> RestSecretScanningRule:
        """Edit a global secret scanning rule."""
        return await self._put(
            EDIT_RULE_2.path.format(id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestSecretScanningRule,
        )

    async def get_all_certificates(self) -> RestX509Certificate:
        """Get all X.509 certificates"""
        return await self._get(GET_ALL_CERTIFICATES.path, model=RestX509Certificate)

    async def create_certificate(self, body: ExampleCertificateMultipartFormData) -> RestX509Certificate:
        """Create an X.509 certificate"""
        return await self._post(
            CREATE_CERTIFICATE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestX509Certificate,
        )

    async def update_certificate_revocation_list_entries(self, id: str) -> None:
        """Update X.509 CRL entries"""
        return await self._put(UPDATE_CERTIFICATE_REVOCATION_LIST_ENTRIES.path.format(id=id))

    async def delete_certificate(self, id: str) -> None:
        """Delete an X.509 certificate"""
        return await self._delete(DELETE_CERTIFICATE.path.format(id=id))

    async def get_system_signing_configuration(self) -> RestSystemSigningConfiguration:
        """Get system signing configuration"""
        return await self._get(GET_SYSTEM_SIGNING_CONFIGURATION.path, model=RestSystemSigningConfiguration)

    async def update_system_signing_configuration(self) -> RestSystemSigningConfiguration:
        """Update system signing configuration"""
        return await self._post(UPDATE_SYSTEM_SIGNING_CONFIGURATION.path, model=RestSystemSigningConfiguration)

    async def delete_for_user(self, *, user: str | None = None) -> None:
        """Delete all GPG keys for user"""
        return await self._delete(DELETE_FOR_USER.path, params={"user": user})

    def get_keys_for_user(
        self,
        *,
        user: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestGpgKey]:
        """Get all GPG keys"""
        return self._get_paged(
            GET_KEYS_FOR_USER.path,
            params={"user": user},
            model=RestGpgKey,
            start=start,
            limit=limit,
        )

    async def add_key(self, body: RestGpgKey, *, user: str | None = None) -> RestGpgKey:
        """Create a GPG key"""
        return await self._post(
            ADD_KEY.path,
            params={"user": user},
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestGpgKey,
        )

    async def delete_key(self, fingerprint_or_id: str) -> None:
        """Delete a GPG key"""
        return await self._delete(DELETE_KEY.path.format(fingerprintOrId=fingerprint_or_id))


class AsyncAdminResource(AsyncResource):
    async def get_global_settings(self) -> RestSshKeySettings:
        """Get global SSH key settings"""
        return await self._get(GET_GLOBAL_SETTINGS.path, model=RestSshKeySettings)

    async def update_global_settings(self, body: RestSshKeySettings) -> None:
        """Update global SSH key settings"""
        return await self._put(UPDATE_GLOBAL_SETTINGS.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_supported_key_types(self) -> None:
        """Get supported SSH key algorithms and lengths"""
        return await self._get(GET_SUPPORTED_KEY_TYPES.path)

    async def delete_banner(self) -> None:
        """Delete announcement banner"""
        return await self._delete(DELETE_BANNER.path)

    async def get_banner(self) -> RestAnnouncementBanner:
        """Get announcement banner"""
        return await self._get(GET_BANNER.path, model=RestAnnouncementBanner)

    async def set_banner(self) -> None:
        """Update/Set announcement banner"""
        return await self._put(SET_BANNER.path)

    async def get_information(self) -> RestClusterInformation:
        """Get cluster node information"""
        return await self._get(GET_INFORMATION.path, model=RestClusterInformation)

    async def clear_default_branch(self) -> None:
        """Clear default branch"""
        return await self._delete(CLEAR_DEFAULT_BRANCH.path)

    async def get_default_branch(self) -> None:
        """Get the default branch"""
        return await self._get(GET_DEFAULT_BRANCH.path)

    async def set_default_branch(self) -> None:
        """Update/Set default branch"""
        return await self._put(SET_DEFAULT_BRANCH.path)

    async def get_control_plane_public_key(self) -> None:
        """Get the control plane PEM"""
        return await self._get(GET_CONTROL_PLANE_PUBLIC_KEY.path)

    async def connectivity(self) -> RestMeshConnectivityReport:
        """Generate Mesh connectivity report"""
        return await self._get(CONNECTIVITY.path, model=RestMeshConnectivityReport)

    async def get_all_registered_mesh_nodes(self) -> RestMeshNode:
        """Get all registered Mesh nodes"""
        return await self._get(GET_ALL_REGISTERED_MESH_NODES.path, model=RestMeshNode)

    async def register_new_mesh_node(self, body: RestMeshNode) -> RestMeshNode:
        """Register new Mesh node"""
        return await self._post(
            REGISTER_NEW_MESH_NODE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestMeshNode,
        )

    async def delete_2(self, id: int, *, force: bool | None = False) -> None:
        """Delete Mesh node"""
        return await self._delete(DELETE_2.path.format(id=id), params={"force": force})

    async def get_registered_mesh_node_by_id(self, id: str) -> RestMeshNode:
        """Get Mesh node"""
        return await self._get(GET_REGISTERED_MESH_NODE_BY_ID.path.format(id=id), model=RestMeshNode)

    async def update_mesh_node(self, id: str, body: RestMeshNode) -> RestMeshNode:
        """Update Mesh node"""
        return await self._put(
            UPDATE_MESH_NODE.path.format(id=id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestMeshNode,
        )

    async def get_support_zips(self) -> None:
        """Get support zips for all Mesh nodes"""
        return await self._get(GET_SUPPORT_ZIPS.path)

    async def get_support_zip(self, id: str) -> None:
        """Get support zip for node"""
        return await self._get(GET_SUPPORT_ZIP.path.format(id=id))

    async def get_2(self) -> RestBitbucketLicense:
        """Get license details"""
        return await self._get(GET_2.path, model=RestBitbucketLicense)

    async def update_license(self, body: RestBitbucketLicense) -> RestBitbucketLicense:
        """Update license"""
        return await self._post(
            UPDATE_LICENSE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestBitbucketLicense,
        )

    async def delete_mail_config(self) -> None:
        """Delete mail configuration"""
        return await self._delete(DELETE_MAIL_CONFIG.path)

    async def get_mail_config(self) -> RestMailConfiguration:
        """Get mail configuration"""
        return await self._get(GET_MAIL_CONFIG.path, model=RestMailConfiguration)

    async def set_mail_config(self) -> RestMailConfiguration:
        """Update mail configuration"""
        return await self._put(SET_MAIL_CONFIG.path, model=RestMailConfiguration)

    async def clear_sender_address(self) -> None:
        """Update mail configuration"""
        return await self._delete(CLEAR_SENDER_ADDRESS.path)

    async def get_sender_address(self) -> None:
        """Get server mail address"""
        return await self._get(GET_SENDER_ADDRESS.path)

    async def set_sender_address(self) -> None:
        """Update server mail address"""
        return await self._put(SET_SENDER_ADDRESS.path)

    def get_history(
        self,
        *,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestAggregateRejectCounter]:
        """Get rate limit history"""
        return self._get_paged(
            GET_HISTORY.path,
            params={"order": order},
            model=RestAggregateRejectCounter,
            start=start,
            limit=limit,
        )

    async def get_settings_2(self) -> RestRateLimitSettings:
        """Get rate limit settings"""
        return await self._get(GET_SETTINGS_2.path, model=RestRateLimitSettings)

    async def set_settings_2(self, body: RestRateLimitSettings) -> RestRateLimitSettings:
        """Set rate limit"""
        return await self._put(
            SET_SETTINGS_2.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRateLimitSettings,
        )

    def get_all_rate_limit_settings(
        self,
        *,
        filter: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestUserRateLimitSettings]:
        """Get rate limit settings for user"""
        return self._get_paged(
            GET_ALL_RATE_LIMIT_SETTINGS.path,
            params={"filter": filter},
            model=RestUserRateLimitSettings,
            start=start,
            limit=limit,
        )

    async def set_2(self, body: RestBulkUserRateLimitSettingsUpdateRequest) -> RestUserRateLimitSettings:
        """Set rate limit settings for users"""
        return await self._post(
            SET_2.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestUserRateLimitSettings,
        )

    async def delete_8(self, user_slug: str) -> None:
        """Delete user specific rate limit settings"""
        return await self._delete(DELETE_8.path.format(userSlug=user_slug))

    async def get_6(self, user_slug: str) -> RestUserRateLimitSettings:
        """Get user specific rate limit settings"""
        return await self._get(GET_6.path.format(userSlug=user_slug), model=RestUserRateLimitSettings)

    async def set_3(self, user_slug: str, body: RestUserRateLimitSettingsUpdateRequest) -> RestUserRateLimitSettings:
        """Set rate limit settings for user"""
        return await self._put(
            SET_3.path.format(userSlug=user_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestUserRateLimitSettings,
        )

    async def get_application_properties(self) -> RestApplicationProperties:
        """Get application properties"""
        return await self._get(GET_APPLICATION_PROPERTIES.path, model=RestApplicationProperties)

    async def create_hook_script(self, body: ExamplePostMultipartFormData) -> RestHookScript:
        """Create a new hook script"""
        return await self._post(
            CREATE_HOOK_SCRIPT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestHookScript,
        )

    async def delete_hook_script(self, script_id: str) -> None:
        """Delete a hook script."""
        return await self._delete(DELETE_HOOK_SCRIPT.path.format(scriptId=script_id))

    async def get_hook_script(self, script_id: str) -> RestHookScript:
        """Get a hook script"""
        return await self._get(GET_HOOK_SCRIPT.path.format(scriptId=script_id), model=RestHookScript)

    async def update_hook_script(self, script_id: str, body: ExamplePutMultipartFormData) -> RestHookScript:
        """Update a hook script"""
        return await self._put(
            UPDATE_HOOK_SCRIPT.path.format(scriptId=script_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestHookScript,
        )

    async def read(self, script_id: str) -> None:
        """Get hook script content"""
        return await self._get(READ.path.format(scriptId=script_id))

    def get_labels(self, *, prefix: str | None = None, start: int = 0, limit: int = 25) -> AsyncPageIterator[RestLabel]:
        """Get all labels"""
        return self._get_paged(GET_LABELS.path, params={"prefix": prefix}, model=RestLabel, start=start, limit=limit)

    async def get_label(self, label_name: str) -> RestLabel:
        """Get label"""
        return await self._get(GET_LABEL.path.format(labelName=label_name), model=RestLabel)

    def get_labelables(
        self,
        label_name: str,
        *,
        type_: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestLabelable]:
        """Get labelables for label"""
        return self._get_paged(
            GET_LABELABLES.path.format(labelName=label_name),
            params={"type": type_},
            model=RestLabelable,
            start=start,
            limit=limit,
        )

    async def get_level(self, logger_name: str) -> RestLogLevel:
        """Get current log level"""
        return await self._get(GET_LEVEL.path.format(loggerName=logger_name), model=RestLogLevel)

    async def set_level(self, level_name: str, logger_name: str) -> None:
        """Set log level"""
        return await self._put(SET_LEVEL.path.format(levelName=level_name, loggerName=logger_name))

    async def get_root_level(self) -> RestLogLevel:
        """Get root log level"""
        return await self._get(GET_ROOT_LEVEL.path, model=RestLogLevel)

    async def set_root_level(self, level_name: str) -> None:
        """Set root log level"""
        return await self._put(SET_ROOT_LEVEL.path.format(levelName=level_name))

    async def start_export(self, body: RestExportRequest) -> RestJob:
        """Start export job"""
        return await self._post(
            START_EXPORT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestJob,
        )

    async def preview_export(self, body: RestExportRequest) -> RestScopesExample:
        """Preview export"""
        return await self._post(
            PREVIEW_EXPORT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestScopesExample,
        )

    async def get_export_job(self, job_id: str) -> RestJob:
        """Get export job details"""
        return await self._get(GET_EXPORT_JOB.path.format(jobId=job_id), model=RestJob)

    async def cancel_export_job(self, job_id: str) -> None:
        """Cancel export job"""
        return await self._post(CANCEL_EXPORT_JOB.path.format(jobId=job_id))

    def get_export_job_messages(
        self,
        job_id: str,
        *,
        severity: str | None = None,
        subject: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestJobMessage]:
        """Get job messages"""
        return self._get_paged(
            GET_EXPORT_JOB_MESSAGES.path.format(jobId=job_id),
            params={"severity": severity, "subject": subject},
            model=RestJobMessage,
            start=start,
            limit=limit,
        )

    async def start_import(self, body: RestImportRequest) -> RestJob:
        """Start import job"""
        return await self._post(
            START_IMPORT.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestJob,
        )

    async def get_import_job(self, job_id: str) -> RestJob:
        """Get import job status"""
        return await self._get(GET_IMPORT_JOB.path.format(jobId=job_id), model=RestJob)

    async def cancel_import_job(self, job_id: str) -> None:
        """Cancel import job"""
        return await self._post(CANCEL_IMPORT_JOB.path.format(jobId=job_id))

    def get_import_job_messages(
        self,
        job_id: str,
        *,
        severity: str | None = None,
        subject: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestJobMessage]:
        """Get import job messages"""
        return self._get_paged(
            GET_IMPORT_JOB_MESSAGES.path.format(jobId=job_id),
            params={"severity": severity, "subject": subject},
            model=RestJobMessage,
            start=start,
            limit=limit,
        )

    async def start_mesh_migration(self) -> RestJob:
        """Start Mesh migration job"""
        return await self._post(START_MESH_MIGRATION.path, model=RestJob)

    async def preview_mesh_migration(self, body: RestMeshMigrationRequest) -> ExamplePreviewMigration:
        """Preview Mesh migration"""
        return await self._post(
            PREVIEW_MESH_MIGRATION.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=ExamplePreviewMigration,
        )

    def search_mesh_migration_repos(
        self,
        *,
        migration_id: str | None = None,
        project_key: str | None = None,
        name: str | None = None,
        state: str | None = None,
        remote: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMigrationRepository]:
        """Find repositories by Mesh migration state"""
        return self._get_paged(
            SEARCH_MESH_MIGRATION_REPOS.path,
            params={
                "migrationId": migration_id,
                "projectKey": project_key,
                "name": name,
                "state": state,
                "remote": remote,
            },
            model=RestMigrationRepository,
            start=start,
            limit=limit,
        )

    def get_all_mesh_migration_summaries(
        self,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMeshMigrationSummary]:
        """Get all Mesh migration job summaries"""
        return self._get_paged(
            GET_ALL_MESH_MIGRATION_SUMMARIES.path,
            model=RestMeshMigrationSummary,
            start=start,
            limit=limit,
        )

    async def get_active_mesh_migration_summary(self) -> RestMeshMigrationSummary:
        """Get summary for Mesh migration job"""
        return await self._get(GET_ACTIVE_MESH_MIGRATION_SUMMARY.path, model=RestMeshMigrationSummary)

    async def get_mesh_migration_job(self, job_id: str) -> None:
        """Get Mesh migration job details"""
        return await self._get(GET_MESH_MIGRATION_JOB.path.format(jobId=job_id))

    async def cancel_mesh_migration_job(self, job_id: str) -> None:
        """Cancel Mesh migration job"""
        return await self._post(CANCEL_MESH_MIGRATION_JOB.path.format(jobId=job_id))

    def get_mesh_migration_job_messages(
        self,
        job_id: str,
        *,
        severity: str | None = None,
        subject: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestJobMessage]:
        """Get Mesh migration job messages"""
        return self._get_paged(
            GET_MESH_MIGRATION_JOB_MESSAGES.path.format(jobId=job_id),
            params={"severity": severity, "subject": subject},
            model=RestJobMessage,
            start=start,
            limit=limit,
        )

    async def get_mesh_migration_job_summary(self, job_id: str) -> RestMeshMigrationSummary:
        """Get Mesh migration job summary"""
        return await self._get(GET_MESH_MIGRATION_JOB_SUMMARY.path.format(jobId=job_id), model=RestMeshMigrationSummary)

    async def get_users_2(
        self,
        *,
        filter: str | None = None,
        permission_n: str | None = None,
        permission: str | None = None,
        group: str | None = None,
    ) -> RestApplicationUser:
        """Get all users"""
        return await self._get(
            GET_USERS_2.path,
            params={"filter": filter, "permission.N": permission_n, "permission": permission, "group": group},
            model=RestApplicationUser,
        )

    async def update_user_details_1(self, body: UserUpdateWithCredentials) -> RestApplicationUser:
        """Update user details"""
        return await self._put(
            UPDATE_USER_DETAILS_1.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestApplicationUser,
        )

    async def update_user_password_1(self, body: UserPasswordUpdate) -> None:
        """Set password"""
        return await self._put(UPDATE_USER_PASSWORD_1.path, json=body.model_dump(by_alias=True, exclude_none=True))

    async def get_user(self, user_slug: str) -> RestApplicationUser:
        """Get user"""
        return await self._get(GET_USER.path.format(userSlug=user_slug), model=RestApplicationUser)

    async def delete_avatar(self, user_slug: str) -> RestNamedLink:
        """Delete user avatar"""
        return await self._delete(DELETE_AVATAR.path.format(userSlug=user_slug), model=RestNamedLink)

    async def upload_avatar_1(self, user_slug: str, body: ExampleAvatarMultipartFormData) -> None:
        """Update user avatar"""
        return await self._post(
            UPLOAD_AVATAR_1.path.format(userSlug=user_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_user_settings(self, user_slug: str) -> ExampleSettingsMap:
        """Get user settings"""
        return await self._get(GET_USER_SETTINGS.path.format(userSlug=user_slug), model=ExampleSettingsMap)

    async def update_settings(self, user_slug: str, body: ExampleSettingsMap) -> None:
        """Update user settings"""
        return await self._post(
            UPDATE_SETTINGS.path.format(userSlug=user_slug),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def dismiss_retention_config_review_notification(self) -> None:
        """Dismiss retention config notification"""
        return await self._delete(DISMISS_RETENTION_CONFIG_REVIEW_NOTIFICATION.path)

    async def get_repository_archive_policy(self) -> RestRepositoryPolicy:
        """Get repository archive policy"""
        return await self._get(GET_REPOSITORY_ARCHIVE_POLICY.path, model=RestRepositoryPolicy)

    async def set_repository_archive_policy(self, body: RestRepositoryPolicy) -> RestRepositoryPolicy:
        """Update repository archive policy"""
        return await self._put(
            SET_REPOSITORY_ARCHIVE_POLICY.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepositoryPolicy,
        )

    async def get_repository_delete_policy(self) -> RestRepositoryPolicy:
        """Get repository delete policy"""
        return await self._get(GET_REPOSITORY_DELETE_POLICY.path, model=RestRepositoryPolicy)

    async def set_repository_delete_policy(self, body: RestRepositoryPolicy) -> RestRepositoryPolicy:
        """Update the repository delete policy"""
        return await self._put(
            SET_REPOSITORY_DELETE_POLICY.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestRepositoryPolicy,
        )


class AsyncDashboardResource(AsyncResource):
    def get_pull_request_suggestions(
        self,
        *,
        changes_since: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequestSuggestion]:
        """Get pull request suggestions"""
        return self._get_paged(
            GET_PULL_REQUEST_SUGGESTIONS.path,
            params={"changesSince": changes_since},
            model=RestPullRequestSuggestion,
            start=start,
            limit=limit,
        )

    def get_pull_requests_1(
        self,
        *,
        closed_since: str | None = None,
        role: str | None = None,
        participant_status: str | None = None,
        state: str | None = None,
        user: str | None = None,
        order: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestPullRequest]:
        """Get pull requests for a user"""
        return self._get_paged(
            GET_PULL_REQUESTS_1.path,
            params={
                "closedSince": closed_since,
                "role": role,
                "participantStatus": participant_status,
                "state": state,
                "user": user,
                "order": order,
            },
            model=RestPullRequest,
            start=start,
            limit=limit,
        )

    async def get_pull_requests_2(
        self,
        *,
        role: str | None = "reviewer",
        limit: int | None = 25,
        start: int | None = 0,
    ) -> None:
        """Get pull requests in inbox"""
        return await self._get(GET_PULL_REQUESTS_2.path, params={"role": role, "limit": limit, "start": start})

    async def get_pull_request_count(self) -> None:
        """Get total number of pull requests in inbox"""
        return await self._get(GET_PULL_REQUEST_COUNT.path)


class AsyncMirroringResource(AsyncResource):
    async def delete_preferred_mirror_id(self) -> None:
        """Remove preferred mirror"""
        return await self._delete(DELETE_PREFERRED_MIRROR_ID.path)

    async def get_preferred_mirror_id(self) -> RestMirrorServer:
        """Get preferred mirror"""
        return await self._get(GET_PREFERRED_MIRROR_ID.path, model=RestMirrorServer)

    async def set_preferred_mirror_id(self) -> None:
        """Set preferred mirror"""
        return await self._post(SET_PREFERRED_MIRROR_ID.path)

    async def analytics_settings(self) -> RestAnalyticsSettings:
        """Get analytics settings from upstream"""
        return await self._get(ANALYTICS_SETTINGS.path, model=RestAnalyticsSettings)

    async def authenticate(self, body: RestAuthenticationRequest) -> RestApplicationUserWithPermissions:
        """Authenticate on behalf of a user"""
        return await self._post(
            AUTHENTICATE_MIRRORING_AUTHENTICATE.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestApplicationUserWithPermissions,
        )

    async def get_farm_nodes(self) -> RestClusterNode:
        """Get farm nodes"""
        return await self._get(GET_FARM_NODES.path, model=RestClusterNode)

    async def get_mirrored_repository(self, external_repository_id: str) -> RestMirroredRepository:
        """Get clone URLs"""
        return await self._get(
            GET_MIRRORED_REPOSITORY.path.format(externalRepositoryId=external_repository_id),
            model=RestMirroredRepository,
        )

    def list_mirrors(self, *, start: int = 0, limit: int = 25) -> AsyncPageIterator[RestMirrorServer]:
        """Get all mirrors"""
        return self._get_paged(LIST_MIRRORS.path, model=RestMirrorServer, start=start, limit=limit)

    async def remove(self, mirror_id: str) -> None:
        """Delete mirror by ID"""
        return await self._delete(REMOVE.path.format(mirrorId=mirror_id))

    async def get_mirror(self, mirror_id: str) -> RestMirrorServer:
        """Get mirror by ID"""
        return await self._get(GET_MIRROR.path.format(mirrorId=mirror_id), model=RestMirrorServer)

    async def upgrade(self, mirror_id: str, body: RestMirrorUpgradeRequest) -> RestMirrorServer:
        """Upgrade mirror server"""
        return await self._put(
            UPGRADE.path.format(mirrorId=mirror_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestMirrorServer,
        )

    async def publish_event(self, mirror_id: str, body: RestRepositoryMirrorEvent) -> None:
        """Publish RepositoryMirrorEvent"""
        return await self._post(
            PUBLISH_EVENT.path.format(mirrorId=mirror_id),
            json=body.model_dump(by_alias=True, exclude_none=True),
        )

    async def get_synchronization_progress(self) -> RestSyncProgress:
        """Get synchronization progress state"""
        return await self._get(GET_SYNCHRONIZATION_PROGRESS.path, model=RestSyncProgress)

    async def get_project_by_id(self, project_id: str) -> RestProject:
        """Get project"""
        return await self._get(GET_PROJECT_BY_ID.path.format(projectId=project_id), model=RestProject)

    def get_all_repos_for_project(
        self,
        project_id: str,
        *,
        include_default_branch: str | None = "false",
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[EnrichedRepository]:
        """Get hashes for repositories in project"""
        return self._get_paged(
            GET_ALL_REPOS_FOR_PROJECT.path.format(projectId=project_id),
            params={"includeDefaultBranch": include_default_branch},
            model=EnrichedRepository,
            start=start,
            limit=limit,
        )

    async def get_all_content_hashes(self, *, include_default_branch: str | None = "false") -> EnrichedRepository:
        """Get content hashes for repositories"""
        return await self._get(
            GET_ALL_CONTENT_HASHES.path,
            params={"includeDefaultBranch": include_default_branch},
            model=EnrichedRepository,
        )

    async def get_content_hash_by_id(
        self,
        repo_id: str,
        *,
        include_default_branch: bool | None = False,
    ) -> EnrichedRepository:
        """Get content hash for a repository"""
        return await self._get(
            GET_CONTENT_HASH_BY_ID.path.format(repoId=repo_id),
            params={"includeDefaultBranch": include_default_branch},
            model=EnrichedRepository,
        )

    async def get_repository_mirrors(
        self,
        repo_id: str,
        *,
        pre_authorized: bool | None = None,
    ) -> RestMirroredRepositoryDescriptor:
        """Get mirrors for repository"""
        return await self._get(
            GET_REPOSITORY_MIRRORS.path.format(repoId=repo_id),
            params={"preAuthorized": pre_authorized},
            model=RestMirroredRepositoryDescriptor,
        )

    def list_requests(
        self,
        *,
        state: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMirroringRequest]:
        """Get mirroring requests"""
        return self._get_paged(
            LIST_REQUESTS.path,
            params={"state": state},
            model=RestMirroringRequest,
            start=start,
            limit=limit,
        )

    async def register(self, body: RestMirroringRequest) -> RestMirroringRequest:
        """Create a mirroring request"""
        return await self._post(
            REGISTER.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestMirroringRequest,
        )

    async def delete_mirroring_request(self, mirroring_request_id: str) -> None:
        """Delete a mirroring request"""
        return await self._delete(DELETE_MIRRORING_REQUEST.path.format(mirroringRequestId=mirroring_request_id))

    async def get_mirroring_request(self, mirroring_request_id: str) -> RestMirroringRequest:
        """Get a mirroring request"""
        return await self._get(
            GET_MIRRORING_REQUEST.path.format(mirroringRequestId=mirroring_request_id),
            model=RestMirroringRequest,
        )

    async def accept(self, mirroring_request_id: str) -> RestMirrorServer:
        """Accept a mirroring request"""
        return await self._post(ACCEPT.path.format(mirroringRequestId=mirroring_request_id), model=RestMirrorServer)

    async def reject(self, mirroring_request_id: str) -> RestMirrorServer:
        """Reject a mirroring request"""
        return await self._post(REJECT.path.format(mirroringRequestId=mirroring_request_id), model=RestMirrorServer)

    async def get_out_of_sync_repositories(self) -> None:
        """Get out-of-sync repositories"""
        return await self._get(GET_OUT_OF_SYNC_REPOSITORIES.path)

    async def get_repository_lock_owner(self, project_key: str, repository_slug: str) -> RestRepositoryLockOwner:
        """Get the repository lock owner for the syncing process"""
        return await self._get(
            GET_REPOSITORY_LOCK_OWNER.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestRepositoryLockOwner,
        )

    async def get_repo_sync_status_1(
        self,
        project_key: str,
        repository_slug: str,
    ) -> RestMirrorRepositorySynchronizationStatus:
        """Gets information about the mirrored repository"""
        return await self._get(
            GET_REPO_SYNC_STATUS_1.path.format(projectKey=project_key, repositorySlug=repository_slug),
            model=RestMirrorRepositorySynchronizationStatus,
        )

    async def get_ref_changes_queue(self) -> RestRefSyncQueue:
        """Get items in ref changes queue"""
        return await self._get(GET_REF_CHANGES_QUEUE.path, model=RestRefSyncQueue)

    async def get_ref_changes_queue_count(self) -> None:
        """Get total number of items in ref changes queue"""
        return await self._get(GET_REF_CHANGES_QUEUE_COUNT.path)

    async def get_repository_lock_owners(self) -> RestRepositoryLockOwner:
        """Get all the repository lock owners for the syncing process"""
        return await self._get(GET_REPOSITORY_LOCK_OWNERS.path, model=RestRepositoryLockOwner)

    def get_repo_sync_status(
        self,
        *,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestMirrorRepositorySynchronizationStatus]:
        """Get sync status of repositories"""
        return self._get_paged(
            GET_REPO_SYNC_STATUS.path,
            model=RestMirrorRepositorySynchronizationStatus,
            start=start,
            limit=limit,
        )

    async def get_mirror_settings(self) -> RestUpstreamSettings:
        """Get upstream settings"""
        return await self._get(GET_MIRROR_SETTINGS.path, model=RestUpstreamSettings)

    async def set_mirror_settings(self, body: RestUpstreamSettings) -> RestUpstreamSettings:
        """Update upstream settings"""
        return await self._put(
            SET_MIRROR_SETTINGS.path,
            json=body.model_dump(by_alias=True, exclude_none=True),
            model=RestUpstreamSettings,
        )

    async def get_mirror_mode(self) -> None:
        """Get mirror mode"""
        return await self._get(GET_MIRROR_MODE.path)

    async def set_mirror_mode(self) -> None:
        """Update mirror mode"""
        return await self._put(SET_MIRROR_MODE.path)

    async def get_mirrored_projects(self) -> None:
        """Get mirrored project IDs"""
        return await self._get(GET_MIRRORED_PROJECTS.path)

    async def start_mirroring_projects(self) -> None:
        """Add multiple projects to be mirrored"""
        return await self._post(START_MIRRORING_PROJECTS.path)

    async def stop_mirroring_project(self, project_id: str) -> None:
        """Stop mirroring project"""
        return await self._delete(STOP_MIRRORING_PROJECT.path.format(projectId=project_id))

    async def start_mirroring_project(self, project_id: str) -> None:
        """Add project to be mirrored"""
        return await self._post(START_MIRRORING_PROJECT.path.format(projectId=project_id))

    async def get_upstream_server(self) -> RestUpstreamServer:
        """Get upstream server"""
        return await self._get(GET_UPSTREAM_SERVER.path, model=RestUpstreamServer)

    async def end_rolling_upgrade(self) -> RestRollingUpgradeState:
        """End ZDU upgrade on mirror farm"""
        return await self._post(END_ROLLING_UPGRADE.path, model=RestRollingUpgradeState)

    async def start_rolling_upgrade(self) -> RestRollingUpgradeState:
        """Start ZDU upgrade on mirror farm"""
        return await self._post(START_ROLLING_UPGRADE.path, model=RestRollingUpgradeState)


class AsyncJiraIntegrationResource(AsyncResource):
    async def create_issue(self, comment_id: str, *, application_id: str | None = None) -> RestCommentJiraIssue:
        """Create Jira Issue"""
        return await self._post(
            CREATE_ISSUE.path.format(commentId=comment_id),
            params={"applicationId": application_id},
            model=RestCommentJiraIssue,
        )

    def get_commits_by_issue_key(
        self,
        issue_key: str,
        *,
        max_changes: str | None = None,
        start: int = 0,
        limit: int = 25,
    ) -> AsyncPageIterator[RestChangeset]:
        """Get changesets for issue key"""
        return self._get_paged(
            GET_COMMITS_BY_ISSUE_KEY.path.format(issueKey=issue_key),
            params={"maxChanges": max_changes},
            model=RestChangeset,
            start=start,
            limit=limit,
        )

    async def get_enhanced_entity_link_for_project(self, project_key: str) -> RestEnhancedEntityLink:
        """Get entity link"""
        return await self._get(
            GET_ENHANCED_ENTITY_LINK_FOR_PROJECT.path.format(projectKey=project_key),
            model=RestEnhancedEntityLink,
        )

    async def get_issue_keys_for_pull_request(
        self,
        project_key: str,
        pull_request_id: str,
        repository_slug: str,
    ) -> RestJiraIssue:
        """Get issues for a pull request"""
        return await self._get(
            GET_ISSUE_KEYS_FOR_PULL_REQUEST.path.format(
                projectKey=project_key, pullRequestId=pull_request_id, repositorySlug=repository_slug
            ),
            model=RestJiraIssue,
        )


class AsyncMarkupResource(AsyncResource):
    async def preview(
        self,
        *,
        html_escape: str | None = None,
        url_mode: str | None = None,
        include_heading_id: str | None = None,
        hardwrap: str | None = None,
    ) -> RestMarkup:
        """Preview markdown render"""
        return await self._post(
            PREVIEW.path,
            params={
                "htmlEscape": html_escape,
                "urlMode": url_mode,
                "includeHeadingId": include_heading_id,
                "hardwrap": hardwrap,
            },
            model=RestMarkup,
        )
