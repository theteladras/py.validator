from typing import List, TypedDict

from .utils.assert_string import assert_string
from .utils.merge import merge


class IsUrlOptions(TypedDict):
    no_scheme: bool
    with_no_path: bool
    insensitive: bool
    top_level_domains: List[str]
    domains: List[str]


default_email_options: IsUrlOptions = {
    "no_scheme": False,
    "with_no_path": False,
    "insensitive": True,
    "top_level_domains": [],
    "domains": [],
}


def is_url(input: str, options={}) -> bool:
    input = assert_string(input)

    options = merge(options, default_email_options)

    domains = options["domains"]
    top_level_domains = options["top_level_domains"]
    insensitive = options["insensitive"]

    domains_pattern = ""

    if len(domains) > 0:
        for domain in domains:
            if not domains_pattern:
                domains_pattern = domain.strip()
            else:
                domains_pattern = f"{domains_pattern}|{domain}"
        domains_pattern = f"(?=.*({domains_pattern})\.)"

    top_level_domain_pattern = ""

    if len(top_level_domains) > 0:
        for domain in top_level_domains:
            if not top_level_domain_pattern:
                top_level_domain_pattern = domain.strip()
            else:
                top_level_domain_pattern = f"{top_level_domain_pattern}|{domain}"
        top_level_domain_pattern = f"(\.({top_level_domain_pattern}))"
    else:
        top_level_domain_pattern = r"\.[a-z]{2,63}"

    protocol_pattern = "" if options["no_scheme"] else r"((http(s)?):\/\/)?"

    limit_domain_length = "{1,255}"
    base_url_pattern = fr"{protocol_pattern}(www\.)?(?!-)[(\-a-z0-9.]{limit_domain_length}[a-z0-9]{top_level_domain_pattern}"

    path_pattern = r"\/?" if options["with_no_path"] else r"\b(\/[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?"

    pattern = fr"^({domains_pattern}{base_url_pattern}{path_pattern})$"

    return input.match(pattern, 'i') if insensitive else input.match(pattern)
