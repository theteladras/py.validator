from typing import Union

from .utils.to_int import to_int


def is_prime(input: Union[int, str]) -> bool:
    input = to_int(input)

    if input == None:
        return False

    if input <= 1:
        return False

    for n in range(2, int(input ** 0.5) + 1):
        if input % n == 0:
            return False

    return True
