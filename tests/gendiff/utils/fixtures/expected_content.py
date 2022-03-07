from types import MappingProxyType

_FILE_1_JSON_CONTENT = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"doge": {"wow": ""}, "key": "value"},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}

# yes, files content are equal
_FILE_1_YAML_CONTENT = _FILE_1_JSON_CONTENT
_BASE_YML_CONTENT = _FILE_1_JSON_CONTENT

EXPECTED_CONTENT: MappingProxyType[str, dict] = MappingProxyType(
    {
        "file1.json": _FILE_1_JSON_CONTENT,
        "file1.yaml": _FILE_1_YAML_CONTENT,
        "base.yml": _BASE_YML_CONTENT,
    }
)
