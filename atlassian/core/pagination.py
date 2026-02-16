from __future__ import annotations

from collections.abc import Awaitable, Callable, Iterator
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
        fetch_page: Callable[[int], Awaitable[tuple[list[T], int | None]]],
        *,
        start: int = 0,
    ) -> None:
        self._fetch_page = fetch_page
        self._next_start: int | None = start
        self._current_items: list[T] = []
        self._index = 0

    def __aiter__(self) -> AsyncPageIterator[T]:
        return self

    async def __anext__(self) -> T:
        while self._index >= len(self._current_items):
            if self._next_start is None:
                raise StopAsyncIteration

            items, next_start = await self._fetch_page(self._next_start)
            self._current_items = items
            self._index = 0
            self._next_start = next_start

            if not self._current_items and self._next_start is None:
                raise StopAsyncIteration
            if not self._current_items:
                continue

        item = self._current_items[self._index]
        self._index += 1
        return item


class PageIterator(Generic[T]):
    """Synchronous page iterator for the sync client."""

    def __init__(
        self,
        fetch_page: Callable[[int], tuple[list[T], int | None]],
        *,
        start: int = 0,
    ) -> None:
        self._fetch_page = fetch_page
        self._next_start: int | None = start
        self._current_items: list[T] = []
        self._index = 0

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        while self._index >= len(self._current_items):
            if self._next_start is None:
                raise StopIteration

            items, next_start = self._fetch_page(self._next_start)
            self._current_items = items
            self._index = 0
            self._next_start = next_start

            if not self._current_items and self._next_start is None:
                raise StopIteration
            if not self._current_items:
                continue

        item = self._current_items[self._index]
        self._index += 1
        return item
