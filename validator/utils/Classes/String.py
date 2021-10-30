from typing import TypeVar, Union

from ..slice import slice
from .List import List

T = TypeVar('T', bound='String')

class String(str):
    def slice(self, start: int, end: Union[int, None] = None) -> T:
        sliced_string = slice(self, start, end)
        return String(sliced_string)

    def split(self, separator = None) -> List:
        if bool(separator):
            string = self.__str__().split(separator)
            split_string = List(string)
            return split_string

        split_string =  List(self)
        return split_string

    @property
    def length(self):
        return len(self)
