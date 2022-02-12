from json import dumps
from types import MappingProxyType
from typing import Any, List, Tuple

from gendiff.classes.change import Change, ChangeType

_DIFF_STRING_TEMPLATES = MappingProxyType(
    {
        ChangeType.MISSING: "- {key}: {value}",
        ChangeType.NO_CHANGE: "  {key}: {value}",
        ChangeType.ADDED: "+ {key}: {value}",
        ChangeType.CHANGED: "- {key}: {value}\n  + {key}: {changed_value}",
    }
)


def make_diff_string(changes: List[Change]) -> str:
    diff_start = "{\n  "
    diff_end = "\n}\n"
    prepared_changes = [_generate_diff_string(change) for change in changes]
    prepared_changes_string = "\n  ".join(prepared_changes)
    return diff_start + prepared_changes_string + diff_end


def _generate_diff_string(change: Change) -> str:
    json_value, changed_json_value, key = _extract_change_data(change)
    return _DIFF_STRING_TEMPLATES[change.type].format(
        key=key, value=json_value, changed_value=changed_json_value
    )


def _convert_to_json_value(value: Any) -> str:
    return dumps(value).replace('"', "")


def _extract_change_data(change: Change) -> Tuple[str, str, str]:
    json_value = _convert_to_json_value(change.value)
    changed_json_value = _convert_to_json_value(change.changed_value)
    return json_value, changed_json_value, change.key
