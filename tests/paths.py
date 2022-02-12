from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


PROJECT_ROOT = get_project_root()
TESTS_PATH = f"{PROJECT_ROOT}/tests"
