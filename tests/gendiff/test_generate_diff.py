from pathlib import Path

import pytest
from gendiff import generate_diff
from gendiff.utils.file_paths import RESOURCE_FIXTURES_PATH, TEST_FIXTURES_PATH


class TestGenerateDiff:
    base_json_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/base.json"
    missing_json_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/missing.json"
    added_json_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/added.json"
    changed_json_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/changed.json"
    combined_json_file_path: str = f"{RESOURCE_FIXTURES_PATH}/file2.json"

    base_yaml_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/base.yml"
    missing_yaml_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/missing.yml"
    added_yaml_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/added.yml"
    changed_yaml_file_path: str = f"{TEST_FIXTURES_PATH}/gendiff/changed.yaml"
    combined_yaml_file_path: str = f"{RESOURCE_FIXTURES_PATH}/file2.yml"

    identical_diff_path: str = f"{TEST_FIXTURES_PATH}/gendiff/diffs/identical"
    missing_diff_path: str = f"{TEST_FIXTURES_PATH}/gendiff/diffs/missing"
    added_diff_path: str = f"{TEST_FIXTURES_PATH}/gendiff/diffs/added"
    changed_diff_path: str = f"{TEST_FIXTURES_PATH}/gendiff/diffs/changed"
    combined_diff_path: str = f"{TEST_FIXTURES_PATH}/gendiff/diffs/full"

    @pytest.mark.parametrize(
        ("original_file", "changed_file", "awaited_diff_file"),
        [
            pytest.param(
                base_json_file_path,
                base_json_file_path,
                identical_diff_path,
                id="identical json files diff",
            ),
            pytest.param(
                base_json_file_path,
                missing_json_file_path,
                missing_diff_path,
                id="missing json files diff",
            ),
            pytest.param(
                base_json_file_path,
                added_json_file_path,
                added_diff_path,
                id="added json files diff",
            ),
            pytest.param(
                base_json_file_path,
                changed_json_file_path,
                changed_diff_path,
                id="changed json files diff",
            ),
            pytest.param(
                base_json_file_path,
                combined_json_file_path,
                combined_diff_path,
                id="combined json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                base_yaml_file_path,
                identical_diff_path,
                id="identical yaml files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                missing_yaml_file_path,
                missing_diff_path,
                id="missing yaml files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                added_yaml_file_path,
                added_diff_path,
                id="added yaml files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                changed_yaml_file_path,
                changed_diff_path,
                id="changed yaml files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                combined_yaml_file_path,
                combined_diff_path,
                id="combined yaml files diff",
            ),
        ],
    )
    def test_generate_diff(
        self,
        original_file,
        changed_file,
        awaited_diff_file,
    ):
        diff = generate_diff(original_file, changed_file)
        awaited_diff = Path(awaited_diff_file).read_text()
        assert awaited_diff == diff
