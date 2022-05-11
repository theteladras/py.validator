from typing import Union


def gather_then_check(input: str, min: Union[str, int, float, None]) -> bool:
    try:
        if min is None:
            return True

        input_num = float(input)
        min_num = float(min)

        return input_num >= min_num
    except:
        return False


def less_then_check(input: str, max: Union[str, int, float, None]) -> bool:
    try:
        if max is None:
            return True

        input_num = float(input)
        max_num = float(max)

        return input_num <= max_num
    except:
        return False
