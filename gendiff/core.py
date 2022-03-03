from typing import Dict

from gendiff.diff import build_changes_dict
from gendiff.formatting import generate_output
from gendiff.utils.file_operations import get_file_content


def generate_diff(
    first_file_path: str, second_file_path: str, output_format: str = "stylish"
) -> str:
    diff_dict = generate_changes_dict(first_file_path, second_file_path)

    return generate_output(diff_dict, output_format=output_format)


def generate_changes_dict(first_file_path: str, second_file_path: str) -> Dict:
    first_file_content = get_file_content(first_file_path)
    second_file_content = get_file_content(second_file_path)

    changes_dict = build_changes_dict(first_file_content, second_file_content)

    return changes_dict
