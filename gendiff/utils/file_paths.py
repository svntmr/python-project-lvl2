from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


PROJECT_ROOT = get_project_root()
TESTS_PATH = f"{PROJECT_ROOT}/tests"
RESOURCES_PATH = f"{PROJECT_ROOT}/resources"
RESOURCE_FIXTURES_PATH = f"{RESOURCES_PATH}/fixtures"
TEST_FIXTURES_PATH = f"{TESTS_PATH}/fixtures"
