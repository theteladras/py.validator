from typing import List


def join(array: List[str], join_with: str = '') -> str:
    string = ""
    for i, item in enumerate(array):
        string = string + item
        if i != (len(array) - 1):
            string = string + join_with

    return string
