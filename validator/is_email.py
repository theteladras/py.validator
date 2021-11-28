from typing import TypedDict

from .utils.Classes.RegEx import RegEx
from .utils.Classes.String import String
from .utils.Classes.List import List
from .utils.assert_string import assert_string
from .utils.merge import merge
from .utils.includes import includesSome
from .is_byte_length import is_byte_length
from .is_ip import is_ip
from .is_fqdn import is_fqdn

class IsEmailOptions(TypedDict):
    allow_display_name: bool
    require_display_name: bool
    allow_utf8_local_part: bool
    require_tld: bool
    ignore_max_length: bool
    domain_specific_validation: bool
    allow_ip_domain: bool
    blacklisted_chars: str
    host_blacklist: List

default_email_options: IsEmailOptions = {
  "allow_display_name": False,
  "require_display_name": False,
  "allow_utf8_local_part": True,
  "require_tld": True,
  "ignore_max_length": False,
  "domain_specific_validation": False,
  "allow_ip_domain": False,
  "blacklisted_chars": '',
  "host_blacklist": [],
}

split_name_address = r"^([^\x00-\x1F\x7F-\x9F]+)<"
email_user_part = r"^[a-z\d!#\$%&'\*\+\-\/=\?\^_`{\|}~]+$"
gmail_user_part = r"^[a-z\d]+$"
quoted_email_user = r"^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f]))*$"
email_user_utf8_part = r"^[a-z\d!#\$%&'\*\+\-\/=\?\^_`{\|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+$"
quoted_email_user_utf8 = r"^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*$"
default_max_email_length = 254


def validate_display_name(display_name: String):
    display_name_without_quotes = display_name
    if display_name[0] == '"' and display_name[display_name.length - 1] == '"':
        display_name_without_quotes = display_name.substring(1, display_name.length - 1)

    if not display_name_without_quotes.trim():
        return False

    illegal_chars = ['"', '.', ';', '<', '>']
    contains_illegal = includesSome(display_name_without_quotes, illegal_chars)

    if contains_illegal:
        
        if display_name_without_quotes == display_name:
            return False

        all_start_with_back_slash = (
            display_name_without_quotes.split('"').length == display_name_without_quotes.split('\\"').length
        )

        if not all_start_with_back_slash:
            return False

    return True

def is_email(input: str, options: IsEmailOptions = {}) -> bool:
    input = assert_string(input)
    options = merge(options, default_email_options)

    if options["require_display_name"] or options["allow_display_name"]:
        display_email = input.findMatches(split_name_address, 'i')
        if display_email:
            display_name = String(display_email[0])

            input = input.sub(RegEx.escape(display_name), '').sub(r"(^<|>$)", '')
            if display_name.endswith(' '):
                display_name = display_name.substring(0, display_name.length-1)
            
            if not validate_display_name(display_name):
                return False
        elif options["require_display_name"]:
            return False

    if (not options["ignore_max_length"]) and input.length > default_max_email_length:
        return False

    parts = input.split('@')
    domain = String(parts.pop())
    parts = List(parts[:-1])
    lower_domain = domain.lower()

    if List(options["host_blacklist"]).includes(lower_domain):
        return False

    user = String(parts.join('@'))

    if options["domain_specific_validation"] and (lower_domain == 'gmail.com' or lower_domain == 'googlemail.com'):
        user = user.lower()
        username = String(user.split('+')[0])

        if not is_byte_length(username.sub(RegEx('\.', 'g'), ''), { "min": 6, "max": 30 }):
            return False

        user_parts = username.split('.')
        for user_part in user_parts:
            if not String(user_part).match(gmail_user_part):
                return False

    if (
        (not options["ignore_max_length"]) and  (
            not is_byte_length(user, { "max": 64 }) or
            not is_byte_length(domain, { "max": 254 })
        )
    ):
        return False

    if not is_fqdn(domain, { "require_tld": options["require_tld"] }):

        if (not options["allow_ip_domain"]):
            return False

        if not is_ip(domain):
            if not domain.startswith('[') or not domain.endswith(']'):
                return False

            no_bracketdomain = domain.substring(1, domain.length - 2)

            if no_bracketdomain.length == 0 or not is_ip(no_bracketdomain):
                return False

    if user.length and user[0] == '"':
        user = user.slice(1, user.length - 1)
        if options["allow_utf8_local_part"]:
            return user.match(quoted_email_user_utf8, 'i')
        else:
            return user.match(quoted_email_user, 'i')

    pattern = email_user_utf8_part if options["allow_utf8_local_part"] else email_user_part
    user_parts = user.split('.')
    for user_part in user_parts:
        if not String(user_part).match(pattern, 'i'):
                return False

    if options["blacklisted_chars"]:
        if user.findMatches(RegEx("[" + options["blacklisted_chars"] + "]+", 'g')):
            return False

    return True
