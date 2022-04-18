from typing import Union

from ..is_float import is_float


def to_float(input: str) -> Union[float, None]:
    if not is_float(input):
        return None
    else:
        return float(input)
