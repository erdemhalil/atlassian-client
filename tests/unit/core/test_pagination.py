from __future__ import annotations

import pytest

from atlassian.core.pagination import AsyncPageIterator


@pytest.mark.asyncio
async def test_async_page_iterator_iterates_all_values() -> None:
    pages: dict[int, tuple[list[int], int | None]] = {
        0: ([1, 2], 2),
        2: ([3], None),
    }

    async def fetch_page(start: int) -> tuple[list[int], int | None]:
        return pages[start]

    iterator = AsyncPageIterator(fetch_page)

    collected: list[int] = []
    async for item in iterator:
        collected.append(item)

    assert collected == [1, 2, 3]


@pytest.mark.asyncio
async def test_async_page_iterator_handles_empty_last_page() -> None:
    async def fetch_page(_: int) -> tuple[list[int], int | None]:
        return [], None

    iterator = AsyncPageIterator(fetch_page)

    collected = [item async for item in iterator]
    assert collected == []
