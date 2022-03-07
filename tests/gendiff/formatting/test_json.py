from json import dumps

from gendiff.change_type import ChangeType
from gendiff.formatting.json import generate_output
from tests.gendiff.fixtures.diffs import EXPECTED_DIFFS


def test_json_formatter_dumps_difference():
    changes_dict = EXPECTED_DIFFS["nested"]["tricky"]

    expected_diff_string = dumps(
        changes_dict,
        # convert Enum to str
        default=lambda x: x.value if isinstance(x, ChangeType) else x,
        indent=4,
    )

    diff_string = generate_output(changes_dict)

    assert expected_diff_string == diff_string
