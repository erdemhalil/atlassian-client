from __future__ import annotations

from atlassian.core.endpoint import Endpoint

PROJECTS_LIST = Endpoint(
    method="GET",
    path="/rest/api/latest/projects",
    description="List projects",
)
