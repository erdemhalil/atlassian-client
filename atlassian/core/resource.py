from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel

from .async_client import AsyncBaseClient


class AsyncResource:
    def __init__(self, client: AsyncBaseClient) -> None:
        self._client = client

    async def _get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request("GET", path, params=params, headers=headers)
        return self._deserialize(response, model)

    async def _post(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request(
            "POST",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    async def _put(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request(
            "PUT",
            path,
            params=params,
            json=json,
            data=data,
            headers=headers,
        )
        return self._deserialize(response, model)

    async def _delete(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        model: type[BaseModel] | None = None,
    ) -> Any:
        response = await self._client._request("DELETE", path, params=params, headers=headers)
        return self._deserialize(response, model)

    @staticmethod
    def _deserialize(response: Any, model: type[BaseModel] | None) -> Any:
        if model is None:
            return response

        payload = response.json()
        return model.model_validate(payload)
