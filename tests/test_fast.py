from pydanticx.fast import validate_fast


def test_validate_fast():
    result = validate_fast(dict[str, int], {"a": 1, "b": 2})
    assert result["a"] == 1
