from typing import Union

from .utils.to_int import to_int


def is_even(input: Union[int, str]) -> bool:
    input = to_int(input)

    if input == None:
        return False

    return not bool(input % 2)
