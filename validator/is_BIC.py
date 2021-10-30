import re

from .utils.assert_string import assert_string
from .utils.slice import slice_and_upper_case
from .is_ISO31661_alpha2 import country_codes

is_bic_reg = re.compile('^[A-Za-z]{6}[A-Za-z0-9]{2}([A-Za-z0-9]{3})?$')

def is_bic(input):
    assert_string(input)

    if not slice_and_upper_case(input, 4, 6) in country_codes:
        return False

    return is_bic_reg.match(input)
