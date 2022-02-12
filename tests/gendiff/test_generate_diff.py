from pathlib import Path

import pytest
from gendiff import generate_diff
from tests.paths import TESTS_PATH


class TestGenerateDiffPlainFiles:
    base_folder: str = f"{TESTS_PATH}/gendiff/fixtures/plain"

    base_json_file_path: str = f"{base_folder}/base.json"
    base_yaml_file_path: str = f"{base_folder}/base.yml"
    identical_diff_path: str = f"{base_folder}/diffs/identical"

    missing_json_file_path: str = f"{base_folder}/missing.json"
    missing_yaml_file_path: str = f"{base_folder}/missing.yml"
    missing_diff_path: str = f"{base_folder}/diffs/missing"

    added_json_file_path: str = f"{base_folder}/added.json"
    added_yaml_file_path: str = f"{base_folder}/added.yml"
    added_diff_path: str = f"{base_folder}/diffs/added"

    changed_json_file_path: str = f"{base_folder}/changed.json"
    changed_yaml_file_path: str = f"{base_folder}/changed.yaml"
    changed_diff_path: str = f"{base_folder}/diffs/changed"

    combined_json_file_path: str = f"{base_folder}/file2.json"
    combined_yaml_file_path: str = f"{base_folder}/file2.yml"
    combined_diff_path: str = f"{base_folder}/diffs/full"

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
                base_yaml_file_path,
                base_yaml_file_path,
                identical_diff_path,
                id="identical yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                missing_json_file_path,
                missing_diff_path,
                id="missing json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                missing_yaml_file_path,
                missing_diff_path,
                id="missing yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                added_json_file_path,
                added_diff_path,
                id="added json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                added_yaml_file_path,
                added_diff_path,
                id="added yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                changed_json_file_path,
                changed_diff_path,
                id="changed json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                changed_yaml_file_path,
                changed_diff_path,
                id="changed yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                combined_json_file_path,
                combined_diff_path,
                id="combined json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                combined_yaml_file_path,
                combined_diff_path,
                id="combined yaml files diff",
            ),
        ],
    )
    def test_generate_diff_plain_files(
        self,
        original_file,
        changed_file,
        awaited_diff_file,
    ):
        diff = generate_diff(original_file, changed_file)
        awaited_diff = Path(awaited_diff_file).read_text()
        assert diff == awaited_diff
