from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string


def is_semantic_version(input: str) -> bool:
    input = assert_string(input)

    semantic_version_pattern = RegEx(
        r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)" +
        r"(?:-((?:0|[1-9]\d*|\d*[a-z-][0-9a-z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-z-][0-9a-z-]*))*))" +
        r"?(?:\+([0-9a-z-]+(?:\.[0-9a-z-]+)*))?$", "i"
    )

    return semantic_version_pattern.match(input)
