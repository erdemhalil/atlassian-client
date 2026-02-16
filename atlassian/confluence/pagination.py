from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ConfluencePageLinks(BaseModel):
    next: str | None = Field(default=None, alias="next")
    prev: str | None = Field(default=None, alias="prev")
    base: str | None = None
    self_link: str | None = Field(default=None, alias="self")
    context: str | None = None

    model_config = ConfigDict(populate_by_name=True)


class ConfluencePage(BaseModel, Generic[T]):
    results: list[T] = Field(default_factory=list)
    start: int = 0
    limit: int = 25
    size: int = 0
    total_count: int | None = Field(default=None, alias="totalCount")
    links: ConfluencePageLinks | None = Field(default=None, alias="_links")

    model_config = ConfigDict(populate_by_name=True)

    @property
    def has_next(self) -> bool:
        return self.links is not None and self.links.next is not None
