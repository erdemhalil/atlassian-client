"""Scaffold generator for product endpoints and async resource classes.

Reads the OpenAPI spec and generates:
  - endpoints.py  (Endpoint constants)
  - async_resources.py (typed resource methods)

Usage:
    uv run python scripts/generate_resources.py bitbucket
    uv run python scripts/generate_resources.py confluence
    uv run python scripts/generate_resources.py jira
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LINE_LENGTH = 120

# ---------------------------------------------------------------------------
# Tag → resource class mappings (per product)
# ---------------------------------------------------------------------------
BITBUCKET_TAG_TO_RESOURCE: dict[str, str] = {
    "Project": "AsyncProjectsResource",
    "Repository": "AsyncRepositoriesResource",
    "Pull Requests": "AsyncPullRequestsResource",
    "Authentication": "AsyncAuthenticationResource",
    "Builds and Deployments": "AsyncBuildsResource",
    "Permission Management": "AsyncPermissionsResource",
    "Security": "AsyncSecurityResource",
    "System Maintenance": "AsyncAdminResource",
    "Dashboard": "AsyncDashboardResource",
    "Mirroring (Mirror)": "AsyncMirroringResource",
    "Mirroring (Upstream)": "AsyncMirroringResource",
    "Jira Integration": "AsyncJiraIntegrationResource",
    "Markup": "AsyncMarkupResource",
    "Capabilities": "AsyncBuildsResource",  # only 2 ops, fits builds
    "Deprecated": "AsyncDeprecatedResource",
}

CONFLUENCE_TAG_TO_RESOURCE: dict[str, str] = {
    "Content Resource": "AsyncContentResource",
    "Content Blueprint": "AsyncContentResource",
    "Content Body": "AsyncContentResource",
    "Content Version": "AsyncContentResource",
    "Content Watchers": "AsyncContentResource",
    "Content Labels": "AsyncContentLabelsResource",
    "Content Property": "AsyncContentPropertyResource",
    "Content Restrictions": "AsyncContentRestrictionsResource",
    "Content Descendant": "AsyncContentDescendantResource",
    "Child Content": "AsyncChildContentResource",
    "Attachments": "AsyncAttachmentsResource",
    "Space": "AsyncSpaceResource",
    "Space Label": "AsyncSpaceLabelResource",
    "Space Permissions": "AsyncSpacePermissionsResource",
    "Space Property": "AsyncSpacePropertyResource",
    "Space Watchers": "AsyncSpaceResource",
    "SpaceColorScheme": "AsyncSpaceColorSchemeResource",
    "Group": "AsyncGroupResource",
    "User": "AsyncUserResource",
    "Admin Group": "AsyncAdminResource",
    "Admin User": "AsyncAdminResource",
    "User Group": "AsyncGroupResource",
    "User Watch": "AsyncUserWatchResource",
    "Search": "AsyncSearchResource",
    "Label": "AsyncLabelResource",
    "Long Task": "AsyncLongTaskResource",
    "Backup and Restore": "AsyncBackupRestoreResource",
    "Webhooks": "AsyncWebhooksResource",
    "Global Permissions": "AsyncGlobalPermissionsResource",
    "GlobalColorScheme": "AsyncGlobalColorSchemeResource",
    "Category": "AsyncCategoryResource",
    "Access Mode": "AsyncAccessModeResource",
    "Server Information": "AsyncServerInfoResource",
    "Instance Metrics": "AsyncServerInfoResource",
}

JIRA_TAG_TO_RESOURCE: dict[str, str] = {
    "application-properties": "AsyncSystemResource",
    "applicationrole": "AsyncUserResource",
    "attachment": "AsyncIssueResource",
    "avatar": "AsyncAvatarResource",
    "backlog": "AsyncAgileResource",
    "board": "AsyncAgileResource",
    "cluster": "AsyncOperationsResource",
    "comment": "AsyncIssueResource",
    "component": "AsyncProjectResource",
    "configuration": "AsyncSystemResource",
    "customFieldOption": "AsyncIssueMetaResource",
    "customFields": "AsyncIssueMetaResource",
    "dashboard": "AsyncDashboardFilterResource",
    "email-templates": "AsyncSystemResource",
    "epic": "AsyncAgileResource",
    "field": "AsyncIssueMetaResource",
    "filter": "AsyncDashboardFilterResource",
    "group": "AsyncGroupResource",
    "groups": "AsyncGroupResource",
    "groupuserpicker": "AsyncUserResource",
    "index": "AsyncOperationsResource",
    "index-snapshot": "AsyncOperationsResource",
    "issue": "AsyncIssueResource",
    "issueLink": "AsyncIssueResource",
    "issueLinkType": "AsyncIssueResource",
    "issuesecurityschemes": "AsyncPermissionSecurityResource",
    "issuetype": "AsyncIssueMetaResource",
    "issuetypescheme": "AsyncIssueMetaResource",
    "jql": "AsyncIssueResource",
    "licenseValidator": "AsyncSystemResource",
    "monitoring": "AsyncOperationsResource",
    "mypermissions": "AsyncPermissionSecurityResource",
    "mypreferences": "AsyncUserResource",
    "myself": "AsyncUserResource",
    "notificationscheme": "AsyncPermissionSecurityResource",
    "password": "AsyncAuthResource",
    "permissions": "AsyncPermissionSecurityResource",
    "permissionscheme": "AsyncPermissionSecurityResource",
    "priority": "AsyncIssueMetaResource",
    "priorityschemes": "AsyncIssueMetaResource",
    "project": "AsyncProjectResource",
    "projectCategory": "AsyncProjectResource",
    "projects": "AsyncProjectResource",
    "projectvalidate": "AsyncProjectResource",
    "reindex": "AsyncOperationsResource",
    "resolution": "AsyncIssueMetaResource",
    "role": "AsyncProjectResource",
    "screens": "AsyncIssueMetaResource",
    "search": "AsyncIssueResource",
    "securitylevel": "AsyncPermissionSecurityResource",
    "serverInfo": "AsyncSystemResource",
    "session": "AsyncAuthResource",
    "settings": "AsyncSystemResource",
    "sprint": "AsyncAgileResource",
    "status": "AsyncIssueMetaResource",
    "statuscategory": "AsyncIssueMetaResource",
    "terminology": "AsyncSystemResource",
    "universal_avatar": "AsyncAvatarResource",
    "upgrade": "AsyncOperationsResource",
    "user": "AsyncUserResource",
    "version": "AsyncProjectResource",
    "websudo": "AsyncAuthResource",
    "workflow": "AsyncIssueMetaResource",
    "workflowscheme": "AsyncIssueMetaResource",
    "worklog": "AsyncIssueResource",
}

BITBUCKET_RESOURCE_ORDER: list[str] = [
    "AsyncProjectsResource",
    "AsyncRepositoriesResource",
    "AsyncPullRequestsResource",
    "AsyncAuthenticationResource",
    "AsyncBuildsResource",
    "AsyncPermissionsResource",
    "AsyncSecurityResource",
    "AsyncAdminResource",
    "AsyncDashboardResource",
    "AsyncMirroringResource",
    "AsyncJiraIntegrationResource",
    "AsyncMarkupResource",
    "AsyncDeprecatedResource",
]

CONFLUENCE_RESOURCE_ORDER: list[str] = [
    "AsyncContentResource",
    "AsyncContentLabelsResource",
    "AsyncContentPropertyResource",
    "AsyncContentRestrictionsResource",
    "AsyncContentDescendantResource",
    "AsyncChildContentResource",
    "AsyncAttachmentsResource",
    "AsyncSpaceResource",
    "AsyncSpaceLabelResource",
    "AsyncSpacePermissionsResource",
    "AsyncSpacePropertyResource",
    "AsyncSpaceColorSchemeResource",
    "AsyncGroupResource",
    "AsyncUserResource",
    "AsyncUserWatchResource",
    "AsyncSearchResource",
    "AsyncLabelResource",
    "AsyncLongTaskResource",
    "AsyncBackupRestoreResource",
    "AsyncWebhooksResource",
    "AsyncGlobalPermissionsResource",
    "AsyncGlobalColorSchemeResource",
    "AsyncCategoryResource",
    "AsyncAccessModeResource",
    "AsyncServerInfoResource",
    "AsyncAdminResource",
]

JIRA_RESOURCE_ORDER: list[str] = [
    "AsyncAgileResource",
    "AsyncProjectResource",
    "AsyncIssueResource",
    "AsyncIssueMetaResource",
    "AsyncPermissionSecurityResource",
    "AsyncUserResource",
    "AsyncGroupResource",
    "AsyncAvatarResource",
    "AsyncDashboardFilterResource",
    "AsyncSystemResource",
    "AsyncOperationsResource",
    "AsyncAuthResource",
    "AsyncJiraMiscResource",
]


# ---------------------------------------------------------------------------
# Product configuration
# ---------------------------------------------------------------------------


@dataclass
class ProductConfig:
    """Per-product settings for code generation."""

    name: str
    display_name: str
    spec_path: Path
    endpoints_out: Path
    resources_out: Path
    tag_to_resource: dict[str, str]
    resource_order: list[str]
    base_resource_class: str
    base_resource_import: str
    pagination_items_field: str
    default_resource_class: str | None = None


PRODUCT_CONFIGS: dict[str, ProductConfig] = {
    "bitbucket": ProductConfig(
        name="bitbucket",
        display_name="Bitbucket Data Center",
        spec_path=PROJECT_ROOT / "specs" / "bitbucket" / "openapi.json",
        endpoints_out=PROJECT_ROOT / "atlassian" / "bitbucket" / "endpoints.py",
        resources_out=PROJECT_ROOT / "atlassian" / "bitbucket" / "async_resources.py",
        tag_to_resource=BITBUCKET_TAG_TO_RESOURCE,
        resource_order=BITBUCKET_RESOURCE_ORDER,
        base_resource_class="AsyncResource",
        base_resource_import="from atlassian.core.resource import AsyncResource",
        pagination_items_field="values",
    ),
    "confluence": ProductConfig(
        name="confluence",
        display_name="Confluence Data Center",
        spec_path=PROJECT_ROOT / "specs" / "confluence" / "openapi.json",
        endpoints_out=PROJECT_ROOT / "atlassian" / "confluence" / "endpoints.py",
        resources_out=PROJECT_ROOT / "atlassian" / "confluence" / "async_resources.py",
        tag_to_resource=CONFLUENCE_TAG_TO_RESOURCE,
        resource_order=CONFLUENCE_RESOURCE_ORDER,
        base_resource_class="ConfluenceAsyncResource",
        base_resource_import="from atlassian.confluence.resource import ConfluenceAsyncResource",
        pagination_items_field="results",
    ),
    "jira": ProductConfig(
        name="jira",
        display_name="Jira Data Center",
        spec_path=PROJECT_ROOT / "specs" / "jira" / "openapi.json",
        endpoints_out=PROJECT_ROOT / "atlassian" / "jira" / "endpoints.py",
        resources_out=PROJECT_ROOT / "atlassian" / "jira" / "async_resources.py",
        tag_to_resource=JIRA_TAG_TO_RESOURCE,
        resource_order=JIRA_RESOURCE_ORDER,
        base_resource_class="AsyncJiraResource",
        base_resource_import="from atlassian.jira.resource import AsyncJiraResource",
        pagination_items_field="__none__",
        default_resource_class="AsyncJiraMiscResource",
    ),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _camel_to_snake(name: str) -> str:
    """Convert camelCase / PascalCase to snake_case."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def _operation_id_to_method(op_id: str) -> str:
    """Convert operationId like 'getProjects' or 'getAllAccessTokens_1' to snake_case."""
    method_name = _camel_to_snake(op_id)
    if not method_name:
        method_name = "op"
    if re.match(r"^\d", method_name):
        method_name = f"_{method_name}"
    if method_name in PYTHON_KEYWORDS:
        method_name = f"{method_name}_"
    return method_name


def _path_param_to_python(name: str) -> str:
    """Convert path param like 'projectKey' to 'project_key'."""
    return _camel_to_snake(name)


def _endpoint_const_name(op_id: str) -> str:
    """Convert operationId to UPPER_SNAKE endpoint constant."""
    return _camel_to_snake(op_id).upper()


def _resolve_ref(ref: str) -> str | None:
    """Extract model name from $ref like '#/components/schemas/RestProject'."""
    if ref and ref.startswith("#/components/schemas/"):
        model_name = ref.split("/")[-1]
        if model_name and model_name[0].islower():
            model_name = model_name[0].upper() + model_name[1:]
        return model_name
    return None


def _lookup_schema(components: dict[str, dict], schema_name: str) -> dict:
    """Get a schema object by name with lowercase-first fallback handling."""
    schemas = components.get("schemas", {})
    if schema_name in schemas:
        return schemas[schema_name]
    if schema_name:
        lower_first = schema_name[0].lower() + schema_name[1:]
        return schemas.get(lower_first, {})
    return {}


def _find_jira_items_field(props: dict[str, dict]) -> tuple[str, str] | None:
    """Return (items_field_name, item_model_name) when schema matches Jira page shape."""
    array_props: list[tuple[str, str]] = []
    for field_name, field_schema in props.items():
        if field_schema.get("type") != "array":
            continue
        item_ref = field_schema.get("items", {}).get("$ref", "")
        item_model = _resolve_ref(item_ref)
        if item_model:
            array_props.append((field_name, item_model))

    if not array_props:
        return None

    if "values" in props:
        for field_name, item_model in array_props:
            if field_name == "values":
                return field_name, item_model

    preferred = (
        "issues",
        "worklogs",
        "comments",
        "dashboards",
        "sprints",
        "boards",
        "versions",
        "projects",
        "users",
        "epics",
        "statuses",
        "priorities",
        "resolutions",
    )
    for preferred_name in preferred:
        for field_name, item_model in array_props:
            if field_name == preferred_name:
                return field_name, item_model

    if len(array_props) == 1:
        return array_props[0]

    return None


def _detect_jira_paged_model(schema: dict) -> tuple[str, str] | None:
    """Detect Jira-style pagination and return (item_model, items_field)."""
    if schema.get("type") != "object":
        return None

    props = schema.get("properties", {})
    if not props:
        return None

    has_start = "startAt" in props
    has_max = "maxResults" in props
    has_total = "total" in props
    has_is_last = "isLast" in props or "isLastPage" in props
    has_paging_markers = (has_start and has_max) or (has_start and has_total) or has_is_last
    if not has_paging_markers:
        return None

    found = _find_jira_items_field(props)
    if not found:
        return None
    items_field, item_model = found
    return item_model, items_field


PYTHON_KEYWORDS = {
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
    "type",
}


def _safe_param_name(name: str) -> str:
    """Ensure parameter names don't collide with Python keywords or contain invalid chars."""
    snake = _path_param_to_python(name)
    # Replace dots and other invalid chars
    snake = re.sub(r"[^a-z0-9_]", "_", snake)
    # Remove leading digits
    snake = re.sub(r"^(\d)", r"_\1", snake)
    if snake in PYTHON_KEYWORDS:
        return snake + "_"
    return snake


def _truncate_with_ellipsis(text: str, max_len: int) -> str:
    """Truncate text to max_len with ellipsis when needed."""
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return text[:max_len]
    return text[: max_len - 3] + "..."


def _op_key(op: OperationInfo) -> str:
    """Return a stable unique key for an operation within generation pass."""
    return f"{op.resource_class}::{op.op_id}::{op.method}::{op.path}"


def _extract_model_refs_from_type(type_str: str) -> set[str]:
    """Extract candidate model names from a generated Python type string."""
    primitives = {"Any", "None", "bool", "dict", "float", "int", "list", "str"}
    candidates = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", type_str))
    return {name for name in candidates if name[0].isupper() and name not in primitives}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ParamInfo:
    name: str  # original API name
    python_name: str  # snake_case
    location: str  # 'path', 'query'
    param_type: str  # 'str', 'int', 'bool', etc.
    required: bool = False
    description: str = ""
    default: str | None = None


@dataclass
class OperationInfo:
    op_id: str
    method: str  # GET, POST, etc.
    path: str
    summary: str
    description: str
    tags: list[str]
    path_params: list[ParamInfo] = field(default_factory=list)
    query_params: list[ParamInfo] = field(default_factory=list)
    request_body_model: str | None = None
    response_model: str | None = None
    is_paged: bool = False
    paged_items_field: str | None = None
    resource_class: str = ""
    is_deprecated: bool = False


def _schema_type_to_python(schema: dict) -> str:
    """Map OpenAPI schema type to Python type string."""
    t = schema.get("type", "")
    fmt = schema.get("format", "")
    if t == "integer":
        return "int"
    if t == "number":
        if fmt == "int32" or fmt == "int64":
            return "int"
        return "float"
    if t == "boolean":
        return "bool"
    if t == "string":
        return "str"
    if t == "array":
        items = schema.get("items", {})
        inner = _resolve_ref(items.get("$ref", "")) or _schema_type_to_python(items)
        return f"list[{inner}]"
    if t == "object":
        return "dict[str, Any]"
    ref = schema.get("$ref")
    if ref:
        return _resolve_ref(ref) or "Any"
    return "Any"


# ---------------------------------------------------------------------------
# Spec parsing
# ---------------------------------------------------------------------------


def _route_untagged_op(path: str, config: ProductConfig) -> str:
    """Route untagged or deprecated-only operations to a resource class."""
    if config.name == "bitbucket":
        if "/inbox/" in path or "/dashboard/" in path:
            return "AsyncDashboardResource"
        if "/pull-requests/" in path:
            return "AsyncPullRequestsResource"
        if "/repos/" in path:
            return "AsyncRepositoriesResource"
        if "/projects/" in path:
            return "AsyncProjectsResource"
        if "/build-status/" in path or "/builds/" in path:
            return "AsyncBuildsResource"
        return "AsyncAdminResource"
    if config.name == "confluence":
        if "/rest/api/content/" in path:
            return "AsyncContentResource"
        if "/rest/api/space/" in path:
            return "AsyncSpaceResource"
        return "AsyncAdminResource"
    if config.name == "jira":
        if "/agile/" in path:
            return "AsyncAgileResource"
        if "/api/2/project" in path:
            return "AsyncProjectResource"
        if "/api/2/issue" in path:
            return "AsyncIssueResource"
        return config.default_resource_class or "AsyncJiraMiscResource"
    return "AsyncAdminResource"


def parse_spec(spec: dict, config: ProductConfig) -> list[OperationInfo]:
    """Parse every operation from the OpenAPI spec into OperationInfo."""
    operations: list[OperationInfo] = []

    for path, methods in spec.get("paths", {}).items():
        for method, op in methods.items():
            if not isinstance(op, dict):
                continue

            op_id = op.get("operationId", "unknown")
            tags = op.get("tags", [])
            summary = op.get("summary", "")
            description = op.get("description", "")
            is_deprecated = "Deprecated" in tags

            # Determine resource class
            resource_class = ""
            for tag in tags:
                if tag == "Deprecated":
                    continue
                mapped_resource = config.tag_to_resource.get(tag)
                if mapped_resource:
                    resource_class = mapped_resource
                    break

            if not resource_class and tags and config.default_resource_class:
                resource_class = config.default_resource_class
            if not resource_class:
                resource_class = _route_untagged_op(path, config)

            # Parse parameters
            path_params: list[ParamInfo] = []
            query_params: list[ParamInfo] = []
            used_param_names: set[str] = set()
            for param in op.get("parameters", []):
                pname = param.get("name", "")
                ploc = param.get("in", "")
                pschema = param.get("schema", {})
                ptype = _schema_type_to_python(pschema)
                prequired = param.get("required", ploc == "path")
                pdesc = param.get("description", "")
                pdefault = None
                if "default" in pschema:
                    pdefault = repr(pschema["default"])

                python_name = _safe_param_name(pname)
                if python_name in used_param_names:
                    suffix = 2
                    while f"{python_name}_{suffix}" in used_param_names:
                        suffix += 1
                    python_name = f"{python_name}_{suffix}"
                used_param_names.add(python_name)

                info = ParamInfo(
                    name=pname,
                    python_name=python_name,
                    location=ploc,
                    param_type=ptype,
                    required=prequired,
                    description=pdesc,
                    default=pdefault,
                )

                if ploc == "path":
                    path_params.append(info)
                elif ploc == "query":
                    query_params.append(info)

            # Request body
            request_body_model = None
            rb = op.get("requestBody", {})
            for _ct, ct_val in rb.get("content", {}).items():
                schema = ct_val.get("schema", {})
                ref = schema.get("$ref", "")
                if ref:
                    request_body_model = _resolve_ref(ref)
                break

            # Response type
            response_model = None
            is_paged = False
            paged_items_field = None
            components = spec.get("components", {})
            for code in ["200", "201", "202"]:
                if code not in op.get("responses", {}):
                    continue
                resp = op["responses"][code]
                content = resp.get("content", {})
                for _ct, ct_val in content.items():
                    schema = ct_val.get("schema", {})
                    ref = schema.get("$ref", "")
                    if ref:
                        response_model = _resolve_ref(ref)
                        if config.name == "jira" and response_model:
                            ref_schema = _lookup_schema(components, response_model)
                            jira_paged = _detect_jira_paged_model(ref_schema)
                            if jira_paged:
                                response_model, paged_items_field = jira_paged
                                is_paged = True
                    elif schema.get("type") == "object":
                        props = schema.get("properties", {})
                        if config.name == "jira":
                            jira_paged = _detect_jira_paged_model(schema)
                            if jira_paged:
                                response_model, paged_items_field = jira_paged
                                is_paged = True
                        else:
                            items_field = config.pagination_items_field
                            is_paged_response = False
                            if items_field == "values":
                                is_paged_response = "values" in props and "isLastPage" in props
                            elif items_field == "results":
                                has_cursor = any(p.get("name") == "cursor" for p in op.get("parameters", []))
                                is_paged_response = "results" in props and "_links" in props and not has_cursor
                            if is_paged_response:
                                field_items = props[items_field].get("items", {})
                                field_ref = field_items.get("$ref", "")
                                response_model = _resolve_ref(field_ref) if field_ref else None
                                if response_model:
                                    is_paged = True
                    elif schema.get("type") == "array":
                        items = schema.get("items", {})
                        items_ref = items.get("$ref", "")
                        if items_ref:
                            response_model = _resolve_ref(items_ref)
                    break
                break

            operations.append(
                OperationInfo(
                    op_id=op_id,
                    method=method.upper(),
                    path=path,
                    summary=summary,
                    description=description,
                    tags=tags,
                    path_params=path_params,
                    query_params=query_params,
                    request_body_model=request_body_model,
                    response_model=response_model,
                    is_paged=is_paged,
                    paged_items_field=paged_items_field,
                    resource_class=resource_class,
                    is_deprecated=is_deprecated,
                )
            )

    return operations


# ---------------------------------------------------------------------------
# Deduplication: handle operationId collisions within same resource
# ---------------------------------------------------------------------------


def _disambiguate_method_names(ops: list[OperationInfo]) -> dict[str, str]:
    """Return op_id → unique method name mapping."""
    # Group by resource class
    by_resource: dict[str, list[OperationInfo]] = defaultdict(list)
    for op in ops:
        by_resource[op.resource_class].append(op)

    result: dict[str, str] = {}
    for _resource, resource_ops in by_resource.items():
        # Check for duplicate method names within this resource
        name_count: dict[str, list[OperationInfo]] = defaultdict(list)
        for op in resource_ops:
            base_name = _operation_id_to_method(op.op_id)
            name_count[base_name].append(op)

        for base_name, collision_ops in name_count.items():
            if len(collision_ops) == 1:
                key = _op_key(collision_ops[0])
                result[key] = base_name
            else:
                # Disambiguate using path context
                for op in collision_ops:
                    key = _op_key(op)
                    suffix = _derive_suffix(op.path, op.path_params)
                    if suffix:
                        result[key] = f"{base_name}_{suffix}"
                    else:
                        result[key] = base_name

    return result


def _derive_suffix(path: str, path_params: list[ParamInfo]) -> str:
    """Derive a disambiguation suffix from the path structure."""
    parts = path.strip("/").split("/")

    # Find meaningful segments (not params, not 'latest', not 'api')
    meaningful = []
    for p in parts:
        if p.startswith("{") or p in ("api", "latest", "rest"):
            continue
        meaningful.append(p)

    # Use the last 1-2 meaningful segments for context
    if len(meaningful) >= 2:
        suffix = "_".join(meaningful[-2:])
    elif meaningful:
        suffix = meaningful[-1]
    else:
        suffix = ""

    return _camel_to_snake(suffix).replace("-", "_")


def _build_const_name_map(
    ops: list[OperationInfo],
    names: dict[str, str],
) -> dict[str, str]:
    """Build globally unique endpoint constant name map.

    Returns key (resource::op_id::method::path) → unique UPPER_SNAKE constant name.
    """
    const_name_map: dict[str, str] = {}
    used: set[str] = set()
    for op in ops:
        key = _op_key(op)
        method_name = names.get(key, _operation_id_to_method(op.op_id))
        base_const = method_name.upper()

        if base_const not in used:
            const_name_map[key] = base_const
            used.add(base_const)
        else:
            suffix = _derive_suffix(op.path, op.path_params)
            candidate = f"{base_const}_{suffix}".upper() if suffix else base_const
            counter = 2
            while candidate in used:
                candidate = f"{base_const}_{counter}"
                counter += 1
            const_name_map[key] = candidate
            used.add(candidate)
    return const_name_map


# ---------------------------------------------------------------------------
# Code generation: endpoints.py
# ---------------------------------------------------------------------------


def generate_endpoints(
    ops: list[OperationInfo],
    names: dict[str, str],
    const_name_map: dict[str, str],
    config: ProductConfig,
) -> str:
    """Generate the full endpoints.py content."""
    lines = [
        f'"""{config.display_name} REST API endpoint definitions.',
        "",
        "Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from atlassian.core.endpoint import Endpoint",
        "",
    ]

    # Group by resource class
    by_resource: dict[str, list[OperationInfo]] = defaultdict(list)
    for op in ops:
        by_resource[op.resource_class].append(op)

    for resource in config.resource_order:
        if resource not in by_resource:
            continue
        resource_ops = by_resource[resource]

        # Section header
        section_name = resource.replace("Async", "").replace("Resource", "")
        lines.append(f"# --- {section_name} ---")
        lines.append("")

        for op in sorted(resource_ops, key=lambda o: (o.path, o.method)):
            key = _op_key(op)
            const_name = const_name_map[key]

            summary = op.summary.replace('"', '\\"') if op.summary else ""
            prefix = f'{const_name} = Endpoint("{op.method}", "{op.path}", "'
            suffix = '")'
            max_summary_len = LINE_LENGTH - len(prefix) - len(suffix)
            summary = _truncate_with_ellipsis(summary, max_summary_len)
            one_line = f'{const_name} = Endpoint("{op.method}", "{op.path}", "{summary}")'
            if len(one_line) <= LINE_LENGTH:
                lines.append(one_line)
            else:
                lines.append(f"{const_name} = Endpoint(")
                lines.append(f'    "{op.method}",')
                lines.append(f'    "{op.path}",')
                lines.append(f'    "{summary}",')
                lines.append(")")

        lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Code generation: async_resources.py
# ---------------------------------------------------------------------------


def _build_method_signature(
    op: OperationInfo,
    method_name: str,
    display_name: str = "Bitbucket Data Center",
    product_name: str | None = None,
) -> tuple[list[str], str, list[str]]:
    """Build the method signature params, return type, and docstring lines.

    Returns (param_list, return_annotation, docstring_lines).
    """
    # Build parameter list
    params: list[str] = ["self"]

    # Path params (required, positional)
    for pp in op.path_params:
        # Skip pagination params that appear in path (unusual but possible)
        if pp.name in ("start", "limit"):
            continue
        params.append(f"{pp.python_name}: {pp.param_type}")

    # Request body
    if op.request_body_model:
        params.append(f"body: {op.request_body_model}")

    # Keyword-only separator
    has_kwargs = bool(op.query_params) or op.is_paged
    if has_kwargs:
        params.append("*")

    # Query params (optional kwargs) — skip start/limit for paged
    for qp in op.query_params:
        if op.is_paged and qp.name in ("start", "limit", "startAt", "maxResults"):
            continue
        default = qp.default if qp.default is not None else "None"
        if not qp.required:
            params.append(f"{qp.python_name}: {qp.param_type} | None = {default}")
        else:
            params.append(
                f"{qp.python_name}: {qp.param_type} = {default}" if qp.default else f"{qp.python_name}: {qp.param_type}"
            )

    # For paged endpoints, add start/limit as explicit kwargs
    if op.is_paged:
        if product_name == "jira":
            params.append("start_at: int = 0")
            params.append("max_results: int = 50")
        else:
            params.append("start: int = 0")
            params.append("limit: int = 25")

    # Return type
    if op.is_paged and op.response_model:
        return_annotation = f"AsyncPageIterator[{op.response_model}]"
    elif op.response_model:
        return_annotation = op.response_model
    else:
        # Check if 204 (no content) response exists
        return_annotation = "None"

    # Docstring
    doc_lines: list[str] = []
    summary = op.summary or f"{op.method} {op.path}"
    max_doc_summary_len = LINE_LENGTH - 14
    summary = _truncate_with_ellipsis(summary, max_doc_summary_len)
    doc_lines.append(summary)
    if op.is_deprecated:
        doc_lines.append("")
        doc_lines.append(".. deprecated::")
        doc_lines.append(f"    This endpoint is deprecated in the {display_name} API.")

    return params, return_annotation, doc_lines


def _format_method_def(
    method_name: str,
    params: list[str],
    return_annotation: str,
    *,
    is_async: bool,
    indent: str = "    ",
) -> list[str]:
    """Format a method definition and wrap only when needed."""
    keyword = "async def" if is_async else "def"
    signature = ", ".join(params)
    one_liner = f"{indent}{keyword} {method_name}({signature}) -> {return_annotation}:"
    if len(one_liner) <= LINE_LENGTH:
        return [one_liner]

    lines = [f"{indent}{keyword} {method_name}("]
    for param in params:
        lines.append(f"{indent}    {param},")
    lines.append(f"{indent}) -> {return_annotation}:")
    return lines


def _format_call(call_expr: str, indent: str = "        ") -> list[str]:
    """Format a call expression and wrap only when needed."""
    full_line = f"{indent}{call_expr}"
    if len(full_line) <= LINE_LENGTH or "(" not in call_expr or not call_expr.endswith(")"):
        return [full_line]

    paren_idx = call_expr.index("(")
    func_part = call_expr[: paren_idx + 1]
    args_part = call_expr[paren_idx + 1 : -1]
    args = [arg.strip() for arg in args_part.split(",") if arg.strip()]

    lines = [f"{indent}{func_part}"]
    for arg in args:
        lines.append(f"{indent}    {arg},")
    lines.append(f"{indent})")
    return lines


# Indent for method body lines (8 spaces = class indent + method indent)
_BODY_INDENT = "        "


def _build_method_body(op: OperationInfo, const_name: str, config: ProductConfig) -> list[str]:
    """Generate method body lines WITH 8-space indent already included."""
    # Build path with format substitution
    path_format_args: dict[str, str] = {}
    for pp in op.path_params:
        path_format_args[pp.name] = pp.python_name

    path_expr = f"{const_name}.path"
    for key, value in path_format_args.items():
        path_expr = f'{path_expr}.replace("{{{key}}}", str({value}))'

    # Build query params dict
    query_params_entries: list[str] = []
    for qp in op.query_params:
        if op.is_paged and qp.name in ("start", "limit", "startAt", "maxResults"):
            continue
        query_params_entries.append(f'"{qp.name}": {qp.python_name}')

    if op.is_paged:
        if config.name == "jira":
            items_field = op.paged_items_field or "values"
            if op.method == "GET":
                kwargs_parts: list[str] = [path_expr]
                if query_params_entries:
                    kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
                kwargs_parts.append(f"model={op.response_model}")
                kwargs_parts.append(f'items_field="{items_field}"')
                kwargs_parts.append("start_at=start_at")
                kwargs_parts.append("max_results=max_results")
                call_expr = f"return self._get_paged({', '.join(kwargs_parts)})"
                return _format_call(call_expr, indent=_BODY_INDENT)

            kwargs_parts = [f'"{op.method}"', path_expr]
            if query_params_entries:
                kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
            if op.request_body_model:
                kwargs_parts.append("json=body.model_dump(by_alias=True, exclude_none=True)")
            kwargs_parts.append(f"model={op.response_model}")
            kwargs_parts.append(f'items_field="{items_field}"')
            kwargs_parts.append("start_at=start_at")
            kwargs_parts.append("max_results=max_results")
            call_expr = f"return self._request_paged({', '.join(kwargs_parts)})"
            return _format_call(call_expr, indent=_BODY_INDENT)

        if op.method == "GET":
            kwargs_parts: list[str] = [path_expr]
            if query_params_entries:
                kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
            kwargs_parts.append(f"model={op.response_model}")
            kwargs_parts.append("start=start")
            kwargs_parts.append("limit=limit")
            call_expr = f"return self._get_paged({', '.join(kwargs_parts)})"
            return _format_call(call_expr, indent=_BODY_INDENT)

        if config.name == "confluence":
            kwargs_parts = [f'"{op.method}"', path_expr]
            if query_params_entries:
                kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
            if op.request_body_model:
                kwargs_parts.append("json=body.model_dump(by_alias=True, exclude_none=True)")
            kwargs_parts.append(f"model={op.response_model}")
            kwargs_parts.append("start=start")
            kwargs_parts.append("limit=limit")
            call_expr = f"return self._request_paged({', '.join(kwargs_parts)})"
            return _format_call(call_expr, indent=_BODY_INDENT)

        kwargs_parts = [path_expr]
        if query_params_entries:
            kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
        kwargs_parts.append(f"model={op.response_model}")
        kwargs_parts.append("start=start")
        kwargs_parts.append("limit=limit")
        call_expr = f"return self._get_paged({', '.join(kwargs_parts)})"
        return _format_call(call_expr, indent=_BODY_INDENT)
    elif op.method == "GET":
        kwargs_parts: list[str] = [path_expr]
        if query_params_entries:
            kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
        if op.response_model:
            kwargs_parts.append(f"model={op.response_model}")
        call_expr = f"return await self._get({', '.join(kwargs_parts)})"
        return _format_call(call_expr, indent=_BODY_INDENT)
    elif op.method == "DELETE":
        kwargs_parts: list[str] = [path_expr]
        if query_params_entries:
            kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
        if op.response_model:
            kwargs_parts.append(f"model={op.response_model}")
        call_expr = f"return await self._delete({', '.join(kwargs_parts)})"
        return _format_call(call_expr, indent=_BODY_INDENT)
    elif op.method in ("POST", "PUT", "PATCH"):
        helper = {"POST": "_post", "PUT": "_put", "PATCH": "_patch"}[op.method]
        kwargs_parts: list[str] = [path_expr]
        if query_params_entries:
            kwargs_parts.append(f"params={{{', '.join(query_params_entries)}}}")
        if op.request_body_model:
            kwargs_parts.append("json=body.model_dump(by_alias=True, exclude_none=True)")
        if op.response_model:
            kwargs_parts.append(f"model={op.response_model}")
        call_expr = f"return await self.{helper}({', '.join(kwargs_parts)})"
        return _format_call(call_expr, indent=_BODY_INDENT)
    else:
        return [f"{_BODY_INDENT}raise NotImplementedError"]


def generate_resources(
    ops: list[OperationInfo],
    names: dict[str, str],
    const_name_map: dict[str, str],
    config: ProductConfig,
) -> str:
    """Generate the full async_resources.py content."""
    # Group ops by resource class and keep only resources we actually emit.
    by_resource: dict[str, list[OperationInfo]] = defaultdict(list)
    for op in ops:
        by_resource[op.resource_class].append(op)

    emitted_ops: list[OperationInfo] = []
    for resource in config.resource_order:
        emitted_ops.extend(by_resource.get(resource, []))

    # Collect all model types referenced
    model_refs: set[str] = set()
    needs_any = False
    for op in emitted_ops:
        if op.response_model:
            model_refs.add(op.response_model)
        if op.request_body_model:
            model_refs.add(op.request_body_model)
        for pp in op.path_params:
            model_refs.update(_extract_model_refs_from_type(pp.param_type))
        for qp in op.query_params:
            model_refs.update(_extract_model_refs_from_type(qp.param_type))
        # Check if Any is needed (query params with dict type, or untyped response)
        for qp in op.query_params:
            if "Any" in qp.param_type:
                needs_any = True
        if not op.response_model and not op.is_paged:
            needs_any = True

    lines: list[str] = [
        f'"""{config.display_name} resource classes.',
        "",
        "Auto-generated scaffold from the OpenAPI spec. Safe to hand-edit.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
    ]

    # Typing imports
    typing_imports = []
    if needs_any:
        typing_imports.append("Any")
    if typing_imports:
        lines.append(f"from typing import {', '.join(sorted(typing_imports))}")
        lines.append("")

    # Core imports
    lines.append("from atlassian.core.pagination import AsyncPageIterator")
    lines.append(config.base_resource_import)
    lines.append("")

    # Endpoint imports
    lines.append("from .endpoints import (")
    # Collect all endpoint constants used
    endpoint_consts: set[str] = set()
    for op in emitted_ops:
        key = _op_key(op)
        endpoint_consts.add(const_name_map[key])
    for const in sorted(endpoint_consts):
        lines.append(f"    {const},")
    lines.append(")")
    lines.append("")

    # Model imports
    if model_refs:
        lines.append("from .models import (")
        for model in sorted(model_refs):
            lines.append(f"    {model},")
        lines.append(")")
        lines.append("")

    for resource in config.resource_order:
        if resource not in by_resource:
            continue
        resource_ops = by_resource[resource]
        lines.append("")
        lines.append(f"class {resource}({config.base_resource_class}):")

        for op in sorted(resource_ops, key=lambda o: (o.path, o.method)):
            key = _op_key(op)
            method_name = names.get(key, _operation_id_to_method(op.op_id))
            const_name = const_name_map[key]

            param_list, return_annotation, doc_lines = _build_method_signature(
                op,
                method_name,
                config.display_name,
                config.name,
            )
            body_lines = _build_method_body(op, const_name, config)

            lines.append("")
            # For paged endpoints, _get_paged is sync (returns iterator), no async def
            is_async = not op.is_paged
            def_lines = _format_method_def(
                method_name,
                param_list,
                return_annotation,
                is_async=is_async,
                indent="    ",
            )
            lines.extend(def_lines)

            # Docstring
            if doc_lines:
                first_line = f'        """{doc_lines[0]}"""'
                if len(doc_lines) == 1 and len(first_line) <= LINE_LENGTH:
                    lines.append(first_line)
                else:
                    lines.append(f'        """{doc_lines[0]}')
                    for dl in doc_lines[1:]:
                        lines.append(f"        {dl}")
                    lines.append('        """')

            # Body (lines already include 8-space indent)
            lines.extend(body_lines)

        lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate resource classes from OpenAPI spec.",
    )
    parser.add_argument("product", choices=["bitbucket", "confluence", "jira"])
    args = parser.parse_args()

    config = PRODUCT_CONFIGS[args.product]
    spec = json.loads(config.spec_path.read_text(encoding="utf-8"))
    ops = parse_spec(spec, config)
    names = _disambiguate_method_names(ops)
    const_name_map = _build_const_name_map(ops, names)

    print(f"[{config.display_name}] Parsed {len(ops)} operations")
    print(f"  Paged: {sum(1 for o in ops if o.is_paged)}")
    print(f"  With response model: {sum(1 for o in ops if o.response_model)}")
    print(f"  With request body model: {sum(1 for o in ops if o.request_body_model)}")

    # Generate endpoints.py
    endpoints_code = generate_endpoints(ops, names, const_name_map, config)
    config.endpoints_out.write_text(endpoints_code, encoding="utf-8")
    print(f"\nWrote {config.endpoints_out}")

    # Generate async_resources.py
    resources_code = generate_resources(ops, names, const_name_map, config)
    config.resources_out.write_text(resources_code, encoding="utf-8")
    print(f"Wrote {config.resources_out}")

    # Resource summary
    by_resource: dict[str, int] = defaultdict(int)
    for op in ops:
        by_resource[op.resource_class] += 1
    print("\nMethods per resource:")
    for resource, count in sorted(by_resource.items(), key=lambda x: -x[1]):
        print(f"  {resource}: {count}")


if __name__ == "__main__":
    main()
