from typing import Union

from .utils.assert_string import assert_string
from .utils.to_int import to_int
from .utils.to_float import to_float

def is_divisible_by(input: str, num: Union[int, float, str]) -> bool:
    assert_string(input)
    if to_float(input) != None and to_int(num) != None:
        return (to_float(input) % to_int(num)) == 0
    return False
