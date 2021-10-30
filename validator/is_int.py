import re

from .utils.assert_string import assert_string
from .utils.merge import merge

int_pattern = re.compile("^(?:[-+]?(?:0|[1-9][0-9]*))$")
int_leading_zero_pattern = re.compile("^[-+]?[0-9]+$")

__default_options = {
    "allow_leading_zeroes": True,
    "min": None,
    "max": None,
    "lt": None,
    "gt": None,
}

def is_int(input: str, options = __default_options) -> bool:
    input = assert_string(input)

    options = merge(options, __default_options)

    allow_leading_zeroes = options["allow_leading_zeroes"]

    picked_regex = int_pattern if not allow_leading_zeroes else int_leading_zero_pattern

    input_valid = bool(picked_regex.match(input))

    min_check_passed = not bool(options["min"]) or input >= str(options["min"])
    max_check_passed = not bool(options["max"]) or input <= str(options["max"])
    lt_check_passed = not bool(options["lt"]) or input > str(options["lt"])
    gt_check_passed = not bool(options["gt"]) or input < str(options["gt"])

    return input_valid and min_check_passed and max_check_passed and lt_check_passed and gt_check_passed
