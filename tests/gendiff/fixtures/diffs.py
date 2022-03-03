from types import MappingProxyType

from gendiff.change_type import ChangeType

_IDENTICAL = {
    "host": {"type": ChangeType.NO_CHANGE, "value": "hexlet.io", "changed_value": None},
    "timeout": {"type": ChangeType.NO_CHANGE, "value": 50, "changed_value": None},
    "proxy": {
        "type": ChangeType.NO_CHANGE,
        "value": "123.234.53.22",
        "changed_value": None,
    },
    "follow": {"type": ChangeType.NO_CHANGE, "value": False, "changed_value": None},
}

_ADDED = {
    "new_field": {"type": ChangeType.ADDED, "value": 111, "changed_value": None},
    "host": {"type": ChangeType.NO_CHANGE, "value": "hexlet.io", "changed_value": None},
    "timeout": {"type": ChangeType.NO_CHANGE, "value": 50, "changed_value": None},
    "proxy": {
        "type": ChangeType.NO_CHANGE,
        "value": "123.234.53.22",
        "changed_value": None,
    },
    "follow": {"type": ChangeType.NO_CHANGE, "value": False, "changed_value": None},
}

_CHANGED = {
    "host": {
        "type": ChangeType.CHANGED,
        "value": "hexlet.io",
        "changed_value": "pupa.io",
    },
    "timeout": {"type": ChangeType.NO_CHANGE, "value": 50, "changed_value": None},
    "proxy": {
        "type": ChangeType.NO_CHANGE,
        "value": "123.234.53.22",
        "changed_value": None,
    },
    "follow": {"type": ChangeType.NO_CHANGE, "value": False, "changed_value": None},
}

_COMBINED = {
    "proxy": {
        "type": ChangeType.MISSING,
        "value": "123.234.53.22",
        "changed_value": None,
    },
    "follow": {"type": ChangeType.MISSING, "value": False, "changed_value": None},
    "verbose": {"type": ChangeType.ADDED, "value": True, "changed_value": None},
    "host": {"type": ChangeType.NO_CHANGE, "value": "hexlet.io", "changed_value": None},
    "timeout": {"type": ChangeType.CHANGED, "value": 50, "changed_value": 20},
}

_MISSING = {
    "host": {"type": ChangeType.MISSING, "value": "hexlet.io", "changed_value": None},
    "timeout": {"type": ChangeType.NO_CHANGE, "value": 50, "changed_value": None},
    "proxy": {
        "type": ChangeType.NO_CHANGE,
        "value": "123.234.53.22",
        "changed_value": None,
    },
    "follow": {"type": ChangeType.NO_CHANGE, "value": False, "changed_value": None},
}

AWAITED_DIFFS = MappingProxyType(
    {
        "added": _ADDED,
        "changed": _CHANGED,
        "combined": _COMBINED,
        "identical": _IDENTICAL,
        "missing": _MISSING,
    }
)

_IDENTICAL_NESTED = {
    "group2": {
        "type": ChangeType.NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.NO_CHANGE,
                                "value": "",
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.NO_CHANGE,
                "value": True,
                "changed_value": None,
            },
            "setting2": {
                "type": ChangeType.NO_CHANGE,
                "value": 200,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": ChangeType.NO_CHANGE,
                "value": "bas",
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
}

_ADDED_NESTED = {
    "group3": {
        "type": ChangeType.ADDED_NESTED,
        "value": {
            "kek": {
                "type": ChangeType.NESTED,
                "value": {
                    "lol": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "def": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group2": {
        "type": ChangeType.NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting5": {"type": ChangeType.ADDED, "value": 600, "changed_value": None},
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.NO_CHANGE,
                                "value": "",
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.NO_CHANGE,
                "value": True,
                "changed_value": None,
            },
            "setting2": {
                "type": ChangeType.NO_CHANGE,
                "value": 200,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": ChangeType.NO_CHANGE,
                "value": "bas",
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
}

_CHANGED_NESTED = {
    "group2": {
        "type": ChangeType.NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.NO_CHANGE,
                                "value": "",
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.NO_CHANGE,
                "value": True,
                "changed_value": None,
            },
            "setting2": {
                "type": ChangeType.CHANGED,
                "value": 200,
                "changed_value": 300,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.CHANGED,
                        "value": "value",
                        "changed_value": "newValue",
                    }
                },
                "changed_value": None,
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {"type": ChangeType.CHANGED, "value": "bas", "changed_value": "bak"},
        },
        "changed_value": None,
    },
}

_COMBINED_NESTED = {
    "group2": {
        "type": ChangeType.MISSING_NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group3": {
        "type": ChangeType.ADDED_NESTED,
        "value": {
            "fee": {
                "type": ChangeType.NO_CHANGE,
                "value": 100500,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "number": {
                                "type": ChangeType.NO_CHANGE,
                                "value": 45,
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting2": {
                "type": ChangeType.MISSING,
                "value": 200,
                "changed_value": None,
            },
            "setting4": {
                "type": ChangeType.ADDED,
                "value": "blah blah",
                "changed_value": None,
            },
            "follow": {"type": ChangeType.ADDED, "value": False, "changed_value": None},
            "setting5": {
                "type": ChangeType.ADDED_NESTED,
                "value": {
                    "key5": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value5",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "ops": {
                        "type": ChangeType.ADDED,
                        "value": "vops",
                        "changed_value": None,
                    },
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.CHANGED,
                                "value": "",
                                "changed_value": "so much",
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.CHANGED,
                "value": True,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.CHANGED_NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": "str",
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": ChangeType.CHANGED,
                "value": "bas",
                "changed_value": "bars",
            },
        },
        "changed_value": None,
    },
}

_MISSING_NESTED = {
    "group2": {
        "type": ChangeType.MISSING_NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting2": {
                "type": ChangeType.MISSING,
                "value": 200,
                "changed_value": None,
            },
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.NO_CHANGE,
                                "value": "",
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.NO_CHANGE,
                "value": True,
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.MISSING_NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": ChangeType.NO_CHANGE,
                "value": "bas",
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
}

_TRICKY_NESTED = {
    "group2": {
        "type": ChangeType.NESTED,
        "value": {
            "abc": {
                "type": ChangeType.NO_CHANGE,
                "value": 12345,
                "changed_value": None,
            },
            "deep": {
                "type": ChangeType.NESTED,
                "value": {
                    "id": {
                        "type": ChangeType.NO_CHANGE,
                        "value": 45,
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
    "common": {
        "type": ChangeType.NESTED,
        "value": {
            "setting6": {
                "type": ChangeType.NESTED,
                "value": {
                    "doge": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "wow": {
                                "type": ChangeType.NO_CHANGE,
                                "value": "",
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    },
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    },
                },
                "changed_value": None,
            },
            "setting1": {
                "type": ChangeType.NO_CHANGE,
                "value": "Value 1",
                "changed_value": None,
            },
            "setting3": {
                "type": ChangeType.NO_CHANGE,
                "value": True,
                "changed_value": None,
            },
            "setting2": {
                "type": ChangeType.CHANGED_NESTED,
                "value": 200,
                "changed_value": {
                    "kek": {
                        "type": ChangeType.NESTED,
                        "value": {
                            "lol": {
                                "type": ChangeType.NO_CHANGE,
                                "value": 500,
                                "changed_value": None,
                            }
                        },
                        "changed_value": None,
                    }
                },
            },
        },
        "changed_value": None,
    },
    "group1": {
        "type": ChangeType.NESTED,
        "value": {
            "nest": {
                "type": ChangeType.NESTED,
                "value": {
                    "key": {
                        "type": ChangeType.NO_CHANGE,
                        "value": "value",
                        "changed_value": None,
                    }
                },
                "changed_value": None,
            },
            "foo": {
                "type": ChangeType.NO_CHANGE,
                "value": "bar",
                "changed_value": None,
            },
            "baz": {
                "type": ChangeType.NO_CHANGE,
                "value": "bas",
                "changed_value": None,
            },
        },
        "changed_value": None,
    },
}

AWAITED_NESTED_DIFFS = MappingProxyType(
    {
        "added": _ADDED_NESTED,
        "changed": _CHANGED_NESTED,
        "combined": _COMBINED_NESTED,
        "identical": _IDENTICAL_NESTED,
        "missing": _MISSING_NESTED,
        "tricky": _TRICKY_NESTED,
    }
)
