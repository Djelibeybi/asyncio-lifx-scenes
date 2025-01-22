"""LIFX Scene data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LifxScene:
    """Class to represent a LIFX scene."""

    uuid: str
    name: str
    account: dict[str, str]
    states: list[dict[str, Any]]
    created_at: int
    updated_at: int
