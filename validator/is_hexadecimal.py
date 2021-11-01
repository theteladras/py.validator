from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

hexadecimal_pattern = RegEx("^(0x|0h)?[0-9A-F]+$", "i")

def is_hexadecimal(input: str) -> bool:
    input = assert_string(input)

    return hexadecimal_pattern.match(input)
