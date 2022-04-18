from typing import Union


def to_int(input: Union[int, float, str]) -> Union[int, None]:
    try:
        return int(input)
    except:
        return None
