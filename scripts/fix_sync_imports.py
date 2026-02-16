"""Post-process unasyncd output to fix import paths and names.

unasyncd correctly renames identifiers (AsyncFoo → Foo) in function/class bodies
but does NOT rewrite import module paths or imported names. This script applies
those fixes after unasyncd runs.

Usage:
    uv run unasyncd && uv run python scripts/fix_sync_imports.py
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Name replacements that unasyncd misses in import statements
NAME_REPLACEMENTS: dict[str, str] = {
    "AsyncBaseClient": "BaseClient",
    "AsyncResource": "Resource",
    "AsyncJiraResource": "JiraResource",
    "ConfluenceAsyncResource": "ConfluenceResource",
    "AsyncPageIterator": "PageIterator",
    "AsyncProjectsResource": "ProjectsResource",
    "AsyncRepositoriesResource": "RepositoriesResource",
    "AsyncPullRequestsResource": "PullRequestsResource",
    "AsyncAuthenticationResource": "AuthenticationResource",
    "AsyncBuildsResource": "BuildsResource",
    "AsyncPermissionsResource": "PermissionsResource",
    "AsyncSecurityResource": "SecurityResource",
    "AsyncAdminResource": "AdminResource",
    "AsyncDashboardResource": "DashboardResource",
    "AsyncMirroringResource": "MirroringResource",
    "AsyncJiraIntegrationResource": "JiraIntegrationResource",
    "AsyncMarkupResource": "MarkupResource",
    "AsyncContentResource": "ContentResource",
    "AsyncContentLabelsResource": "ContentLabelsResource",
    "AsyncContentPropertyResource": "ContentPropertyResource",
    "AsyncContentRestrictionsResource": "ContentRestrictionsResource",
    "AsyncContentDescendantResource": "ContentDescendantResource",
    "AsyncChildContentResource": "ChildContentResource",
    "AsyncAttachmentsResource": "AttachmentsResource",
    "AsyncSpaceResource": "SpaceResource",
    "AsyncSpaceLabelResource": "SpaceLabelResource",
    "AsyncSpacePermissionsResource": "SpacePermissionsResource",
    "AsyncSpacePropertyResource": "SpacePropertyResource",
    "AsyncSpaceColorSchemeResource": "SpaceColorSchemeResource",
    "AsyncGroupResource": "GroupResource",
    "AsyncUserResource": "UserResource",
    "AsyncUserWatchResource": "UserWatchResource",
    "AsyncSearchResource": "SearchResource",
    "AsyncLabelResource": "LabelResource",
    "AsyncLongTaskResource": "LongTaskResource",
    "AsyncBackupRestoreResource": "BackupRestoreResource",
    "AsyncWebhooksResource": "WebhooksResource",
    "AsyncGlobalPermissionsResource": "GlobalPermissionsResource",
    "AsyncGlobalColorSchemeResource": "GlobalColorSchemeResource",
    "AsyncCategoryResource": "CategoryResource",
    "AsyncAccessModeResource": "AccessModeResource",
    "AsyncServerInfoResource": "ServerInfoResource",
    "AsyncAgileResource": "AgileResource",
    "AsyncIssueResource": "IssueResource",
    "AsyncProjectResource": "ProjectResource",
    "AsyncIssueMetaResource": "IssueMetaResource",
    "AsyncPermissionSecurityResource": "PermissionSecurityResource",
    "AsyncAvatarResource": "AvatarResource",
    "AsyncDashboardFilterResource": "DashboardFilterResource",
    "AsyncSystemResource": "SystemResource",
    "AsyncOperationsResource": "OperationsResource",
    "AsyncAuthResource": "AuthResource",
    "AsyncJiraMiscResource": "JiraMiscResource",
    "AsyncBitBucketClient": "BitBucketClient",
    "AsyncConfluenceClient": "ConfluenceClient",
    "AsyncJiraClient": "JiraClient",
}

# (file, old_import_text, new_import_text) tuples — simple string replacements
IMPORT_FIXES: list[tuple[Path, str, str]] = [
    # core/client.py: transport type annotation
    (
        PROJECT_ROOT / "atlassian" / "core" / "client.py",
        "httpx.AsyncBaseTransport",
        "httpx.BaseTransport",
    ),
    # bitbucket/client.py: fix module paths
    (
        PROJECT_ROOT / "atlassian" / "bitbucket" / "client.py",
        "from atlassian.core.async_client import",
        "from atlassian.core.client import",
    ),
    (
        PROJECT_ROOT / "atlassian" / "bitbucket" / "client.py",
        "from .async_resources import",
        "from .resources import",
    ),
    # confluence/client.py: fix module paths
    (
        PROJECT_ROOT / "atlassian" / "confluence" / "client.py",
        "from atlassian.core.async_client import",
        "from atlassian.core.client import",
    ),
    (
        PROJECT_ROOT / "atlassian" / "confluence" / "client.py",
        "from .async_resources import",
        "from .resources import",
    ),
    # jira/client.py: fix module paths
    (
        PROJECT_ROOT / "atlassian" / "jira" / "client.py",
        "from atlassian.core.async_client import",
        "from atlassian.core.client import",
    ),
    (
        PROJECT_ROOT / "atlassian" / "jira" / "client.py",
        "from .async_resources import",
        "from .resources import",
    ),
]

# Files that need Async→Sync name fixes in import statements
SYNC_FILES: list[Path] = [
    PROJECT_ROOT / "atlassian" / "core" / "client.py",
    PROJECT_ROOT / "atlassian" / "bitbucket" / "client.py",
    PROJECT_ROOT / "atlassian" / "bitbucket" / "resources.py",
    PROJECT_ROOT / "atlassian" / "confluence" / "client.py",
    PROJECT_ROOT / "atlassian" / "confluence" / "resources.py",
    PROJECT_ROOT / "atlassian" / "jira" / "client.py",
    PROJECT_ROOT / "atlassian" / "jira" / "resources.py",
]


def fix_import_paths() -> None:
    """Apply import path fixes to unasyncd-generated sync files."""
    for filepath, old, new in IMPORT_FIXES:
        if not filepath.exists():
            print(f"  SKIP {filepath.name} (not found)")
            continue

        content = filepath.read_text(encoding="utf-8")
        if old not in content:
            print(f"  SKIP {filepath.name}: '{old[:50]}...' not found")
            continue

        if old == new:
            continue  # skip no-op path fixes (names fixed in next pass)

        content = content.replace(old, new)
        filepath.write_text(content, encoding="utf-8")
        print(f"  FIXED {filepath.name}: {old[:40]}... → {new[:40]}...")


def fix_import_names() -> None:
    """Replace Async* names in import statements of generated sync files."""
    for filepath in SYNC_FILES:
        if not filepath.exists():
            continue

        content = filepath.read_text(encoding="utf-8")
        original = content

        for old_name, new_name in NAME_REPLACEMENTS.items():
            content = content.replace(old_name, new_name)

        if content != original:
            filepath.write_text(content, encoding="utf-8")
            print(f"  FIXED {filepath.name}: replaced Async* names in imports")


def fix_aclose() -> None:
    """Fix aclose → close in sync BaseClient."""
    filepath = PROJECT_ROOT / "atlassian" / "core" / "client.py"
    if not filepath.exists():
        return
    content = filepath.read_text(encoding="utf-8")
    if "aclose" in content:
        content = content.replace("aclose", "close")
        filepath.write_text(content, encoding="utf-8")
        print(f"  FIXED {filepath.name}: aclose → close")


def remove_asyncio_import() -> None:
    """Remove leftover 'import asyncio' from sync BaseClient."""
    filepath = PROJECT_ROOT / "atlassian" / "core" / "client.py"
    if not filepath.exists():
        return
    content = filepath.read_text(encoding="utf-8")
    if "import asyncio\n" in content:
        content = content.replace("import asyncio\n", "")
        filepath.write_text(content, encoding="utf-8")
        print(f"  FIXED {filepath.name}: removed 'import asyncio'")


def run_ruff() -> None:
    """Run ruff fix + format on generated sync files."""
    import subprocess

    targets = [str(p) for p in SYNC_FILES if p.exists()]
    if not targets:
        return
    subprocess.run(["uv", "run", "ruff", "check", "--fix", *targets], check=False)
    subprocess.run(["uv", "run", "ruff", "format", *targets], check=False)
    print("  Ran ruff check --fix + format on sync files")


def main() -> None:
    print("Fixing unasyncd-generated sync files...")
    fix_import_paths()
    fix_import_names()
    fix_aclose()
    remove_asyncio_import()
    run_ruff()
    print("Done.")


if __name__ == "__main__":
    main()
