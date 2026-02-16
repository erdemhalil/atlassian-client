"""Confluence Data Center REST API endpoint definitions.

Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.
"""

from __future__ import annotations

from atlassian.core.endpoint import Endpoint

# --- Content ---

GET_CONTENT = Endpoint("GET", "/rest/api/content", "Get content")
CREATE_CONTENT = Endpoint("POST", "/rest/api/content", "Create content")
PUBLISH_LEGACY_DRAFT = Endpoint("POST", "/rest/api/content/blueprint/instance/{draftId}", "Publish legacy draft")
PUBLISH_SHARED_DRAFT = Endpoint("PUT", "/rest/api/content/blueprint/instance/{draftId}", "Publish shared draft")
SCAN_CONTENT = Endpoint("GET", "/rest/api/content/scan", "Scan content by space key")
SEARCH = Endpoint("GET", "/rest/api/content/search", "Search content using CQL")
UPDATE_2 = Endpoint("PUT", "/rest/api/content/{contentId}", "Update content")
INDEX = Endpoint("GET", "/rest/api/content/{contentId}/watchers", "Fetch users watching a given content")
DELETE_3 = Endpoint("DELETE", "/rest/api/content/{id}", "Delete content")
GET_CONTENT_BY_ID = Endpoint("GET", "/rest/api/content/{id}", "Get content by ID")
GET_HISTORY = Endpoint("GET", "/rest/api/content/{id}/history", "Get history of content")
GET_MACRO_BODY_BY_HASH = Endpoint("GET", "/rest/api/content/{id}/history/{version}/macro/hash/{hash}", "Get macro b...")
GET_MACRO_BODY_BY_MACRO_ID = Endpoint("GET", "/rest/api/content/{id}/history/{version}/macro/id/{macroId}", "Get ma...")
DELETE_CONTENT_HISTORY = Endpoint("DELETE", "/rest/api/content/{id}/version/{versionNumber}", "Delete content history")
CONVERT = Endpoint("POST", "/rest/api/contentbody/convert/{to}", "Convert body representation")

# --- ContentLabels ---

DELETE_LABEL_WITH_QUERY_PARAM = Endpoint("DELETE", "/rest/api/content/{id}/label", "Delete label with query param")
LABELS = Endpoint("GET", "/rest/api/content/{id}/label", "Get labels")
ADD_LABELS = Endpoint("POST", "/rest/api/content/{id}/label", "Add Labels")
DELETE_LABEL = Endpoint("DELETE", "/rest/api/content/{id}/label/{label}", "Delete label")

# --- ContentProperty ---

FIND_ALL = Endpoint("GET", "/rest/api/content/{id}/property", "Find all content properties")
CREATE_1 = Endpoint("POST", "/rest/api/content/{id}/property", "Create a content property")
DELETE_2 = Endpoint("DELETE", "/rest/api/content/{id}/property/{key}", "Delete content property")
FIND_BY_KEY = Endpoint("GET", "/rest/api/content/{id}/property/{key}", "Find content property by key")
CREATE_2 = Endpoint("POST", "/rest/api/content/{id}/property/{key}", "")
UPDATE_1 = Endpoint("PUT", "/rest/api/content/{id}/property/{key}", "Update content property")

# --- ContentRestrictions ---

UPDATE_RESTRICTIONS = Endpoint("PUT", "/rest/api/content/{id}/restriction", "Update restrictions")
BY_OPERATION = Endpoint("GET", "/rest/api/content/{id}/restriction/byOperation", "Get all restrictions by Operation")
FOR_OPERATION = Endpoint("GET", "/rest/api/content/{id}/restriction/byOperation/{operationKey}", "Get all restricti...")
RELEVANT_VIEW_RESTRICTIONS = Endpoint("GET", "/rest/api/content/{id}/restriction/relevantViewRestrictions", "Get al...")

# --- ContentDescendant ---

DESCENDANTS = Endpoint("GET", "/rest/api/content/{id}/descendant", "Get Descendants")
DESCENDANTS_OF_TYPE = Endpoint("GET", "/rest/api/content/{id}/descendant/{type}", "Get descendants of type")

# --- ChildContent ---

CHILDREN = Endpoint("GET", "/rest/api/content/{id}/child", "Get children of content")
COMMENTS_OF_CONTENT = Endpoint("GET", "/rest/api/content/{id}/child/comment", "Get comments of content")
CHILDREN_OF_TYPE = Endpoint("GET", "/rest/api/content/{id}/child/{type}", "Get children of content by type")

# --- Attachments ---

GET_ATTACHMENTS = Endpoint("GET", "/rest/api/content/{id}/child/attachment", "Get attachment")
CREATE_ATTACHMENTS = Endpoint("POST", "/rest/api/content/{id}/child/attachment", "Create attachments")
REMOVE_ATTACHMENT = Endpoint("DELETE", "/rest/api/content/{id}/child/attachment/{attachmentId}", "Remove attachment")
UPDATE = Endpoint("PUT", "/rest/api/content/{id}/child/attachment/{attachmentId}", "Update non-binary data of an At...")
UPDATE_DATA = Endpoint("POST", "/rest/api/content/{id}/child/attachment/{attachmentId}/data", "Update binary data o...")
MOVE = Endpoint("POST", "/rest/api/content/{id}/child/attachment/{attachmentId}/move", "Move attachment")
REMOVE_ATTACHMENT_VERSION = Endpoint(
    "DELETE", "/rest/api/content/{id}/child/attachment/{attachmentId}/version/{version}", ""
)

# --- Space ---

SPACES = Endpoint("GET", "/rest/api/space", "Get spaces by key")
CREATE_SPACE = Endpoint("POST", "/rest/api/space", "Creates a new Space.")
CREATE_PRIVATE_SPACE = Endpoint("POST", "/rest/api/space/_private", "Create private space")
CREATE_PERSONAL_SPACE_1 = Endpoint("POST", "/rest/api/space/personal", "Creates the personal Space for self.")
DELETE_5 = Endpoint("DELETE", "/rest/api/space/{spaceKey}", "Delete Space")
SPACE = Endpoint("GET", "/rest/api/space/{spaceKey}", "Get space")
UPDATE_4 = Endpoint("PUT", "/rest/api/space/{spaceKey}", "Update Space")
ARCHIVE = Endpoint("PUT", "/rest/api/space/{spaceKey}/archive", "Archive space")
CONTENTS = Endpoint("GET", "/rest/api/space/{spaceKey}/content", "Get contents in space")
CONTENTS_WITH_TYPE_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/content/{type}", "Get contents by type")
RESTORE = Endpoint("PUT", "/rest/api/space/{spaceKey}/restore", "Restore space")
TRASH = Endpoint("DELETE", "/rest/api/space/{spaceKey}/trash", "Remove all trash contents")
CONTENTS_WITH_TYPE = Endpoint("GET", "/rest/api/space/{spaceKey}/trash", "Get trash contents of space")
INDEX_4 = Endpoint("GET", "/rest/api/space/{spaceKey}/watchers", "Fetch users watching space")

# --- SpaceLabel ---

INDEX_3 = Endpoint("GET", "/rest/api/space/{spaceKey}/labels", "Fetch all labels")
POPULAR_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/labels/popular", "Get popular labels")
RECENT_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/labels/recent", "Get recent labels")
RELATED_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/labels/{labelName}/related", "Get related labels")

# --- SpacePermissions ---

GET_ALL_SPACE_PERMISSIONS = Endpoint("GET", "/rest/api/space/{spaceKey}/permissions", "Get all space permissions")
SET_PERMISSIONS_1 = Endpoint("POST", "/rest/api/space/{spaceKey}/permissions", "Set permissions to multiple users/g...")
GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/permissions/anonymous", "Ge")
GRANT_PERMISSIONS_TO_ANONYMOUS_USERS_1 = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/anonymous/grant", "Gr")
REVOKE_PERMISSIONS_FROM_ANONYMOUS_USER = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/anonymous/revoke", "R")
GET_PERMISSIONS_GRANTED_TO_GROUP_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/permissions/group/{groupName}", "G...")
GRANT_PERMISSIONS_TO_GROUP_1 = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/group/{groupName}/grant", "G...")
REVOKE_PERMISSIONS_FROM_GROUP_1 = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/group/{groupName}/revoke", "")
GET_PERMISSIONS_GRANTED_TO_USER_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/permissions/user/{userKey}", "Gets ...")
GRANT_PERMISSIONS_TO_USER_1 = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/user/{userKey}/grant", "Grant...")
REVOKE_PERMISSIONS_FROM_USER_1 = Endpoint("PUT", "/rest/api/space/{spaceKey}/permissions/user/{userKey}/revoke", "R...")

# --- SpaceProperty ---

GET_1 = Endpoint("GET", "/rest/api/space/{spaceKey}/property", "Get space properties")
CREATE_3 = Endpoint("POST", "/rest/api/space/{spaceKey}/property", "Create a space property")
DELETE_4 = Endpoint("DELETE", "/rest/api/space/{spaceKey}/property/{key}", "Delete space property")
GET = Endpoint("GET", "/rest/api/space/{spaceKey}/property/{key}", "Get space property by key")
CREATE_4 = Endpoint("POST", "/rest/api/space/{spaceKey}/property/{key}", "Create a space property with a specific key")
UPDATE_3 = Endpoint("PUT", "/rest/api/space/{spaceKey}/property/{key}", "Update space property")

# --- SpaceColorScheme ---

GET_SPACE_COLOR_SCHEME = Endpoint("GET", "/rest/api/space/{spaceKey}/color-scheme", "Get Space color scheme")
UPDATE_SPACE_COLOR_SCHEME = Endpoint("PUT", "/rest/api/space/{spaceKey}/color-scheme", "Update Space color scheme")
RESET_SPACE_COLOR_SCHEME = Endpoint("PUT", "/rest/api/space/{spaceKey}/color-scheme/reset", "Reset Space color scheme")
GET_COLOR_SCHEME_TYPE = Endpoint("GET", "/rest/api/space/{spaceKey}/color-scheme/type", "Get Space color scheme type")
UPDATE_COLOR_SCHEME_TYPE = Endpoint("PUT", "/rest/api/space/{spaceKey}/color-scheme/type", "Update Space color sche...")

# --- Group ---

GET_GROUPS = Endpoint("GET", "/rest/api/group", "Get groups")
GET_GROUP = Endpoint("GET", "/rest/api/group/{groupName}", "Get group by name")
GET_NESTED_GROUP_MEMBERS = Endpoint("GET", "/rest/api/group/{groupName}/groupmember", "Get group members of group")
GET_MEMBERS = Endpoint("GET", "/rest/api/group/{groupName}/member", "Get members of group")
DELETE_6 = Endpoint("DELETE", "/rest/api/user/{username}/group/{groupName}", "Delete user group")
UPDATE_5 = Endpoint("PUT", "/rest/api/user/{username}/group/{groupName}", "Update user group")

# --- User ---

GET_USER = Endpoint("GET", "/rest/api/user", "Get user")
GET_ANONYMOUS = Endpoint("GET", "/rest/api/user/anonymous", "Get information about anonymous user type")
GET_CURRENT = Endpoint("GET", "/rest/api/user/current", "Get current user")
UPDATE_USER_1 = Endpoint("PUT", "/rest/api/user/current", "Update details of the current user")
CHANGE_PASSWORD_1 = Endpoint("POST", "/rest/api/user/current/password", "Change password")
GET_USERS = Endpoint("GET", "/rest/api/user/list", "Get registered users")
GET_GROUPS_1 = Endpoint("GET", "/rest/api/user/memberof", "Get groups")

# --- UserWatch ---

REMOVE_CONTENT_WATCHER = Endpoint("DELETE", "/rest/api/user/watch/content/{contentId}", "Remove content watcher")
IS_WATCHING_CONTENT = Endpoint("GET", "/rest/api/user/watch/content/{contentId}", "Get information about content wa...")
ADD_CONTENT_WATCHER = Endpoint("POST", "/rest/api/user/watch/content/{contentId}", "Add content watcher")
REMOVE_SPACE_WATCH = Endpoint("DELETE", "/rest/api/user/watch/space/{spaceKey}", "Remove space watcher")
IS_WATCHING_SPACE = Endpoint("GET", "/rest/api/user/watch/space/{spaceKey}", "Get information about space watcher")
ADD_SPACE_WATCH = Endpoint("POST", "/rest/api/user/watch/space/{spaceKey}", "Add space watcher")

# --- Search ---

SEARCH_1 = Endpoint("GET", "/rest/api/search", "Search for entities in confluence")

# --- Label ---

LABELS_1 = Endpoint("GET", "/rest/api/label/labels", "Get list of labels matching the given label name, namespace, ...")
POPULAR = Endpoint("GET", "/rest/api/label/popular", "Get most popular labels")
RECENT = Endpoint("GET", "/rest/api/label/recent", "Get recently used labels")
RELATED = Endpoint("GET", "/rest/api/label/{labelName}/related", "Get related labels.")

# --- LongTask ---

GET_TASKS = Endpoint("GET", "/rest/api/longtask", "Get tasks")
GET_TASK = Endpoint("GET", "/rest/api/longtask/{id}", "Get task by ID")

# --- BackupRestore ---

CREATE_SITE_BACKUP_JOB = Endpoint("POST", "/rest/api/backup-restore/backup/site", "Create site backup job")
CREATE_SPACE_BACKUP_JOB = Endpoint("POST", "/rest/api/backup-restore/backup/space", "Create space backup job")
FIND_JOBS = Endpoint("GET", "/rest/api/backup-restore/jobs", "Find jobs by filters")
CANCEL_ALL_QUEUED_JOBS = Endpoint("PUT", "/rest/api/backup-restore/jobs/clear-queue", "Cancel all queued jobs")
GET_JOB = Endpoint("GET", "/rest/api/backup-restore/jobs/{jobId}", "Get job by ID")
CANCEL_JOB = Endpoint("PUT", "/rest/api/backup-restore/jobs/{jobId}/cancel", "Cancel job")
DOWNLOAD_BACKUP_FILE = Endpoint("GET", "/rest/api/backup-restore/jobs/{jobId}/download", "Download backup file")
GET_FILES = Endpoint("GET", "/rest/api/backup-restore/restore/files", "Get files in restore directory")
CREATE_SITE_RESTORE_JOB = Endpoint("POST", "/rest/api/backup-restore/restore/site", "Create site restore job")
CREATE_SITE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE = Endpoint("POST", "/rest/api/backup-restore/restore/site/upload", "C")
CREATE_SPACE_RESTORE_JOB = Endpoint("POST", "/rest/api/backup-restore/restore/space", "Create space restore job")
CREATE_SPACE_RESTORE_JOB_FOR_UPLOADED_BACKUP_FILE = Endpoint(
    "POST", "/rest/api/backup-restore/restore/space/upload", ""
)

# --- Webhooks ---

FIND_WEBHOOKS = Endpoint("GET", "/rest/api/webhooks", "Find webhooks")
CREATE_WEBHOOK = Endpoint("POST", "/rest/api/webhooks", "Create webhook")
TEST_WEBHOOK = Endpoint("POST", "/rest/api/webhooks/test", "Test webhook")
DELETE_WEBHOOK = Endpoint("DELETE", "/rest/api/webhooks/{webhookId}", "Delete webhook")
GET_WEBHOOK = Endpoint("GET", "/rest/api/webhooks/{webhookId}", "Get webhook")
UPDATE_WEBHOOK = Endpoint("PUT", "/rest/api/webhooks/{webhookId}", " Update webhook")
GET_LATEST_INVOCATION = Endpoint("GET", "/rest/api/webhooks/{webhookId}/latest", "Get latest invocations")
GET_STATISTICS = Endpoint("GET", "/rest/api/webhooks/{webhookId}/statistics", "Get statistic")
GET_STATISTICS_SUMMARY = Endpoint("GET", "/rest/api/webhooks/{webhookId}/statistics/summary", "Get statistics summary")

# --- GlobalPermissions ---

GET_ALL_GLOBAL_PERMISSIONS = Endpoint("GET", "/rest/api/permissions", "Get global permissions")
SET_PERMISSIONS = Endpoint("PUT", "/rest/api/permissions", "Set global permissions to multiple users/groups")
GET_PERMISSIONS_GRANTED_TO_ANONYMOUS_USERS = Endpoint("GET", "/rest/api/permissions/anonymous", "Gets the permissio...")
GRANT_PERMISSIONS_TO_ANONYMOUS_USERS = Endpoint("PUT", "/rest/api/permissions/anonymous/grant", "Grants global perm...")
REVOKE_PERMISSIONS_FROM_ANONYMOUS_USERS = Endpoint("PUT", "/rest/api/permissions/anonymous/revoke", "Revoke global ...")
GET_PERMISSIONS_GRANTED_TO_GROUP = Endpoint("GET", "/rest/api/permissions/group/{groupName}", "Gets global permissi...")
GRANT_PERMISSIONS_TO_GROUP = Endpoint("PUT", "/rest/api/permissions/group/{groupName}/grant", "Grants global permis...")
REVOKE_PERMISSIONS_FROM_GROUP = Endpoint("PUT", "/rest/api/permissions/group/{groupName}/revoke", "Revoke global pe...")
GET_PERMISSIONS_GRANTED_TO_UNLICENSED_USERS = Endpoint("GET", "/rest/api/permissions/unlicensed", "Gets the permiss...")
GRANT_PERMISSIONS_TO_UNLICENSED_USERS = Endpoint("PUT", "/rest/api/permissions/unlicensed/grant", "Grants global pe...")
REVOKE_PERMISSIONS_FROM_UNLICENSED_USERS = Endpoint("PUT", "/rest/api/permissions/unlicensed/revoke", "Revoke globa...")
GET_PERMISSIONS_GRANTED_TO_USER = Endpoint("GET", "/rest/api/permissions/user/{user}", "Gets global permissions gra...")
GRANT_PERMISSIONS_TO_USER = Endpoint("PUT", "/rest/api/permissions/user/{user}/grant", "Grants global permissions t...")
REVOKE_PERMISSIONS_FROM_USER = Endpoint("PUT", "/rest/api/permissions/user/{user}/revoke", "Revoke global permissio...")

# --- GlobalColorScheme ---

GET_GLOBAL_COLOR_SCHEME = Endpoint("GET", "/rest/api/color-scheme", "Get global color scheme")
UPDATE_COLOR_SCHEME = Endpoint("PUT", "/rest/api/color-scheme", "Set global color scheme")
GET_DEFAULT_COLOR_SCHEME = Endpoint("GET", "/rest/api/color-scheme/default", "Get default global color scheme")
RESET_GLOBAL_COLOR_SCHEME = Endpoint("PUT", "/rest/api/color-scheme/reset", "Reset global color scheme")

# --- Category ---

REMOVE_CATEGORY = Endpoint("DELETE", "/rest/api/space/{spaceKey}/category/{categoryName}", "Remove a category from ...")
ADD = Endpoint("POST", "/rest/api/space/{spaceKey}/category/{labelName}", "Add a category to a space")

# --- AccessMode ---

GET_ACCESS_MODE_STATUS = Endpoint("GET", "/rest/api/accessmode", "Get access mode status")

# --- ServerInfo ---

INDEX_1 = Endpoint("GET", "/rest/api/instance-metrics", "Get instance metrics")
INDEX_2 = Endpoint("GET", "/rest/api/server-information", "Get server information")

# --- Admin ---

CREATE = Endpoint("POST", "/rest/api/admin/group", "Create group")
DELETE = Endpoint("DELETE", "/rest/api/admin/group/{groupName}", "Delete group")
CREATE_USER = Endpoint("POST", "/rest/api/admin/user", "Create user")
DELETE_1 = Endpoint("DELETE", "/rest/api/admin/user/{username}", "Delete user")
UPDATE_USER = Endpoint("PUT", "/rest/api/admin/user/{username}", "Update user")
DISABLE = Endpoint("PUT", "/rest/api/admin/user/{username}/disable", "Disable user")
ENABLE = Endpoint("PUT", "/rest/api/admin/user/{username}/enable", "Enable user")
CHANGE_PASSWORD = Endpoint("POST", "/rest/api/admin/user/{username}/password", "Change password")
GET_AUDIT_RECORDS = Endpoint("GET", "/rest/api/audit", "")
