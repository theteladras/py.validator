from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string
from .alpha import alpha

def is_alpha(input, locale = 'en-US', options = {}):
    input = assert_string(input)

    if 'ignore' in options and options['ignore']:
        ignore = options['ignore']
        if type(ignore).__name__ == 'str':
            pattern = "[{}]".format(RegEx.escape(ignore))
            
            input = input.sub(pattern, '')
        else:
            raise Exception('ignore should be instance of a String or RegExp')

    if locale in alpha:
        pattern = RegEx(alpha[locale], 'i')
        return pattern.match(input)

    raise Exception("Invalid locale {}".format(locale))
            
locales = list(alpha.keys())
