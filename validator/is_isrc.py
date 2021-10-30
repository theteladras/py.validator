from .utils.assert_string import assert_string
from .utils.regex import RegEx

pattern = RegEx("^[A-Z]{2}[0-9A-Z]{3}\d{2}\d{5}$")

def is_isrc(input: str) -> bool:
    input = assert_string(input)
    return pattern.match(input)
