import re
from typing import Union

from .utils.assert_string import assert_string
from .utils.includes import includes
from .utils.merge import merge
from .utils.merge import merge
from .alpha import decimal

__default_options = {
    "min": None,
    "max": None,
    "lt": None,
    "gt": None,
    "locale": None,
}

def is_float(input: Union[int, float, str], options = __default_options) -> bool:
    assert_string(input)

    options = merge(options, __default_options)

    print('options: ', options)

    if includes(['+', '-', '.', ''], input):
        return False

    float_pattern = re.compile("^(?:[-+])?(?:[0-9]+)?(?:\{}[0-9]*)?(?:[eE][\+\-]?(?:[0-9]+))?$".format(decimal[options["locale"]] if bool(options["locale"]) else '.'))

    try:
        transformed_input = re.sub(',', '.', input)
        transformed_input = re.sub('٫', '.', input)
        float_input = float(transformed_input)

        is_valid = bool(float_pattern.match(input))
        min_valid = (not __default_options["min"]) or float_input >= options["min"]
        max_valid = (not __default_options["max"]) or float_input <= options["max"]
        lt_valid = (not __default_options["lt"]) or float_input <= options["lt"]
        gt_valid = (not __default_options["gt"]) or float_input >= options["gt"]
        return is_valid and min_valid and max_valid and lt_valid and gt_valid
    except:
        return False
