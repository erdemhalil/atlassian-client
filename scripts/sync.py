"""Sync Atlassian OpenAPI specs and generate Pydantic models."""

import argparse
import json
import sys
from enum import Enum
from pathlib import Path

import httpx
from datamodel_code_generator import (
    DataModelType,
    Formatter,
    GenerateConfig,
    InputFileType,
    OpenAPIScope,
    PythonVersion,
    TargetPydanticVersion,
    generate,
)


class Product(str, Enum):
    BITBUCKET = "bitbucket"
    CONFLUENCE = "confluence"
    JIRA = "jira"


BITBUCKET_OPENAPI_URL = "https://dac-static.atlassian.com/server/bitbucket/9.4.swagger.v3.json"
CONFLUENCE_OPENAPI_URL = "https://dac-static.atlassian.com/server/confluence/9.3.1.swagger.v3.json"
JIRA_OPENAPI_URL = "https://dac-static.atlassian.com/server/jira/platform/jira_software_dc_10003_swagger.v3.json"

SPEC_MAP = {
    Product.BITBUCKET: BITBUCKET_OPENAPI_URL,
    Product.CONFLUENCE: CONFLUENCE_OPENAPI_URL,
    Product.JIRA: JIRA_OPENAPI_URL,
}

HTTP_TIMEOUT_SECONDS = 30.0


def _get_project_root() -> Path:
    """Return repository root directory."""
    return Path(__file__).parent.parent


def _save_openapi_spec(product: Product) -> Path:
    """Fetch and persist a product OpenAPI document in formatted JSON form."""
    url = SPEC_MAP[product]
    if not url:
        raise ValueError(f"OpenAPI URL is not configured for '{product.value}'.")
    response = httpx.get(url, timeout=HTTP_TIMEOUT_SECONDS)
    response.raise_for_status()

    try:
        payload = response.json()
    except ValueError as exc:
        raise ValueError(f"Downloaded OpenAPI for '{product.value}' is not valid JSON.") from exc

    output_path = _get_project_root() / f"specs/{product.value}/openapi.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    formatted_json = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    output_path.write_text(formatted_json, encoding="utf-8")
    return output_path


def _get_config(product: Product) -> GenerateConfig:
    """Build datamodel-code-generator configuration for a target product."""
    output_path = _get_project_root() / f"atlassian/{product.value}/models.py"
    return GenerateConfig(
        input_file_type=InputFileType.OpenAPI,
        output=output_path,
        output_model_type=DataModelType.PydanticV2BaseModel,
        target_pydantic_version=TargetPydanticVersion.V2,
        target_python_version=PythonVersion.PY_310,
        field_constraints=True,
        snake_case_field=True,
        formatters=[Formatter.RUFF_FORMAT, Formatter.RUFF_CHECK],
        capitalise_enum_members=True,
        include_path_parameters=True,
        use_field_description=True,
        use_attribute_docstrings=True,
        use_operation_id_as_name=True,
        use_inline_field_description=True,
        use_schema_description=True,
        openapi_scopes=[OpenAPIScope.Schemas, OpenAPIScope.Parameters, OpenAPIScope.Paths],
    )


def _parse_product(argv: list[str]) -> Product:
    """Parse target product from CLI arguments."""
    parser = argparse.ArgumentParser(description="Sync OpenAPI spec and generate models")
    parser.add_argument(
        "product",
        choices=[product.value for product in Product],
        help="Product to sync: bitbucket, confluence, jira",
    )
    args = parser.parse_args(argv)
    return Product(args.product)


if __name__ == "__main__":
    product = _parse_product(sys.argv[1:])
    config = _get_config(product)
    spec_path = _save_openapi_spec(product)
    generate(spec_path, config=config)
