from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx


def is_base32(input: str) -> bool:
    base32 = RegEx("^[A-Z2-7]+=*$")
    input = assert_string(input)
    return bool(input.length % 8 == 0 and base32.match(input))
