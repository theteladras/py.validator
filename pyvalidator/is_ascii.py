from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string


def is_ascii(input: str) -> bool:
    pattern = RegEx("^[\x00-\x7F]+$")
    input = assert_string(input)
    return pattern.match(input)
