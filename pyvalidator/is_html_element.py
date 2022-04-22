from typing import TypedDict

from .utils.assert_string import assert_string


class IsHtmlElementOptions(TypedDict):
    contains: bool


default_email_options: IsHtmlElementOptions = {
    "contains": False
}


def is_html_element(input: str, options: IsHtmlElementOptions = default_email_options) -> bool:
    input = assert_string(input).trim()

    html_contains_pattern = r"<\s*?[^/<>]*(!DOCTYPE|!--|br|basefont|hr|source|frame|param|area|meta|col|link|option|base|img|wbr)[^<>]*?>|<\s*?[^<>]*input\s*?[^<>]*/>|<\s*?[^<>]*(a|abbr|acronym|address|applet|article|aside|audio|body|b|bdi|bdo|big|blockquote|button|canvas|caption|center|cite|code|colgroup|command|datalist|dd|del|details|dfn|dialog|dir|div|dl|dt|em|embed|fieldset|figcaption|figure|font|footer|form|frameset|head|header|hgroup|h1|h2|h3|h4|h5|h6|html|i|iframe|ins|kbd|keygen|label|legend|li|map|mark|menu|meter|noframes|nav|noscript|object|ol|optgroup|output|p|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|small|span|strike|strong|style|sub|summary|sup|table|tbody|td|textarea|tfoot|th|thead|time|title|tr|track|tt|u|ul|var|video)(((\s+)[a-z\-A-Z]*=\".*\")|((\s+)[a-zA-Z])*)?(\s+)?>[\s\S]*?(<(\s+)?/(\s+)?\2(\s+)?>)"
    html_strict = "^{}$".format(html_contains_pattern)

    if options["contains"]:
        index = input.search(html_contains_pattern)
        return True if index != None else False

    return input.match(html_strict)
