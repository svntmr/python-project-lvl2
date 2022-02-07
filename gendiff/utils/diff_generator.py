from json import dumps
from typing import List, Any, Tuple

from gendiff.classes.change import Change, ChangeType


def make_diff_string(changes: List[Change]) -> str:
    diff_start = "{\n  "
    diff_end = "\n}\n"
    prepared_changes = []
    for change in changes:
        change_type = change.type
        if change_type is ChangeType.MISSING:
            prepared_changes.append(make_missing_string(change))
        elif change_type is ChangeType.NO_CHANGE:
            prepared_changes.append(make_no_change_string(change))
        elif change_type is ChangeType.ADDED:
            prepared_changes.append(make_added_string(change))
        elif change_type is ChangeType.CHANGED:
            prepared_changes.append(make_changed_string(change))

    prepared_changes_string = "\n  ".join(prepared_changes)
    return diff_start + prepared_changes_string + diff_end


def make_missing_string(change: Change) -> str:
    json_value, __, key = _extract_change_data(change)
    return f"- {key}: {json_value}"


def make_no_change_string(change: Change) -> str:
    json_value, __, key = _extract_change_data(change)
    return f"  {key}: {json_value}"


def make_added_string(change: Change) -> str:
    json_value, __, key = _extract_change_data(change)
    return f"+ {key}: {json_value}"


def make_changed_string(change: Change) -> str:
    json_value, changed_json_value, key = _extract_change_data(change)
    return f"- {key}: {json_value}\n  + {key}: {changed_json_value}"


def _convert_to_json_value(value: Any) -> str:
    return dumps(value).replace('"', "")


def _extract_change_data(change: Change) -> Tuple[str, str, str]:
    json_value = _convert_to_json_value(change.value)
    changed_json_value = _convert_to_json_value(change.changed_value)
    return json_value, changed_json_value, change.key
