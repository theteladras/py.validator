from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx

base58Reg = RegEx("^[A-HJ-NP-Za-km-z1-9]*$")

def is_base58(input: str) -> bool:
    input = assert_string(input)
    return base58Reg.match(input)
