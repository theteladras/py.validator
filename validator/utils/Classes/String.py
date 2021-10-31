from typing import TypeVar, Union

from ..slice import slice
from .List import List
from .RegEx import RegEx

T = TypeVar('T', bound='String')

class String(str):
    def slice(self: T, start: int, end: Union[int, None] = None) -> T:
        sliced_string = slice(self, start, end)
        return String(sliced_string)

    def split(self: T, separator = None) -> List:
        if bool(separator):
            string = self.__str__().split(separator)
            split_string = List(string)
            return split_string

        split_string =  List(self)
        return split_string

    @property
    def length(self: T):
        return len(self)

    def sub(self: T, pattern: str, replacement: str) -> str:
        return String(RegEx.sub(pattern, replacement, self.__str__()))
