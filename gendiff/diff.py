from typing import Any, Dict, Optional

from gendiff.change_type import ChangeType


def build_changes_dict(source: dict, changed: dict) -> Dict:
    dicts_diff = build_dicts_diff(source, changed)
    changes_dict = {}

    for key, change_type in dicts_diff.items():
        value = None
        changed_value = None

        if change_type is ChangeType.NESTED:
            value = build_changes_dict(source.get(key, {}), changed.get(key, {}))

        if change_type is ChangeType.MISSING_NESTED:
            value = build_changes_dict(source.get(key, {}), source.get(key, {}))

        if change_type is ChangeType.ADDED_NESTED:
            value = build_changes_dict(changed.get(key, {}), changed.get(key, {}))

        if change_type is ChangeType.CHANGED_NESTED and isinstance(
            source.get(key), dict
        ):
            value = build_changes_dict(source.get(key, {}), source.get(key, {}))
            changed_value = changed.get(key)

        if change_type is ChangeType.CHANGED_NESTED and isinstance(
            changed.get(key), dict
        ):
            value = source.get(key)
            changed_value = build_changes_dict(
                changed.get(key, {}), changed.get(key, {})
            )

        if change_type is ChangeType.ADDED:
            value = changed.get(key)

        if change_type is ChangeType.CHANGED:
            value = source.get(key)
            changed_value = changed.get(key)

        if change_type in (ChangeType.MISSING, ChangeType.NO_CHANGE):
            value = source.get(key)

        changes_dict[key] = _build_change(
            change_type,
            value,
            changed_value,
        )

    return changes_dict


def build_dicts_diff(source: dict, changed: dict) -> Dict[str, ChangeType]:
    changes_dict = {}

    source_keys = set(source.keys())
    changed_keys = set(changed.keys())
    added_keys = changed_keys - source_keys
    missing_keys = source_keys - changed_keys
    common_keys = source_keys.intersection(changed_keys)

    for missing in missing_keys:
        if isinstance(source[missing], dict):
            changes_dict[missing] = ChangeType.MISSING_NESTED
        else:
            changes_dict[missing] = ChangeType.MISSING

    for added in added_keys:
        if isinstance(changed[added], dict):
            changes_dict[added] = ChangeType.ADDED_NESTED
        else:
            changes_dict[added] = ChangeType.ADDED

    for common in common_keys:
        source_value = source.get(common)
        changed_value = changed.get(common)
        if isinstance(source_value, dict) and isinstance(changed_value, dict):
            changes_dict[common] = ChangeType.NESTED
        elif source_value == changed_value:
            changes_dict[common] = ChangeType.NO_CHANGE
        elif any(isinstance(value, dict) for value in (source_value, changed_value)):
            changes_dict[common] = ChangeType.CHANGED_NESTED
        else:
            changes_dict[common] = ChangeType.CHANGED

    return changes_dict


def _build_change(
    change_type: ChangeType,
    value: Any,
    changed_value: Optional[Any] = None,
) -> Dict:
    return {"type": change_type, "value": value, "changed_value": changed_value}
