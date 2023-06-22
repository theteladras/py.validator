import re

def is_valid_container_number(container_number)-> bool:
    """
    The function checks if a given container number matches a specific pattern and returns True if it
    does, False otherwise.
    
    :param container_number: The parameter `container_number` is a string representing a container
    number that needs to be validated
    :return: a boolean value (True or False) depending on whether the input string matches the specified
    pattern or not.
    """
    pattern: str = r'^[A-Z]{4}\d{6}$'
    if re.match(pattern, container_number) is not None:
        return True
    return False