import urllib.parse as parse
import re

from .utils.assert_string import assert_string
from .utils.merge import merge

default_options = {
    "min": 0,
    "max": None
}

def is_byte_length(input: str, options = {}) -> bool:
    assert_string(input)

    options = merge(options, default_options)

    input_length = len(re.split("%..|.", parse.quote(input, safe='@/:;?&=+$,'))) - 1

    return input_length >= options["min"] and (
        options["max"] == None or input_length <= options["max"]
    )
