from pydanticx import VersionedModel, migrate


class UserV2(VersionedModel):
    schema_version: int = 2
    name: str


@migrate(from_version=1, to_version=2)
def migrate_user(data: dict) -> dict:
    return {"schema_version": 2, "name": data.get("full_name", "")}


def test_versioned_migration():
    obj = UserV2.validate_versioned({"schema_version": 1, "full_name": "Alice"})
    assert obj.schema_version == 2
    assert obj.name == "Alice"
