from json import dumps
from typing import Dict

from gendiff.change_type import ChangeType


def generate_output(changes_dict: Dict) -> str:
    return dumps(
        changes_dict,
        # convert Enum to str
        default=lambda x: x.value if isinstance(x, ChangeType) else x,
        indent=4,
    )
