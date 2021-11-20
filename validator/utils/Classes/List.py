from typing import TypeVar, Union

from ..reduce import reduce
from ..map import map
from ..includes import includes

T = TypeVar('T', bound='List')

class List(list):
    def map(self: T, cb) -> T:
        return List(map(self, cb))

    def reduce(self: T, cb, initializer=None) -> Union[str, int, float, bool, None]:
        return reduce(self, cb, initializer)

    @property
    def length(self: T):
        return len(self)

    def includes(self: T, val: Union[None, bool, str, int, float]) -> bool:
        return includes(self, val)
