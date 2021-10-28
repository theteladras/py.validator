import re

from .utils.assert_string import assert_string

bech32 = re.compile("^(bc1)[a-z0-9]{25,39}$")
base58 = re.compile("^(1|3)[A-HJ-NP-Za-km-z1-9]{25,39}$")

def is_btc_address(input: str) -> bool:
    assert_string(input)

    if input.startswith('bc1'):
        return bech32.match(input)

    return base58.match(input)
