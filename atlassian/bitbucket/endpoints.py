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
GET_PROJECT_AVATAR = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/avatar.png",
    "Get avatar for project",
)
UPLOAD_AVATAR = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/avatar.png",
    "Update project avatar",
)
GET_CONFIGURATIONS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/hook-scripts",
    "Get configured hook scripts",
)
REMOVE_CONFIGURATION = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/hook-scripts/{scriptId}",
    "Remove a hook script",
)
SET_CONFIGURATION = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/hook-scripts/{scriptId}",
    "Create/update a hook script",
)
REVOKE_PERMISSIONS = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/permissions",
    "Revoke project permissions",
)
REVOKE_PERMISSIONS_FOR_GROUP_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/permissions/groups",
    "Revoke group project permission",
)
GET_GROUPS_WITH_ANY_PERMISSION_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/groups",
    "Get groups with permission to project",
)
SET_PERMISSION_FOR_GROUPS_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/permissions/groups",
    "Update group project permission",
)
GET_GROUPS_WITHOUT_ANY_PERMISSION_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/groups/none",
    "Get groups without project permission",
)
SEARCH_PERMISSIONS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/search",
    "Search project permissions",
)
REVOKE_PERMISSIONS_FOR_USER_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/permissions/users",
    "Revoke user project permission",
)
GET_USERS_WITH_ANY_PERMISSION_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/users",
    "Get users with permission to project",
)
SET_PERMISSION_FOR_USERS_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/permissions/users",
    "Update user project permission",
)
GET_USERS_WITHOUT_PERMISSION = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/users/none",
    "Get users without project permission",
)
HAS_ALL_USER_PERMISSION = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/permissions/{permission}/all",
    "Check default project permission",
)
MODIFY_ALL_USER_PERMISSION = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/permissions/{permission}/all",
    "Grant project permission",
)
GET_REPOSITORIES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos",
    "Get repositories for project",
)
CREATE_REPOSITORY = Endpoint("POST", "/api/latest/projects/{projectKey}/repos", "Create repository")
DELETE_REPOSITORY = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Delete repository",
)
GET_REPOSITORY = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Get repository",
)
FORK_REPOSITORY = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Fork repository",
)
UPDATE_REPOSITORY = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Update repository",
)
STREAM_CONTRIBUTING = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/contributing",
    "Get repository contributing guidelines",
)
GET_DEFAULT_BRANCH_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch",
    "Get repository default branch",
)
SET_DEFAULT_BRANCH_2 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch",
    "Update default branch for repository",
)
GET_FORKED_REPOSITORIES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/forks",
    "Get repository forks",
)
STREAM_LICENSE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/license",
    "Get repository license",
)
STREAM_README = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/readme",
    "Get repository readme",
)
RETRY_CREATE_REPOSITORY = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/recreate",
    "Retry repository creation",
)
GET_RELATED_REPOSITORIES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/related",
    "Get related repository",
)
DELETE_9 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/settings-restriction",
    "Stop enforcing project restriction",
)
GET_7 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings-restriction",
    "Get enforcing project setting",
)
CREATE_3 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/settings-restriction",
    "Enforce project restriction",
)
GET_ALL = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings-restriction/all",
    "Get all enforcing project settings",
)
DELETE_AUTO_DECLINE_SETTINGS = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/settings/auto-decline",
    "Delete auto decline settings",
)
GET_AUTO_DECLINE_SETTINGS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/auto-decline",
    "Get auto decline settings",
)
SET_AUTO_DECLINE_SETTINGS = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/settings/auto-decline",
    "Create/Update auto decline settings",
)
DELETE_4 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/settings/auto-merge",
    "Delete pull request auto-merge settings",
)
GET_4 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/auto-merge",
    "Get pull request auto-merge settings",
)
SET = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/settings/auto-merge",
    "Create or update the pull request auto-merge settings",
)
GET_REPOSITORY_HOOKS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/hooks",
    "Get repository hooks",
)
GET_REPOSITORY_HOOK = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}",
    "Get a repository hook",
)
DISABLE_HOOK = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/enabled",
    "Disable repository hook",
)
ENABLE_HOOK = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/enabled",
    "Enable repository hook",
)
GET_SETTINGS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/settings",
    "Get repository hook settings",
)
SET_SETTINGS = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/settings/hooks/{hookKey}/settings",
    "Update repository hook settings",
)
GET_PULL_REQUEST_SETTINGS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/pull-requests/{scmId}",
    "Get merge strategy",
)
UPDATE_PULL_REQUEST_SETTINGS = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/settings/pull-requests/{scmId}",
    "Update merge strategy",
)
FIND_WEBHOOKS = Endpoint("GET", "/api/latest/projects/{projectKey}/webhooks", "Find webhooks")
CREATE_WEBHOOK = Endpoint("POST", "/api/latest/projects/{projectKey}/webhooks", "Create webhook")
TEST_WEBHOOK = Endpoint("POST", "/api/latest/projects/{projectKey}/webhooks/test", "Test webhook")
DELETE_WEBHOOK = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}",
    "Delete webhook",
)
GET_WEBHOOK = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}",
    "Get webhook",
)
UPDATE_WEBHOOK = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}",
    "Update webhook",
)
GET_LATEST_INVOCATION = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}/latest",
    "Get last webhook invocation details",
)
GET_STATISTICS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}/statistics",
    "Get webhook statistics",
)
GET_STATISTICS_SUMMARY = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/webhooks/{webhookId}/statistics/summary",
    "Get webhook statistics summary",
)
GET_RESTRICTIONS = Endpoint(
    "GET",
    "/branch-permissions/latest/projects/{projectKey}/restrictions",
    "Search for ref restrictions",
)
CREATE_RESTRICTIONS = Endpoint(
    "POST",
    "/branch-permissions/latest/projects/{projectKey}/restrictions",
    "Create multiple ref restrictions",
)
DELETE_RESTRICTION = Endpoint(
    "DELETE",
    "/branch-permissions/latest/projects/{projectKey}/restrictions/{id}",
    "Delete a ref restriction",
)
GET_RESTRICTION = Endpoint(
    "GET",
    "/branch-permissions/latest/projects/{projectKey}/restrictions/{id}",
    "Get a ref restriction",
)
DELETE_ALL_DEFAULT_TASKS = Endpoint(
    "DELETE",
    "/default-tasks/latest/projects/{projectKey}/tasks",
    "Deletes all default tasks for the project",
)
GET_DEFAULT_TASKS = Endpoint(
    "GET",
    "/default-tasks/latest/projects/{projectKey}/tasks",
    "Get a page of default tasks",
)
ADD_DEFAULT_TASK = Endpoint(
    "POST",
    "/default-tasks/latest/projects/{projectKey}/tasks",
    "Add a default task",
)
DELETE_DEFAULT_TASK = Endpoint(
    "DELETE",
    "/default-tasks/latest/projects/{projectKey}/tasks/{taskId}",
    "Delete a specific default task",
)
UPDATE_DEFAULT_TASK = Endpoint(
    "PUT",
    "/default-tasks/latest/projects/{projectKey}/tasks/{taskId}",
    "Update a default task",
)

# --- Repositories ---

GET_REPOSITORIES_RECENTLY_ACCESSED = Endpoint(
    "GET",
    "/api/latest/profile/recent/repos",
    "Get recently accessed repositories",
)
GET_ARCHIVE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/archive",
    "Stream archive of repository",
)
DELETE_ATTACHMENT = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}",
    "Delete an attachment",
)
GET_ATTACHMENT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}",
    "Get an attachment",
)
DELETE_ATTACHMENT_METADATA = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata",
    "Delete attachment metadata",
)
GET_ATTACHMENT_METADATA = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata",
    "Get attachment metadata",
)
SAVE_ATTACHMENT_METADATA = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/attachments/{attachmentId}/metadata",
    "Save attachment metadata",
)
GET_BRANCHES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches",
    "Find branches",
)
CREATE_BRANCH_FOR_REPOSITORY = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches",
    "Create branch",
)
GET_DEFAULT_BRANCH_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches/default",
    "Get default branch",
)
SET_DEFAULT_BRANCH_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches/default",
    "Update default branch",
)
GET_CONTENT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse",
    "Get file content at revision",
)
GET_CONTENT_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse/{path}",
    "Get file content",
)
EDIT_FILE = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/browse/{path}",
    "Edit file",
)
GET_CHANGES_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/changes",
    "Get changes made in commit",
)
GET_COMMITS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits",
    "Get commits",
)
GET_COMMIT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}",
    "Get commit by ID",
)
GET_CHANGES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/changes",
    "Get changes in commit",
)
GET_COMMENTS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments",
    "Search for commit comments",
)
CREATE_COMMENT = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments",
    "Add a new commit comment",
)
DELETE_COMMENT = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}",
    "Delete a commit comment",
)
GET_COMMENT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}",
    "Get a commit comment",
)
UPDATE_COMMENT = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}",
    "Update a commit comment",
)
GET_DIFF_STATS_SUMMARY = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/diff-stats-summary/{path}",
    "Get diff stats summary between revisions",
)
STREAM_DIFF = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/diff/{path}",
    "Get diff between revisions",
)
GET_MERGE_BASE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/merge-base",
    "Get the common ancestor between two commits",
)
UNWATCH = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/watch",
    "Stop watching commit",
)
WATCH = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/watch",
    "Watch commit",
)
STREAM_CHANGES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/changes",
    "Compare commits",
)
STREAM_COMMITS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/commits",
    "Get accessible commits",
)
GET_DIFF_STATS_SUMMARY_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/diff-stats-summary{path}",
    "Retrieve the diff stats summary between commits",
)
STREAM_DIFF_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/compare/diff{path}",
    "Get diff between commits",
)
STREAM_RAW_DIFF = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/diff",
    "Get raw diff for path",
)
STREAM_RAW_DIFF_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/diff/{path}",
    "Get raw diff for path",
)
STREAM_FILES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/files",
    "Get files in directory",
)
STREAM_FILES_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/files/{path}",
    "Get files in directory",
)
GET_CONFIGURATIONS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts",
    "Get hook scripts",
)
REMOVE_CONFIGURATION_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts/{scriptId}",
    "Remove a hook script",
)
SET_CONFIGURATION_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/hook-scripts/{scriptId}",
    "Create/update a hook script",
)
GET_ALL_LABELS_FOR_REPOSITORY = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels",
    "Get repository labels",
)
ADD_LABEL = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels",
    "Add repository label",
)
REMOVE_LABEL = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/labels/{labelName}",
    "Remove repository label",
)
STREAM = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/last-modified",
    "Stream files",
)
STREAM_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/last-modified/{path}",
    "Stream files with last modified commit in path",
)
STREAM_PATCH = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/patch",
    "Get patch content at revision",
)
STREAM_RAW = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/raw/{path}",
    "Get raw content of a file at revision",
)
GET_REF_CHANGE_ACTIVITY = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/ref-change-activities",
    "Get ref change activity",
)
FIND_BRANCHES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/ref-change-activities/branches",
    "Get branches with ref change activities for repository",
)
DELETE_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline",
    "Delete auto decline settings",
)
GET_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline",
    "Get auto decline settings",
)
SET_AUTO_DECLINE_SETTINGS_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-decline",
    "Create auto decline settings",
)
DELETE_5 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge",
    "Delete pull request auto-merge settings",
)
GET_5 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge",
    "Get pull request auto-merge settings",
)
SET_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/auto-merge",
    "Create or update the pull request auto-merge settings",
)
GET_REPOSITORY_HOOKS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks",
    "Get repository hooks",
)
DELETE_REPOSITORY_HOOK = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}",
    "Delete repository hook",
)
GET_REPOSITORY_HOOK_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}",
    "Get repository hook",
)
DISABLE_HOOK_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/enabled",
    "Disable repository hook",
)
ENABLE_HOOK_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/enabled",
    "Enable repository hook",
)
GET_SETTINGS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/settings",
    "Get repository hook settings",
)
SET_SETTINGS_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/hooks/{hookKey}/settings",
    "Update repository hook settings",
)
GET_PULL_REQUEST_SETTINGS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/pull-requests",
    "Get pull request settings",
)
UPDATE_PULL_REQUEST_SETTINGS_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/pull-requests",
    "Update pull request settings",
)
GET_TAGS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags",
    "Find tag",
)
CREATE_TAG_FOR_REPOSITORY = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags",
    "Create tag",
)
GET_TAG = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/tags/{name}",
    "Get tag",
)
UNWATCH_2 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/watch",
    "Stop watching repository",
)
WATCH_2 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/watch",
    "Watch repository",
)
FIND_WEBHOOKS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks",
    "Find webhooks",
)
CREATE_WEBHOOK_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks",
    "Create webhook",
)
SEARCH_WEBHOOKS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/search",
    "Search webhooks",
)
TEST_WEBHOOK_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/test",
    "Test webhook",
)
DELETE_WEBHOOK_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}",
    "Delete webhook",
)
GET_WEBHOOK_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}",
    "Get webhook",
)
UPDATE_WEBHOOK_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}",
    "Update webhook",
)
GET_LATEST_INVOCATION_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/latest",
    "Get last webhook invocation details",
)
GET_STATISTICS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/statistics",
    "Get webhook statistics",
)
GET_STATISTICS_SUMMARY_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/webhooks/{webhookId}/statistics/summary",
    "Get webhook statistics summary",
)
GET_REPOSITORIES_1 = Endpoint("GET", "/api/latest/repos", "Search for repositories")
GET_RESTRICTIONS_1 = Endpoint(
    "GET",
    "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions",
    "Search for ref restrictions",
)
CREATE_RESTRICTIONS_1 = Endpoint(
    "POST",
    "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions",
    "Create multiple ref restrictions",
)
DELETE_RESTRICTION_1 = Endpoint(
    "DELETE",
    "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions/{id}",
    "Delete a ref restriction",
)
GET_RESTRICTION_1 = Endpoint(
    "GET",
    "/branch-permissions/latest/projects/{projectKey}/repos/{repositorySlug}/restrictions/{id}",
    "Get a ref restriction",
)
DELETE_BRANCH = Endpoint(
    "DELETE",
    "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches",
    "Delete branch",
)
CREATE_BRANCH = Endpoint(
    "POST",
    "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches",
    "Create branch",
)
FIND_BY_COMMIT = Endpoint(
    "GET",
    "/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches/info/{commitId}",
    "Get branch",
)
UN_REACT = Endpoint(
    "DELETE",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}/reactions/{emoticon}",
    "Remove a reaction from comment",
)
REACT = Endpoint(
    "PUT",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/comments/{commentId}/reactions/{emoticon}",
    "React to a comment",
)
DELETE_ALL_DEFAULT_TASKS_1 = Endpoint(
    "DELETE",
    "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks",
    "Deletes all default tasks for the repository",
)
GET_DEFAULT_TASKS_1 = Endpoint(
    "GET",
    "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks",
    "Get a page of default tasks",
)
ADD_DEFAULT_TASK_1 = Endpoint(
    "POST",
    "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks",
    "Add a default task",
)
DELETE_DEFAULT_TASK_1 = Endpoint(
    "DELETE",
    "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks/{taskId}",
    "Delete a specific default task",
)
UPDATE_DEFAULT_TASK_1 = Endpoint(
    "PUT",
    "/default-tasks/latest/projects/{projectKey}/repos/{repositorySlug}/tasks/{taskId}",
    "Update a default task",
)
CREATE_TAG = Endpoint(
    "POST",
    "/git/latest/projects/{projectKey}/repos/{repositorySlug}/tags",
    "Create tag",
)
DELETE_TAG = Endpoint(
    "DELETE",
    "/git/latest/projects/{projectKey}/repos/{repositorySlug}/tags/{name}",
    "Delete tag",
)
GET_STATUS_PROJECTS_REPOS = Endpoint(
    "GET",
    "/sync/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Get synchronization status",
)
SET_ENABLED = Endpoint(
    "POST",
    "/sync/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Disable synchronization",
)
SYNCHRONIZE = Endpoint(
    "POST",
    "/sync/latest/projects/{projectKey}/repos/{repositorySlug}/synchronize",
    "Manual synchronization",
)

# --- PullRequests ---

GET_MERGE_CONFIG = Endpoint(
    "GET",
    "/api/latest/admin/pull-requests/{scmId}",
    "Get merge strategies",
)
SET_MERGE_CONFIG = Endpoint(
    "POST",
    "/api/latest/admin/pull-requests/{scmId}",
    "Update merge strategies",
)
GET_PULL_REQUESTS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/pull-requests",
    "Get repository pull requests containing commit",
)
SEARCH = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/participants",
    "Search pull request participants",
)
GET_PAGE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests",
    "Get pull requests for repository",
)
CREATE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests",
    "Create pull request",
)
DELETE_3 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}",
    "Delete pull request",
)
GET_3 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}",
    "Get pull request",
)
UPDATE = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}",
    "Update pull request metadata",
)
STREAM_RAW_DIFF_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}.diff",
    "Stream raw pull request diff",
)
STREAM_PATCH_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}.patch",
    "Stream pull request as patch",
)
GET_ACTIVITIES = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/activities",
    "Get pull request activity",
)
WITHDRAW_APPROVAL = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve",
    "Unapprove pull request",
)
APPROVE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve",
    "Approve pull request",
)
CANCEL_AUTO_MERGE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge",
    "Cancel auto-merge for pull request",
)
GET_AUTO_MERGE_REQUEST = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge",
    "Get auto-merge request for pull request",
)
TRY_AUTO_MERGE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/auto-merge",
    "Auto-merge pull request",
)
GET_COMMENTS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments",
    "Search pull request comments",
)
CREATE_COMMENT_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments",
    "Add new blocker comment",
)
DELETE_COMMENT_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "Delete pull request comment",
)
GET_COMMENT_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "Get pull request comment",
)
UPDATE_COMMENT_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/blocker-comments/{commentId}",
    "Update pull request comment",
)
STREAM_CHANGES_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/changes",
    "Gets pull request changes",
)
GET_COMMENTS_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments",
    "Get pull request comments for path",
)
CREATE_COMMENT_2 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments",
    "Add pull request comment",
)
DELETE_COMMENT_2 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "Delete a pull request comment",
)
GET_COMMENT_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "Get a pull request comment",
)
UPDATE_COMMENT_2 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}",
    "Update pull request comment",
)
APPLY_SUGGESTION = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/apply-suggestion",
    "Apply pull request suggestion",
)
GET_COMMIT_MESSAGE_SUGGESTION = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/commit-message-suggestion",
    "Get commit message suggestion",
)
GET_COMMITS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/commits",
    "Get pull request commits",
)
DECLINE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/decline",
    "Decline pull request",
)
GET_DIFF_STATS_SUMMARY_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/diff-stats-summary/{path}",
    "Get diff stats summary for pull request",
)
STREAM_DIFF_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/diff/{path}",
    "Stream a diff within a pull request",
)
CAN_MERGE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge",
    "Test if pull request can be merged",
)
MERGE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge",
    "Merge pull request",
)
GET_MERGE_BASE_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge-base",
    "Get the common ancestor between the latest commits of the source and target branches of t...",
)
UNASSIGN_PARTICIPANT_ROLE_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants",
    "Unassign pull request participant",
)
LIST_PARTICIPANTS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants",
    "Get pull request participants",
)
ASSIGN_PARTICIPANT_ROLE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants",
    "Assign pull request participant role",
)
UNASSIGN_PARTICIPANT_ROLE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants/{userSlug}",
    "Unassign pull request participant",
)
UPDATE_STATUS = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/participants/{userSlug}",
    "Change pull request status",
)
REOPEN = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/reopen",
    "Re-open pull request",
)
DISCARD_REVIEW = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review",
    "Discard pull request review",
)
GET_REVIEW = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review",
    "Get pull request comment thread",
)
FINISH_REVIEW = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/review",
    "Complete pull request review",
)
UNWATCH_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/watch",
    "Stop watching pull request",
)
WATCH_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/watch",
    "Watch pull request",
)
GET_REVIEWER_GROUPS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups",
    "Get all reviewer groups",
)
CREATE_2 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups",
    "Create reviewer group",
)
DELETE_7 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}",
    "Delete reviewer group",
)
GET_REVIEWER_GROUP_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}",
    "Get reviewer group",
)
UPDATE_2 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}",
    "Update reviewer group attributes",
)
GET_USERS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/settings/reviewer-groups/{id}/users",
    "Get reviewer group users",
)
GET_REVIEWER_GROUPS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/reviewer-groups",
    "Get all reviewer groups",
)
CREATE_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/settings/reviewer-groups",
    "Create reviewer group",
)
DELETE_6 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}",
    "Delete reviewer group",
)
GET_REVIEWER_GROUP = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}",
    "Get reviewer group",
)
UPDATE_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/settings/reviewer-groups/{id}",
    "Update reviewer group attributes",
)
UN_REACT_1 = Endpoint(
    "DELETE",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/reactions/{emoticon}",
    "Remove a reaction from a PR comment",
)
REACT_1 = Endpoint(
    "PUT",
    "/comment-likes/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/comments/{commentId}/reactions/{emoticon}",
    "React to a PR comment",
)
CREATE_PULL_REQUEST_CONDITION = Endpoint(
    "POST",
    "/default-reviewers/latest/projects/{projectKey}/condition",
    "Create default reviewer",
)
DELETE_PULL_REQUEST_CONDITION = Endpoint(
    "DELETE",
    "/default-reviewers/latest/projects/{projectKey}/condition/{id}",
    "Remove default reviewer",
)
UPDATE_PULL_REQUEST_CONDITION = Endpoint(
    "PUT",
    "/default-reviewers/latest/projects/{projectKey}/condition/{id}",
    "Update the default reviewer",
)
GET_PULL_REQUEST_CONDITIONS = Endpoint(
    "GET",
    "/default-reviewers/latest/projects/{projectKey}/conditions",
    "Get default reviewers",
)
CREATE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "POST",
    "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition",
    "Create default reviewers condition",
)
DELETE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "DELETE",
    "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}",
    "Delete a default reviewer condition",
)
UPDATE_PULL_REQUEST_CONDITION_1 = Endpoint(
    "PUT",
    "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}",
    "Update a default reviewer condition",
)
GET_PULL_REQUEST_CONDITIONS_1 = Endpoint(
    "GET",
    "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/conditions",
    "Get configured default reviewers",
)
GET_REVIEWERS = Endpoint(
    "GET",
    "/default-reviewers/latest/projects/{projectKey}/repos/{repositorySlug}/reviewers",
    "Get required reviewers for PR creation",
)
CAN_REBASE = Endpoint(
    "GET",
    "/git/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/rebase",
    "Check PR rebase precondition",
)
REBASE = Endpoint(
    "POST",
    "/git/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/rebase",
    "Rebase pull request",
)

# --- Authentication ---

GET_ALL_ACCESS_TOKENS = Endpoint(
    "GET",
    "/access-tokens/latest/projects/{projectKey}",
    "Get project HTTP tokens",
)
CREATE_ACCESS_TOKEN = Endpoint(
    "PUT",
    "/access-tokens/latest/projects/{projectKey}",
    "Create project HTTP token",
)
GET_ALL_ACCESS_TOKENS_1 = Endpoint(
    "GET",
    "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Get repository HTTP tokens",
)
CREATE_ACCESS_TOKEN_1 = Endpoint(
    "PUT",
    "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}",
    "Create repository HTTP token",
)
DELETE_BY_ID_1 = Endpoint(
    "DELETE",
    "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}",
    "Delete a HTTP token",
)
GET_BY_ID_1 = Endpoint(
    "GET",
    "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}",
    "Get HTTP token by ID",
)
UPDATE_ACCESS_TOKEN_1 = Endpoint(
    "POST",
    "/access-tokens/latest/projects/{projectKey}/repos/{repositorySlug}/{tokenId}",
    "Update HTTP token",
)
DELETE_BY_ID = Endpoint(
    "DELETE",
    "/access-tokens/latest/projects/{projectKey}/{tokenId}",
    "Delete a HTTP token",
)
GET_BY_ID = Endpoint(
    "GET",
    "/access-tokens/latest/projects/{projectKey}/{tokenId}",
    "Get HTTP token by ID",
)
UPDATE_ACCESS_TOKEN = Endpoint(
    "POST",
    "/access-tokens/latest/projects/{projectKey}/{tokenId}",
    "Update HTTP token",
)
GET_ALL_ACCESS_TOKENS_2 = Endpoint(
    "GET",
    "/access-tokens/latest/users/{userSlug}",
    "Get personal HTTP tokens",
)
CREATE_ACCESS_TOKEN_2 = Endpoint(
    "PUT",
    "/access-tokens/latest/users/{userSlug}",
    "Create personal HTTP token",
)
DELETE_BY_ID_2 = Endpoint(
    "DELETE",
    "/access-tokens/latest/users/{userSlug}/{tokenId}",
    "Delete a HTTP token",
)
GET_BY_ID_2 = Endpoint(
    "GET",
    "/access-tokens/latest/users/{userSlug}/{tokenId}",
    "Get HTTP token by ID",
)
UPDATE_ACCESS_TOKEN_2 = Endpoint(
    "POST",
    "/access-tokens/latest/users/{userSlug}/{tokenId}",
    "Update HTTP token",
)
GET_IDPS = Endpoint("GET", "/authconfig/latest/idps", "Get all configured IdPs")
ADD_IDP = Endpoint("POST", "/authconfig/latest/idps", "Create IdP configuration")
REMOVE_IDP = Endpoint("DELETE", "/authconfig/latest/idps/{id}", "Delete IdP configuration")
GET_IDP = Endpoint("GET", "/authconfig/latest/idps/{id}", "Get IdP configuration")
UPDATE_IDP = Endpoint("PATCH", "/authconfig/latest/idps/{id}", "Update IdP configuration")
GET_JIT_PROVISIONED_USERS = Endpoint(
    "GET",
    "/authconfig/latest/jit-users",
    "Get all JIT provisioned users",
)
GET_LOGIN_OPTIONS = Endpoint(
    "GET",
    "/authconfig/latest/login-options",
    "Get available login options",
)
GET_CONFIG = Endpoint("GET", "/authconfig/latest/sso", "Get SSO configuration")
UPDATE_CONFIG = Endpoint("PATCH", "/authconfig/latest/sso", "Update SSO configuration")
GET = Endpoint("GET", "/basicauth/latest/config", "Get basic auth configuration")
PUT = Endpoint("PUT", "/basicauth/latest/config", "Update basic auth configuration")
GET_FOR_REPOSITORY_1 = Endpoint(
    "GET",
    "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh",
    "Get repository SSH keys",
)
ADD_FOR_REPOSITORY = Endpoint(
    "POST",
    "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh",
    "Add repository SSH key",
)
REVOKE_FOR_REPOSITORY = Endpoint(
    "DELETE",
    "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}",
    "Revoke repository SSH key",
)
GET_FOR_REPOSITORY = Endpoint(
    "GET",
    "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}",
    "Get repository SSH key",
)
UPDATE_PERMISSION_1 = Endpoint(
    "PUT",
    "/keys/latest/projects/{projectKey}/repos/{repositorySlug}/ssh/{keyId}/permission/{permission}",
    "Update repository SSH key permission",
)
GET_SSH_KEYS_FOR_PROJECT = Endpoint("GET", "/keys/latest/projects/{projectKey}/ssh", "Get SSH key")
ADD_FOR_PROJECT = Endpoint("POST", "/keys/latest/projects/{projectKey}/ssh", "Add project SSH key")
REVOKE_FOR_PROJECT = Endpoint(
    "DELETE",
    "/keys/latest/projects/{projectKey}/ssh/{keyId}",
    "Revoke project SSH key",
)
GET_FOR_PROJECT = Endpoint(
    "GET",
    "/keys/latest/projects/{projectKey}/ssh/{keyId}",
    "Get project SSH key",
)
UPDATE_PERMISSION = Endpoint(
    "PUT",
    "/keys/latest/projects/{projectKey}/ssh/{keyId}/permission/{permission}",
    "Update project SSH key permission",
)
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
AUTHENTICATE_WITH_RECOVERY_CODE = Endpoint(
    "POST",
    "/tsv/latest/authenticate/recovery-code",
    "Authenticate using recovery code",
)
VERIFY_CODE = Endpoint("POST", "/tsv/latest/authenticate/totp-code", "Authenticate using TOTP code")
GET_ELEVATED_PERMISSION_STATUS = Endpoint(
    "GET",
    "/tsv/latest/elevate-permissions",
    "Get elevated session status",
)
ELEVATE_PERMISSIONS_WITH_PASSWORD = Endpoint(
    "POST",
    "/tsv/latest/elevate-permissions/password",
    "Create elevated session with password",
)
ELEVATE_PERMISSIONS_WITH_RECOVERY_CODE = Endpoint(
    "POST",
    "/tsv/latest/elevate-permissions/recovery-code",
    "Create elevated session with recovery code",
)
ELEVATE_PERMISSIONS_WITH_TOTP = Endpoint(
    "POST",
    "/tsv/latest/elevate-permissions/totp",
    "Create elevated session with TOTP",
)
GET_SSO_MANAGEMENT_STATUS = Endpoint(
    "GET",
    "/tsv/latest/sso-management-status",
    "Get SSO management status",
)
GET_STATUS = Endpoint("GET", "/tsv/latest/status", "Get two-step verification status")
COMPLETE_ENFORCED_ENROLLMENT = Endpoint(
    "POST",
    "/tsv/latest/totp/complete-enforced-enrollment",
    "Complete enforced enrollment in 2SV",
)
COMPLETE_AUTHENTICATION_CHANGE = Endpoint(
    "POST",
    "/tsv/latest/totp/complete-enrollment-update",
    "Complete authentication app update for 2SV",
)
COMPLETE_VOLUNTARY_ENROLLMENT = Endpoint(
    "POST",
    "/tsv/latest/totp/complete-voluntary-enrollment",
    "Complete voluntary enrollment in 2SV",
)
ROTATE_RECOVER_CODE = Endpoint(
    "POST",
    "/tsv/latest/totp/recovery-code/rotate",
    "Rotate recovery code",
)
START_ENFORCED_ENROLLMENT = Endpoint(
    "POST",
    "/tsv/latest/totp/start-enforced-enrollment",
    "Start enforced enrollment in 2SV",
)
START_ENROLLMENT_UPDATE = Endpoint(
    "POST",
    "/tsv/latest/totp/start-enrollment-update",
    "Start authentication app update for 2SV",
)
START_VOLUNTARY_ENROLLMENT = Endpoint(
    "POST",
    "/tsv/latest/totp/start-voluntary-enrollment",
    "Start voluntary enrollment in 2SV",
)
UNENROLL = Endpoint(
    "DELETE",
    "/tsv/latest/totp/unenroll",
    "Uneroll current user from two-step verification",
)
UNENROLL_USER = Endpoint(
    "DELETE",
    "/tsv/latest/totp/unenroll/user/{userName}",
    "Unenroll specific user from two-step verification",
)

# --- Builds ---

GET_CAPABILITIES = Endpoint("GET", "/api/latest/build/capabilities", "Get build capabilities")
GET_CAPABILITIES_1 = Endpoint(
    "GET",
    "/api/latest/deployment/capabilities",
    "Get deployment capabilities",
)
DELETE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds",
    "Delete a specific build status",
)
GET_COMMITS_BUILDS = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds",
    "Get a specific build status",
)
ADD = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds",
    "Store a build status",
)
DELETE_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments",
    "Delete a deployment",
)
GET_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments",
    "Get a deployment",
)
CREATE_OR_UPDATE_DEPLOYMENT = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/deployments",
    "Create or update a deployment",
)
GET_MULTIPLE_BUILD_STATUS_STATS = Endpoint(
    "POST",
    "/build-status/latest/commits/stats",
    "Get build status statistics for multiple commits",
)
GET_BUILD_STATUS_STATS = Endpoint(
    "GET",
    "/build-status/latest/commits/stats/{commitId}",
    "Get build status statistics for commit",
)
GET_BUILD_STATUS = Endpoint(
    "GET",
    "/build-status/latest/commits/{commitId}",
    "Get build statuses for commit",
)
ADD_BUILD_STATUS = Endpoint(
    "POST",
    "/build-status/latest/commits/{commitId}",
    "Create build status for commit",
)
GET_ANNOTATIONS_1 = Endpoint(
    "GET",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/annotations",
    "Get Code Insights annotations for a commit",
)
GET_REPORTS = Endpoint(
    "GET",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports",
    "Get all Code Insights reports for a commit",
)
DELETE_A_CODE_INSIGHTS_REPORT = Endpoint(
    "DELETE",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}",
    "Delete a Code Insights report",
)
GET_A_CODE_INSIGHTS_REPORT = Endpoint(
    "GET",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}",
    "Get a Code Insights report",
)
SET_A_CODE_INSIGHTS_REPORT = Endpoint(
    "PUT",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}",
    "Create a Code Insights report",
)
DELETE_ANNOTATIONS = Endpoint(
    "DELETE",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "Delete Code Insights annotations",
)
GET_ANNOTATIONS = Endpoint(
    "GET",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "Get Code Insights annotations for a report",
)
ADD_ANNOTATIONS = Endpoint(
    "POST",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations",
    "Add Code Insights annotations",
)
SET_ANNOTATION = Endpoint(
    "PUT",
    "/insights/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/reports/{key}/annotations/{externalId}",
    "Create or replace a Code Insights annotation",
)
CREATE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "POST",
    "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition",
    "Create a required builds merge check",
)
DELETE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "DELETE",
    "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}",
    "Delete a required builds merge check",
)
UPDATE_REQUIRED_BUILDS_MERGE_CHECK = Endpoint(
    "PUT",
    "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}",
    "Update a required builds merge check",
)
GET_PAGE_OF_REQUIRED_BUILDS_MERGE_CHECKS = Endpoint(
    "GET",
    "/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/conditions",
    "Get required builds merge checks",
)

# --- Permissions ---

DELETE_GROUP = Endpoint("DELETE", "/api/latest/admin/groups", "Remove group")
GET_GROUPS_1 = Endpoint("GET", "/api/latest/admin/groups", "Get groups")
CREATE_GROUP = Endpoint("POST", "/api/latest/admin/groups", "Create group")
ADD_USER_TO_GROUP = Endpoint("POST", "/api/latest/admin/groups/add-user", "Add user to group")
ADD_USERS_TO_GROUP = Endpoint(
    "POST",
    "/api/latest/admin/groups/add-users",
    "Add multiple users to group",
)
FIND_USERS_IN_GROUP = Endpoint("GET", "/api/latest/admin/groups/more-members", "Get group members")
FIND_USERS_NOT_IN_GROUP = Endpoint(
    "GET",
    "/api/latest/admin/groups/more-non-members",
    "Get members not in group",
)
REMOVE_USER_FROM_GROUP = Endpoint(
    "POST",
    "/api/latest/admin/groups/remove-user",
    "Remove user from group",
)
REVOKE_PERMISSIONS_FOR_GROUP = Endpoint(
    "DELETE",
    "/api/latest/admin/permissions/groups",
    "Revoke all global permissions for group",
)
GET_GROUPS_WITH_ANY_PERMISSION = Endpoint(
    "GET",
    "/api/latest/admin/permissions/groups",
    "Get groups with a global permission",
)
SET_PERMISSION_FOR_GROUPS = Endpoint(
    "PUT",
    "/api/latest/admin/permissions/groups",
    "Update global permission for group",
)
GET_GROUPS_WITHOUT_ANY_PERMISSION = Endpoint(
    "GET",
    "/api/latest/admin/permissions/groups/none",
    "Get groups with no global permission",
)
REVOKE_PERMISSIONS_FOR_USER = Endpoint(
    "DELETE",
    "/api/latest/admin/permissions/users",
    "Revoke all global permissions for user",
)
GET_USERS_WITH_ANY_PERMISSION = Endpoint(
    "GET",
    "/api/latest/admin/permissions/users",
    "Get users with a global permission",
)
SET_PERMISSION_FOR_USERS = Endpoint(
    "PUT",
    "/api/latest/admin/permissions/users",
    "Update global permission for user",
)
GET_USERS_WITHOUT_ANY_PERMISSION = Endpoint(
    "GET",
    "/api/latest/admin/permissions/users/none",
    "Get users with no global permission",
)
GET_USER_DIRECTORIES = Endpoint("GET", "/api/latest/admin/user-directories", "Get directories")
DELETE_USER = Endpoint("DELETE", "/api/latest/admin/users", "Remove user")
GET_USERS_1 = Endpoint("GET", "/api/latest/admin/users", "Get users")
CREATE_USER = Endpoint("POST", "/api/latest/admin/users", "Create user")
UPDATE_USER_DETAILS = Endpoint("PUT", "/api/latest/admin/users", "Update user details")
ADD_GROUP_TO_USER = Endpoint("POST", "/api/latest/admin/users/add-group", "Add user to group")
ADD_USER_TO_GROUPS = Endpoint("POST", "/api/latest/admin/users/add-groups", "Add user to groups")
CLEAR_USER_CAPTCHA_CHALLENGE = Endpoint(
    "DELETE",
    "/api/latest/admin/users/captcha",
    "Clear CAPTCHA for user",
)
UPDATE_USER_PASSWORD = Endpoint(
    "PUT",
    "/api/latest/admin/users/credentials",
    "Set password for user",
)
VALIDATE_ERASABLE = Endpoint("GET", "/api/latest/admin/users/erasure", "Check user removal")
ERASE_USER = Endpoint("POST", "/api/latest/admin/users/erasure", "Erase user information")
FIND_GROUPS_FOR_USER = Endpoint(
    "GET",
    "/api/latest/admin/users/more-members",
    "Get groups for user",
)
FIND_OTHER_GROUPS_FOR_USER = Endpoint(
    "GET",
    "/api/latest/admin/users/more-non-members",
    "Find other groups for user",
)
REMOVE_GROUP_FROM_USER = Endpoint(
    "POST",
    "/api/latest/admin/users/remove-group",
    "Remove user from group",
)
RENAME_USER = Endpoint("POST", "/api/latest/admin/users/rename", "Rename user")
GET_GROUPS = Endpoint("GET", "/api/latest/groups", "Get group names")
REVOKE_PERMISSIONS_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions",
    "Revoke all repository permissions for users and groups",
)
REVOKE_PERMISSIONS_FOR_GROUP_2 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups",
    "Revoke group repository permission",
)
GET_GROUPS_WITH_ANY_PERMISSION_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups",
    "Get groups with permission to repository",
)
SET_PERMISSION_FOR_GROUP = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups",
    "Update group repository permission",
)
GET_GROUPS_WITHOUT_ANY_PERMISSION_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/groups/none",
    "Get groups without repository permission",
)
SEARCH_PERMISSIONS_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/search",
    "Search repository permissions",
)
REVOKE_PERMISSIONS_FOR_USER_2 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users",
    "Revoke user repository permission",
)
GET_USERS_WITH_ANY_PERMISSION_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users",
    "Get users with permission to repository",
)
SET_PERMISSION_FOR_USER = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users",
    "Update user repository permission",
)
GET_USERS_WITHOUT_PERMISSION_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/permissions/users/none",
    "Get users without repository permission",
)

# --- Security ---

SEARCH_2 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist",
    "Find repository secret scanning allowlist rules",
)
CREATE_ALLOWLIST_RULE_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist",
    "Create repository secret scanning allowlist rule",
)
DELETE_ALLOWLIST_RULE_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}",
    "Delete a repository secret scanning allowlist rule",
)
GET_ALLOWLIST_RULE_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}",
    "Get a repository secret scanning allowlist rule",
)
EDIT_ALLOWLIST_RULE_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/allowlist/{id}",
    "Edit an existing repository secret scanning allowlist rule",
)
DELETE_EXEMPT_REPO = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt",
    "Delete an exempt repository",
)
IS_REPO_EXEMPT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt",
    "Get whether a repository is exempt",
)
ADD_EXEMPT_REPO = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/exempt",
    "Exempt a repo from secret scanning",
)
SEARCH_3 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules",
    "Find repository secret scanning rules",
)
CREATE_RULE_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules",
    "Create repository secret scanning rule",
)
DELETE_RULE_1 = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}",
    "Delete a repository secret scanning rule",
)
GET_RULE_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}",
    "Get a repository secret scanning rule",
)
EDIT_RULE_1 = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/repos/{repositorySlug}/secret-scanning/rules/{id}",
    "Edit an existing repository secret scanning rule",
)
SEARCH_ALLOWLIST_RULE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/secret-scanning/allowlist",
    "Find project secret scanning allowlist rules",
)
CREATE_ALLOWLIST_RULE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/secret-scanning/allowlist",
    "Create project secret scanning allowlist rule",
)
DELETE_ALLOWLIST_RULE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}",
    "Delete a project secret scanning allowlist rule",
)
GET_ALLOWLIST_RULE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}",
    "Get a project secret scanning allowlist rule",
)
EDIT_ALLOWLIST_RULE = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/secret-scanning/allowlist/{id}",
    "Edit an existing project secret scanning allowlist rule",
)
FIND_EXEMPT_REPOS_BY_PROJECT = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/secret-scanning/exempt",
    "Find repos exempt from secret scanning for a project",
)
BULK_ADD_EXEMPT_REPOSITORIES_1 = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/secret-scanning/exempt",
    "Bulk exempt repos from secret scanning",
)
SEARCH_1 = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/secret-scanning/rules",
    "Find project secret scanning rules",
)
CREATE_RULE = Endpoint(
    "POST",
    "/api/latest/projects/{projectKey}/secret-scanning/rules",
    "Create project secret scanning rule",
)
DELETE_RULE = Endpoint(
    "DELETE",
    "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}",
    "Delete a project secret scanning rule",
)
GET_RULE = Endpoint(
    "GET",
    "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}",
    "Get a project secret scanning rule",
)
EDIT_RULE = Endpoint(
    "PUT",
    "/api/latest/projects/{projectKey}/secret-scanning/rules/{id}",
    "Edit an existing project secret scanning rule",
)
FIND_EXEMPT_REPOS_BY_SCOPE = Endpoint(
    "GET",
    "/api/latest/secret-scanning/exempt",
    "Find all repos exempt from secret scan",
)
BULK_ADD_EXEMPT_REPOSITORIES = Endpoint(
    "POST",
    "/api/latest/secret-scanning/exempt",
    "Bulk exempt repos from secret scanning",
)
SEARCH_4 = Endpoint("GET", "/api/latest/secret-scanning/rules", "Find global secret scanning rules")
CREATE_RULE_2 = Endpoint(
    "POST",
    "/api/latest/secret-scanning/rules",
    "Create global secret scanning rule",
)
DELETE_RULE_2 = Endpoint(
    "DELETE",
    "/api/latest/secret-scanning/rules/{id}",
    "Delete a global secret scanning rule",
)
GET_RULE_2 = Endpoint(
    "GET",
    "/api/latest/secret-scanning/rules/{id}",
    "Get a global secret scanning rule",
)
EDIT_RULE_2 = Endpoint(
    "PUT",
    "/api/latest/secret-scanning/rules/{id}",
    "Edit a global secret scanning rule.",
)
GET_ALL_CERTIFICATES = Endpoint(
    "GET",
    "/api/latest/signing/x509-certificates",
    "Get all X.509 certificates",
)
CREATE_CERTIFICATE = Endpoint(
    "POST",
    "/api/latest/signing/x509-certificates",
    "Create an X.509 certificate",
)
UPDATE_CERTIFICATE_REVOCATION_LIST_ENTRIES = Endpoint(
    "PUT",
    "/api/latest/signing/x509-certificates/crl/{id}",
    "Update X.509 CRL entries",
)
DELETE_CERTIFICATE = Endpoint(
    "DELETE",
    "/api/latest/signing/x509-certificates/{id}",
    "Delete an X.509 certificate",
)
GET_SYSTEM_SIGNING_CONFIGURATION = Endpoint(
    "GET",
    "/api/latest/system-signing/configuration",
    "Get system signing configuration",
)
UPDATE_SYSTEM_SIGNING_CONFIGURATION = Endpoint(
    "POST",
    "/api/latest/system-signing/configuration",
    "Update system signing configuration",
)
DELETE_FOR_USER = Endpoint("DELETE", "/gpg/latest/keys", "Delete all GPG keys for user")
GET_KEYS_FOR_USER = Endpoint("GET", "/gpg/latest/keys", "Get all GPG keys")
ADD_KEY = Endpoint("POST", "/gpg/latest/keys", "Create a GPG key")
DELETE_KEY = Endpoint("DELETE", "/gpg/latest/keys/{fingerprintOrId}", "Delete a GPG key")

# --- Admin ---

GET_GLOBAL_SETTINGS = Endpoint("GET", "/admin", "Get global SSH key settings")
UPDATE_GLOBAL_SETTINGS = Endpoint("PUT", "/admin", "Update global SSH key settings")
GET_SUPPORTED_KEY_TYPES = Endpoint(
    "GET",
    "/admin/supported-key-types",
    "Get supported SSH key algorithms and lengths",
)
DELETE_BANNER = Endpoint("DELETE", "/api/latest/admin/banner", "Delete announcement banner")
GET_BANNER = Endpoint("GET", "/api/latest/admin/banner", "Get announcement banner")
SET_BANNER = Endpoint("PUT", "/api/latest/admin/banner", "Update/Set announcement banner")
GET_INFORMATION = Endpoint("GET", "/api/latest/admin/cluster", "Get cluster node information")
CLEAR_DEFAULT_BRANCH = Endpoint(
    "DELETE",
    "/api/latest/admin/default-branch",
    "Clear default branch",
)
GET_DEFAULT_BRANCH = Endpoint("GET", "/api/latest/admin/default-branch", "Get the default branch")
SET_DEFAULT_BRANCH = Endpoint(
    "PUT",
    "/api/latest/admin/default-branch",
    "Update/Set default branch",
)
GET_CONTROL_PLANE_PUBLIC_KEY = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/config/control-plane.pem",
    "Get the control plane PEM",
)
CONNECTIVITY = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/diagnostics/connectivity",
    "Generate Mesh connectivity report",
)
GET_ALL_REGISTERED_MESH_NODES = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/nodes",
    "Get all registered Mesh nodes",
)
REGISTER_NEW_MESH_NODE = Endpoint(
    "POST",
    "/api/latest/admin/git/mesh/nodes",
    "Register new Mesh node",
)
DELETE_2 = Endpoint("DELETE", "/api/latest/admin/git/mesh/nodes/{id}", "Delete Mesh node")
GET_REGISTERED_MESH_NODE_BY_ID = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/nodes/{id}",
    "Get Mesh node",
)
UPDATE_MESH_NODE = Endpoint("PUT", "/api/latest/admin/git/mesh/nodes/{id}", "Update Mesh node")
GET_SUPPORT_ZIPS = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/support-zips",
    "Get support zips for all Mesh nodes",
)
GET_SUPPORT_ZIP = Endpoint(
    "GET",
    "/api/latest/admin/git/mesh/support-zips/{id}",
    "Get support zip for node",
)
GET_2 = Endpoint("GET", "/api/latest/admin/license", "Get license details")
UPDATE_LICENSE = Endpoint("POST", "/api/latest/admin/license", "Update license")
DELETE_MAIL_CONFIG = Endpoint(
    "DELETE",
    "/api/latest/admin/mail-server",
    "Delete mail configuration",
)
GET_MAIL_CONFIG = Endpoint("GET", "/api/latest/admin/mail-server", "Get mail configuration")
SET_MAIL_CONFIG = Endpoint("PUT", "/api/latest/admin/mail-server", "Update mail configuration")
CLEAR_SENDER_ADDRESS = Endpoint(
    "DELETE",
    "/api/latest/admin/mail-server/sender-address",
    "Update mail configuration",
)
GET_SENDER_ADDRESS = Endpoint(
    "GET",
    "/api/latest/admin/mail-server/sender-address",
    "Get server mail address",
)
SET_SENDER_ADDRESS = Endpoint(
    "PUT",
    "/api/latest/admin/mail-server/sender-address",
    "Update server mail address",
)
GET_HISTORY = Endpoint("GET", "/api/latest/admin/rate-limit/history", "Get rate limit history")
GET_SETTINGS_2 = Endpoint("GET", "/api/latest/admin/rate-limit/settings", "Get rate limit settings")
SET_SETTINGS_2 = Endpoint("PUT", "/api/latest/admin/rate-limit/settings", "Set rate limit")
GET_ALL_RATE_LIMIT_SETTINGS = Endpoint(
    "GET",
    "/api/latest/admin/rate-limit/settings/users",
    "Get rate limit settings for user",
)
SET_2 = Endpoint(
    "POST",
    "/api/latest/admin/rate-limit/settings/users",
    "Set rate limit settings for users",
)
DELETE_8 = Endpoint(
    "DELETE",
    "/api/latest/admin/rate-limit/settings/users/{userSlug}",
    "Delete user specific rate limit settings",
)
GET_6 = Endpoint(
    "GET",
    "/api/latest/admin/rate-limit/settings/users/{userSlug}",
    "Get user specific rate limit settings",
)
SET_3 = Endpoint(
    "PUT",
    "/api/latest/admin/rate-limit/settings/users/{userSlug}",
    "Set rate limit settings for user",
)
GET_APPLICATION_PROPERTIES = Endpoint(
    "GET",
    "/api/latest/application-properties",
    "Get application properties",
)
CREATE_HOOK_SCRIPT = Endpoint("POST", "/api/latest/hook-scripts", "Create a new hook script")
DELETE_HOOK_SCRIPT = Endpoint(
    "DELETE",
    "/api/latest/hook-scripts/{scriptId}",
    "Delete a hook script.",
)
GET_HOOK_SCRIPT = Endpoint("GET", "/api/latest/hook-scripts/{scriptId}", "Get a hook script")
UPDATE_HOOK_SCRIPT = Endpoint("PUT", "/api/latest/hook-scripts/{scriptId}", "Update a hook script")
READ = Endpoint("GET", "/api/latest/hook-scripts/{scriptId}/content", "Get hook script content")
GET_LABELS = Endpoint("GET", "/api/latest/labels", "Get all labels")
GET_LABEL = Endpoint("GET", "/api/latest/labels/{labelName}", "Get label")
GET_LABELABLES = Endpoint(
    "GET",
    "/api/latest/labels/{labelName}/labeled",
    "Get labelables for label",
)
GET_LEVEL = Endpoint("GET", "/api/latest/logs/logger/{loggerName}", "Get current log level")
SET_LEVEL = Endpoint("PUT", "/api/latest/logs/logger/{loggerName}/{levelName}", "Set log level")
GET_ROOT_LEVEL = Endpoint("GET", "/api/latest/logs/rootLogger", "Get root log level")
SET_ROOT_LEVEL = Endpoint("PUT", "/api/latest/logs/rootLogger/{levelName}", "Set root log level")
START_EXPORT = Endpoint("POST", "/api/latest/migration/exports", "Start export job")
PREVIEW_EXPORT = Endpoint("POST", "/api/latest/migration/exports/preview", "Preview export")
GET_EXPORT_JOB = Endpoint("GET", "/api/latest/migration/exports/{jobId}", "Get export job details")
CANCEL_EXPORT_JOB = Endpoint(
    "POST",
    "/api/latest/migration/exports/{jobId}/cancel",
    "Cancel export job",
)
GET_EXPORT_JOB_MESSAGES = Endpoint(
    "GET",
    "/api/latest/migration/exports/{jobId}/messages",
    "Get job messages",
)
START_IMPORT = Endpoint("POST", "/api/latest/migration/imports", "Start import job")
GET_IMPORT_JOB = Endpoint("GET", "/api/latest/migration/imports/{jobId}", "Get import job status")
CANCEL_IMPORT_JOB = Endpoint(
    "POST",
    "/api/latest/migration/imports/{jobId}/cancel",
    "Cancel import job",
)
GET_IMPORT_JOB_MESSAGES = Endpoint(
    "GET",
    "/api/latest/migration/imports/{jobId}/messages",
    "Get import job messages",
)
START_MESH_MIGRATION = Endpoint("POST", "/api/latest/migration/mesh", "Start Mesh migration job")
PREVIEW_MESH_MIGRATION = Endpoint(
    "POST",
    "/api/latest/migration/mesh/preview",
    "Preview Mesh migration",
)
SEARCH_MESH_MIGRATION_REPOS = Endpoint(
    "GET",
    "/api/latest/migration/mesh/repos",
    "Find repositories by Mesh migration state",
)
GET_ALL_MESH_MIGRATION_SUMMARIES = Endpoint(
    "GET",
    "/api/latest/migration/mesh/summaries",
    "Get all Mesh migration job summaries",
)
GET_ACTIVE_MESH_MIGRATION_SUMMARY = Endpoint(
    "GET",
    "/api/latest/migration/mesh/summary",
    "Get summary for Mesh migration job",
)
GET_MESH_MIGRATION_JOB = Endpoint(
    "GET",
    "/api/latest/migration/mesh/{jobId}",
    "Get Mesh migration job details",
)
CANCEL_MESH_MIGRATION_JOB = Endpoint(
    "POST",
    "/api/latest/migration/mesh/{jobId}/cancel",
    "Cancel Mesh migration job",
)
GET_MESH_MIGRATION_JOB_MESSAGES = Endpoint(
    "GET",
    "/api/latest/migration/mesh/{jobId}/messages",
    "Get Mesh migration job messages",
)
GET_MESH_MIGRATION_JOB_SUMMARY = Endpoint(
    "GET",
    "/api/latest/migration/mesh/{jobId}/summary",
    "Get Mesh migration job summary",
)
GET_USERS_2 = Endpoint("GET", "/api/latest/users", "Get all users")
UPDATE_USER_DETAILS_1 = Endpoint("PUT", "/api/latest/users", "Update user details")
UPDATE_USER_PASSWORD_1 = Endpoint("PUT", "/api/latest/users/credentials", "Set password")
GET_USER = Endpoint("GET", "/api/latest/users/{userSlug}", "Get user")
DELETE_AVATAR = Endpoint("DELETE", "/api/latest/users/{userSlug}/avatar.png", "Delete user avatar")
UPLOAD_AVATAR_1 = Endpoint("POST", "/api/latest/users/{userSlug}/avatar.png", "Update user avatar")
GET_USER_SETTINGS = Endpoint("GET", "/api/latest/users/{userSlug}/settings", "Get user settings")
UPDATE_SETTINGS = Endpoint("POST", "/api/latest/users/{userSlug}/settings", "Update user settings")
DISMISS_RETENTION_CONFIG_REVIEW_NOTIFICATION = Endpoint(
    "DELETE",
    "/audit/latest/notification-settings/retention-config-review",
    "Dismiss retention config notification",
)
GET_REPOSITORY_ARCHIVE_POLICY = Endpoint(
    "GET",
    "/policies/latest/admin/repos/archive",
    "Get repository archive policy",
)
SET_REPOSITORY_ARCHIVE_POLICY = Endpoint(
    "PUT",
    "/policies/latest/admin/repos/archive",
    "Update repository archive policy",
)
GET_REPOSITORY_DELETE_POLICY = Endpoint(
    "GET",
    "/policies/latest/admin/repos/delete",
    "Get repository delete policy",
)
SET_REPOSITORY_DELETE_POLICY = Endpoint(
    "PUT",
    "/policies/latest/admin/repos/delete",
    "Update the repository delete policy",
)

# --- Dashboard ---

GET_PULL_REQUEST_SUGGESTIONS = Endpoint(
    "GET",
    "/api/latest/dashboard/pull-request-suggestions",
    "Get pull request suggestions",
)
GET_PULL_REQUESTS_1 = Endpoint(
    "GET",
    "/api/latest/dashboard/pull-requests",
    "Get pull requests for a user",
)
GET_PULL_REQUESTS_2 = Endpoint(
    "GET",
    "/api/latest/inbox/pull-requests",
    "Get pull requests in inbox",
)
GET_PULL_REQUEST_COUNT = Endpoint(
    "GET",
    "/api/latest/inbox/pull-requests/count",
    "Get total number of pull requests in inbox",
)

# --- Mirroring ---

DELETE_PREFERRED_MIRROR_ID = Endpoint(
    "DELETE",
    "/mirroring/latest/account/settings/preferred-mirror",
    "Remove preferred mirror",
)
GET_PREFERRED_MIRROR_ID = Endpoint(
    "GET",
    "/mirroring/latest/account/settings/preferred-mirror",
    "Get preferred mirror",
)
SET_PREFERRED_MIRROR_ID = Endpoint(
    "POST",
    "/mirroring/latest/account/settings/preferred-mirror",
    "Set preferred mirror",
)
ANALYTICS_SETTINGS = Endpoint(
    "GET",
    "/mirroring/latest/analyticsSettings",
    "Get analytics settings from upstream",
)
AUTHENTICATE_MIRRORING_AUTHENTICATE = Endpoint(
    "POST",
    "/mirroring/latest/authenticate",
    "Authenticate on behalf of a user",
)
GET_FARM_NODES = Endpoint("GET", "/mirroring/latest/farmNodes", "Get farm nodes")
GET_MIRRORED_REPOSITORY = Endpoint(
    "GET",
    "/mirroring/latest/mirrorRepos/{externalRepositoryId}",
    "Get clone URLs",
)
LIST_MIRRORS = Endpoint("GET", "/mirroring/latest/mirrorServers", "Get all mirrors")
REMOVE = Endpoint("DELETE", "/mirroring/latest/mirrorServers/{mirrorId}", "Delete mirror by ID")
GET_MIRROR = Endpoint("GET", "/mirroring/latest/mirrorServers/{mirrorId}", "Get mirror by ID")
UPGRADE = Endpoint("PUT", "/mirroring/latest/mirrorServers/{mirrorId}", "Upgrade mirror server")
PUBLISH_EVENT = Endpoint(
    "POST",
    "/mirroring/latest/mirrorServers/{mirrorId}/events",
    "Publish RepositoryMirrorEvent",
)
GET_SYNCHRONIZATION_PROGRESS = Endpoint(
    "GET",
    "/mirroring/latest/progress",
    "Get synchronization progress state",
)
GET_PROJECT_BY_ID = Endpoint("GET", "/mirroring/latest/projects/{projectId}", "Get project")
GET_ALL_REPOS_FOR_PROJECT = Endpoint(
    "GET",
    "/mirroring/latest/projects/{projectId}/repos",
    "Get hashes for repositories in project",
)
GET_ALL_CONTENT_HASHES = Endpoint(
    "GET",
    "/mirroring/latest/repos",
    "Get content hashes for repositories",
)
GET_CONTENT_HASH_BY_ID = Endpoint(
    "GET",
    "/mirroring/latest/repos/{repoId}",
    "Get content hash for a repository",
)
GET_REPOSITORY_MIRRORS = Endpoint(
    "GET",
    "/mirroring/latest/repos/{repoId}/mirrors",
    "Get mirrors for repository",
)
LIST_REQUESTS = Endpoint("GET", "/mirroring/latest/requests", "Get mirroring requests")
REGISTER = Endpoint("POST", "/mirroring/latest/requests", "Create a mirroring request")
DELETE_MIRRORING_REQUEST = Endpoint(
    "DELETE",
    "/mirroring/latest/requests/{mirroringRequestId}",
    "Delete a mirroring request",
)
GET_MIRRORING_REQUEST = Endpoint(
    "GET",
    "/mirroring/latest/requests/{mirroringRequestId}",
    "Get a mirroring request",
)
ACCEPT = Endpoint(
    "POST",
    "/mirroring/latest/requests/{mirroringRequestId}/accept",
    "Accept a mirroring request",
)
REJECT = Endpoint(
    "POST",
    "/mirroring/latest/requests/{mirroringRequestId}/reject",
    "Reject a mirroring request",
)
GET_OUT_OF_SYNC_REPOSITORIES = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/out-of-sync-repos/content",
    "Get out-of-sync repositories",
)
GET_REPOSITORY_LOCK_OWNER = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/projects/{projectKey}/repos/{repositorySlug}/repo-lock-owner",
    "Get the repository lock owner for the syncing process",
)
GET_REPO_SYNC_STATUS_1 = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/projects/{projectKey}/repos/{repositorySlug}/repoSyncStatus",
    "Gets information about the mirrored repository",
)
GET_REF_CHANGES_QUEUE = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/refChangesQueue",
    "Get items in ref changes queue",
)
GET_REF_CHANGES_QUEUE_COUNT = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/refChangesQueue/count",
    "Get total number of items in ref changes queue",
)
GET_REPOSITORY_LOCK_OWNERS = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/repo-lock-owners",
    "Get all the repository lock owners for the syncing process",
)
GET_REPO_SYNC_STATUS = Endpoint(
    "GET",
    "/mirroring/latest/supportInfo/repoSyncStatus",
    "Get sync status of repositories",
)
GET_MIRROR_SETTINGS = Endpoint("GET", "/mirroring/latest/syncSettings", "Get upstream settings")
SET_MIRROR_SETTINGS = Endpoint("PUT", "/mirroring/latest/syncSettings", "Update upstream settings")
GET_MIRROR_MODE = Endpoint("GET", "/mirroring/latest/syncSettings/mode", "Get mirror mode")
SET_MIRROR_MODE = Endpoint("PUT", "/mirroring/latest/syncSettings/mode", "Update mirror mode")
GET_MIRRORED_PROJECTS = Endpoint(
    "GET",
    "/mirroring/latest/syncSettings/projects",
    "Get mirrored project IDs",
)
START_MIRRORING_PROJECTS = Endpoint(
    "POST",
    "/mirroring/latest/syncSettings/projects",
    "Add multiple projects to be mirrored",
)
STOP_MIRRORING_PROJECT = Endpoint(
    "DELETE",
    "/mirroring/latest/syncSettings/projects/{projectId}",
    "Stop mirroring project",
)
START_MIRRORING_PROJECT = Endpoint(
    "POST",
    "/mirroring/latest/syncSettings/projects/{projectId}",
    "Add project to be mirrored",
)
GET_UPSTREAM_SERVER = Endpoint("GET", "/mirroring/latest/upstreamServer", "Get upstream server")
END_ROLLING_UPGRADE = Endpoint(
    "POST",
    "/mirroring/latest/zdu/end",
    "End ZDU upgrade on mirror farm",
)
START_ROLLING_UPGRADE = Endpoint(
    "POST",
    "/mirroring/latest/zdu/start",
    "Start ZDU upgrade on mirror farm",
)

# --- JiraIntegration ---

CREATE_ISSUE = Endpoint("POST", "/jira/latest/comments/{commentId}/issues", "Create Jira Issue")
GET_COMMITS_BY_ISSUE_KEY = Endpoint(
    "GET",
    "/jira/latest/issues/{issueKey}/commits",
    "Get changesets for issue key",
)
GET_ENHANCED_ENTITY_LINK_FOR_PROJECT = Endpoint(
    "GET",
    "/jira/latest/projects/{projectKey}/primary-enhanced-entitylink",
    "Get entity link",
)
GET_ISSUE_KEYS_FOR_PULL_REQUEST = Endpoint(
    "GET",
    "/jira/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/issues",
    "Get issues for a pull request",
)

# --- Markup ---

PREVIEW = Endpoint("POST", "/api/latest/markup/preview", "Preview markdown render")
