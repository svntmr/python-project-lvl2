import pytest
from gendiff.core import generate_changes_dict
from tests.gendiff.fixtures.diffs import AWAITED_DIFFS, AWAITED_NESTED_DIFFS
from tests.paths import TESTS_PATH


class TestGenerateDiffPlainFiles:
    base_folder: str = f"{TESTS_PATH}/gendiff/fixtures/plain"

    base_json_file_path: str = f"{base_folder}/base.json"
    base_yaml_file_path: str = f"{base_folder}/base.yml"

    missing_json_file_path: str = f"{base_folder}/missing.json"
    missing_yaml_file_path: str = f"{base_folder}/missing.yml"

    added_json_file_path: str = f"{base_folder}/added.json"
    added_yaml_file_path: str = f"{base_folder}/added.yml"

    changed_json_file_path: str = f"{base_folder}/changed.json"
    changed_yaml_file_path: str = f"{base_folder}/changed.yaml"

    combined_json_file_path: str = f"{base_folder}/file2.json"
    combined_yaml_file_path: str = f"{base_folder}/file2.yml"

    @pytest.mark.parametrize(
        ("original_file", "changed_file", "awaited_diff"),
        [
            pytest.param(
                base_json_file_path,
                base_json_file_path,
                AWAITED_DIFFS["identical"],
                id="identical json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                base_yaml_file_path,
                AWAITED_DIFFS["identical"],
                id="identical yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                missing_json_file_path,
                AWAITED_DIFFS["missing"],
                id="missing json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                missing_yaml_file_path,
                AWAITED_DIFFS["missing"],
                id="missing yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                added_json_file_path,
                AWAITED_DIFFS["added"],
                id="added json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                added_yaml_file_path,
                AWAITED_DIFFS["added"],
                id="added yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                changed_json_file_path,
                AWAITED_DIFFS["changed"],
                id="changed json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                changed_yaml_file_path,
                AWAITED_DIFFS["changed"],
                id="changed yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                combined_json_file_path,
                AWAITED_DIFFS["combined"],
                id="combined json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                combined_yaml_file_path,
                AWAITED_DIFFS["combined"],
                id="combined yaml files diff",
            ),
        ],
    )
    def test_generate_diff(
        self,
        original_file,
        changed_file,
        awaited_diff,
    ):
        diff_dict = generate_changes_dict(original_file, changed_file)
        assert diff_dict == awaited_diff


class TestGenerateDiffNestedFiles:
    base_folder: str = f"{TESTS_PATH}/gendiff/fixtures/nested"

    base_json_file_path: str = f"{base_folder}/base.json"
    base_yaml_file_path: str = f"{base_folder}/base.yml"

    missing_json_file_path: str = f"{base_folder}/missing.json"
    missing_yaml_file_path: str = f"{base_folder}/missing.yml"

    added_json_file_path: str = f"{base_folder}/added.json"
    added_yaml_file_path: str = f"{base_folder}/added.yml"

    changed_json_file_path: str = f"{base_folder}/changed.json"
    changed_yaml_file_path: str = f"{base_folder}/changed.yml"

    combined_json_file_path: str = f"{base_folder}/file2.json"
    combined_yaml_file_path: str = f"{base_folder}/file2.yaml"

    tricky_json_file_path: str = f"{base_folder}/tricky.json"
    tricky_yaml_file_path: str = f"{base_folder}/tricky.yml"

    @pytest.mark.parametrize(
        ("original_file", "changed_file", "awaited_diff"),
        [
            pytest.param(
                base_json_file_path,
                base_json_file_path,
                AWAITED_NESTED_DIFFS["identical"],
                id="identical nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                base_yaml_file_path,
                AWAITED_NESTED_DIFFS["identical"],
                id="identical nested yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                missing_json_file_path,
                AWAITED_NESTED_DIFFS["missing"],
                id="missing nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                missing_yaml_file_path,
                AWAITED_NESTED_DIFFS["missing"],
                id="missing nested yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                added_json_file_path,
                AWAITED_NESTED_DIFFS["added"],
                id="added nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                added_yaml_file_path,
                AWAITED_NESTED_DIFFS["added"],
                id="added nested yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                changed_json_file_path,
                AWAITED_NESTED_DIFFS["changed"],
                id="changed nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                changed_yaml_file_path,
                AWAITED_NESTED_DIFFS["changed"],
                id="changed nested yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                combined_json_file_path,
                AWAITED_NESTED_DIFFS["combined"],
                id="combined nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                combined_yaml_file_path,
                AWAITED_NESTED_DIFFS["combined"],
                id="combined nested yaml files diff",
            ),
            pytest.param(
                base_json_file_path,
                tricky_json_file_path,
                AWAITED_NESTED_DIFFS["tricky"],
                id="tricky nested json files diff",
            ),
            pytest.param(
                base_yaml_file_path,
                tricky_yaml_file_path,
                AWAITED_NESTED_DIFFS["tricky"],
                id="tricky nested yaml files diff",
            ),
        ],
    )
    def test_generate_diff(
        self,
        original_file,
        changed_file,
        awaited_diff,
    ):
        diff_dict = generate_changes_dict(original_file, changed_file)
        assert diff_dict == awaited_diff
