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


def test_sanitizers():
    u = User.model_validate({"name": "  John   Smith  ", "email": "  TEST@EXAMPLE.COM "})
    assert u.name == "John Smith"
    assert u.email == "test@example.com"
