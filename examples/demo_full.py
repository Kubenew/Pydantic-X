from pydantic_x import BaseModelX


# ---------------------------
# Example 1: Sanitizers
# ---------------------------
class UserInput(BaseModelX):
    name: str
    email: str

    class Config:
        sanitize = True
        strip_whitespace = True
        lowercase_email = True


print("=== Sanitizer Demo ===")
u = UserInput(name="   Alice   ", email=" ALICE@EXAMPLE.COM ")
print(u.model_dump())


# ---------------------------
# Example 2: Schema Versioning
# ---------------------------
class UserV1(BaseModelX, version=1):
    name: str


class UserV2(BaseModelX, version=2):
    name: str
    email: str = "unknown@example.com"

    @classmethod
    def migrate(cls, old_data: dict, old_version: int) -> dict:
        if old_version == 1:
            old_data["email"] = "migrated@example.com"
        return old_data


print("\n=== Schema Migration Demo ===")
old = {"name": "Bob"}

user2 = UserV2.from_previous(old, previous_version=1)
print(user2.model_dump())
