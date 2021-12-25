from typing import TypedDict

from .utils.Classes.RegEx import RegEx
from .utils.Classes.String import String
from .utils.assert_string import assert_string
from .utils.merge import merge

class IsFqdnOptions(TypedDict):
    require_tld: bool
    allow_underscores: bool
    allow_trailing_dot: bool
    allow_numeric_tld: bool
    allow_wildcard: bool

default_fqdn_options: IsFqdnOptions = {
  "require_tld": True,
  "allow_underscores": False,
  "allow_trailing_dot": False,
  "allow_numeric_tld": False,
  "allow_wildcard": False,
}

def is_fqdn(input: str, options: IsFqdnOptions = {}) -> bool:
    input = assert_string(input)
    options = merge(options, default_fqdn_options)

    if options["allow_trailing_dot"] and input[input.length - 1] == '.':
        input = input.substring(0, input.length - 1)

    if options["allow_wildcard"] and input.index('*.') == 0:
        input = input.substring(2)

    parts = input.split('.')
    tld = String(parts[parts.length - 1])

    if options["require_tld"]:
        if parts.length < 2:
            return False
        if not tld.match(RegEx("^([a-z\u00A1-\u00A8\u00AA-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]{2,}|xn[a-z0-9-]{2,})$", 'i')):
            return False

        if RegEx('\s').findall(tld):
            return False

    if not options["allow_numeric_tld"] and tld.match("^\d+$"):
        return False

    for part in parts:
        part = String(part)
        if part.length > 63:
            return False
        if not part.match(r"^[a-z_\u00a1-\uffff0-9-]+$", 'i'):
            return False
        if part.match(r"[\uff01-\uff5e]"):
            return False
        if part.match(r"^-|-$"):
            return False
        if not options["allow_underscores"] and part.match(r"_"):
            return False

    return True
