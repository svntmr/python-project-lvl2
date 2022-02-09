from pathlib import Path

from gendiff.gendiff import generate_diff
from gendiff.utils.file_paths import TEST_FIXTURES_PATH, RESOURCE_FIXTURES_PATH


class TestGenerateDiff:
    base_file_path: str

    @classmethod
    def setup_class(cls):
        cls.base_file_path = f"{TEST_FIXTURES_PATH}/gendiff/baseFile.json"

    def test_generate_diff_prints_file_content_when_files_are_identical(self):
        file_path = self.base_file_path
        identical_file_path = file_path
        diff = generate_diff(file_path, identical_file_path)
        awaited_diff = Path(
            f"{TEST_FIXTURES_PATH}/gendiff/awaitedDiffs/identical"
        ).read_text()
        assert (
            awaited_diff == diff
        ), "it should output file content when files are identical"

    def test_generate_diff_is_able_to_find_missing_field(self):
        first_file_path = self.base_file_path
        second_file_path = f"{TEST_FIXTURES_PATH}/gendiff/baseFileMissing.json"
        diff = generate_diff(first_file_path, second_file_path)
        awaited_diff = Path(
            f"{TEST_FIXTURES_PATH}/gendiff/awaitedDiffs/missing"
        ).read_text()
        assert awaited_diff == diff, "it should output the missing field"

    def test_generate_diff_is_able_to_find_added_field(self):
        first_file_path = self.base_file_path
        second_file_path = f"{TEST_FIXTURES_PATH}/gendiff/baseFileAdded.json"
        diff = generate_diff(first_file_path, second_file_path)
        awaited_diff = Path(
            f"{TEST_FIXTURES_PATH}/gendiff/awaitedDiffs/added"
        ).read_text()
        assert awaited_diff == diff, "it should output the added field"

    def test_generate_diff_is_able_to_find_changed_field(self):
        first_file_path = self.base_file_path
        second_file_path = f"{TEST_FIXTURES_PATH}/gendiff/baseFileChanged.json"
        diff = generate_diff(first_file_path, second_file_path)
        awaited_diff = Path(
            f"{TEST_FIXTURES_PATH}/gendiff/awaitedDiffs/changed"
        ).read_text()
        assert awaited_diff == diff, "it should output the changed field"

    def test_generate_diff(self):
        first_file_path = f"{RESOURCE_FIXTURES_PATH}/file1.json"
        second_file_path = f"{RESOURCE_FIXTURES_PATH}/file2.json"
        diff = generate_diff(first_file_path, second_file_path)
        awaited_diff = Path(
            f"{TEST_FIXTURES_PATH}/gendiff/awaitedDiffs/full"
        ).read_text()
        assert awaited_diff == diff, "it should output all the stuff"
