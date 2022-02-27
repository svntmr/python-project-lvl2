from enum import Enum


class ChangeType(Enum):
    ADDED = "added"
    ADDED_NESTED = "added_nested"
    CHANGED = "changed"
    CHANGED_NESTED = "changed_nested"
    NESTED = "nested"
    NO_CHANGE = "no_change"
    MISSING = "missing"
    MISSING_NESTED = "missing_nested"
