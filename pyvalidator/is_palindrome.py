from typing import TypedDict
from .utils.assert_string import assert_string
from .utils.merge import merge


class IsPalindromeOptions(TypedDict):
	insensitive: bool

default_is_palindrome_options: IsPalindromeOptions = {
  "insensitive": True,
}

def is_palindrome(input: str, options: IsPalindromeOptions = {}) -> bool:
    input = assert_string(input)

    options = merge(options, default_is_palindrome_options)

    input = input.sub(r'[^a-zA-Z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]', '')

    if not options['insensitive']: 
        return input == input[::-1]

    return input.lower() == input[::-1].lower()
