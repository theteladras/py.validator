from typing import TypedDict

from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .utils.merge import merge

class IsEmailOptions(TypedDict):
    allow_hyphens: bool

default_email_options: IsEmailOptions = {
  "allow_hyphens": False,
}

imei_regex_without_hypens = r"^[0-9]{15}$"
imei_regex_with_hypens = r"^\d{2}-\d{6}-\d{6}-\d{1}$"

def is_imei(input: str, options = {}) -> bool:
    input = assert_string(input)
    options = merge(options, default_email_options)

    imei_regex = imei_regex_with_hypens if options["allow_hyphens"] else imei_regex_without_hypens

    if not input.match(imei_regex):
        return False

    input = input.sub(RegEx('-', 'g'), '')

    sum = 0
    mul = 2
    l = 14

    for i in range(14):
        digit = input.substring(l - i - 1, l - i)
        tp = int(digit) * mul
        if tp >= 10:
            sum += (tp % 10) + 1
        else:
            sum += tp
        if mul == 1:
            mul += 1
        else:
            mul -= 1

    chk = ((10 - (sum % 10)) % 10)

    if chk != int(input.substring(14, 15)):
        return False
    return True
