from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx


def is_half_width(input: str) -> bool:
    input = assert_string(input)

    half_width_pattern = RegEx(r'[\u0020-\u007E\uFF61-\uFF9F\uFFA0-\uFFDC\uFFE8-\uFFEE0-9a-zA-Z]')

    return half_width_pattern.match(input)
