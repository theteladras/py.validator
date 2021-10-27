import re

from utils.assert_string import assert_string
from utils.assert_string import assert_string

base32 = re.compile("^[A-Z2-7]+=*$")

def is_base32(input):
    assert_string(input)
    input_length = len(input)
    return input_length % 8 == 0 and base32.match(input)
