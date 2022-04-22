from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string


def is_base58(input: str) -> bool:
    base58Reg = RegEx("^[A-HJ-NP-Za-km-z1-9]*$")
    input = assert_string(input)
    return base58Reg.match(input)
