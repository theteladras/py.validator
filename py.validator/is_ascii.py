import re

from utils.assert_string import assert_string

pattern = re.compile("^[\x00-\x7F]+$")

def is_ascii(input):
    assert_string(input)
    return bool(pattern.match(input))
