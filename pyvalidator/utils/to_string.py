import inspect

# Storing as an object so that tests will continue to function properly if this string is ever changed
obj_str = '[object Object]'


def to_string(input):
    if isinstance(input, str):
        # in case a custom string type is passed, return as an actual str
        return str(input)
    elif isinstance(input, (int, float)):
        return str(input)
    elif isinstance(input, (dict, list)) or inspect.ismodule(input):
        return obj_str
    return ''
