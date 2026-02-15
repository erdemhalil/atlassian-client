from __future__ import annotations

from atlassian.core.endpoint import Endpoint


def test_endpoint_dataclass_fields() -> None:
    endpoint = Endpoint(method="GET", path="/rest/api/1.0/projects", description="List projects")

    assert endpoint.method == "GET"
    assert endpoint.path == "/rest/api/1.0/projects"
    assert endpoint.description == "List projects"
