from pathlib import Path
from types import MappingProxyType

from tests.paths import TESTS_PATH

_IDENTICAL_STYLISH = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

_ADDED_STYLISH = """{
    follow: false
    host: hexlet.io
  + new_field: 111
    proxy: 123.234.53.22
    timeout: 50
}"""

_CHANGED_STYLISH = """{
    follow: false
  - host: hexlet.io
  + host: pupa.io
    proxy: 123.234.53.22
    timeout: 50
}"""

_COMBINED_STYLISH = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

_MISSING_STYLISH = """{
    follow: false
  - host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

_IDENTICAL_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/identical_nested.diff"
).read_text()

_ADDED_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/added_nested.diff"
).read_text()

_CHANGED_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/changed_nested.diff"
).read_text()

_COMBINED_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/combined_nested.diff"
).read_text()

_MISSING_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/missing_nested.diff"
).read_text()

_TRICKY_NESTED_STYLISH = Path(
    f"{TESTS_PATH}/gendiff/fixtures/tricky_nested.diff"
).read_text()

_IDENTICAL_PLAIN = ""

_ADDED_PLAIN = "Property 'new_field' was added with value: 111"

_CHANGED_PLAIN = "Property 'host' was updated. From 'hexlet.io' to 'pupa.io'"

_COMBINED_PLAIN = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

_MISSING_PLAIN = "Property 'host' was removed"

_IDENTICAL_NESTED_PLAIN = _IDENTICAL_PLAIN

_ADDED_NESTED_PLAIN = """Property 'common.setting5' was added with value: 600
Property 'group3' was added with value: [complex value]"""

_CHANGED_NESTED_PLAIN = """Property 'common.setting2' was updated. From 200 to 300
Property 'group1.baz' was updated. From 'bas' to 'bak'
Property 'group1.nest.key' was updated. From 'value' to 'newValue'"""

_COMBINED_NESTED_PLAIN = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

_MISSING_NESTED_PLAIN = """Property 'common.setting2' was removed
Property 'group1.nest' was removed
Property 'group2' was removed"""

_TRICKY_NESTED_PLAIN = (
    "Property 'common.setting2' was updated. From 200 to [complex value]"
)


EXPECTED_OUTPUTS = MappingProxyType(
    {
        "stylish": {
            "plain": {
                "added": _ADDED_STYLISH,
                "changed": _CHANGED_STYLISH,
                "combined": _COMBINED_STYLISH,
                "identical": _IDENTICAL_STYLISH,
                "missing": _MISSING_STYLISH,
            },
            "nested": {
                "added": _ADDED_NESTED_STYLISH,
                "changed": _CHANGED_NESTED_STYLISH,
                "combined": _COMBINED_NESTED_STYLISH,
                "identical": _IDENTICAL_NESTED_STYLISH,
                "missing": _MISSING_NESTED_STYLISH,
                "tricky": _TRICKY_NESTED_STYLISH,
            },
        },
        "plain": {
            "plain": {
                "added": _ADDED_PLAIN,
                "changed": _CHANGED_PLAIN,
                "combined": _COMBINED_PLAIN,
                "identical": _IDENTICAL_PLAIN,
                "missing": _MISSING_PLAIN,
            },
            "nested": {
                "added": _ADDED_NESTED_PLAIN,
                "changed": _CHANGED_NESTED_PLAIN,
                "combined": _COMBINED_NESTED_PLAIN,
                "identical": _IDENTICAL_NESTED_PLAIN,
                "missing": _MISSING_NESTED_PLAIN,
                "tricky": _TRICKY_NESTED_PLAIN,
            },
        },
    }
)
