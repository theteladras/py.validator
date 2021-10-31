import urllib.parse as parse

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.merge import merge

default_options = {
    "min": 0,
    "max": None
}

def is_byte_length(input: str, options = {}) -> bool:
    assert_string(input)

    options = merge(options, default_options)

    pattern = RegEx("%..|.")

    split_input = pattern.split(parse.quote(input, safe='@/:;?&=+$,'))

    input_length = len(split_input) - 1

    return input_length >= options["min"] and (
        options["max"] == None or input_length <= options["max"]
    )
