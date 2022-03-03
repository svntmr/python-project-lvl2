from json import dumps
from types import MappingProxyType
from typing import Any, Dict

from gendiff.change_type import ChangeType

DIFF_START = "{\n"

_INDENT = "    "

_DIFF_STRING_TEMPLATES = MappingProxyType(
    {
        ChangeType.MISSING: "{indent}- {key}: {value}\n",
        ChangeType.NO_CHANGE: "{indent}{key}: {value}\n",
        ChangeType.ADDED: "{indent}+ {key}: {value}\n",
        ChangeType.CHANGED: (
            "{indent}- {key}: {value}\n{indent}+ {key}: {changed_value}\n"
        ),
        ChangeType.NESTED: "{indent}{key}: {value}\n",
        ChangeType.MISSING_NESTED: "{indent}- {key}: {value}\n",
        ChangeType.ADDED_NESTED: "{indent}+ {key}: {value}\n",
        ChangeType.CHANGED_NESTED: (
            "{indent}- {key}: {value}\n{indent}+ {key}: {changed_value}\n"
        ),
    }
)


def generate_output(changes_dict: Dict, indent: str = _INDENT) -> str:
    diff_end = indent[:-4] + "}"
    prepared_changes = [DIFF_START]

    for key, change in sorted(changes_dict.items(), key=lambda item: item[0]):
        change_type = change.get("type")

        if change_type in (
            ChangeType.NESTED,
            ChangeType.MISSING_NESTED,
            ChangeType.ADDED_NESTED,
            ChangeType.CHANGED_NESTED,
        ):
            prepared_changes.append(
                _generate_nested_change_string(
                    change_type=change_type,
                    key=key,
                    change=change,
                    indent=indent,
                )
            )
        else:
            prepared_changes.append(
                _generate_change_string(
                    change_type=change_type,
                    key=key,
                    source_value=_to_json(change.get("value")),
                    changed_value=_to_json(change.get("changed_value")),
                    indent=indent,
                )
            )

    prepared_changes.append(diff_end)
    prepared_changes_string = "".join(prepared_changes)
    return prepared_changes_string


def _generate_nested_change_string(
    change_type: ChangeType,
    key: str,
    change: dict,
    indent: str,
) -> str:
    base_indent = indent
    if change_type in (
        ChangeType.MISSING_NESTED,
        ChangeType.ADDED_NESTED,
        ChangeType.CHANGED_NESTED,
    ):
        base_indent = indent[:-2]

    value = change["value"]
    changed_value = change["changed_value"]
    if change_type is ChangeType.CHANGED_NESTED and isinstance(
        change.get("changed_value"), dict
    ):
        changed_value = generate_output(
            change["changed_value"], indent=indent + _INDENT
        )
        value = _to_json(value)
    else:
        value = generate_output(change["value"], indent=indent + _INDENT)

    formatted_string = _DIFF_STRING_TEMPLATES[change_type].format(
        indent=base_indent,
        key=key,
        value=value,
        changed_value=changed_value,
    )
    return formatted_string


def _generate_change_string(
    change_type: ChangeType,
    key: str,
    source_value: str,
    changed_value: str,
    indent: str,
) -> str:
    if change_type in (ChangeType.ADDED, ChangeType.CHANGED, ChangeType.MISSING):
        indent = indent[:-2]
    formatted_string = _DIFF_STRING_TEMPLATES[change_type].format(
        indent=indent,
        key=key,
        value=source_value,
        changed_value=changed_value,
    )
    return formatted_string


def _to_json(value: Any) -> str:
    return dumps(value).replace('"', "")
