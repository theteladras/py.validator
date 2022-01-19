from .utils.Classes.RegEx import RegEx
from .utils.assert_string import assert_string

hsl_comma = RegEx(r"^hsla?\(((\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?))(deg|grad|rad|turn)?(,(\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?)%){2}(,((\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?)%?))?\)$", 'i')
hsl_space = RegEx(r"^hsla?\(((\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?))(deg|grad|rad|turn)?(\s(\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?)%){2}\s?(\/\s((\+|\-)?([0-9]+(\.[0-9]+)?(e(\+|\-)?[0-9]+)?|\.[0-9]+(e(\+|\-)?[0-9]+)?)%?)\s?)?\)$", 'i')

def is_hsl(input: str) -> bool:
	input = assert_string(input)

	stripped = input.sub(r"\s+", ' ') \
					.sub(r"\s?(hsla\()\s?", 'hsla(', 'i') \
					.sub(r"\s?(hsl\()\s?", 'hsl(', 'i') \
					.sub(r"\s?(\))\s?", ')', 'i') \
					.sub(r"\s?(,)\s?", ',', 'i')
	
	if ',' in stripped:
		return stripped.match(hsl_comma)

	return stripped.match(hsl_space)
