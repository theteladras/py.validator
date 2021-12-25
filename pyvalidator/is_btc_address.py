from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

bech32 = RegEx("^(bc1)[a-z0-9]{25,39}$")
base58 = RegEx("^(1|3)[A-HJ-NP-Za-km-z1-9]{25,39}$")

def is_btc_address(input: str) -> bool:
    input = assert_string(input)

    if input.startswith('bc1'):
        return bech32.match(input)

    return base58.match(input)
