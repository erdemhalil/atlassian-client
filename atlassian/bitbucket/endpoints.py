"""Bitbucket Data Center REST API endpoint definitions.

Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.
"""

from __future__ import annotations

from atlassian.core.endpoint import Endpoint

# --- Projects ---

GET_AVATAR = Endpoint("GET", "/api/latest/hooks/{hookKey}/avatar", "Get project avatar")
GET_PROJECTS = Endpoint("GET", "/api/latest/projects", "Get projects")
CREATE_PROJECT = Endpoint("POST", "/api/latest/projects", "Create a new project")
DELETE_PROJECT = Endpoint("DELETE", "/api/latest/projects/{projectKey}", "Delete project")
GET_PROJECT = Endpoint("GET", "/api/latest/projects/{projectKey}", "Get a project")
UPDATE_PROJECT = Endpoint("PUT", "/api/latest/projects/{projectKey}", "Update project")
GET_PROJECT_AVATAR = Endpoint("GET", "/api/latest/projects/{projectKey}/avatar.png", "Get avatar for project")
UPLOAD_AVATAR = Endpoint("POST", "/api/latest/projects/{projectKey}/avatar.png", "Update project avatar")
GET_CONFIGURATIONS = Endpoint("GET", "/api/latest/projects/{projectKey}/hook-scripts", "Get configured hook scripts")
REMOVE_CONFIGURATION = Endpoint("DELETE", "/api/latest/projects/{projectKey}/hook-scripts/{scriptId}", "Remove a ho...")
SET_CONFIGURATION = Endpoint("PUT", "/api/latest/projects/{projectKey}/hook-scripts/{scriptId}", "Create/update a h...")
REVOKE_PERMISSIONS = Endpoint("DELETE", "/api/latest/projects/{projectKey}/permissions", "Revoke project permissions")
REVOKE_PERMISSIONS_FOR_GROUP_1 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/permissions/groups", "Revoke...")
GET_GROUPS_WITH_ANY_PERMISSION_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/groups", "Get gro...")
SET_PERMISSION_FOR_GROUPS_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/permissions/groups", "Update group...")
GET_GROUPS_WITHOUT_ANY_PERMISSION_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/groups/none", "Ge")
SEARCH_PERMISSIONS = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/search", "Search project permis...")
REVOKE_PERMISSIONS_FOR_USER_1 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/permissions/users", "Revoke u...")
GET_USERS_WITH_ANY_PERMISSION_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/users", "Get users...")
SET_PERMISSION_FOR_USERS_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/permissions/users", "Update user pr...")
GET_USERS_WITHOUT_PERMISSION = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/users/none", "Get use...")
HAS_ALL_USER_PERMISSION = Endpoint("GET", "/api/latest/projects/{projectKey}/permissions/{permission}/all", "Check ...")
MODIFY_ALL_USER_PERMISSION = Endpoint("POST", "/api/latest/projects/{projectKey}/permissions/{permission}/all", "Gr...")
GET_REPOSITORIES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos", "Get repositories for project")
CREATE_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos", "Create repository")
DELETE_REPOSITORY = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}", "Delete repository")
GET_REPOSITORY = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}", "Get repository")
FORK_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}", "Fork repository")
UPDATE_REPOSITORY = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}", "Update repository")
STREAM_CONTRIBUTING = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/contributing", "Get...")
GET_DEFAULT_BRANCH_2 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch", "Get")
SET_DEFAULT_BRANCH_2 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch", "Upd")
GET_FORKED_REPOSITORIES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/forks", "Get re...")
STREAM_LICENSE = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/license", "Get repositor...")
STREAM_README = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/readme", "Get repository ...")
RETRY_CREATE_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/recreate", "Re...")
GET_RELATED_REPOSITORIES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/related", "Get...")
DELETE_9 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/settings-restriction", "Stop enforcing project res...")
GET_7 = Endpoint("GET", "/api/latest/projects/{projectKey}/settings-restriction", "Get enforcing project setting")
CREATE_3 = Endpoint("POST", "/api/latest/projects/{projectKey}/settings-restriction", "Enforce project restriction")
GET_ALL = Endpoint("GET", "/api/latest/projects/{projectKey}/settings-restriction/all", "Get all enforcing project ...")
DELETE_AUTO_DECLINE_SETTINGS = Endpoint("DELETE", "/api/latest/projects/{projectKey}/settings/auto-decline", "Delet...")
GET_AUTO_DECLINE_SETTINGS = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/auto-decline", "Get auto de...")
SET_AUTO_DECLINE_SETTINGS = Endpoint("PUT", "/api/latest/projects/{projectKey}/settings/auto-decline", "Create/Upda...")
DELETE_4 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/settings/auto-merge", "Delete pull request auto-me...")
GET_4 = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/auto-merge", "Get pull request auto-merge settings")
SET = Endpoint("PUT", "/api/latest/projects/{projectKey}/settings/auto-merge", "Create or update the pull request a...")
GET_REPOSITORY_HOOKS = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/hooks", "Get repository hooks")
GET_REPOSITORY_HOOK = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}", "Get a reposito...")
DISABLE_HOOK = Endpoint("DELETE", "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/enabled", "Disable re...")
ENABLE_HOOK = Endpoint("PUT", "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/enabled", "Enable reposit...")
GET_SETTINGS = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/settings", "Get reposito...")
SET_SETTINGS = Endpoint("PUT", "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/settings", "Update repos...")
GET_PULL_REQUEST_SETTINGS = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/pull-requests/{scmId}", "Ge...")
UPDATE_PULL_REQUEST_SETTINGS = Endpoint("POST", "/api/latest/projects/{projectKey}/settings/pull-requests/{scmId}", "U")
FIND_WEBHOOKS = Endpoint("GET", "/api/latest/projects/{projectKey}/webhooks", "Find webhooks")
CREATE_WEBHOOK = Endpoint("POST", "/api/latest/projects/{projectKey}/webhooks", "Create webhook")
TEST_WEBHOOK = Endpoint("POST", "/api/latest/projects/{projectKey}/webhooks/test", "Test webhook")
DELETE_WEBHOOK = Endpoint("DELETE", "/api/latest/projects/{projectKey}/webhooks/{webhookId}", "Delete webhook")
GET_WEBHOOK = Endpoint("GET", "/api/latest/projects/{projectKey}/webhooks/{webhookId}", "Get webhook")
UPDATE_WEBHOOK = Endpoint("PUT", "/api/latest/projects/{projectKey}/webhooks/{webhookId}", "Update webhook")
GET_LATEST_INVOCATION = Endpoint("GET", "/api/latest/projects/{projectKey}/webhooks/{webhookId}/latest", "Get last ...")
GET_STATISTICS = Endpoint("GET", "/api/latest/projects/{projectKey}/webhooks/{webhookId}/statistics", "Get webhook ...")
GET_STATISTICS_SUMMARY = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/webhooks/{webhookId}/statistics/summary", ""
)
GET_RESTRICTIONS = Endpoint("GET", "/branch-permissions/latest/projects/{projectKey}/restrictions", "Search for ref...")
CREATE_RESTRICTIONS = Endpoint("POST", "/branch-permissions/latest/projects/{projectKey}/restrictions", "Create mul...")
DELETE_RESTRICTION = Endpoint("DELETE", "/branch-permissions/latest/projects/{projectKey}/restrictions/{id}", "Dele...")
GET_RESTRICTION = Endpoint("GET", "/branch-permissions/latest/projects/{projectKey}/restrictions/{id}", "Get a ref ...")
DELETE_ALL_DEFAULT_TASKS = Endpoint("DELETE", "/default-tasks/latest/projects/{projectKey}/tasks", "Deletes all def...")
GET_DEFAULT_TASKS = Endpoint("GET", "/default-tasks/latest/projects/{projectKey}/tasks", "Get a page of default tasks")
ADD_DEFAULT_TASK = Endpoint("POST", "/default-tasks/latest/projects/{projectKey}/tasks", "Add a default task")
DELETE_DEFAULT_TASK = Endpoint("DELETE", "/default-tasks/latest/projects/{projectKey}/tasks/{taskId}", "Delete a sp...")
UPDATE_DEFAULT_TASK = Endpoint("PUT", "/default-tasks/latest/projects/{projectKey}/tasks/{taskId}", "Update a defau...")

# --- Repositories ---

GET_REPOSITORIES_RECENTLY_ACCESSED = Endpoint("GET", "/api/latest/profile/recent/repos", "Get recently accessed rep...")
GET_ARCHIVE = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/archive", "Stream archive o...")
DELETE_ATTACHMENT = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}", ""
)
GET_ATTACHMENT = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}", ""
)
DELETE_ATTACHMENT_METADATA = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata", ""
)
GET_ATTACHMENT_METADATA = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata", ""
)
SAVE_ATTACHMENT_METADATA = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata", ""
)
GET_BRANCHES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches", "Find branches")
CREATE_BRANCH_FOR_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches", "")
GET_DEFAULT_BRANCH_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches/default", "G")
SET_DEFAULT_BRANCH_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches/default", "U")
GET_CONTENT = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse", "Get file content ...")
GET_CONTENT_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse/{path}", "Get file...")
EDIT_FILE = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse/{path}", "Edit file")
GET_CHANGES_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/changes", "Get changes ma...")
GET_COMMITS = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits", "Get commits")
GET_COMMIT = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}", "Get co...")
GET_CHANGES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/changes", "")
GET_COMMENTS = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments", ""
)
CREATE_COMMENT = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments", ""
)
DELETE_COMMENT = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}", ""
)
GET_COMMENT = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}", ""
)
UPDATE_COMMENT = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}", ""
)
GET_DIFF_STATS_SUMMARY = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/diff-stats-summary/{path}", ""
)
STREAM_DIFF = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/diff/{path}", ""
)
GET_MERGE_BASE = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/merge-base", ""
)
UNWATCH = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/watch", "Sto")
WATCH = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/watch", "Watc...")
STREAM_CHANGES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/changes", "Compa...")
STREAM_COMMITS = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/commits", "Get a...")
GET_DIFF_STATS_SUMMARY_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/diff-stats-summary{path}", ""
)
STREAM_DIFF_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/diff{path}", "Get...")
STREAM_RAW_DIFF = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/diff", "Get raw diff fo...")
STREAM_RAW_DIFF_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/diff/{path}", "Get ra...")
STREAM_FILES = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/files", "Get files in dire...")
STREAM_FILES_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/files/{path}", "Get file...")
GET_CONFIGURATIONS_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts", "Ge...")
REMOVE_CONFIGURATION_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts/{scriptId}", ""
)
SET_CONFIGURATION_1 = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts/{scriptId}", ""
)
GET_ALL_LABELS_FOR_REPOSITORY = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels", "Ge")
ADD_LABEL = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels", "Add repository label")
REMOVE_LABEL = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels/{labelName}", "R...")
STREAM = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/last-modified", "Stream files")
STREAM_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/last-modified/{path}", "Stream...")
STREAM_PATCH = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/patch", "Get patch content...")
STREAM_RAW = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/raw/{path}", "Get raw conten...")
GET_REF_CHANGE_ACTIVITY = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/ref-change-activities", ""
)
FIND_BRANCHES = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/ref-change-activities/branches", ""
)
DELETE_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline", ""
)
GET_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline", ""
)
SET_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline", ""
)
DELETE_5 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge", "Dele...")
GET_5 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge", "Get pull r...")
SET_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge", "Create or ...")
GET_REPOSITORY_HOOKS_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks", "G")
DELETE_REPOSITORY_HOOK = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}", ""
)
GET_REPOSITORY_HOOK_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}", ""
)
DISABLE_HOOK_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/enabled", ""
)
ENABLE_HOOK_1 = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/enabled", ""
)
GET_SETTINGS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/settings", ""
)
SET_SETTINGS_1 = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/settings", ""
)
GET_PULL_REQUEST_SETTINGS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/pull-requests", ""
)
UPDATE_PULL_REQUEST_SETTINGS_1 = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/pull-requests", ""
)
GET_TAGS = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags", "Find tag")
CREATE_TAG_FOR_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags", "Crea...")
GET_TAG = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags/{name}", "Get tag")
UNWATCH_2 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/watch", "Stop watching rep...")
WATCH_2 = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/watch", "Watch repository")
FIND_WEBHOOKS_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks", "Find webhooks")
CREATE_WEBHOOK_1 = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks", "Create we...")
SEARCH_WEBHOOKS = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/search", "Sear...")
TEST_WEBHOOK_1 = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/test", "Test w...")
DELETE_WEBHOOK_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}", ""
)
GET_WEBHOOK_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}", "G...")
UPDATE_WEBHOOK_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}", "U")
GET_LATEST_INVOCATION_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/latest", ""
)
GET_STATISTICS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/statistics", ""
)
GET_STATISTICS_SUMMARY_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/statistics/summary", ""
)
GET_REPOSITORIES_1 = Endpoint("GET", "/api/latest/repos", "Search for repositories")
GET_RESTRICTIONS_1 = Endpoint(
    "GET", "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions", ""
)
CREATE_RESTRICTIONS_1 = Endpoint(
    "POST", "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions", ""
)
DELETE_RESTRICTION_1 = Endpoint(
    "DELETE", "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions/{id}", ""
)
GET_RESTRICTION_1 = Endpoint(
    "GET", "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions/{id}", ""
)
DELETE_BRANCH = Endpoint("DELETE", "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches", "D...")
CREATE_BRANCH = Endpoint("POST", "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches", "Cre...")
FIND_BY_COMMIT = Endpoint(
    "GET", "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches/info/{commitId}", ""
)
UN_REACT = Endpoint(
    "DELETE",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}/reactions/{emoticon}",
    "",
)
REACT = Endpoint(
    "PUT",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}/reactions/{emoticon}",
    "",
)
DELETE_ALL_DEFAULT_TASKS_1 = Endpoint(
    "DELETE", "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks", ""
)
GET_DEFAULT_TASKS_1 = Endpoint("GET", "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks", "Get")
ADD_DEFAULT_TASK_1 = Endpoint("POST", "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks", "Add")
DELETE_DEFAULT_TASK_1 = Endpoint(
    "DELETE", "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks/{taskId}", ""
)
UPDATE_DEFAULT_TASK_1 = Endpoint(
    "PUT", "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks/{taskId}", ""
)
CREATE_TAG = Endpoint("POST", "/git/latest/projects/{projectKey}/repos/{repositorySlug}/tags", "Create tag")
DELETE_TAG = Endpoint("DELETE", "/git/latest/projects/{projectKey}/repos/{repositorySlug}/tags/{name}", "Delete tag")
GET_STATUS_PROJECTS_REPOS = Endpoint("GET", "/sync/latest/projects/{projectKey}/repos/{repositorySlug}", "Get synch...")
SET_ENABLED = Endpoint("POST", "/sync/latest/projects/{projectKey}/repos/{repositorySlug}", "Disable synchronization")
SYNCHRONIZE = Endpoint("POST", "/sync/latest/projects/{projectKey}/repos/{repositorySlug}/synchronize", "Manual syn...")

# --- PullRequests ---

GET_MERGE_CONFIG = Endpoint("GET", "/api/latest/admin/pull-requests/{scmId}", "Get merge strategies")
SET_MERGE_CONFIG = Endpoint("POST", "/api/latest/admin/pull-requests/{scmId}", "Update merge strategies")
GET_PULL_REQUESTS = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/pull-requests", ""
)
SEARCH = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/participants", "Search pull requ...")
GET_PAGE = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests", "Get pull requ...")
CREATE = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests", "Create pull re...")
DELETE_3 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}", ""
)
GET_3 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}", "Get")
UPDATE = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}", "Up")
STREAM_RAW_DIFF_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}.diff", ""
)
STREAM_PATCH_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}.patch", ""
)
GET_ACTIVITIES = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/activities", ""
)
WITHDRAW_APPROVAL = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve", ""
)
APPROVE = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve", ""
)
CANCEL_AUTO_MERGE = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge", ""
)
GET_AUTO_MERGE_REQUEST = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge", ""
)
TRY_AUTO_MERGE = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge", ""
)
GET_COMMENTS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments", ""
)
CREATE_COMMENT_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments",
    "",
)
DELETE_COMMENT_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "",
)
GET_COMMENT_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "",
)
UPDATE_COMMENT_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "",
)
STREAM_CHANGES_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/changes", ""
)
GET_COMMENTS_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments", ""
)
CREATE_COMMENT_2 = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments", ""
)
DELETE_COMMENT_2 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "",
)
GET_COMMENT_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "",
)
UPDATE_COMMENT_2 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "",
)
APPLY_SUGGESTION = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/apply-suggestion",
    "",
)
GET_COMMIT_MESSAGE_SUGGESTION = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/commit-message-suggestion",
    "",
)
GET_COMMITS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/commits", ""
)
DECLINE = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/decline", ""
)
GET_DIFF_STATS_SUMMARY_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/diff-stats-summary/{path}",
    "",
)
STREAM_DIFF_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/diff/{path}", ""
)
CAN_MERGE = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge", ""
)
MERGE = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge", ""
)
GET_MERGE_BASE_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge-base", ""
)
UNASSIGN_PARTICIPANT_ROLE_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants", ""
)
LIST_PARTICIPANTS = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants", ""
)
ASSIGN_PARTICIPANT_ROLE = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants", ""
)
UNASSIGN_PARTICIPANT_ROLE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants/{userSlug}",
    "",
)
UPDATE_STATUS = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants/{userSlug}",
    "",
)
REOPEN = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/reopen", ""
)
DISCARD_REVIEW = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review", ""
)
GET_REVIEW = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review", ""
)
FINISH_REVIEW = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review", ""
)
UNWATCH_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/watch", ""
)
WATCH_1 = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/watch", ""
)
GET_REVIEWER_GROUPS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups", ""
)
CREATE_2 = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups", "C...")
DELETE_7 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}", ""
)
GET_REVIEWER_GROUP_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}", ""
)
UPDATE_2 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}", "")
GET_USERS = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}/users", ""
)
GET_REVIEWER_GROUPS = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/reviewer-groups", "Get all review...")
CREATE_1 = Endpoint("POST", "/api/latest/projects/{projectKey}/settings/reviewer-groups", "Create reviewer group")
DELETE_6 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}", "Delete reviewer g...")
GET_REVIEWER_GROUP = Endpoint("GET", "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}", "Get review...")
UPDATE_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}", "Update reviewer grou...")
UN_REACT_1 = Endpoint(
    "DELETE",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/reactions/{emoticon}",
    "",
)
REACT_1 = Endpoint(
    "PUT",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/reactions/{emoticon}",
    "",
)
CREATE_PULL_REQUEST_CONDITION = Endpoint("POST", "/default-reviewers/latest/projects/{projectKey}/condition", "Crea...")
DELETE_PULL_REQUEST_CONDITION = Endpoint("DELETE", "/default-reviewers/latest/projects/{projectKey}/condition/{id}", "")
UPDATE_PULL_REQUEST_CONDITION = Endpoint("PUT", "/default-reviewers/latest/projects/{projectKey}/condition/{id}", "Upd")
GET_PULL_REQUEST_CONDITIONS = Endpoint("GET", "/default-reviewers/latest/projects/{projectKey}/conditions", "Get de...")
CREATE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "POST", "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition", ""
)
DELETE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "DELETE", "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}", ""
)
UPDATE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "PUT", "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}", ""
)
GET_PULL_REQUEST_CONDITIONS_1 = Endpoint(
    "GET", "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/conditions", ""
)
GET_REVIEWERS = Endpoint("GET", "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/reviewers", "G")
CAN_REBASE = Endpoint(
    "GET", "/git/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/rebase", ""
)
REBASE = Endpoint(
    "POST", "/git/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/rebase", ""
)

# --- Authentication ---

GET_ALL_ACCESS_TOKENS = Endpoint("GET", "/access-tokens/latest/projects/{projectKey}", "Get project HTTP tokens")
CREATE_ACCESS_TOKEN = Endpoint("PUT", "/access-tokens/latest/projects/{projectKey}", "Create project HTTP token")
GET_ALL_ACCESS_TOKENS_1 = Endpoint("GET", "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}", "Ge...")
CREATE_ACCESS_TOKEN_1 = Endpoint("PUT", "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}", "Crea...")
DELETE_BY_ID_1 = Endpoint("DELETE", "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}", "D")
GET_BY_ID_1 = Endpoint("GET", "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}", "Get ...")
UPDATE_ACCESS_TOKEN_1 = Endpoint(
    "POST", "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}", ""
)
DELETE_BY_ID = Endpoint("DELETE", "/access-tokens/latest/projects/{projectKey}/{tokenId}", "Delete a HTTP token")
GET_BY_ID = Endpoint("GET", "/access-tokens/latest/projects/{projectKey}/{tokenId}", "Get HTTP token by ID")
UPDATE_ACCESS_TOKEN = Endpoint("POST", "/access-tokens/latest/projects/{projectKey}/{tokenId}", "Update HTTP token")
GET_ALL_ACCESS_TOKENS_2 = Endpoint("GET", "/access-tokens/latest/users/{userSlug}", "Get personal HTTP tokens")
CREATE_ACCESS_TOKEN_2 = Endpoint("PUT", "/access-tokens/latest/users/{userSlug}", "Create personal HTTP token")
DELETE_BY_ID_2 = Endpoint("DELETE", "/access-tokens/latest/users/{userSlug}/{tokenId}", "Delete a HTTP token")
GET_BY_ID_2 = Endpoint("GET", "/access-tokens/latest/users/{userSlug}/{tokenId}", "Get HTTP token by ID")
UPDATE_ACCESS_TOKEN_2 = Endpoint("POST", "/access-tokens/latest/users/{userSlug}/{tokenId}", "Update HTTP token")
GET_IDPS = Endpoint("GET", "/authconfig/latest/idps", "Get all configured IdPs")
ADD_IDP = Endpoint("POST", "/authconfig/latest/idps", "Create IdP configuration")
REMOVE_IDP = Endpoint("DELETE", "/authconfig/latest/idps/{id}", "Delete IdP configuration")
GET_IDP = Endpoint("GET", "/authconfig/latest/idps/{id}", "Get IdP configuration")
UPDATE_IDP = Endpoint("PATCH", "/authconfig/latest/idps/{id}", "Update IdP configuration")
GET_JIT_PROVISIONED_USERS = Endpoint("GET", "/authconfig/latest/jit-users", "Get all JIT provisioned users")
GET_LOGIN_OPTIONS = Endpoint("GET", "/authconfig/latest/login-options", "Get available login options")
GET_CONFIG = Endpoint("GET", "/authconfig/latest/sso", "Get SSO configuration")
UPDATE_CONFIG = Endpoint("PATCH", "/authconfig/latest/sso", "Update SSO configuration")
GET = Endpoint("GET", "/basicauth/latest/config", "Get basic auth configuration")
PUT = Endpoint("PUT", "/basicauth/latest/config", "Update basic auth configuration")
GET_FOR_REPOSITORY_1 = Endpoint("GET", "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh", "Get reposi...")
ADD_FOR_REPOSITORY = Endpoint("POST", "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh", "Add reposit...")
REVOKE_FOR_REPOSITORY = Endpoint("DELETE", "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}", "R")
GET_FOR_REPOSITORY = Endpoint("GET", "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}", "Get ...")
UPDATE_PERMISSION_1 = Endpoint(
    "PUT", "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}/permission/{permission}", ""
)
GET_SSH_KEYS_FOR_PROJECT = Endpoint("GET", "/keys/latest/projects/{projectKey}/ssh", "Get SSH key")
ADD_FOR_PROJECT = Endpoint("POST", "/keys/latest/projects/{projectKey}/ssh", "Add project SSH key")
REVOKE_FOR_PROJECT = Endpoint("DELETE", "/keys/latest/projects/{projectKey}/ssh/{keyId}", "Revoke project SSH key")
GET_FOR_PROJECT = Endpoint("GET", "/keys/latest/projects/{projectKey}/ssh/{keyId}", "Get project SSH key")
UPDATE_PERMISSION = Endpoint("PUT", "/keys/latest/projects/{projectKey}/ssh/{keyId}/permission/{permission}", "Upda...")
REVOKE_MANY = Endpoint("DELETE", "/keys/latest/ssh/{keyId}", "Revoke project SSH key")
GET_FOR_PROJECTS = Endpoint("GET", "/keys/latest/ssh/{keyId}/projects", "Get project SSH keys")
GET_FOR_REPOSITORIES = Endpoint("GET", "/keys/latest/ssh/{keyId}/repos", "Get repository SSH key")
DELETE_SSH_KEYS = Endpoint("DELETE", "/ssh/latest/keys", "Delete all user SSH key")
GET_SSH_KEYS = Endpoint("GET", "/ssh/latest/keys", "Get SSH keys for user")
ADD_SSH_KEY = Endpoint("POST", "/ssh/latest/keys", "Add SSH key for user")
DELETE_SSH_KEY = Endpoint("DELETE", "/ssh/latest/keys/{keyId}", "Remove SSH key")
GET_SSH_KEY = Endpoint("GET", "/ssh/latest/keys/{keyId}", "Get SSH key for user by keyId")
SSH_SETTINGS = Endpoint("GET", "/ssh/latest/settings", "Get SSH settings")
AUTHENTICATE = Endpoint("POST", "/tsv/latest/authenticate", "Authenticate with 2SV")
GET_CAPTCHA_DATA = Endpoint("GET", "/tsv/latest/authenticate/captcha", "Get CAPTCHA challenge")
AUTHENTICATE_WITH_RECOVERY_CODE = Endpoint("POST", "/tsv/latest/authenticate/recovery-code", "Authenticate using re...")
VERIFY_CODE = Endpoint("POST", "/tsv/latest/authenticate/totp-code", "Authenticate using TOTP code")
GET_ELEVATED_PERMISSION_STATUS = Endpoint("GET", "/tsv/latest/elevate-permissions", "Get elevated session status")
ELEVATE_PERMISSIONS_WITH_PASSWORD = Endpoint("POST", "/tsv/latest/elevate-permissions/password", "Create elevated s...")
ELEVATE_PERMISSIONS_WITH_RECOVERY_CODE = Endpoint("POST", "/tsv/latest/elevate-permissions/recovery-code", "Create ...")
ELEVATE_PERMISSIONS_WITH_TOTP = Endpoint("POST", "/tsv/latest/elevate-permissions/totp", "Create elevated session w...")
GET_SSO_MANAGEMENT_STATUS = Endpoint("GET", "/tsv/latest/sso-management-status", "Get SSO management status")
GET_STATUS = Endpoint("GET", "/tsv/latest/status", "Get two-step verification status")
COMPLETE_ENFORCED_ENROLLMENT = Endpoint("POST", "/tsv/latest/totp/complete-enforced-enrollment", "Complete enforced...")
COMPLETE_AUTHENTICATION_CHANGE = Endpoint("POST", "/tsv/latest/totp/complete-enrollment-update", "Complete authenti...")
COMPLETE_VOLUNTARY_ENROLLMENT = Endpoint("POST", "/tsv/latest/totp/complete-voluntary-enrollment", "Complete volunt...")
ROTATE_RECOVER_CODE = Endpoint("POST", "/tsv/latest/totp/recovery-code/rotate", "Rotate recovery code")
START_ENFORCED_ENROLLMENT = Endpoint("POST", "/tsv/latest/totp/start-enforced-enrollment", "Start enforced enrollme...")
START_ENROLLMENT_UPDATE = Endpoint("POST", "/tsv/latest/totp/start-enrollment-update", "Start authentication app up...")
START_VOLUNTARY_ENROLLMENT = Endpoint("POST", "/tsv/latest/totp/start-voluntary-enrollment", "Start voluntary enrol...")
UNENROLL = Endpoint("DELETE", "/tsv/latest/totp/unenroll", "Uneroll current user from two-step verification")
UNENROLL_USER = Endpoint("DELETE", "/tsv/latest/totp/unenroll/user/{userName}", "Unenroll specific user from two-st...")

# --- Builds ---

GET_CAPABILITIES = Endpoint("GET", "/api/latest/build/capabilities", "Get build capabilities")
GET_CAPABILITIES_1 = Endpoint("GET", "/api/latest/deployment/capabilities", "Get deployment capabilities")
DELETE = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds", "Del")
GET_COMMITS_BUILDS = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds", ""
)
ADD = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds", "Store...")
DELETE_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments", ""
)
GET_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments", "Ge")
CREATE_OR_UPDATE_DEPLOYMENT = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments", ""
)
GET_MULTIPLE_BUILD_STATUS_STATS = Endpoint("POST", "/build-status/latest/commits/stats", "Get build status statisti...")
GET_BUILD_STATUS_STATS = Endpoint("GET", "/build-status/latest/commits/stats/{commitId}", "Get build status statist...")
GET_BUILD_STATUS = Endpoint("GET", "/build-status/latest/commits/{commitId}", "Get build statuses for commit")
ADD_BUILD_STATUS = Endpoint("POST", "/build-status/latest/commits/{commitId}", "Create build status for commit")
GET_ANNOTATIONS_1 = Endpoint(
    "GET", "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/annotations", ""
)
GET_REPORTS = Endpoint(
    "GET", "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports", ""
)
DELETE_A_CODE_INSIGHTS_REPORT = Endpoint(
    "DELETE", "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}", ""
)
GET_A_CODE_INSIGHTS_REPORT = Endpoint(
    "GET", "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}", ""
)
SET_A_CODE_INSIGHTS_REPORT = Endpoint(
    "PUT", "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}", ""
)
DELETE_ANNOTATIONS = Endpoint(
    "DELETE",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "",
)
GET_ANNOTATIONS = Endpoint(
    "GET",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "",
)
ADD_ANNOTATIONS = Endpoint(
    "POST",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "",
)
SET_ANNOTATION = Endpoint(
    "PUT",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations/{externalId}",
    "",
)
CREATE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "POST", "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition", ""
)
DELETE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "DELETE", "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}", ""
)
UPDATE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "PUT", "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}", ""
)
GET_PAGE_OF_REQUIRED_BUILDS_MERGE_CHECKS = Endpoint(
    "GET", "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/conditions", ""
)

# --- Permissions ---

DELETE_GROUP = Endpoint("DELETE", "/api/latest/admin/groups", "Remove group")
GET_GROUPS_1 = Endpoint("GET", "/api/latest/admin/groups", "Get groups")
CREATE_GROUP = Endpoint("POST", "/api/latest/admin/groups", "Create group")
ADD_USER_TO_GROUP = Endpoint("POST", "/api/latest/admin/groups/add-user", "Add user to group")
ADD_USERS_TO_GROUP = Endpoint("POST", "/api/latest/admin/groups/add-users", "Add multiple users to group")
FIND_USERS_IN_GROUP = Endpoint("GET", "/api/latest/admin/groups/more-members", "Get group members")
FIND_USERS_NOT_IN_GROUP = Endpoint("GET", "/api/latest/admin/groups/more-non-members", "Get members not in group")
REMOVE_USER_FROM_GROUP = Endpoint("POST", "/api/latest/admin/groups/remove-user", "Remove user from group")
REVOKE_PERMISSIONS_FOR_GROUP = Endpoint("DELETE", "/api/latest/admin/permissions/groups", "Revoke all global permis...")
GET_GROUPS_WITH_ANY_PERMISSION = Endpoint("GET", "/api/latest/admin/permissions/groups", "Get groups with a global ...")
SET_PERMISSION_FOR_GROUPS = Endpoint("PUT", "/api/latest/admin/permissions/groups", "Update global permission for g...")
GET_GROUPS_WITHOUT_ANY_PERMISSION = Endpoint("GET", "/api/latest/admin/permissions/groups/none", "Get groups with n...")
REVOKE_PERMISSIONS_FOR_USER = Endpoint("DELETE", "/api/latest/admin/permissions/users", "Revoke all global permissi...")
GET_USERS_WITH_ANY_PERMISSION = Endpoint("GET", "/api/latest/admin/permissions/users", "Get users with a global per...")
SET_PERMISSION_FOR_USERS = Endpoint("PUT", "/api/latest/admin/permissions/users", "Update global permission for user")
GET_USERS_WITHOUT_ANY_PERMISSION = Endpoint("GET", "/api/latest/admin/permissions/users/none", "Get users with no g...")
GET_USER_DIRECTORIES = Endpoint("GET", "/api/latest/admin/user-directories", "Get directories")
DELETE_USER = Endpoint("DELETE", "/api/latest/admin/users", "Remove user")
GET_USERS_1 = Endpoint("GET", "/api/latest/admin/users", "Get users")
CREATE_USER = Endpoint("POST", "/api/latest/admin/users", "Create user")
UPDATE_USER_DETAILS = Endpoint("PUT", "/api/latest/admin/users", "Update user details")
ADD_GROUP_TO_USER = Endpoint("POST", "/api/latest/admin/users/add-group", "Add user to group")
ADD_USER_TO_GROUPS = Endpoint("POST", "/api/latest/admin/users/add-groups", "Add user to groups")
CLEAR_USER_CAPTCHA_CHALLENGE = Endpoint("DELETE", "/api/latest/admin/users/captcha", "Clear CAPTCHA for user")
UPDATE_USER_PASSWORD = Endpoint("PUT", "/api/latest/admin/users/credentials", "Set password for user")
VALIDATE_ERASABLE = Endpoint("GET", "/api/latest/admin/users/erasure", "Check user removal")
ERASE_USER = Endpoint("POST", "/api/latest/admin/users/erasure", "Erase user information")
FIND_GROUPS_FOR_USER = Endpoint("GET", "/api/latest/admin/users/more-members", "Get groups for user")
FIND_OTHER_GROUPS_FOR_USER = Endpoint("GET", "/api/latest/admin/users/more-non-members", "Find other groups for user")
REMOVE_GROUP_FROM_USER = Endpoint("POST", "/api/latest/admin/users/remove-group", "Remove user from group")
RENAME_USER = Endpoint("POST", "/api/latest/admin/users/rename", "Rename user")
GET_GROUPS = Endpoint("GET", "/api/latest/groups", "Get group names")
REVOKE_PERMISSIONS_1 = Endpoint("DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions", "Rev")
REVOKE_PERMISSIONS_FOR_GROUP_2 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups", ""
)
GET_GROUPS_WITH_ANY_PERMISSION_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups", ""
)
SET_PERMISSION_FOR_GROUP = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups", ""
)
GET_GROUPS_WITHOUT_ANY_PERMISSION_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups/none", ""
)
SEARCH_PERMISSIONS_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/search", ""
)
REVOKE_PERMISSIONS_FOR_USER_2 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users", ""
)
GET_USERS_WITH_ANY_PERMISSION_2 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users", ""
)
SET_PERMISSION_FOR_USER = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users", ""
)
GET_USERS_WITHOUT_PERMISSION_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users/none", ""
)

# --- Security ---

SEARCH_2 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist", "F...")
CREATE_ALLOWLIST_RULE_1 = Endpoint(
    "POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist", ""
)
DELETE_ALLOWLIST_RULE_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}", ""
)
GET_ALLOWLIST_RULE_1 = Endpoint(
    "GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}", ""
)
EDIT_ALLOWLIST_RULE_1 = Endpoint(
    "PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}", ""
)
DELETE_EXEMPT_REPO = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt", ""
)
IS_REPO_EXEMPT = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt", "G")
ADD_EXEMPT_REPO = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt", "")
SEARCH_3 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules", "Find ...")
CREATE_RULE_1 = Endpoint("POST", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules", "Cr")
DELETE_RULE_1 = Endpoint(
    "DELETE", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}", ""
)
GET_RULE_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}", "G")
EDIT_RULE_1 = Endpoint("PUT", "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}", "")
SEARCH_ALLOWLIST_RULE = Endpoint("GET", "/api/latest/projects/{projectKey}/secret-scanning/allowlist", "Find projec...")
CREATE_ALLOWLIST_RULE = Endpoint("POST", "/api/latest/projects/{projectKey}/secret-scanning/allowlist", "Create pro...")
DELETE_ALLOWLIST_RULE = Endpoint("DELETE", "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}", "Del...")
GET_ALLOWLIST_RULE = Endpoint("GET", "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}", "Get a pro...")
EDIT_ALLOWLIST_RULE = Endpoint("PUT", "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}", "Edit an ...")
FIND_EXEMPT_REPOS_BY_PROJECT = Endpoint("GET", "/api/latest/projects/{projectKey}/secret-scanning/exempt", "Find re...")
BULK_ADD_EXEMPT_REPOSITORIES_1 = Endpoint("POST", "/api/latest/projects/{projectKey}/secret-scanning/exempt", "Bulk...")
SEARCH_1 = Endpoint("GET", "/api/latest/projects/{projectKey}/secret-scanning/rules", "Find project secret scanning...")
CREATE_RULE = Endpoint("POST", "/api/latest/projects/{projectKey}/secret-scanning/rules", "Create project secret sc...")
DELETE_RULE = Endpoint("DELETE", "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}", "Delete a project ...")
GET_RULE = Endpoint("GET", "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}", "Get a project secret sc...")
EDIT_RULE = Endpoint("PUT", "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}", "Edit an existing proje...")
FIND_EXEMPT_REPOS_BY_SCOPE = Endpoint("GET", "/api/latest/secret-scanning/exempt", "Find all repos exempt from secr...")
BULK_ADD_EXEMPT_REPOSITORIES = Endpoint("POST", "/api/latest/secret-scanning/exempt", "Bulk exempt repos from secre...")
SEARCH_4 = Endpoint("GET", "/api/latest/secret-scanning/rules", "Find global secret scanning rules")
CREATE_RULE_2 = Endpoint("POST", "/api/latest/secret-scanning/rules", "Create global secret scanning rule")
DELETE_RULE_2 = Endpoint("DELETE", "/api/latest/secret-scanning/rules/{id}", "Delete a global secret scanning rule")
GET_RULE_2 = Endpoint("GET", "/api/latest/secret-scanning/rules/{id}", "Get a global secret scanning rule")
EDIT_RULE_2 = Endpoint("PUT", "/api/latest/secret-scanning/rules/{id}", "Edit a global secret scanning rule.")
GET_ALL_CERTIFICATES = Endpoint("GET", "/api/latest/signing/x509-certificates", "Get all X.509 certificates")
CREATE_CERTIFICATE = Endpoint("POST", "/api/latest/signing/x509-certificates", "Create an X.509 certificate")
UPDATE_CERTIFICATE_REVOCATION_LIST_ENTRIES = Endpoint("PUT", "/api/latest/signing/x509-certificates/crl/{id}", "Upd...")
DELETE_CERTIFICATE = Endpoint("DELETE", "/api/latest/signing/x509-certificates/{id}", "Delete an X.509 certificate")
GET_SYSTEM_SIGNING_CONFIGURATION = Endpoint("GET", "/api/latest/system-signing/configuration", "Get system signing ...")
UPDATE_SYSTEM_SIGNING_CONFIGURATION = Endpoint("POST", "/api/latest/system-signing/configuration", "Update system s...")
DELETE_FOR_USER = Endpoint("DELETE", "/gpg/latest/keys", "Delete all GPG keys for user")
GET_KEYS_FOR_USER = Endpoint("GET", "/gpg/latest/keys", "Get all GPG keys")
ADD_KEY = Endpoint("POST", "/gpg/latest/keys", "Create a GPG key")
DELETE_KEY = Endpoint("DELETE", "/gpg/latest/keys/{fingerprintOrId}", "Delete a GPG key")

# --- Admin ---

GET_GLOBAL_SETTINGS = Endpoint("GET", "/admin", "Get global SSH key settings")
UPDATE_GLOBAL_SETTINGS = Endpoint("PUT", "/admin", "Update global SSH key settings")
GET_SUPPORTED_KEY_TYPES = Endpoint("GET", "/admin/supported-key-types", "Get supported SSH key algorithms and lengths")
DELETE_BANNER = Endpoint("DELETE", "/api/latest/admin/banner", "Delete announcement banner")
GET_BANNER = Endpoint("GET", "/api/latest/admin/banner", "Get announcement banner")
SET_BANNER = Endpoint("PUT", "/api/latest/admin/banner", "Update/Set announcement banner")
GET_INFORMATION = Endpoint("GET", "/api/latest/admin/cluster", "Get cluster node information")
CLEAR_DEFAULT_BRANCH = Endpoint("DELETE", "/api/latest/admin/default-branch", "Clear default branch")
GET_DEFAULT_BRANCH = Endpoint("GET", "/api/latest/admin/default-branch", "Get the default branch")
SET_DEFAULT_BRANCH = Endpoint("PUT", "/api/latest/admin/default-branch", "Update/Set default branch")
GET_CONTROL_PLANE_PUBLIC_KEY = Endpoint("GET", "/api/latest/admin/git/mesh/config/control-plane.pem", "Get the cont...")
CONNECTIVITY = Endpoint("GET", "/api/latest/admin/git/mesh/diagnostics/connectivity", "Generate Mesh connectivity r...")
GET_ALL_REGISTERED_MESH_NODES = Endpoint("GET", "/api/latest/admin/git/mesh/nodes", "Get all registered Mesh nodes")
REGISTER_NEW_MESH_NODE = Endpoint("POST", "/api/latest/admin/git/mesh/nodes", "Register new Mesh node")
DELETE_2 = Endpoint("DELETE", "/api/latest/admin/git/mesh/nodes/{id}", "Delete Mesh node")
GET_REGISTERED_MESH_NODE_BY_ID = Endpoint("GET", "/api/latest/admin/git/mesh/nodes/{id}", "Get Mesh node")
UPDATE_MESH_NODE = Endpoint("PUT", "/api/latest/admin/git/mesh/nodes/{id}", "Update Mesh node")
GET_SUPPORT_ZIPS = Endpoint("GET", "/api/latest/admin/git/mesh/support-zips", "Get support zips for all Mesh nodes")
GET_SUPPORT_ZIP = Endpoint("GET", "/api/latest/admin/git/mesh/support-zips/{id}", "Get support zip for node")
GET_2 = Endpoint("GET", "/api/latest/admin/license", "Get license details")
UPDATE_LICENSE = Endpoint("POST", "/api/latest/admin/license", "Update license")
DELETE_MAIL_CONFIG = Endpoint("DELETE", "/api/latest/admin/mail-server", "Delete mail configuration")
GET_MAIL_CONFIG = Endpoint("GET", "/api/latest/admin/mail-server", "Get mail configuration")
SET_MAIL_CONFIG = Endpoint("PUT", "/api/latest/admin/mail-server", "Update mail configuration")
CLEAR_SENDER_ADDRESS = Endpoint("DELETE", "/api/latest/admin/mail-server/sender-address", "Update mail configuration")
GET_SENDER_ADDRESS = Endpoint("GET", "/api/latest/admin/mail-server/sender-address", "Get server mail address")
SET_SENDER_ADDRESS = Endpoint("PUT", "/api/latest/admin/mail-server/sender-address", "Update server mail address")
GET_HISTORY = Endpoint("GET", "/api/latest/admin/rate-limit/history", "Get rate limit history")
GET_SETTINGS_2 = Endpoint("GET", "/api/latest/admin/rate-limit/settings", "Get rate limit settings")
SET_SETTINGS_2 = Endpoint("PUT", "/api/latest/admin/rate-limit/settings", "Set rate limit")
GET_ALL_RATE_LIMIT_SETTINGS = Endpoint("GET", "/api/latest/admin/rate-limit/settings/users", "Get rate limit settin...")
SET_2 = Endpoint("POST", "/api/latest/admin/rate-limit/settings/users", "Set rate limit settings for users")
DELETE_8 = Endpoint("DELETE", "/api/latest/admin/rate-limit/settings/users/{userSlug}", "Delete user specific rate ...")
GET_6 = Endpoint("GET", "/api/latest/admin/rate-limit/settings/users/{userSlug}", "Get user specific rate limit set...")
SET_3 = Endpoint("PUT", "/api/latest/admin/rate-limit/settings/users/{userSlug}", "Set rate limit settings for user")
GET_APPLICATION_PROPERTIES = Endpoint("GET", "/api/latest/application-properties", "Get application properties")
CREATE_HOOK_SCRIPT = Endpoint("POST", "/api/latest/hook-scripts", "Create a new hook script")
DELETE_HOOK_SCRIPT = Endpoint("DELETE", "/api/latest/hook-scripts/{scriptId}", "Delete a hook script.")
GET_HOOK_SCRIPT = Endpoint("GET", "/api/latest/hook-scripts/{scriptId}", "Get a hook script")
UPDATE_HOOK_SCRIPT = Endpoint("PUT", "/api/latest/hook-scripts/{scriptId}", "Update a hook script")
READ = Endpoint("GET", "/api/latest/hook-scripts/{scriptId}/content", "Get hook script content")
GET_LABELS = Endpoint("GET", "/api/latest/labels", "Get all labels")
GET_LABEL = Endpoint("GET", "/api/latest/labels/{labelName}", "Get label")
GET_LABELABLES = Endpoint("GET", "/api/latest/labels/{labelName}/labeled", "Get labelables for label")
GET_LEVEL = Endpoint("GET", "/api/latest/logs/logger/{loggerName}", "Get current log level")
SET_LEVEL = Endpoint("PUT", "/api/latest/logs/logger/{loggerName}/{levelName}", "Set log level")
GET_ROOT_LEVEL = Endpoint("GET", "/api/latest/logs/rootLogger", "Get root log level")
SET_ROOT_LEVEL = Endpoint("PUT", "/api/latest/logs/rootLogger/{levelName}", "Set root log level")
START_EXPORT = Endpoint("POST", "/api/latest/migration/exports", "Start export job")
PREVIEW_EXPORT = Endpoint("POST", "/api/latest/migration/exports/preview", "Preview export")
GET_EXPORT_JOB = Endpoint("GET", "/api/latest/migration/exports/{jobId}", "Get export job details")
CANCEL_EXPORT_JOB = Endpoint("POST", "/api/latest/migration/exports/{jobId}/cancel", "Cancel export job")
GET_EXPORT_JOB_MESSAGES = Endpoint("GET", "/api/latest/migration/exports/{jobId}/messages", "Get job messages")
START_IMPORT = Endpoint("POST", "/api/latest/migration/imports", "Start import job")
GET_IMPORT_JOB = Endpoint("GET", "/api/latest/migration/imports/{jobId}", "Get import job status")
CANCEL_IMPORT_JOB = Endpoint("POST", "/api/latest/migration/imports/{jobId}/cancel", "Cancel import job")
GET_IMPORT_JOB_MESSAGES = Endpoint("GET", "/api/latest/migration/imports/{jobId}/messages", "Get import job messages")
START_MESH_MIGRATION = Endpoint("POST", "/api/latest/migration/mesh", "Start Mesh migration job")
PREVIEW_MESH_MIGRATION = Endpoint("POST", "/api/latest/migration/mesh/preview", "Preview Mesh migration")
SEARCH_MESH_MIGRATION_REPOS = Endpoint("GET", "/api/latest/migration/mesh/repos", "Find repositories by Mesh migrat...")
GET_ALL_MESH_MIGRATION_SUMMARIES = Endpoint("GET", "/api/latest/migration/mesh/summaries", "Get all Mesh migration ...")
GET_ACTIVE_MESH_MIGRATION_SUMMARY = Endpoint("GET", "/api/latest/migration/mesh/summary", "Get summary for Mesh mig...")
GET_MESH_MIGRATION_JOB = Endpoint("GET", "/api/latest/migration/mesh/{jobId}", "Get Mesh migration job details")
CANCEL_MESH_MIGRATION_JOB = Endpoint("POST", "/api/latest/migration/mesh/{jobId}/cancel", "Cancel Mesh migration job")
GET_MESH_MIGRATION_JOB_MESSAGES = Endpoint("GET", "/api/latest/migration/mesh/{jobId}/messages", "Get Mesh migratio...")
GET_MESH_MIGRATION_JOB_SUMMARY = Endpoint("GET", "/api/latest/migration/mesh/{jobId}/summary", "Get Mesh migration ...")
GET_USERS_2 = Endpoint("GET", "/api/latest/users", "Get all users")
UPDATE_USER_DETAILS_1 = Endpoint("PUT", "/api/latest/users", "Update user details")
UPDATE_USER_PASSWORD_1 = Endpoint("PUT", "/api/latest/users/credentials", "Set password")
GET_USER = Endpoint("GET", "/api/latest/users/{userSlug}", "Get user")
DELETE_AVATAR = Endpoint("DELETE", "/api/latest/users/{userSlug}/avatar.png", "Delete user avatar")
UPLOAD_AVATAR_1 = Endpoint("POST", "/api/latest/users/{userSlug}/avatar.png", "Update user avatar")
GET_USER_SETTINGS = Endpoint("GET", "/api/latest/users/{userSlug}/settings", "Get user settings")
UPDATE_SETTINGS = Endpoint("POST", "/api/latest/users/{userSlug}/settings", "Update user settings")
DISMISS_RETENTION_CONFIG_REVIEW_NOTIFICATION = Endpoint(
    "DELETE", "/audit/latest/notification-settings/retention-config-review", ""
)
GET_REPOSITORY_ARCHIVE_POLICY = Endpoint("GET", "/policies/latest/admin/repos/archive", "Get repository archive policy")
SET_REPOSITORY_ARCHIVE_POLICY = Endpoint("PUT", "/policies/latest/admin/repos/archive", "Update repository archive ...")
GET_REPOSITORY_DELETE_POLICY = Endpoint("GET", "/policies/latest/admin/repos/delete", "Get repository delete policy")
SET_REPOSITORY_DELETE_POLICY = Endpoint("PUT", "/policies/latest/admin/repos/delete", "Update the repository delete...")

# --- Dashboard ---

GET_PULL_REQUEST_SUGGESTIONS = Endpoint("GET", "/api/latest/dashboard/pull-request-suggestions", "Get pull request ...")
GET_PULL_REQUESTS_1 = Endpoint("GET", "/api/latest/dashboard/pull-requests", "Get pull requests for a user")
GET_PULL_REQUESTS_2 = Endpoint("GET", "/api/latest/inbox/pull-requests", "Get pull requests in inbox")
GET_PULL_REQUEST_COUNT = Endpoint("GET", "/api/latest/inbox/pull-requests/count", "Get total number of pull request...")

# --- Mirroring ---

DELETE_PREFERRED_MIRROR_ID = Endpoint("DELETE", "/mirroring/latest/account/settings/preferred-mirror", "Remove pref...")
GET_PREFERRED_MIRROR_ID = Endpoint("GET", "/mirroring/latest/account/settings/preferred-mirror", "Get preferred mirror")
SET_PREFERRED_MIRROR_ID = Endpoint("POST", "/mirroring/latest/account/settings/preferred-mirror", "Set preferred mi...")
ANALYTICS_SETTINGS = Endpoint("GET", "/mirroring/latest/analyticsSettings", "Get analytics settings from upstream")
AUTHENTICATE_MIRRORING_AUTHENTICATE = Endpoint("POST", "/mirroring/latest/authenticate", "Authenticate on behalf of...")
GET_FARM_NODES = Endpoint("GET", "/mirroring/latest/farmNodes", "Get farm nodes")
GET_MIRRORED_REPOSITORY = Endpoint("GET", "/mirroring/latest/mirrorRepos/{externalRepositoryId}", "Get clone URLs")
LIST_MIRRORS = Endpoint("GET", "/mirroring/latest/mirrorServers", "Get all mirrors")
REMOVE = Endpoint("DELETE", "/mirroring/latest/mirrorServers/{mirrorId}", "Delete mirror by ID")
GET_MIRROR = Endpoint("GET", "/mirroring/latest/mirrorServers/{mirrorId}", "Get mirror by ID")
UPGRADE = Endpoint("PUT", "/mirroring/latest/mirrorServers/{mirrorId}", "Upgrade mirror server")
PUBLISH_EVENT = Endpoint("POST", "/mirroring/latest/mirrorServers/{mirrorId}/events", "Publish RepositoryMirrorEvent")
GET_SYNCHRONIZATION_PROGRESS = Endpoint("GET", "/mirroring/latest/progress", "Get synchronization progress state")
GET_PROJECT_BY_ID = Endpoint("GET", "/mirroring/latest/projects/{projectId}", "Get project")
GET_ALL_REPOS_FOR_PROJECT = Endpoint("GET", "/mirroring/latest/projects/{projectId}/repos", "Get hashes for reposit...")
GET_ALL_CONTENT_HASHES = Endpoint("GET", "/mirroring/latest/repos", "Get content hashes for repositories")
GET_CONTENT_HASH_BY_ID = Endpoint("GET", "/mirroring/latest/repos/{repoId}", "Get content hash for a repository")
GET_REPOSITORY_MIRRORS = Endpoint("GET", "/mirroring/latest/repos/{repoId}/mirrors", "Get mirrors for repository")
LIST_REQUESTS = Endpoint("GET", "/mirroring/latest/requests", "Get mirroring requests")
REGISTER = Endpoint("POST", "/mirroring/latest/requests", "Create a mirroring request")
DELETE_MIRRORING_REQUEST = Endpoint("DELETE", "/mirroring/latest/requests/{mirroringRequestId}", "Delete a mirrorin...")
GET_MIRRORING_REQUEST = Endpoint("GET", "/mirroring/latest/requests/{mirroringRequestId}", "Get a mirroring request")
ACCEPT = Endpoint("POST", "/mirroring/latest/requests/{mirroringRequestId}/accept", "Accept a mirroring request")
REJECT = Endpoint("POST", "/mirroring/latest/requests/{mirroringRequestId}/reject", "Reject a mirroring request")
GET_OUT_OF_SYNC_REPOSITORIES = Endpoint("GET", "/mirroring/latest/supportInfo/out-of-sync-repos/content", "Get out-...")
GET_REPOSITORY_LOCK_OWNER = Endpoint(
    "GET", "/mirroring/latest/supportInfo/projects/{projectKey}/repos/{repositorySlug}/repo-lock-owner", ""
)
GET_REPO_SYNC_STATUS_1 = Endpoint(
    "GET", "/mirroring/latest/supportInfo/projects/{projectKey}/repos/{repositorySlug}/repoSyncStatus", ""
)
GET_REF_CHANGES_QUEUE = Endpoint("GET", "/mirroring/latest/supportInfo/refChangesQueue", "Get items in ref changes ...")
GET_REF_CHANGES_QUEUE_COUNT = Endpoint("GET", "/mirroring/latest/supportInfo/refChangesQueue/count", "Get total num...")
GET_REPOSITORY_LOCK_OWNERS = Endpoint("GET", "/mirroring/latest/supportInfo/repo-lock-owners", "Get all the reposit...")
GET_REPO_SYNC_STATUS = Endpoint("GET", "/mirroring/latest/supportInfo/repoSyncStatus", "Get sync status of reposito...")
GET_MIRROR_SETTINGS = Endpoint("GET", "/mirroring/latest/syncSettings", "Get upstream settings")
SET_MIRROR_SETTINGS = Endpoint("PUT", "/mirroring/latest/syncSettings", "Update upstream settings")
GET_MIRROR_MODE = Endpoint("GET", "/mirroring/latest/syncSettings/mode", "Get mirror mode")
SET_MIRROR_MODE = Endpoint("PUT", "/mirroring/latest/syncSettings/mode", "Update mirror mode")
GET_MIRRORED_PROJECTS = Endpoint("GET", "/mirroring/latest/syncSettings/projects", "Get mirrored project IDs")
START_MIRRORING_PROJECTS = Endpoint("POST", "/mirroring/latest/syncSettings/projects", "Add multiple projects to be...")
STOP_MIRRORING_PROJECT = Endpoint("DELETE", "/mirroring/latest/syncSettings/projects/{projectId}", "Stop mirroring ...")
START_MIRRORING_PROJECT = Endpoint("POST", "/mirroring/latest/syncSettings/projects/{projectId}", "Add project to b...")
GET_UPSTREAM_SERVER = Endpoint("GET", "/mirroring/latest/upstreamServer", "Get upstream server")
END_ROLLING_UPGRADE = Endpoint("POST", "/mirroring/latest/zdu/end", "End ZDU upgrade on mirror farm")
START_ROLLING_UPGRADE = Endpoint("POST", "/mirroring/latest/zdu/start", "Start ZDU upgrade on mirror farm")

# --- JiraIntegration ---

CREATE_ISSUE = Endpoint("POST", "/jira/latest/comments/{commentId}/issues", "Create Jira Issue")
GET_COMMITS_BY_ISSUE_KEY = Endpoint("GET", "/jira/latest/issues/{issueKey}/commits", "Get changesets for issue key")
GET_ENHANCED_ENTITY_LINK_FOR_PROJECT = Endpoint(
    "GET", "/jira/latest/projects/{projectKey}/primary-enhanced-entitylink", ""
)
GET_ISSUE_KEYS_FOR_PULL_REQUEST = Endpoint(
    "GET", "/jira/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/issues", ""
)

# --- Markup ---

PREVIEW = Endpoint("POST", "/api/latest/markup/preview", "Preview markdown render")
