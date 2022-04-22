import http.client as httplib
import urllib.request
from typing import Union

from .is_url import is_url
from .utils.assert_string import assert_string


def is_online(input: Union[str, None] = None) -> bool:
    if not bool(input):
        conn = httplib.HTTPSConnection('8.8.8.8', timeout=5)
        try:
            conn.request('HEAD', '/')
            return True
        except Exception:
            return False
        finally:
            conn.close()

    input = assert_string(input)

    valid_url = is_url(input)

    if not valid_url:
        return False

    try:
        contains_protocol = input.match(r"^http(s)?://.*")
        if not contains_protocol:
            input = "http://{}".format(input)
        urllib.request.urlopen(input, timeout=100).getcode()
        return True
    except Exception:
        return False
