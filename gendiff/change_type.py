from enum import Enum, auto


class ChangeType(Enum):
    ADDED = auto()
    ADDED_NESTED = auto()
    CHANGED = auto()
    CHANGED_NESTED = auto()
    NESTED = auto()
    NO_CHANGE = auto()
    MISSING = auto()
    MISSING_NESTED = auto()
