from .alpha import decimal
from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.includes import includes
from .utils.math import gather_then_check, less_then_check
from .utils.merge import merge

__default_options = {
    "min": None,
    "max": None,
    "lt": None,
    "gt": None,
    "locale": None,
}


def is_float(input: str, options=__default_options) -> bool:
    input = assert_string(input)

    options = merge(options, __default_options)

    if includes(['+', '-', '.', ''], input):
        return False

    float_pattern = RegEx(r"^(?:[-+])?(?:[0-9]+)?(?:\{}[0-9]*)?(?:[eE][\+\-]?(?:[0-9]+))?$".format(decimal[options["locale"]] if bool(options["locale"]) else '.'))

    transformed_input = input.sub(',', '.').sub('٫', '.')

    is_valid = float_pattern.match(input)

    min_valid = gather_then_check(transformed_input, options["min"])
    max_valid = less_then_check(transformed_input, options["max"])
    gt_valid = gather_then_check(transformed_input, options["gt"])
    lt_valid = less_then_check(transformed_input, options["lt"])

    return is_valid and min_valid and max_valid and lt_valid and gt_valid
