from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

full_width_pattern = RegEx("[^\u0020-\u007E\uFF61-\uFF9F\uFFA0-\uFFDC\uFFE8-\uFFEE0-9a-zA-Z]")

def is_full_width(input: str) -> bool:
    input = assert_string(input)
    return full_width_pattern.match(input)
