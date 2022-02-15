from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

multibyte_pattern = RegEx(r"[^\x00-\x7F]", 'i')

def is_multibyte(input: str) -> bool:
    input = assert_string(input)

    return any(ord(char) > 127 for char in input)


