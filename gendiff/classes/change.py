from enum import Enum, auto
from typing import Any, Optional

from pydantic import BaseModel


class ChangeType(Enum):
    NO_CHANGE = auto()
    MISSING = auto()
    CHANGED = auto()
    ADDED = auto()


class Change(BaseModel):
    key: str
    value: Any
    changed_value: Optional[Any] = None
    type: ChangeType
