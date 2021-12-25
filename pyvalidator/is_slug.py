from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

charset_pattern = RegEx(r"^[^\s_-](?!.*?[-_]{2,})[a-z0-9-\\][^\s]*[^-_\s]$")

def is_slug(input: str) -> bool:
    input = assert_string(input)

    return charset_pattern.match(input)
