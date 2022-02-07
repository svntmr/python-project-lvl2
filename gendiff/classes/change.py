from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


class ChangeType(Enum):
    no_change = "no_change"
    missing = "missing"
    changed = "changed"
    added = "added"


class Change(BaseModel):
    key: str
    value: Any
    changed_value: Optional[Any] = None
    type: ChangeType
