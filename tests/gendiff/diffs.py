from pathlib import Path
from types import MappingProxyType

from tests.paths import TESTS_PATH

_IDENTICAL = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}
"""

_ADDED = """{
    follow: false
    host: hexlet.io
  + new_field: 111
    proxy: 123.234.53.22
    timeout: 50
}
"""

_CHANGED = """{
    follow: false
  - host: hexlet.io
  + host: pupa.io
    proxy: 123.234.53.22
    timeout: 50
}
"""

_COMBINED = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""

_MISSING = """{
    follow: false
  - host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}
"""

AWAITED_DIFFS = MappingProxyType(
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

# _ADDED_NESTED = """{
#     follow: false
#     host: hexlet.io
#   + new_field: 111
#     proxy: 123.234.53.22
#     timeout: 50
# }
# """

# _CHANGED_NESTED = """{
#     follow: false
#   - host: hexlet.io
#   + host: pupa.io
#     proxy: 123.234.53.22
#     timeout: 50
# }
# """

# _COMBINED_NESTED = """{
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }
# """

# _MISSING_NESTED = """{
#     follow: false
#   - host: hexlet.io
#     proxy: 123.234.53.22
#     timeout: 50
# }
# """

AWAITED_NESTED_DIFFS = MappingProxyType(
    {
        # "added": _ADDED_NESTED,
        # "changed": _CHANGED_NESTED,
        # "combined": _COMBINED_NESTED,
        "identical": _IDENTICAL_NESTED,
        # "missing": _MISSING_NESTED,
    }
)
