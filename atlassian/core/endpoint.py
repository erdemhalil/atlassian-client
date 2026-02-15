from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Endpoint:
    method: str
    path: str
    description: str = ""
