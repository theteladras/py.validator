import re

from utils.assert_string import assert_string

base58Reg = re.compile("^[A-HJ-NP-Za-km-z1-9]*$")

def is_base58(input):
    assert_string(input)
    return bool(base58Reg.match(input))
