"""Core primitives shared by Atlassian product clients."""

from .async_client import AsyncBaseClient
from .auth import AuthBase, BasicAuth, TokenAuth
from .client import BaseClient
from .endpoint import Endpoint
from .exceptions import (
    AtlassianError,
    AuthenticationError,
    ConflictError,
    ForbiddenError,
    HttpError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_status,
)
from .pagination import AsyncPageIterator, Page, PageIterator
from .resource import AsyncResource, Resource

__all__ = [
    "AsyncBaseClient",
    "BaseClient",
    "AuthBase",
    "BasicAuth",
    "TokenAuth",
    "AtlassianError",
    "HttpError",
    "AuthenticationError",
    "ForbiddenError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "ValidationError",
    "raise_for_status",
    "Endpoint",
    "Page",
    "AsyncPageIterator",
    "PageIterator",
    "AsyncResource",
    "Resource",
]
