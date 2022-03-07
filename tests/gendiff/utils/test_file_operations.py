import pytest
from gendiff.utils.file_operations import get_file_content
from tests.gendiff.utils.fixtures.expected_content import EXPECTED_CONTENT
from tests.paths import TESTS_PATH

BASE_FILEPATH = f"{TESTS_PATH}/gendiff/fixtures/nested"


def test_get_file_content_works_with_json_files():
    json_file = f"{BASE_FILEPATH}/file1.json"
    expected_content = EXPECTED_CONTENT["file1.json"]

    file_content = get_file_content(json_file)

    assert expected_content == file_content


@pytest.mark.parametrize(
    "yaml_file, expected_content",
    [
        pytest.param(
            f"{BASE_FILEPATH}/file1.yaml",
            EXPECTED_CONTENT["file1.yaml"],
            id="yaml file",
        ),
        pytest.param(
            f"{BASE_FILEPATH}/base.yml",
            EXPECTED_CONTENT["base.yml"],
            id="yml file",
        ),
    ],
)
def test_get_file_content_works_with_yaml_files(yaml_file, expected_content):
    file_content = get_file_content(yaml_file)

    assert expected_content == file_content


def test_get_file_content_throws_if_file_type_is_not_json_or_yaml():
    file_type = "foo"
    file = f"{BASE_FILEPATH}/file1.{file_type}"

    with pytest.raises(ValueError) as err:
        get_file_content(file)

        assert err.value == f"Unsupported file type: {file_type}"
