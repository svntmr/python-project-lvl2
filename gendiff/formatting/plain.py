from json import dumps
from types import MappingProxyType
from typing import Any, Dict

from gendiff.change_type import ChangeType

_DIFF_STRING_TEMPLATES = MappingProxyType(
    {
        ChangeType.MISSING: "Property '{key}' was removed",
        ChangeType.ADDED: "Property '{key}' was added with value: {value}",
        ChangeType.CHANGED: (
            "Property '{key}' was updated. From {value} to {changed_value}"
        ),
        ChangeType.NO_CHANGE: "",
        ChangeType.MISSING_NESTED: "Property '{key}' was removed",
        ChangeType.ADDED_NESTED: "Property '{key}' was added with value: {value}",
        ChangeType.CHANGED_NESTED: (
            "Property '{key}' was updated. From {value} to {changed_value}"
        ),
    }
)


def generate_output(changes_dict: Dict, parent_key: str = "") -> str:
    prepared_changes = []

    for key, change in sorted(changes_dict.items(), key=lambda item: item[0]):
        change_type = change.get("type")
        full_key = f"{parent_key}.{key}" if parent_key else key

        if change_type is ChangeType.NESTED:
            prepared_changes.append(
                generate_output(
                    changes_dict=change["value"],
                    parent_key=full_key,
                )
            )
        else:
            if change_type is ChangeType.ADDED_NESTED:
                source_value = _to_string(change.get("value"))
                changed_value = ""
            else:
                source_value = _to_string(change.get("value"))
                changed_value = _to_string(change.get("changed_value"))

            prepared_changes.append(
                _generate_change_string(
                    change_type=change_type,
                    key=full_key,
                    source_value=source_value,
                    changed_value=changed_value,
                )
            )

    prepared_changes_string = "\n".join(
        prepared_change
        for prepared_change in prepared_changes
        if prepared_change.strip()
    )
    return prepared_changes_string


def _generate_change_string(
    change_type: ChangeType,
    key: str,
    source_value: str,
    changed_value: str,
) -> str:
    formatted_string = _DIFF_STRING_TEMPLATES[change_type].format(
        key=key,
        value=source_value,
        changed_value=changed_value,
    )
    return formatted_string


def _to_string(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    return dumps(value).replace('"', "'")
