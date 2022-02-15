# py.validator

A library of string validators and sanitizers

_Insipired by validator.js_

## Strings only

**This library validates and sanitizes strings only.**

Passing anything other than a string will result in an error.

## Instalation

You can install it by running:
`pip install py.validator`

## Usage

```py
from pyvalidator import is_email, is_mobile_number, is_port

email = 'some@email.com'

is_email_flag = is_email(email)

mobile_number = '+15673628910'

is_mobile_number_flag = is_mobile_number(mobile_number)

port = '8000'

is_port_flag = is_port(port)

if is_email_flag and is_mobile_number_flag and is_port_flag:
    print('All True!')

```

## Validators

Here is a list of the validators currently available.

Validator                                | Description
---------------------------------------  | --------------------------------------
**is_after(str [, date])**               | check if the string is a date that's after the specified date (defaults to now).
**is_alpha(str [, locale, options])**    | check if the string contains only letters (a-zA-Z).<br/><br/>Locale is one of `['ar', 'ar-AE', 'ar-BH', 'ar-DZ', 'ar-EG', 'ar-IQ', 'ar-JO', 'ar-KW', 'ar-LB', 'ar-LY', 'ar-MA', 'ar-QA', 'ar-QM', 'ar-SA', 'ar-SD', 'ar-SY', 'ar-TN', 'ar-YE', 'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-HK', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'en-ZM', 'es-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'he', 'hi-IN', 'hu-HU', 'it-IT', 'ku-IQ', 'nb-NO', 'nl-NL', 'nn-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'ru-RU', 'sl-SI', 'sk-SK', 'sr-RS', 'sr-RS@latin', 'sv-SE', 'tr-TR', 'uk-UA']`) and defaults to `en-US`. The locale list can be picked up from `validator.locales`. Options is an optional dictionary that can be supplied with the following key(s): ignore which can either be a String or RegExp of characters to be ignored e.g. " -" will ignore spaces and -'s.
**is_alphanumeric(str [, locale, options])**      | check if the string contains only letters and numbers (a-zA-Z0-9).<br/><br/>Locale is one of `['ar', 'ar-AE', 'ar-BH', 'ar-DZ', 'ar-EG', 'ar-IQ', 'ar-JO', 'ar-KW', 'ar-LB', 'ar-LY', 'ar-MA', 'ar-QA', 'ar-QM', 'ar-SA', 'ar-SD', 'ar-SY', 'ar-TN', 'ar-YE', 'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-HK', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'en-ZM', 'es-ES', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'he', 'hi-IN', 'hu-HU', 'it-IT', 'ku-IQ', 'nb-NO', 'nl-NL', 'nn-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'ru-RU', 'sl-SI', 'sk-SK', 'sr-RS', 'sr-RS@latin', 'sv-SE', 'tr-TR', 'uk-UA']`) and defaults to `en-US`. The locale list can be picked up from `validator.locales`. options is an optional dictionary that can be supplied with the following key(s): ignore which can either be a String or RegExp of characters to be ignored e.g. " -" will ignore spaces and -'s.
**is_ascii(str)**                        | check if the string contains ASCII chars only.
**is_base32(str)**                       | check if a string is base32 encoded.
**is_base58(str)**                       | check if a string is base58 encoded.
**is_base64(str [, options])**           | check if a string is base64 encoded. options is optional and defaults to `{ "url_safe": False }`<br/> when `url_safe` is true it tests the given base64 encoded string is [url safe](https://base64.guru/standards/base64url).
**is_before(str [, date])**              | check if the string is a date that's before the specified date.
**is_bic(str)**                          | check if a string is a BIC (Bank Identification Code) or SWIFT code.
**is_boolean(str [, options])**          | check if a string is a boolean.<br/>`options` is an dictionary which defaults to `{ "loose": False }`. If loose is is set to false, the validator will strictly match ['True', 'False', 'true', 'false', '0', '1']. If loose is set to true, the validator will also match 'yes', 'no', and will match a valid boolean string of any case. (eg: ['true', 'True', 'TRUE']).
**is_btc_address(str)**                  | check if the string is a valid BTC address.
**is_byte_length(str [, options])**      | check if the string's length (in UTF-8 bytes) falls in a range.<br/><br/>`options` is an dictionary which defaults to `{ "min": 0, "max": None }`.
**is_credit_card(str)**                  | check if the string is a credit card.
**is_currency(str [, options])**         | check if the string is a valid currency amount.<br/><br/>`options` is an dictionary which is defaultet to:<br/>{ <br/> &nbsp;&nbsp; "symbol": '$', <br/> &nbsp;&nbsp; "require_symbol": False, <br/> &nbsp;&nbsp; "allow_space_after_symbol": False, <br/> &nbsp;&nbsp; "symbol_after_digits": False, <br/> &nbsp;&nbsp; "allow_negatives": True, <br/> &nbsp;&nbsp; "parens_for_negatives": False, <br/> &nbsp;&nbsp; "negative_sign_before_digits": False, <br/> &nbsp;&nbsp; "negative_sign_after_digits": False, <br/> &nbsp;&nbsp; "allow_negative_sign_placeholder": False, <br/> &nbsp;&nbsp; "thousands_separator": ',', <br/> &nbsp;&nbsp; "decimal_separator": '.', <br/> &nbsp;&nbsp; "allow_decimal": True, <br/> &nbsp;&nbsp; "require_decimal": False, <br/> &nbsp;&nbsp; "digits_after_decimal": [2], <br/> &nbsp;&nbsp; "allow_space_after_digits": False <br/>}  <br/>**Note:** The array `digits_after_decimal` is filled with the exact number of digits allowed not a range, for example a range 1 to 3 will be given as [1, 2, 3].
**is_data_uri(str)**                  | check if the string is a [data uri format](https://developer.mozilla.org/en-US/docs/Web/HTTP/data_URIs).
**is_date(str [, options])**          | Check if the input is a valid date. e.g. `[2002-07-15, new Date()]`.<br/><br/> `options` is an dictionary which can contain the keys `format`, `strict_mode` and/or `delimiters`<br/><br/>`format` is a string and defaults to `YYYY/MM/DD`.<br/><br/>`strict_mode` is a boolean and defaults to `False`. If `strict_mode` is set to true, the validator will reject inputs different from `format`.<br/><br/> `delimiters` is an array of allowed date delimiters and defaults to `['/', '-']`, supported delimiters are `['/', '-', '.', ',', ';', ':', '\|' ]`.
**is_decimal(str [, options])**      | check if the string represents a decimal number, such as 0.1, .3, 1.1, 1.00003, 4.0, etc.<br/><br/>`options` is an dictionary which defaults to `{"force_decimal": False, "decimal_digits": '1,', "locale": 'en-US'}`<br/><br/>`locale` determine the decimal separator and is one of `['ar', 'ar-AE', 'ar-BH', 'ar-DZ', 'ar-EG', 'ar-IQ', 'ar-JO', 'ar-KW', 'ar-LB', 'ar-LY', 'ar-MA', 'ar-QA', 'ar-QM', 'ar-SA', 'ar-SD', 'ar-SY', 'ar-TN', 'ar-YE', 'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-HK', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'en-ZM', 'es-ES', 'fa', 'fa-AF', 'fa-IR', 'fr-FR', 'fr-CA', 'hu-HU', 'id-ID', 'it-IT', 'ku-IQ', 'nb-NO', 'nl-NL', 'nn-NO', 'pl-PL', 'pl-Pl', 'pt-BR', 'pt-PT', 'ru-RU', 'sl-SI', 'sr-RS', 'sr-RS@latin', 'sv-SE', 'tr-TR', 'uk-UA', 'vi-VN']`.<br/>**Note:** `decimal_digits` is given as a range like '1,3', a specific value like '3' or min like '1,'.
**is_divisible_by(str, number)**      | check if the string is a number that's divisible by another.
**is_ean(str)**                       | check if the string is an EAN (European Article Number).
**is_email(str [, options])**         | check if the string is an email.<br/><br/>`options` is an dictionary which defaults to `{ "allow_display_name": False, "require_display_name": False, "allow_utf8_local_part": True, "require_tld": True, "allow_ip_domain": False, "domain_specific_validation": False, "ignore_max_length": False, "blacklisted_chars": '', "host_blacklist": [] }`. If `allow_display_name` is set to True, the validator will also match `Display Name <email-address>`. If `require_display_name` is set to True, the validator will reject strings without the format `Display Name <email-address>`. If `allow_utf8_local_part` is set to False, the validator will not allow any non-English UTF8 character in email address' local part. If `require_tld` is set to False, e-mail addresses without having TLD in their domain will also be matched. If `ignore_max_length` is set to True, the validator will not check for the standard max length of an email. If `allow_ip_domain` is set to True, the validator will allow IP addresses in the host part. If `domain_specific_validation` is true, some additional validation will be enabled, e.g. disallowing certain syntactically valid email addresses that are rejected by GMail. If `blacklisted_chars` receives a string, then the validator will reject emails that include any of the characters in the string, in the name part. If `host_blacklist` is set to an array of strings and the part of the email after the `@` symbol matches one of the strings defined in it, the validation fails.
**is_emoji(str [, options])**         | check if the provided string is a valid emoji. A string of length grater then 1, is considered as a valid emoji if all of its characters are emoji characters, for example '🍗🍗🍗' is valid, while '🍗@🍗🍗' would be invalid. You can provide a second dict argument with the property 'omit_rule' to pass a regex patter which will be used to igore certain characters, for example passing `{ "omit_rule": r'[=]' }` would treat the string "💪=💪=💪" as valid.
**is_ethereum_address(str)**          | check if the string is an [Ethereum](https://ethereum.org/) address using basic regex. Does not validate address checksums.
**is_float(str [, options])**         | check if the string is a float.<br/><br/>`options` is an dictionary which can contain the keys `min`, `max`, `gt`, and/or `lt` to validate the float is within boundaries (e.g. `{ "min": 7.22, "max": 9.55 }`) it also has `locale` as an option.<br/><br/>`min` and `max` are equivalent to 'greater or equal' and 'less or equal', respectively while `gt` and `lt` are their strict counterparts.<br/><br/>`locale` determine the decimal separator and is one of `['ar', 'ar-AE', 'ar-BH', 'ar-DZ', 'ar-EG', 'ar-IQ', 'ar-JO', 'ar-KW', 'ar-LB', 'ar-LY', 'ar-MA', 'ar-QA', 'ar-QM', 'ar-SA', 'ar-SD', 'ar-SY', 'ar-TN', 'ar-YE', 'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'en-AU', 'en-GB', 'en-HK', 'en-IN', 'en-NZ', 'en-US', 'en-ZA', 'en-ZM', 'es-ES', 'fr-CA', 'fr-FR', 'hu-HU', 'it-IT', 'nb-NO', 'nl-NL', 'nn-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'ru-RU', 'sl-SI', 'sr-RS', 'sr-RS@latin', 'sv-SE', 'tr-TR', 'uk-UA']`. Locale list is `validator.isFloatLocales`.
**is_fqdn(str [, options])**          | check if the string is a fully qualified domain name (e.g. domain.com).<br/><br/>`options` is an dictionary which defaults to `{ "require_tld": True, "allow_underscores": False, "allow_trailing_dot": False, "allow_numeric_tld": False, "allow_wildcard": False }`. If `allow_wildcard` is set to true, the validator will allow domain starting with `*.` (e.g. `*.example.com` or `*.shop.example.com`).
**is_full_width(str)**                | check if the string contains any full-width chars.
**is_hash(str, algorithm)**           | check if the string is a hash of type algorithm.<br/><br/>Algorithm is one of `['md4', 'md5', 'sha1', 'sha256', 'sha384', 'sha512', 'ripemd128', 'ripemd160', 'tiger128', 'tiger160', 'tiger192', 'crc32', 'crc32b']`
**is_hexadecimal(str)**               | check if the string is a hexadecimal number.
**is_hsl(str)**                       | check if the string is an HSL (hue, saturation, lightness, optional alpha) color based on [CSS Colors Level 4 specification](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value).<br/><br/>Comma-separated format supported. Space-separated format supported with the exception of a few edge cases (ex: `hsl(200grad+.1%62%/1)`).
**is_imei(str [, options]))**         | check if the string is a valid IMEI number. Imei should be of format `###############` or `##-######-######-#`.<br/><br/>`options` is an dictionary which can contain the property `allow_hyphens` (bool - default value is False). If the `allow_hyphens` prop is set to True, it will validate the IMEI with the hyphens.
**is_int(str [, options])**           | check if the string is an integer.<br/><br/>`options` is an dictionary which can contain the keys `min` and/or `max` to check the integer is within boundaries (e.g. `{ "min": 10, "max": 99 }`). `options` can also contain the key `allow_leading_zeroes`, which when set to false will disallow integer values with leading zeroes (e.g. `{ "allow_leading_zeroes": False }`). Finally, `options` can contain the keys `gt` and/or `lt` which will enforce integers being greater than or less than, respectively, the value provided (e.g. `{ "gt": 1, "lt": 4 }` for a number between 1 and 4).
**is_ip(str [, version])**            | check if the string is an IP (version 4 or 6).
**is_ip_range(str [, version])**      | check if the string is an IP Range (version 4 or 6).
**is_ISO31661_alpha2(str)**           | check if the string is a valid [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) officially assigned country code.
**is_isrc(str)**                      | check if the string is a [ISRC](https://en.wikipedia.org/wiki/International_Standard_Recording_Code).
**is_json(str [, options])**          | check if the string is valid JSON (note: uses JSON.parse).<br/><br/>`options` is an dictionary which defaults to `{ "allow_primitives": False }`. If `allow_primitives` is True, the primitives 'true', 'false' and 'null' are accepted as valid JSON values.
**is_jwt(str)**                       | check if the string is valid JWT token.
**is_lat_long(str [, options])**      | check if the string is a valid latitude-longitude coordinate in the format `lat,long` or `lat, long`.<br/><br/>`options` is an object that defaults to `{ "check_dms": False }`. Pass `check_dms` as `True` to validate DMS(degrees, minutes, and seconds) latitude-longitude format.
**isLowercase(str)**                  | check if the string is lowercase.
**is_md5(str)**                       | check if the string is a MD5 hash.<br/><br/>Please note that you can also use the `isHash(str, 'md5')` function. Keep in mind that MD5 has some collision weaknesses compared to other algorithms (e.g., SHA).
**is_mobile_number(str [, locale [, options]])**          | check if the string is a mobile phone number,<br/><br/>locale can be an array of locales (e.g `['sr-RS', 'bs-BA']`) or a single locale from `['am-Am', 'ar-AE', 'ar-BH', 'ar-DZ', 'ar-EG', 'ar-IQ', ar-JO', 'ar-KW', 'ar-SA', 'ar-SY', 'ar-TN', 'az-AZ', 'az-LY', 'az-LB', 'bs-BA', 'be-BY', 'bg-BG', 'bn-BD', 'ca-AD', 'cs-CZ', 'da-DK', 'de-DE', 'de-AT', 'de-CH', 'de-LU', 'el-GR', 'en-AU', 'en-BM', 'en-CA', 'en-GB', 'en-GG', 'en-GH', 'en-HK', 'en-MO', 'en-IE', 'en-IN', 'en-KE', 'en-MT', 'en-MU', 'en-NG', 'en-NZ', 'en-PK', 'en-PH', 'en-RW', 'en-SG', 'en-SL', 'en-UG', 'en-US', 'en-TZ', 'en-ZA', 'en-ZM', 'en-ZW', 'es-AR', 'es-BO', 'es-CL', 'es-CO', 'es-CR', 'es-CU', 'es-DO', 'es-HN', 'es-PE', 'es-EC', 'es-ES', 'es-MX', 'es-PA', 'es-PY', 'es-UY', 'es-VE', 'et-EE', 'fa-IR', 'fi-FI', 'fj-FJ', 'fo-FO', 'fr-BE', 'fr-FR', 'fr-GF', 'fr-GP', 'fr-MQ', 'fr-RE', 'ga-IE', 'he-IL', 'hu-HU', 'id-ID', 'it-IT', 'it-SM', 'ja-JP', 'ka-GE', 'kk-KZ', 'kl-GL', 'ko-KR', 'lt-LT', 'ms-MY', ''mz-MZ', nb-NO', 'ne-NP', 'nl-BE', 'nl-NL', 'nn-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'pt-AO', 'ro-RO', 'ru-RU', 'si-LK' 'sl-SI', 'sk-SK', 'sq-AL', 'sr-RS', 'sv-SE', 'tg-TJ', 'th-TH', 'tr-TR', 'uk-UA', 'uz-UZ', 'vi-VN', 'zh-CN', 'zh-HK', 'zh-MO', 'zh-TW', 'dz-BT']`, or can be left out which would implicitly set it to 'any' and it would try to find a signle valid value from the previouse list of locales (can be explicitly set as well).<br/><br/>`options` is an optional dictionary that can be supplied with the following keys: `strictMode`, if this is set to `True`, the mobile number must be supplied with the country code and therefore must start with `+`. If an invalid locale is provided, it will raise an exception.
**is_mongo_id(str)**                  | check if the string is a valid hex-encoded representation of a [MongoDB ObjectId][mongoid].
**is_multibyte(str)**                 | check if the string contains one or more multibyte chars.
**is_number(str [, options])**        | check if the string is a number (int or float)
**is_octal(str)**                     | check if the string is a valid octal number.
**is_passport_number(str, country_code)**                     | check if the string is a valid passport number.<br/><br/>(country_code is one of `[ 'AM', 'AR', 'AT', 'AU', 'BA', 'BE', 'BG', 'BY', 'BR', 'CA', 'CH', 'CN', 'CY', 'CZ', 'DE', 'DK', 'DZ', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'HR', 'HU', 'IE' 'IN', 'IR', 'ID', 'IS', 'IT', 'JP', 'KR', 'LT', 'LU', 'LV', 'LY', 'MT', 'MY', 'MZ', 'NL', 'PL', 'PT', 'RO', 'RS', 'RU', 'SE', 'SL', 'SK', 'TR', 'UA', 'US' ]`.
**is_port(str)**                      | check if the string is a valid port number.
**is_rgb_color(str [, include_percent_values])**               | check if the string is a rgb or rgba color.<br/><br/>`include_percent_values` defaults to `true`. If you don't want to allow to set `rgb` or `rgba` values with percents, like `rgb(5%,5%,5%)`, or `rgba(90%,90%,90%,.3)`, then set it to false.
**is_semantic_version(str)**          | check if the string is a Semantic Versioning Specification.
**is_uppercase(str)**                 | check if the string is uppercase.
**is_uuid(str [, version])**          | check if the string is a UUID (version 1, 2, 3, 4 or 5).
**is_slug(str)**                      | Check if the string is of type slug. `Options` allow a single hyphen between string. e.g. [`cn-cn`, `cn-c-c`]
**is_strong_password(str [, options])**   | Check if a password is strong or not. Allows for custom requirements or scoring rules. If `return_score` is True, then the function returns an integer score for the password rather than a boolean.<br/>Default options: <br/>`{ "min_length": 8, "min_lowercase": 1, "min_uppercase": 1, "min_numbers": 1, "min_symbols": 1, "return_score": False, "points_perUnique": 1, "points_per_repeat": 0.5, "points_for_containing_lower": 10, "points_for_containing_upper": 10, "points_for_containing_number": 10, "points_for_containing_symbol": 10 }`

## Contributing

1. Fork the repo on GitHub
2. Create a unique branch with prefixes feat/ for new features or fix/ for any fixes or improvements
3. Work on your branch
    - if modifications are chainging the behaviour of an existing validator, do upgrade the tests of it to cover that functionality as well.
    - tests are the main requirement of any new validators.
4. Commit changes to your own branch
5. Pull changes from the origin main branch in order to avoid conflicts.
6. Push your work back up to your fork
7. Submit a Pull request so that we can review your changes
