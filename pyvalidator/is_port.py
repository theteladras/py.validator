from .utils.assert_string import assert_string
from .is_int import is_int

def is_port(input: str) -> bool:
    input = assert_string(input)
    return is_int(input, { "min": 0, "max": 65535 })
