from operator import attrgetter
from typing import List

from gendiff.classes.change import Change, ChangeType
from gendiff.utils.diff_generator import make_diff_string
from gendiff.utils.file_operations import get_json_file_content


def generate_diff(first_file_path: str, second_file_path: str) -> str:
    first_file_content = get_json_file_content(first_file_path)
    second_file_content = get_json_file_content(second_file_path)

    changes = build_changes(
        source=first_file_content,
        changed=second_file_content,
    )

    return make_diff_string(changes)


def build_changes(source: dict, changed: dict) -> List[Change]:
    changes = []

    source_keys = set(source.keys())
    changed_keys = set(changed.keys())
    added_keys = changed_keys - source_keys
    missing_keys = source_keys - changed_keys
    common_keys = source_keys.intersection(changed_keys)

    for key in missing_keys:
        changes.append(
            Change(
                key=key,
                value=source.get(key),
                type=ChangeType.MISSING,
            )
        )

    for key in added_keys:
        changes.append(
            Change(
                key=key,
                value=changed.get(key),
                type=ChangeType.ADDED,
            )
        )

    for key in common_keys:
        if source[key] == changed[key]:
            changes.append(
                Change(
                    key=key,
                    value=source[key],
                    type=ChangeType.NO_CHANGE,
                )
            )
        else:
            changes.append(
                Change(
                    key=key,
                    value=source[key],
                    changed_value=changed[key],
                    type=ChangeType.CHANGED,
                )
            )

    changes.sort(key=attrgetter("key"))
    return changes
