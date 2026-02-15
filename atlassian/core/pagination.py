from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class Page(BaseModel, Generic[T]):
    values: list[T] = Field(default_factory=list)
    start: int = 0
    limit: int = 25
    size: int = 0
    is_last_page: bool = Field(default=False, alias="isLastPage")
    next_page_start: int | None = Field(default=None, alias="nextPageStart")

    model_config = ConfigDict(populate_by_name=True)


class AsyncPageIterator(Generic[T]):
    def __init__(
        self,
        fetch_page: Callable[[int], Awaitable[Page[T]]],
        *,
        start: int = 0,
    ) -> None:
        self._fetch_page = fetch_page
        self._next_start = start
        self._current_items: list[T] = []
        self._index = 0
        self._exhausted = False

    def __aiter__(self) -> AsyncPageIterator[T]:
        return self

    async def __anext__(self) -> T:
        while self._index >= len(self._current_items):
            if self._exhausted:
                raise StopAsyncIteration

            page = await self._fetch_page(self._next_start)
            self._current_items = page.values
            self._index = 0

            if page.is_last_page:
                self._exhausted = True
            elif page.next_page_start is not None:
                self._next_start = page.next_page_start
            else:
                self._next_start = page.start + page.limit

            if not self._current_items and self._exhausted:
                raise StopAsyncIteration
            if not self._current_items:
                continue

        item = self._current_items[self._index]
        self._index += 1
        return item
