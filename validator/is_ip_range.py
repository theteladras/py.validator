from typing import Union

from .utils.assert_string import assert_string
from .utils.Classes.String import String
from .is_ip import is_ip

subnet_maybe = "^\d{1,3}$"
subnet_v4 = 32
subnet_v6 = 128

def is_ip_range(input: str, version: Union[str, int] = None) -> bool:
    try:
        input = assert_string(input)

        parts = input.split('/')

        ip_part = String(parts[0])

        subnet_part = String(parts[1])

        if parts.length != 2:
            return False

        is_subnet_maybe = subnet_part.match(subnet_maybe)

        if not is_subnet_maybe:
            return False
        
        if subnet_part.length > 1 and subnet_part.starts_with('0'):
            return False

        is_valid_ip = is_ip(ip_part, version)

        if not is_valid_ip:
            return False

        expected_subnet = None
        if String(version) == '4':
            expected_subnet = subnet_v4
        elif String(version) == '6':
            expected_subnet = subnet_v6
        else:
            expected_subnet = subnet_v6 if is_ip(ip_part, '6') else subnet_v4

        return int(subnet_part) <= expected_subnet and int(subnet_part) >= 0
    except:
        return False
