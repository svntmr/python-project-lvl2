from operator import attrgetter
from typing import List

from gendiff.classes.change import Change, ChangeType
from gendiff.utils.diff_generator import make_diff_string
from gendiff.utils.file_operations import get_json_file_content


def generate_diff(first_file_path: str, second_file_path: str) -> str:
    first_file_content = get_json_file_content(first_file_path)
    second_file_content = get_json_file_content(second_file_path)

    keys_to_check = set(list(first_file_content) + list(second_file_content))

    changes = build_changes(
        first_dict=first_file_content,
        second_dict=second_file_content,
        keys_to_check=keys_to_check,
    )

    return make_diff_string(changes)


def build_changes(
    first_dict: dict, second_dict: dict, keys_to_check: set
) -> List[Change]:
    changes = []
    for key in keys_to_check:
        first_file_value = first_dict.get(key)
        second_file_value = second_dict.get(key)
        if first_file_value is not None and second_file_value is None:
            changes.append(
                Change(
                    key=key,
                    value=first_file_value,
                    type=ChangeType.MISSING,
                )
            )
        elif first_file_value == second_file_value:
            changes.append(
                Change(
                    key=key,
                    value=first_file_value,
                    type=ChangeType.NO_CHANGE,
                )
            )
        elif first_file_value is None and second_file_value is not None:
            changes.append(
                Change(key=key, value=second_file_value, type=ChangeType.ADDED)
            )
        elif first_file_value != second_file_value:
            changes.append(
                Change(
                    key=key,
                    value=first_file_value,
                    changed_value=second_file_value,
                    type=ChangeType.CHANGED,
                )
            )

    changes.sort(key=attrgetter("key"))
    return changes
