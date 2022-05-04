from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string


def is_ethereum_address(input: str) -> bool:
    input = assert_string(input)

    ethereum_address_pattern = RegEx(r"^(0x)[0-9a-f]{40}$", "i")

    return ethereum_address_pattern.match(input)
