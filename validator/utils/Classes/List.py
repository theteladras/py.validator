from typing import TypeVar, Union

from ..reduce import reduce
from ..map import map

T = TypeVar('T', bound='List')

class List(list):
    def map(self: T, cb) -> T:
        return List(map(self, cb))

    def reduce(self: T, cb, initializer=None) -> Union[str, int, float, bool, None]:
        return reduce(self, cb, initializer)

    @property
    def length(self: T):
        return len(self)
