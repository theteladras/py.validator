from typing import Union

__map = map


def map(item: Union[str, list], cb):
    cb_num_arg = cb.__code__.co_argcount
    if cb_num_arg == 1:
        return __map(cb, item)
    elif cb_num_arg == 2:
        return __map(cb, item, range(item.length))
    else:
        empty_args = ['None' * item.length] * (cb_num_arg - 2)
        arguments = [cb, item, range(item.length), *empty_args]
        return __map(*arguments)
