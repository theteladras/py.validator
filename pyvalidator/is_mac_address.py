from typing import Literal, TypedDict, Union

from .utils.assert_string import assert_string
from .utils.merge import merge


class IsMacAddressOptions(TypedDict):
    no_separators: bool
    eui: Union[
        Literal[48],
        Literal[64],
        Literal[None],
    ]


default_mac_address_options: IsMacAddressOptions = {
    "no_separators": False,
    "eui": None
}


def is_mac_address(input: str, options={}) -> bool:
    input = assert_string(input)

    options = merge(options, default_mac_address_options)

    mac_address48 = r"^(?:[0-9a-fA-F]{2}([-:\s]))([0-9a-fA-F]{2}\1){4}([0-9a-fA-F]{2})$"
    mac_address48_no_separators = r"^([0-9a-fA-F]){12}$"
    mac_address48_with_dots = r"^([0-9a-fA-F]{4}\.){2}([0-9a-fA-F]{4})$"
    mac_address64 = r"^(?:[0-9a-fA-F]{2}([-:\s]))([0-9a-fA-F]{2}\1){6}([0-9a-fA-F]{2})$"
    mac_address64_no_separators = r"^([0-9a-fA-F]){16}$"
    mac_address64_with_dots = r"^([0-9a-fA-F]{4}\.){3}([0-9a-fA-F]{4})$"

    if options["no_separators"]:
        if options["eui"] == 48:
            return input.match(mac_address48_no_separators)
        if options["eui"] == 64:
            return input.match(mac_address64_no_separators)
        return input.match(mac_address48_no_separators) or input.match(mac_address64_no_separators)

    if options["eui"] == 48:
        return input.match(mac_address48) or input.match(mac_address48_with_dots)
    if options["eui"] == 64:
        return input.match(mac_address64) or input.match(mac_address64_with_dots)

    return (
        input.match(mac_address48) or
        input.match(mac_address48_with_dots) or
        input.match(mac_address64) or
        input.match(mac_address64_with_dots)
    )
