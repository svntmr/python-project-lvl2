import pytest
from gendiff.formatting import generate_output


def test_generate_output_throws_if_formatter_type_is_not_known():
    with pytest.raises(ValueError) as err:
        formatter_type = "unknown"
        generate_output({}, output_format=formatter_type)

        assert err.value == f"Unknown output format: {formatter_type}"
