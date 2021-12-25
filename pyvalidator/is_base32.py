from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.assert_string import assert_string

base32 = RegEx("^[A-Z2-7]+=*$")

def is_base32(input: str) -> bool:
    input = assert_string(input)
    return bool(input.length % 8 == 0 and base32.match(input))
