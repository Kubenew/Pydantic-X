from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Tuple


MigrationFunc = Callable[[dict], dict]


@dataclass
class MigrationRegistry:
    migrations: Dict[Tuple[int, int], MigrationFunc]

    def __init__(self):
        self.migrations = {}

    def register(self, from_version: int, to_version: int, fn: MigrationFunc):
        self.migrations[(from_version, to_version)] = fn

    def migrate(self, data: dict, from_version: int, to_version: int) -> dict:
        if from_version == to_version:
            return data

        key = (from_version, to_version)
        if key in self.migrations:
            return self.migrations[key](data)

        current = from_version
        payload = dict(data)

        while current < to_version:
            step_key = (current, current + 1)
            if step_key not in self.migrations:
                raise ValueError(f"No migration registered for {step_key}")
            payload = self.migrations[step_key](payload)
            current += 1

        return payload


GLOBAL_MIGRATIONS = MigrationRegistry()


def migrate(from_version: int, to_version: int):
    """Decorator to register migration functions."""
    def _decorator(fn: MigrationFunc):
        GLOBAL_MIGRATIONS.register(from_version, to_version, fn)
        return fn
    return _decorator
