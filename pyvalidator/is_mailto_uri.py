from .utils.assert_string import assert_string
import re

def is_mailto_uri(input):
    input = assert_string(input)
    """
    The function checks if a given string is a valid mailto link with one or more email addresses
    separated by commas.

    :param input: The input string that needs to be checked if it is a valid mailto link or not. A mailto
    link is a hyperlink that opens the user's email client and pre-fills the "To" field with an email
    address. The link starts with "mailto:" followed by one or more email addresses separated by commas.
    :return: a boolean value (True or False) depending on whether the input string matches the
    specified pattern and contains at least one comma-separated email address.
    """
    pattern = r'^mailto:([\w.-]+@[\w.-]+\.\w+)(?:,([\w.-]+@[\w.-]+\.\w+))*\??(subject=([\w%]+))?(?:(&)?cc=([\w.-]+@[\w.-]+\.\w+))?(?:(&)?bcc=([\w.-]+@[\w.-]+\.\w+))?(?:(&)?body=([\w,\.\-\_%]+))?$'
    if re.match(pattern, input):
        return True
    return False

