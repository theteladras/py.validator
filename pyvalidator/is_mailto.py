import re

def is_valid_mailto_link(link):
    """
    The function checks if a given string is a valid mailto link with one or more email addresses
    separated by commas.

    :param link: The input string that needs to be checked if it is a valid mailto link or not. A mailto
    link is a hyperlink that opens the user's email client and pre-fills the "To" field with an email
    address. The link starts with "mailto:" followed by one or more email addresses separated by commas.
    :return: a boolean value (True or False) depending on whether the input string `link` matches the
    specified pattern and contains at least one comma-separated email address.
    """
    pattern = r'^mailto:\s*([^,\s@]+@[^\s@]+\.[^\s@]+)(, [^,\s@]+@[^\s@]+\.[^\s@]+)*$'
    if re.match(pattern, link):
        return True
    return False

