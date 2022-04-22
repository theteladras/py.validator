from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.index_of import index_of
from .utils.merge import merge

default_base64_options = {
    "url_safe": False
}


def is_base64(input: str, options={}) -> bool:
    assert_string(input)

    not_base64 = RegEx("[^A-Z0-9+\/=]", "i")
    url_safe_base64 = RegEx("^[A-Z0-9_\-]*$", "i")

    options = merge(options, default_base64_options)
    input_length = len(input)

    if options["url_safe"]:
        return url_safe_base64.match(input)

    if (input_length % 4) != 0 or not_base64.match(input):
        return False

    first_padding_char = index_of(input, "=")
    return (
        first_padding_char == -1 or
        first_padding_char == input_length - 1 or
        (
            first_padding_char == input_length - 2 and
            input[input_length - 1] == "="
        )
    )
