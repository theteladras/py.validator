from .utils.assert_string import assert_string
from .is_hexadecimal import is_hexadecimal

def is_mongo_id(input: str) -> bool:
    input = assert_string(input)

    return input.length == 24 and is_hexadecimal(input)
