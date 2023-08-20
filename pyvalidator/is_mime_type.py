from .utils.Classes.RegEx import RegEx

from .utils.assert_string import assert_string

_mime_type_simple = RegEx(
    '^(application|audio|font|image|message|model|multipart|text|video)\/[a-zA-Z0-9\.\-\+_]{1,100}$', 'i')

_mime_type_text = RegEx(
    '^text\/[a-zA-Z0-9\.\-\+]{1,100};\s?charset=("[a-zA-Z0-9\.\-\+\s]{0,70}"|[a-zA-Z0-9\.\-\+]{0,70})(\s?\([a-zA-Z0-9\.\-\+\s]{1,20}\))?$',
    'i')
_mime_type_multipart = RegEx(
    '^multipart\/[a-zA-Z0-9\.\-\+]{1,100}(;\s?(boundary|charset)=("[a-zA-Z0-9\.\-\+\s]{0,70}"|[a-zA-Z0-9\.\-\+]{0,70})(\s?\([a-zA-Z0-9\.\-\+\s]{1,20}\))?){0,2}$',
    'i')


def is_mime_type(input: str):
    input = assert_string(input)
    return _mime_type_simple.match(input) or _mime_type_text.match(input) or _mime_type_multipart.match(input)
