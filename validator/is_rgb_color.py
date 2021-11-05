from .utils.assert_string import assert_string

rgb_color = "^rgb\((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]),){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\)$"
rgba_color = "^rgba\((([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]),){3}(0?\.\d|1(\.0)?|0(\.0)?)\)$"
rgb_color_percent = "^rgb\((([0-9]%|[1-9][0-9]%|100%),){2}([0-9]%|[1-9][0-9]%|100%)\)"
rgba_color_percent = "^rgba\((([0-9]%|[1-9][0-9]%|100%),){3}(0?\.\d|1(\.0)?|0(\.0)?)\)"

def is_rgb_color(input: str, include_percent_values: bool = True) -> bool:
    input = assert_string(input)

    is_valid_no_percent_color: bool = input.match(rgb_color) or input.match(rgba_color)

    if not include_percent_values:
        return is_valid_no_percent_color

    is_valid_percent_color: bool = input.match(rgb_color_percent) or input.match(rgba_color_percent)

    return is_valid_no_percent_color or is_valid_percent_color
