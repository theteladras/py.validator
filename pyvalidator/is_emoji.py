from typing import TypedDict

from .utils.Classes.String import String
from .utils.assert_string import assert_string
from .utils.merge import merge

emoji_patterns = (
    "^["
    r"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    r"\U0001F300-\U0001F5FF"  # symbols & pictographs
    r"\U0001F600-\U0001F64F"  # emoticons
    r"\U0001F680-\U0001F6FF"  # transport & map symbols
    r"\U0001F700-\U0001F77F"  # alchemical symbols
    r"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    r"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    r"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    r"\U0001FA00-\U0001FA6F"  # Chess Symbols
    r"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    r"\U00002702-\U000027B0"  # Dingbats
    "]$"
)


class IsEmojiOptions(TypedDict):
    omit_rule: str


default_emoji_options: IsEmojiOptions = {
    "omit_rule": None,
}


def is_emoji(input: str, options: IsEmojiOptions = {}) -> bool:
    input = assert_string(input)

    options = merge(options, default_emoji_options)

    def is_flag_emoji(c):
        return (
            r"\U0001F1E6\U0001F1E8" <= c <= r"\U0001F1FF\U0001F1FC"
            or (
                c in [
                    r"\U0001F3F4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
                    r"\U0001F3F4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f",
                    r"\U0001F3F4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f"
                ]
            )
        )

    if options["omit_rule"] is not None:
        input = input.sub(options["omit_rule"], '')

    if not input.length:
        return False

    for char in input:
        char = String(char)
        if not (char.match(emoji_patterns) or is_flag_emoji(char)):
            return False

    return True
