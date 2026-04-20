from __future__ import annotations

from typing import Any, Dict, Type, TypeVar

from pydantic import BaseModel, model_validator

from .versioning import GLOBAL_MIGRATIONS

T = TypeVar("T", bound="BaseModel")


class SanitizedModel(BaseModel):
    """BaseModel with sanitizer support via model_config['sanitizers']."""

    @model_validator(mode="before")
    @classmethod
    def _apply_sanitizers(cls, data: Any):
        if not isinstance(data, dict):
            return data

        config = getattr(cls, "model_config", {}) or {}
        sanitizers = config.get("sanitizers") or {}

        if not isinstance(sanitizers, dict):
            return data

        out = dict(data)

        for field, funcs in sanitizers.items():
            if field not in out:
                continue

            value = out[field]
            if value is None:
                continue

            if isinstance(value, str):
                for fn in funcs:
                    value = fn(value)
                out[field] = value

        return out


class VersionedModel(SanitizedModel):
    """Model with schema_version + automatic migration support."""

    schema_version: int = 1

    @classmethod
    def validate_versioned(cls: Type[T], data: Dict[str, Any]) -> T:
        if not isinstance(data, dict):
            raise TypeError("validate_versioned expects dict input")

        incoming_version = int(data.get("schema_version", 1))
        target_version = int(getattr(cls, "schema_version", 1))

        migrated = GLOBAL_MIGRATIONS.migrate(data, incoming_version, target_version)
        return cls.model_validate(migrated)
