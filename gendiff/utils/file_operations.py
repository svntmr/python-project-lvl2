from json import load
from pathlib import Path
from types import MappingProxyType
from typing import Union

from yaml import safe_load


def get_file_content(file_path: str) -> dict:
    file = Path(file_path)
    return _SUPPORTED_FILE_TYPES[file.suffix](file)


def get_json_file_content(file_path: Union[Path, str]) -> dict:
    with open(file_path, "r") as json_file_stream:
        file_content = load(json_file_stream)

    return dict(file_content)


def get_yaml_file_content(file_path: Path) -> dict:
    with open(file_path, "r") as yaml_file_stream:
        file_content = safe_load(yaml_file_stream)

    return dict(file_content)


_SUPPORTED_FILE_TYPES = MappingProxyType(
    {
        ".json": get_json_file_content,
        ".yaml": get_yaml_file_content,
        ".yml": get_yaml_file_content,
    }
)
