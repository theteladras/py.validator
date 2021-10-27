import re

from utils.assert_string import assert_string
from alpha import alpha

def is_alpha(input, locale = 'en-US', options = {}):
    assert_string(input)

    string = input

    if 'ignore' in options and options['ignore']:
        ignore = options['ignore']
        if type(ignore).__name__ == 'str':
            pattern = "[{}]".format(re.escape(ignore))
            
            string = re.sub(pattern, '', string)
            print(pattern)
        else:
            raise Exception('ignore should be instance of a String or RegExp')

    if locale in alpha:
        pattern = re.compile(alpha[locale], re.IGNORECASE)
        isMatched = pattern.match(string)
        return bool(isMatched)

    raise Exception("Invalid locale {}".format(locale))
            
locales = list(alpha.keys())
