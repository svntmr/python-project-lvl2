from json import dumps
from types import MappingProxyType
from typing import Any, List, Tuple

from gendiff.classes.change import Change, ChangeType

_INDENT = "    "
# change showing takes two spaces in format string (+ /- )
_CHANGE_INDENT = "  "
_CHANGE_SYMBOLS = ("+", "-")

_DIFF_STRING_TEMPLATES = MappingProxyType(
    {
        ChangeType.MISSING: "{indent}- {key}: {value}",
        ChangeType.NO_CHANGE: "{indent}{key}: {value}",
        ChangeType.ADDED: "{indent}+ {key}: {value}",
        ChangeType.CHANGED: (
            "{indent}- {key}: {value}\n" "{indent}+ {key}: {changed_value}"
        ),
    }
)


def generate_diff_string(changes: List[Change]) -> str:
    if any(change.has_nested_changes for change in changes):
        ...
    return _make_plain_diff_string(changes)


def _make_plain_diff_string(changes: List[Change]) -> str:
    diff_start = "{\n"
    diff_end = "\n}\n"
    prepared_changes = [_generate_diff_string(change) for change in changes]
    prepared_changes_string = "\n".join(prepared_changes)
    return diff_start + prepared_changes_string + diff_end


def _generate_diff_string(change: Change, indent: str = _INDENT) -> str:
    json_value, changed_json_value, key = _extract_change_data(change)
    formatted_string = _DIFF_STRING_TEMPLATES[change.type].format(
        indent=indent,
        key=key,
        value=json_value,
        changed_value=changed_json_value,
    )
    # check if string has any changes symbols
    extra_symbols_check = tuple(
        symbol in formatted_string for symbol in _CHANGE_SYMBOLS
    )
    if all(extra_symbols_check):
        # ChangeType.CHANGED case, two replacements needed
        old_value, new_value = formatted_string.split("\n")
        old_value = old_value.replace(_CHANGE_INDENT, "", 1)
        new_value = new_value.replace(_CHANGE_INDENT, "", 1)
        formatted_string = "\n".join((old_value, new_value))
    elif any(extra_symbols_check):
        # ChangeType.MISSING or ChangeType.ADDED case, one replacement needed
        formatted_string = formatted_string.replace(_CHANGE_INDENT, "", 1)

    return formatted_string


def _convert_to_json_value(value: Any) -> str:
    return dumps(value).replace('"', "")


def _extract_change_data(change: Change) -> Tuple[str, str, str]:
    json_value = _convert_to_json_value(change.value)
    changed_json_value = _convert_to_json_value(change.changed_value)
    return json_value, changed_json_value, change.key
