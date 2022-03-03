from pathlib import Path
from types import MappingProxyType

from tests.paths import TESTS_PATH

_IDENTICAL = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

_ADDED = """{
    follow: false
    host: hexlet.io
  + new_field: 111
    proxy: 123.234.53.22
    timeout: 50
}"""

_CHANGED = """{
    follow: false
  - host: hexlet.io
  + host: pupa.io
    proxy: 123.234.53.22
    timeout: 50
}"""

_COMBINED = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

_MISSING = """{
    follow: false
  - host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

AWAITED_OUTPUTS = MappingProxyType(
    {
        "added": _ADDED,
        "changed": _CHANGED,
        "combined": _COMBINED,
        "identical": _IDENTICAL,
        "missing": _MISSING,
    }
)

_IDENTICAL_NESTED = Path(
    f"{TESTS_PATH}/gendiff/fixtures/identical_nested.diff"
).read_text()

_ADDED_NESTED = Path(f"{TESTS_PATH}/gendiff/fixtures/added_nested.diff").read_text()

_CHANGED_NESTED = Path(f"{TESTS_PATH}/gendiff/fixtures/changed_nested.diff").read_text()

_COMBINED_NESTED = Path(
    f"{TESTS_PATH}/gendiff/fixtures/combined_nested.diff"
).read_text()

_MISSING_NESTED = Path(f"{TESTS_PATH}/gendiff/fixtures/missing_nested.diff").read_text()

_TRICKY_NESTED = Path(f"{TESTS_PATH}/gendiff/fixtures/tricky_nested.diff").read_text()

AWAITED_NESTED_OUTPUTS = MappingProxyType(
    {
        "added": _ADDED_NESTED,
        "changed": _CHANGED_NESTED,
        "combined": _COMBINED_NESTED,
        "identical": _IDENTICAL_NESTED,
        "missing": _MISSING_NESTED,
        "tricky": _TRICKY_NESTED,
    }
)
