from __future__ import annotations

from enum import Enum, auto
from typing import Any, List, Optional

from pydantic import BaseModel


class ChangeType(Enum):
    NO_CHANGE = auto()
    MISSING = auto()
    CHANGED = auto()
    ADDED = auto()


class Change(BaseModel):
    key: str
    type: ChangeType
    value: Any
    changed_value: Optional[Any] = None
    nested_changes: Optional[List[Change]] = None

    @property
    def has_nested_changes(self) -> bool:
        return bool(self.nested_changes)
