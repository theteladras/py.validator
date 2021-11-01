from .utils.assert_string import assert_string

def is_uppercase(input: str) -> bool:
    input = assert_string(input)

    return input == input.upper()
