import re

from utils.assert_string import assert_string
from utils.merge import merge
from utils.index_of import index_of

not_base64 = re.compile("[^A-Z0-9+\/=]", re.IGNORECASE)
url_safe_base64 = re.compile("^[A-Z0-9_\-]*$", re.IGNORECASE)

default_base64_options = {
    "urlSafe": False
}

def is_base64(input, options = {}):
    assert_string(input)
    merge(options, default_base64_options)
    input_length = len(input)

    if options.url_safe:
        return url_safe_base64.match(input)

    if len % 4 != 0 or not_base64.match(input):
        return False

    first_padding_char = index_of(input, '=')
    return (
        first_padding_char == -1 or
        first_padding_char == input_length - 1 or
        (
            first_padding_char == input_length - 2 and 
            input[input_length - 1] == '='
        )
    )
