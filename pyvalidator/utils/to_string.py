import inspect


def to_string(input):
    if isinstance(input, str):
        # in case a custom string type is passed, return as an actual str
        return str(input)
    elif isinstance(input, (int, float)):
        return str(input)
    elif isinstance(input, (dict, list)) or inspect.ismodule(input):
        return '[object Object]'
    return ''
