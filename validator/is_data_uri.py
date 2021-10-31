from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

valid_media_type = RegEx("^[a-z]+\/[a-z0-9\-\+]+$", 'i')

valid_attribute = RegEx("^[a-z\-]+=[a-z0-9\-]+$", 'i')

valid_data = RegEx("^[a-z0-9!\$&'\(\)\*\+,;=\-\._~:@\/\?%\s]*$", 'i')

def is_data_uri(input: str) -> bool:
    assert_string(input)

    data = input.split(',')

    if len(data) < 2:
        return False

    attributes = data.pop(0).strip().split(';')
    scheme_and_media_type = attributes.pop(0)

    has_required_prefix = scheme_and_media_type[0:5] == 'data:'

    if not has_required_prefix:
        return False

    media_type = scheme_and_media_type[5:]

    is_valid_media_type = bool(valid_media_type.match(media_type))

    if media_type != '' and not is_valid_media_type:
        return False

    for i, attribute in enumerate(attributes):
        is_last_item = i == len(attributes) - 1
        is_base64 = attribute.lower() == 'base64'
        is_valid_attribute = valid_attribute.match(attribute)

        if not (is_last_item and is_base64) and not is_valid_attribute:
            return False

    for item in data:
        is_valid_data = valid_data.match(item)
        if not is_valid_data:
            return False

    return True
