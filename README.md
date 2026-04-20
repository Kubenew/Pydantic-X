# pydantic-x

**Pydantic-X** is a lightweight toolkit for **Pydantic v2** that provides:

- **Sanitizers** (trim, lower, strip HTML, normalize whitespace)
- **Schema versioning** (versioned models + migration hooks)
- **Fast validation helpers** (compiled TypeAdapter cache)

This is **not a replacement** for Pydantic.  
It is a thin layer that helps you build production APIs with strict data control.

## Install

```bash
pip install pydantic-x
```

## Example: Sanitized Model

```python
from pydanticx import SanitizedModel, sanitize

class User(SanitizedModel):
    name: str
    email: str

    model_config = {
        "sanitizers": {
            "name": [sanitize.trim, sanitize.collapse_spaces],
            "email": [sanitize.trim, sanitize.lower],
        }
    }

u = User.model_validate({"name": "  John   Smith  ", "email": "  TEST@EXAMPLE.COM "})
print(u.name)   # "John Smith"
print(u.email)  # "test@example.com"
```

## Example: Versioned Schema + Migration

```python
from pydanticx import VersionedModel, migrate

class UserV1(VersionedModel):
    schema_version: int = 1
    full_name: str

class UserV2(VersionedModel):
    schema_version: int = 2
    name: str

@migrate(from_version=1, to_version=2)
def migrate_user_v1_to_v2(data: dict) -> dict:
    return {
        "schema_version": 2,
        "name": data.get("full_name", "")
    }

obj = UserV2.validate_versioned({"schema_version": 1, "full_name": "Alice"})
print(obj.name)  # Alice
```

## Example: Fast TypeAdapter Cache

```python
from pydanticx.fast import validate_fast

result = validate_fast(dict[str, int], {"a": 1, "b": 2})
```

## Notes
- Works with **Pydantic v2**
- No external dependencies beyond Pydantic

## License
MIT
