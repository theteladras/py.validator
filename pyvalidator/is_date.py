from typing import TypedDict, List as ListT, Tuple, Union, Literal

from .utils.Classes.RegEx import RegEx
from .utils.Classes.List import List
from .utils.Classes.String import String
from .utils.assert_string import assert_string
from .utils.merge import merge
from .utils.to_date import to_date

date_format_pattern = RegEx(r"(^(y{4}|y{2})[|:;,.\/-](m{1,2})[|:;,.\/-](d{1,2})$)|(^(m{1,2})[|:;,.\/-](d{1,2})[|:;,.\/-]((y{4}|y{2})$))|(^(d{1,2})[|:;,.\/-](m{1,2})[|:;,.\/-]((y{4}|y{2})$))", 'i')

class IsDateOptions(TypedDict):
    format: Union[
        Literal['DD/MM/YYYY'],
        Literal['D/MM/YYYY'],
        Literal['D/M/YYYY'],
        Literal['D/M/YY'],
        Literal['D/MM/YY'],
        Literal['DD/MM/YY'],
        Literal['YYYY/MM/DD'],
        Literal['YYYY/MM/D'],
        Literal['YYYY/M/D'],
        Literal['YY/M/D'],
        Literal['YY/MM/D'],
        Literal['YY/MM/DD'],
        Literal['MM/DD/YYYY'],
        Literal['M/DD/YYYY'],
        Literal['M/D/YYYY'],
        Literal['M/D/YY'],
        Literal['M/DD/YY'],
        Literal['MM/DD/YY'],
    ]
    delimiters: ListT[Union[
        Literal['|'],
        Literal[':'],
        Literal[';'],
        Literal[','],
        Literal['.'],
        Literal['-'],
        Literal['/'],
    ]]
    strict_mode: bool

__default_options: IsDateOptions = {
  "format": 'YYYY/MM/DD',
  "delimiters": ['/', '-'],
  "strict_mode": False,
}

def zip(date_list: ListT[str], format_list: ListT[str]) -> ListT[Tuple[str, str]]:
    zipped = []
    smaller_list = date_list if date_list.length < format_list.length else format_list
    for i, _ in enumerate(smaller_list):
        zipped.append([date_list[i], format_list[i]])
    return zipped

def is_date(input: str, options: IsDateOptions = {}) -> bool:
    input = assert_string(input)

    options = merge(options, __default_options)

    format = String(options['format'])

    if not date_format_pattern.match(format):
        raise Exception('Not supported format provided: ', format)

    format_delimiter: Union[str, None] = List(options['delimiters']).find(lambda delimiter, _: delimiter in format)

    date_delimiter = format_delimiter if options['strict_mode'] else '/'
    if not date_delimiter:
        return False

    input_delimiter: Union[str, None] = List(options['delimiters']).find(lambda delimiter, _: delimiter in input)

    if not input_delimiter:
        return False

    format = format if options['strict_mode'] else format.sub("\{}".format(input_delimiter), '/')
    input = input if options['strict_mode'] else input.sub("\{}".format(input_delimiter), '/')

    format_tupples = zip(
        input.split(date_delimiter),
        format.lower().split(date_delimiter)
    )

    date_dict = {}

    for format_tupple in format_tupples:
        if len(format_tupple[0]) != len(format_tupple[1]):
            return False
        format_char = format_tupple[1][0]
        date_dict[format_char] = format_tupple[0]

    return bool(to_date("{}/{}/{}".format(date_dict['m'], date_dict['d'], date_dict['y'])))
