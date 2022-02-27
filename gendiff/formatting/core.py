from enum import Enum
from typing import Callable, Dict

from gendiff.formatting.json import generate_output as json_output
from gendiff.formatting.plain import generate_output as plain_output
from gendiff.formatting.stylish import generate_output as stylish_output


class AvailableFormatsEnum(Enum):
    STYLISH = "stylish"
    PLAIN = "plain"
    JSON = "json"

    @classmethod
    def values(cls) -> tuple:
        return tuple(value.value for value in cls)


def generate_output(
    changes_dict: Dict, output_format: str = AvailableFormatsEnum.STYLISH.value
) -> str:
    output_formats: Dict[str, Callable[[Dict], str]] = {
        AvailableFormatsEnum.STYLISH.value: stylish_output,
        AvailableFormatsEnum.PLAIN.value: plain_output,
        AvailableFormatsEnum.JSON.value: json_output,
    }
    if output_format not in output_formats.keys():
        raise ValueError(f"Unknown output format: {output_format}")

    return output_formats[output_format](changes_dict)
