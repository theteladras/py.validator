from .utils.assert_string import assert_string

octal_pattern = "^(0o)?[0-7]+$"

def is_octal(input: str) -> bool:
    input = assert_string(input)

    return input.match(octal_pattern, "i")
