from typing import Literal

from .utils.assert_string import assert_string
from .utils.Classes.RegEx import RegEx
from .utils.includes import includesNot

ip_v4_segment= "(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
ip_v4_address = "({}[.]){{3}}{}".format(ip_v4_segment, ip_v4_segment)
ip_v4_address_pattern = RegEx('^' + ip_v4_address + '$')

ip_v6_segment_format = "(?:[0-9a-fA-F]{1,4})"
ip_v6_address_part_1 = "^((?:{}:){{7}}(?:{}|:)|".format(ip_v6_segment_format, ip_v6_segment_format)
ip_v6_address_part_2 = "(?:{}:){{6}}(?:{}|:{}|:)|".format(ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_3 = "(?:{}:){{5}}(?::{}|(:{}){{1,2}}|:)|".format(ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_4 = "(?:{}:){{4}}(?:(:{}){{0,1}}:{}|(:{}){{1,3}}|:)|".format(ip_v6_segment_format, ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_5 = "(?:{}:){{3}}(?:(:{}){{0,2}}:{}|(:{}){{1,4}}|:)|".format(ip_v6_segment_format, ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_6 = "(?:{}:){{2}}(?:(:{}){{0,3}}:{}|(:{}){{1,5}}|:)|".format(ip_v6_segment_format, ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_7 = "(?:{}:){{1}}(?:(:{}){{0,4}}:{}|(:{}){{1,6}}|:)|".format(ip_v6_segment_format, ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_8 = "(?::((?::{}){{0,5}}:{}|(?::{}){{1,7}}|:))".format(ip_v6_segment_format, ip_v4_address, ip_v6_segment_format)
ip_v6_address_part_9 = ")(%[0-9a-zA-Z-.:]{1,})?$"
ip_v6_address = (
    ip_v6_address_part_1 +
    ip_v6_address_part_2 +
    ip_v6_address_part_3 +
    ip_v6_address_part_4 +
    ip_v6_address_part_5 +
    ip_v6_address_part_6 +
    ip_v6_address_part_7 +
    ip_v6_address_part_8 +
    ip_v6_address_part_9
)
ip_v6_address_pattern = RegEx(ip_v6_address)

ip_versions = [4, 6, '4', '6']

def is_ip(input: str, version: Literal[4, 6, '4', '6', None] = None) -> bool:
    input = assert_string(input)

    if version == None:
        return is_ip(input, 4) or is_ip(input, 6)

    if includesNot(ip_versions, version):
        return False

    if version == 6 or version == '6':
        return ip_v6_address_pattern.match(input)

    if not ip_v4_address_pattern.match(input):
        return False

    parts = input.split('.')
    parts.sort()

    try:
        return int(parts[3]) <= 255
    except:
        return False



