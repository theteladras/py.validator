from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx

md5_pattern = RegEx("^[a-f0-9]{32}$")

def is_md5(input: str) -> bool:
    input = assert_string(input)
    return md5_pattern.match(input)


