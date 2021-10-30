from typing import TypeVar

from ..reduce import reduce

T = TypeVar('T', bound='List')

class List(list):
    def map(self, cb) -> T:
        cb_num_arg = cb.__code__.co_argcount
        if cb_num_arg == 1:
            return List(map(cb, self))
        elif cb_num_arg == 2:
            return List(map(cb, self, range(self.__len__())))
        else:
            empty_args = ['None' * self.__len__()] * (cb_num_arg - 2)
            arguments = [cb, self, range(self.__len__()), *empty_args]
            return List(map(*arguments))

    def reduce(self, cb, initializer=None):
        return reduce(self, cb, initializer)
