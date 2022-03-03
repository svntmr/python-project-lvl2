from operator import attrgetter
from typing import List

from gendiff.classes.change import Change, ChangeType
from gendiff.utils.diff_generator import generate_diff_string
from gendiff.utils.file_operations import get_file_content


def generate_diff(first_file_path: str, second_file_path: str) -> str:
    first_file_content = get_file_content(first_file_path)
    second_file_content = get_file_content(second_file_path)

    changes = build_changes(
        source=first_file_content,
        changed=second_file_content,
    )

    return generate_diff_string(changes)


def _build_nested_changes(key: str, source: dict, changed: dict) -> List[Change]:
    nested_changes = []
    if isinstance(source.get(key), dict):
        nested_changes = build_changes(
            source.get(key, {}),
            changed.get(key, {}),
        )
    return nested_changes


def build_changes(source: dict, changed: dict) -> List[Change]:
    changes = []

    source_keys = set(source.keys())
    changed_keys = set(changed.keys())
    added_keys = changed_keys - source_keys
    missing_keys = source_keys - changed_keys
    common_keys = source_keys.intersection(changed_keys)

    for key in missing_keys:
        nested_changes = _build_nested_changes(key, source, changed)
        changes.append(
            Change(
                key=key,
                value=source.get(key),
                type=ChangeType.MISSING,
                nested_changes=nested_changes,
            )
        )

    for key in added_keys:
        nested_changes = _build_nested_changes(key, source, changed)
        changes.append(
            Change(
                key=key,
                value=changed.get(key),
                type=ChangeType.ADDED,
                nested_changes=nested_changes,
            )
        )

    for key in common_keys:
        nested_changes = _build_nested_changes(key, source, changed)
        if source.get(key) == changed.get(key):
            changes.append(
                Change(
                    key=key,
                    value=source.get(key),
                    type=ChangeType.NO_CHANGE,
                    nested_changes=nested_changes,
                )
            )
        else:
            changes.append(
                Change(
                    key=key,
                    value=source.get(key),
                    changed_value=changed.get(key),
                    type=ChangeType.CHANGED,
                    nested_changes=nested_changes,
                )
            )

    changes.sort(key=attrgetter("key"))
    return changes
