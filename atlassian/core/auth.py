from __future__ import annotations

import base64
from abc import ABC, abstractmethod

import httpx


class AuthBase(ABC):
    @abstractmethod
    async def apply(self, request: httpx.Request) -> httpx.Request:
        raise NotImplementedError


class BasicAuth(AuthBase):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    async def apply(self, request: httpx.Request) -> httpx.Request:
        auth_value = f"{self.username}:{self.password}".encode()
        encoded = base64.b64encode(auth_value).decode("ascii")
        request.headers["Authorization"] = f"Basic {encoded}"
        return request


class TokenAuth(AuthBase):
    def __init__(self, token: str) -> None:
        self.token = token

    async def apply(self, request: httpx.Request) -> httpx.Request:
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request
