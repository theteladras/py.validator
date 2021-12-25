from .utils.assert_string import assert_string

default_options = { "loose": False }
strict_booleans = ['true', 'false', '1', '0']
loose_booleans = [*strict_booleans, 'yes', 'no', 'y', 'n']

def is_boolean(input: str, options = default_options) -> bool:
    assert_string(input)

    input_lower_case = input.lower()

    if options["loose"]:
        return input_lower_case in loose_booleans

    return input_lower_case in strict_booleans

