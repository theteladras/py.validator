from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx

pattern = RegEx("^[\x00-\x7F]+$")

def is_ascii(input: str) -> bool:
    input = assert_string(input)
    return pattern.match(input)
