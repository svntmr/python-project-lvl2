from json import dumps
from types import MappingProxyType
from typing import Any, List, Tuple

from gendiff.classes.change import Change, ChangeType

DIFF_END = "\n}\n"

DIFF_START = "{\n"

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
            "{indent}- {key}: {value}\n{indent}+ {key}: {changed_value}"
        ),
        ChangeType.NESTED_START: "{indent}{key}:",
    }
)


def generate_diff_string(changes: List[Change]) -> str:
    if any(change.has_nested_changes for change in changes):
        return _make_nested_diff_string(changes)
    else:
        return _make_plain_diff_string(changes)


def _make_plain_diff_string(changes: List[Change]) -> str:
    prepared_changes = [_generate_diff_string(change) for change in changes]
    prepared_changes_string = "\n".join(prepared_changes)
    return DIFF_START + prepared_changes_string + DIFF_END


def _make_nested_diff_string(changes: List[Change]) -> str:
    prepared_changes = []

    for change in changes:
        if change.has_nested_changes:
            prepared_changes.append(_generate_nested_diff_string(change))
        else:
            prepared_changes.append(_generate_diff_string(change))
    prepared_changes_string = "\n".join(prepared_changes)
    return DIFF_START + prepared_changes_string + DIFF_END


def _generate_diff_string(change: Change, indent: str = _INDENT) -> str:
    json_value, changed_json_value, key = _extract_change_data(change)
    return _generate_change_string(
        change_type=change.type,
        key=key,
        source_value=json_value,
        changed_value=changed_json_value,
        indent=indent,
    )


def _generate_change_string(
    change_type: ChangeType,
    key: str = "",
    source_value: str = "",
    changed_value: str = "",
    indent: str = "",
) -> str:
    formatted_string = _DIFF_STRING_TEMPLATES[change_type].format(
        indent=indent,
        key=key,
        value=source_value,
        changed_value=changed_value,
    )
    # check if string has any changes symbols
    change_symbols_check = tuple(
        symbol in formatted_string for symbol in _CHANGE_SYMBOLS
    )
    if all(change_symbols_check):
        # ChangeType.CHANGED case, two replacements needed
        old_value, new_value = formatted_string.split("\n")
        old_value = old_value.replace(_CHANGE_INDENT, "", 1)
        new_value = new_value.replace(_CHANGE_INDENT, "", 1)
        formatted_string = "\n".join((old_value, new_value))
    elif any(change_symbols_check):
        # ChangeType.MISSING or ChangeType.ADDED case, one replacement needed
        formatted_string = formatted_string.replace(_CHANGE_INDENT, "", 1)
    return formatted_string


def _generate_nested_diff_string(change: Change, indent: str = _INDENT) -> str:
    assert change.nested_changes
    change_string = _generate_change_string(
        change_type=ChangeType.NESTED_START,
        key=change.key,
        indent=indent,
    )
    start = change_string + " {\n"
    end = "\n" + indent + "}"

    contents = []
    for nested_change in change.nested_changes:
        if not nested_change.has_nested_changes:
            contents.append(
                _generate_diff_string(nested_change, indent=indent + _INDENT)
            )
        else:
            contents.append(
                _generate_nested_diff_string(
                    nested_change,
                    indent=indent + _INDENT,
                )
            )
    content = "\n".join(contents)
    return start + content + end


def _convert_to_json_value(value: Any) -> str:
    return dumps(value).replace('"', "")


def _extract_change_data(change: Change) -> Tuple[str, str, str]:
    json_value = _convert_to_json_value(change.value)
    changed_json_value = _convert_to_json_value(change.changed_value)
    return json_value, changed_json_value, change.key
