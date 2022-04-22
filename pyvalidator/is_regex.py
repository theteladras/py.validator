from typing import TypedDict

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.join import join
from .utils.merge import merge


class IsRegExpOptions(TypedDict):
    with_flags: bool


default_email_options: IsRegExpOptions = {
    "with_flags": False
}


def is_regex(input: str, options={}) -> bool:
    input = assert_string(input)

    if not input:
        return False

    options = merge(options, default_email_options)

    if options["with_flags"]:
        rgx = r"^/.+/([gimsuyd]){0,7}?$"

        if not input.match(rgx):
            return False

        input = join(input.split('/')[1:-1])

        if not input:
            return False

    try:
        RegEx(input)
        return True
    except:
        return False
