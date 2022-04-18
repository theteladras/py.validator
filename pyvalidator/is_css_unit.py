from .utils.assert_string import assert_string


def is_css_unit(input: str) -> bool:
    input = assert_string(input)

    pattern = r"^((-?(\d*\.)?\d+)((px)|(em)|(%)|(ex)|(ch)|(rem)|(vw)|(vh)|(vmin)|(vmax)|(cm)|(mm)|(in)|(pt)|(pc))|0)$"

    return input.match(pattern)
