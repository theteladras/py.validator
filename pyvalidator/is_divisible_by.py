from typing import Union

from .utils.assert_string import assert_string
from .utils.to_float import to_float
from .utils.to_int import to_int


def is_divisible_by(input: str, num: Union[int, float, str]) -> bool:
    assert_string(input)
    if to_float(input) is not None and to_int(num) is not None:
        return (to_float(input) % to_int(num)) == 0
    return False
