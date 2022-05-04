from typing import TypeVar

T = TypeVar('T')


def merge(main_dict: T, default_dict: T) -> T:
    return {**default_dict, **main_dict}
