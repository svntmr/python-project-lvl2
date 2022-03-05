from enum import Enum
from typing import Dict

from gendiff.formatting.plain import generate_output as plain_output
from gendiff.formatting.stylish import generate_output as stylish_output


class AvailableFormatsEnum(Enum):
    STYLISH = "stylish"
    PLAIN = "plain"

    @classmethod
    def values(cls) -> tuple:
        return tuple(value.value for value in cls)


def generate_output(
    changes_dict: Dict, output_format: str = AvailableFormatsEnum.STYLISH.value
) -> str:
    if output_format == AvailableFormatsEnum.STYLISH.value:
        return stylish_output(changes_dict)
    elif output_format == AvailableFormatsEnum.PLAIN.value:
        return plain_output(changes_dict)
    raise ValueError(f"Unknown output format: {output_format}")
