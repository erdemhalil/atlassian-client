"""Core primitives shared by Atlassian product clients."""

from .async_client import AsyncBaseClient
from .auth import AuthBase, BasicAuth, TokenAuth
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
from .pagination import AsyncPageIterator, Page
from .resource import AsyncResource

__all__ = [
    "AsyncBaseClient",
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
    "AsyncResource",
]
