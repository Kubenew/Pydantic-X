from __future__ import annotations

from functools import lru_cache
from typing import Any

from pydantic import TypeAdapter


@lru_cache(maxsize=2048)
def adapter_for(tp: Any) -> TypeAdapter:
    """Cached TypeAdapter compilation for faster repeated validation."""
    return TypeAdapter(tp)


def validate_fast(tp: Any, value: Any) -> Any:
    """Validate value using cached TypeAdapter."""
    return adapter_for(tp).validate_python(value)
