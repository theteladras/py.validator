from .utils.assert_string import assert_string

magnet_uri_pattern = r"(?:^magnet:\?(tr=udp://.+&)?)xt(?:\.1)?=urn:(?:(?:aich|bitprint|btih|ed2k|ed2khash|kzhash|md5|sha1|tree:tiger):[a-z0-9]{32}(?:[a-z0-9]{8})?|btmh:1220[a-z0-9]{64})(?:$|&)"


def is_magnet_uri(input: str) -> bool:
    input = assert_string(input)
    
    if input.index_of('magnet:?') != 0:
        return False

    return input.match(magnet_uri_pattern, 'i')
    
