import inspect


def to_string(input):
    if type(input).__name__ == 'str':
        return input
    elif type(input).__name__ == 'int' or type(input).__name__ == 'float':
        return str(input)
    elif type(input).__name__ == 'dict' or type(input).__name__ == 'list' or inspect(input):
        return '[object Object]'
    return ''
