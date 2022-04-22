from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string


def is_md5(input: str) -> bool:
    input = assert_string(input)

    md5_pattern = RegEx("^[a-f0-9]{32}$")

    return md5_pattern.match(input)
