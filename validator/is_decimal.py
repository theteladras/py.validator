from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.merge import merge
from .utils.includes import includesNot
from .alpha import decimal

def decimal_regexp(options):
    local = options["locale"]
    local_decimal = decimal[local]
    decimal_digits = options["decimal_digits"]
    require_decimal = '' if options["force_decimal"] else '?'
    regex = "^[-+]?([0-9]+)?(\{}[0-9]{{".format(local_decimal) + "{}}}){}$".format(decimal_digits, require_decimal)
    return RegEx(regex)

default_decimal_options = {
  "force_decimal": False,
  "decimal_digits": '1,',
  "locale": 'en-US',
}

blacklist = ['', '-', '+']

def is_decimal(input: str, options = {}) -> bool:
    input = assert_string(input)

    input = input.rstrip()

    options = merge(options, default_decimal_options)

    if options["locale"] not in decimal:
        raise Exception("Invalid locale '{}'".format(options["locale"]))

    without_white_space = input.sub(" ", '')
    return includesNot(blacklist, without_white_space) and bool(decimal_regexp(options).match(input))

