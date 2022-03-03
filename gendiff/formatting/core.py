from typing import Dict

from gendiff.formatting.stylish import generate_output as stylish_output


def generate_output(changes_dict: Dict, output_format: str = "stylish") -> str:
    if output_format == "stylish":
        return stylish_output(changes_dict)
    raise ValueError(f"Unknown output format: {output_format}")
