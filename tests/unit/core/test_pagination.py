from __future__ import annotations

import pytest

from atlassian.core.pagination import AsyncPageIterator, Page


@pytest.mark.asyncio
async def test_async_page_iterator_iterates_all_values() -> None:
    pages = {
        0: Page[int](
            values=[1, 2],
            start=0,
            limit=2,
            size=2,
            is_last_page=False,
            next_page_start=2,
        ),
        2: Page[int](values=[3], start=2, limit=2, size=1, is_last_page=True),
    }

    async def fetch_page(start: int) -> Page[int]:
        return pages[start]

    iterator = AsyncPageIterator(fetch_page)

    collected: list[int] = []
    async for item in iterator:
        collected.append(item)

    assert collected == [1, 2, 3]


@pytest.mark.asyncio
async def test_async_page_iterator_handles_empty_last_page() -> None:
    async def fetch_page(_: int) -> Page[int]:
        return Page[int](values=[], start=0, limit=25, size=0, is_last_page=True)

    iterator = AsyncPageIterator(fetch_page)

    collected = [item async for item in iterator]
    assert collected == []
