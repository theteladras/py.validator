from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.merge import merge
from .utils.join import join

def currency_regex(options):
    decimal_digits = "\d{" + str(options["digits_after_decimal"][0]) + "}"
    for index, digit in enumerate(options["digits_after_decimal"]):
        if index != 0:
            decimal_digits = "{}|\d{}{}{}".format(decimal_digits, '{', digit, '}')
    
    def __match(x):
        return "\\{}".format(x.group(0))

    symbol = "({}){}".format(RegEx.sub("\W", __match, options["symbol"]), '' if options["require_symbol"] else '?')
    negative = '-?'
    whole_dollar_amount_without_sep = '[1-9]\d*'
    whole_dollar_amount_with_sep = "[1-9]\d{{0,2}}({}\d{{3}})*".format(options["thousands_separator"])
    valid_whole_dollar_amounts = [
        '0',
        whole_dollar_amount_without_sep,
        whole_dollar_amount_with_sep
    ]
    whole_dollar_amount = "({})?".format(join(valid_whole_dollar_amounts, '|'))
    decimal_amount = "(\{}({})){}".format(options["decimal_separator"], decimal_digits, '' if options["require_decimal"] else '?')
    pattern = "{}{}".format(
        whole_dollar_amount,
        decimal_amount if (options["allow_decimal"] or options["require_decimal"]) else ''
    )

    if options["allow_negatives"] and not options["parens_for_negatives"]:
        if options["negative_sign_after_digits"]:
            pattern += negative
        elif options["negative_sign_before_digits"]:
            pattern = negative + pattern

    if options["allow_negative_sign_placeholder"]:
        pattern = "( (?!\-))?" + pattern
    elif options["allow_space_after_symbol"]:
        pattern = " ?" + pattern
    elif options["allow_space_after_digits"]:
        pattern += '( (?!$))?'

    if options["symbol_after_digits"]:
        pattern += symbol
    else:
        pattern = symbol + pattern

    if options["allow_negatives"]:
        if options["parens_for_negatives"]:
            pattern = "(({})|{})".format(pattern, pattern)
        elif not (options["negative_sign_before_digits"] and options["negative_sign_after_digits"]):
            pattern = negative + pattern

    return RegEx("^(?!-? )(?=.*\d){}$".format(pattern))

default_currency_options = {
  "symbol": "$",
  "require_symbol": False,
  "allow_space_after_symbol": False,
  "symbol_after_digits": False,
  "allow_negatives": True,
  "parens_for_negatives": False,
  "negative_sign_before_digits": False,
  "negative_sign_after_digits": False,
  "allow_negative_sign_placeholder": False,
  "thousands_separator": ',',
  "decimal_separator": '.',
  "allow_decimal": True,
  "require_decimal": False,
  "digits_after_decimal": [2],
  "allow_space_after_digits": False,
}

def is_currency(input: str, options = {}) -> bool:
    assert_string(input)
    options = merge(options, default_currency_options)
    return bool(currency_regex(options).match(input))
