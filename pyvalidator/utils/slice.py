from typing import Union


def slice(val: str, start: int, end: Union[int, None]) -> str:
    if end == None:
        return val[start:]
    return val[start:end]


def slice_and_upper_case(val: str, start: int, end: Union[int, None]) -> str:
    sliced = slice(val, start, end)
    return sliced.upper()


def slice_and_lower_case(val: str, start: int, end: Union[int, None]) -> str:
    sliced = slice(val, start, end)
    return sliced.lower()
