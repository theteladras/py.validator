from typing import Any, Callable, TypeVar, Union

from ..includes import includes
from ..map import map
from ..reduce import reduce

T = TypeVar('T', bound='List')


class List(list):
    def map(self: T, cb) -> T:
        return List(map(self, cb))

    def reduce(self: T, cb, initializer=None) -> Union[str, int, float, bool, None]:
        return reduce(self, cb, initializer)

    @property
    def length(self: T) -> int:
        return len(self)

    def includes(self: T, val: Union[None, bool, str, int, float]) -> bool:
        return includes(self, val)

    def pop(self: T) -> Any:
        return list(self).pop()

    def join(self: T, join_with: str) -> str:
        return join_with.join(self)

    def find(self, cb: Callable[[Any, int], bool]) -> Union[Any, None]:
        for index, item in enumerate(self):
            if cb(item, index):
                return item
        return None
