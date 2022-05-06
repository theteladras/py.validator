from typing import List, Literal, Tuple, TypedDict

from .utils.assert_string import assert_string
from .utils.merge import merge


class IsMobileNumberOptions(TypedDict):
    strict_mode: bool


Locals = Literal[
    'am-AM',
    'ar-AE',
    'ar-BH',
    'ar-DZ',
    'ar-LB',
    'ar-EG',
    'ar-IQ',
    'ar-JO',
    'ar-KW',
    'ar-LY',
    'ar-MA',
    'ar-OM',
    'ar-SA',
    'ar-SY',
    'ar-TN',
    'az-AZ',
    'bs-BA',
    'be-BY',
    'bg-BG',
    'bn-BD',
    'ca-AD',
    'cs-CZ',
    'da-DK',
    'de-DE',
    'de-AT',
    'de-CH',
    'de-LU',
    'el-GR',
    'en-AU',
    'en-BM',
    'en-GB',
    'en-GG',
    'en-GH',
    'en-HK',
    'en-MO',
    'en-IE',
    'en-IN',
    'en-KE',
    'en-MT',
    'en-MU',
    'en-NG',
    'en-NZ',
    'en-PK',
    'en-PH',
    'en-RW',
    'en-SG',
    'en-SL',
    'en-TZ',
    'en-UG',
    'en-US',
    'en-ZA',
    'en-ZM',
    'en-ZW',
    'es-AR',
    'es-BO',
    'es-CO',
    'es-CL',
    'es-CR',
    'es-CU',
    'es-DO',
    'es-HN',
    'es-EC',
    'es-ES',
    'es-PE',
    'es-MX',
    'es-PA',
    'es-PY',
    'es-UY',
    'es-VE',
    'et-EE',
    'fa-IR',
    'fi-FI',
    'fj-FJ',
    'fo-FO',
    'fr-CM',
    'fr-FR',
    'fr-GF',
    'fr-GP',
    'fr-MQ',
    'fr-RE',
    'he-IL',
    'hu-HU',
    'id-ID',
    'it-IT',
    'it-SM',
    'ja-JP',
    'ka-GE',
    'kk-KZ',
    'kl-GL',
    'ko-KR',
    'lt-LT',
    'lv-LV',
    'ms-MY',
    'mz-MZ',
    'nb-NO',
    'ne-NP',
    'nl-BE',
    'nl-NL',
    'nn-NO',
    'pl-PL',
    'pt-BR',
    'pt-PT',
    'pt-AO',
    'ro-RO',
    'ru-RU',
    'si-LK',
    'sl-SI',
    'sk-SK',
    'sq-AL',
    'sr-RS',
    'sv-SE',
    'tg-TJ',
    'th-TH',
    'tr-TR',
    'uk-UA',
    'uz-UZ',
    'vi-VN',
    'zh-CN',
    'zh-TW',
    'dz-BT',
    'en-CA',
    'fr-CA',
    'fr-BE',
    'zh-HK',
    'zh-MO',
    'ga-IE',
    'fr-CH',
    'it-CH'
]

mobile_number_patterns = {
    'am-AM': r'^(\+?374|0)((10|[9|7][0-9])\d{6}$|[2-4]\d{7}$)',
    'ar-AE': r'^((\+?971)|0)?5[024568]\d{7}$',
    'ar-BH': r'^(\+?973)?(3|6)\d{7}$',
    'ar-DZ': r'^(\+?213|0)(5|6|7)\d{8}$',
    'ar-LB': r'^(\+?961)?((3|81)\d{6}|7\d{7})$',
    'ar-EG': r'^((\+?20)|0)?1[0125]\d{8}$',
    'ar-IQ': r'^(\+?964|0)?7[0-9]\d{8}$',
    'ar-JO': r'^(\+?962|0)?7[789]\d{7}$',
    'ar-KW': r'^(\+?965)[569]\d{7}$',
    'ar-LY': r'^((\+?218)|0)?(9[1-6]\d{7}|[1-8]\d{7,9})$',
    'ar-MA': r'^(?:(?:\+|00)212|0)[5-7]\d{8}$',
    'ar-OM': r'^((\+|00)968)?(9[1-9])\d{6}$',
    'ar-SA': r'^(!?(\+?966)|0)?5\d{8}$',
    'ar-SY': r'^(!?(\+?963)|0)?9\d{8}$',
    'ar-TN': r'^(\+?216)?[2459]\d{7}$',
    'az-AZ': r'^(\+994|0)(5[015]|7[07]|99)\d{7}$',
    'bs-BA': r'^((((\+|00)3876)|06))((([0-3]|[5-6])\d{6})|(4\d{7}))$',
    'be-BY': r'^(\+?375)?(24|25|29|33|44)\d{7}$',
    'bg-BG': r'^(\+?359|0)?8[789]\d{7}$',
    'bn-BD': r'^(\+?880|0)1[13456789][0-9]{8}$',
    'ca-AD': r'^(\+376)?[346]\d{5}$',
    'cs-CZ': r'^(\+?420)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}$',
    'da-DK': r'^(\+?45)?\s?\d{2}\s?\d{2}\s?\d{2}\s?\d{2}$',
    'de-DE': r'^((\+49|0)[1|3])([0|5][0-45-9]\d|6([23]|0\d?)|7([0-57-9]|6\d))\d{7,9}$',
    'de-AT': r'^(\+43|0)\d{1,4}\d{3,12}$',
    'de-CH': r'^(\+41|0)([1-9])\d{1,9}$',
    'de-LU': r'^(\+352)?((6\d1)\d{6})$',
    'el-GR': r'^(\+?30|0)?(69\d{8})$',
    'en-AU': r'^(\+?61|0)4\d{8}$',
    'en-BM': r'^(\+?1)?441(((3|7)\d{6}$)|(5[0-3][0-9]\d{4}$)|(59\d{5}))',
    'en-GB': r'^(\+?44|0)7\d{9}$',
    'en-GG': r'^(\+?44|0)1481\d{6}$',
    'en-GH': r'^(\+233|0)(20|50|24|54|27|57|26|56|23|28|55|59)\d{7}$',
    'en-HK': r'^(\+?852[-\s]?)?[456789]\d{3}[-\s]?\d{4}$',
    'en-MO': r'^(\+?853[-\s]?)?[6]\d{3}[-\s]?\d{4}$',
    'en-IE': r'^(\+?353|0)8[356789]\d{7}$',
    'en-IN': r'^(\+?91|0)?[6789]\d{9}$',
    'en-KE': r'^(\+?254|0)(7|1)\d{8}$',
    'en-MT': r'^(\+?356|0)?(99|79|77|21|27|22|25)[0-9]{6}$',
    'en-MU': r'^(\+?230|0)?\d{8}$',
    'en-NG': r'^(\+?234|0)?[789]\d{9}$',
    'en-NZ': r'^(\+?64|0)[28]\d{7,9}$',
    'en-PK': r'^((00|\+)?92|0)3[0-6]\d{8}$',
    'en-PH': r'^(09|\+639)\d{9}$',
    'en-RW': r'^(\+?250|0)?[7]\d{8}$',
    'en-SG': r'^(\+65)?[3689]\d{7}$',
    'en-SL': r'^(\+?232|0)\d{8}$',
    'en-TZ': r'^(\+?255|0)?[67]\d{8}$',
    'en-UG': r'^(\+?256|0)?[7]\d{8}$',
    'en-US': r'^((\+1|1)?( |-)?)?(\([2-9][0-9]{2}\)|[2-9][0-9]{2})( |-)?([2-9][0-9]{2}( |-)?[0-9]{4})$',
    'en-ZA': r'^(\+?27|0)\d{9}$',
    'en-ZM': r'^(\+?26)?09[567]\d{7}$',
    'en-ZW': r'^(\+263)[0-9]{9}$',
    'es-AR': r'^\+?549(11|[2368]\d)\d{8}$',
    'es-BO': r'^(\+?591)?(6|7)\d{7}$',
    'es-CO': r'^(\+?57)?3(0(0|1|2|4|5)|1\d|2[0-4]|5(0|1))\d{7}$',
    'es-CL': r'^(\+?56|0)[2-9]\d{1}\d{7}$',
    'es-CR': r'^(\+506)?[2-8]\d{7}$',
    'es-CU': r'^(\+53|0053)?5\d{7}',
    'es-DO': r'^(\+?1)?8[024]9\d{7}$',
    'es-HN': r'^(\+?504)?[9|8]\d{7}$',
    'es-EC': r'^(\+?593|0)([2-7]|9[2-9])\d{7}$',
    'es-ES': r'^(\+?34)?[6|7]\d{8}$',
    'es-PE': r'^(\+?51)?9\d{8}$',
    'es-MX': r'^(\+?52)?(1|01)?\d{10,11}$',
    'es-PA': r'^(\+?507)\d{7,8}$',
    'es-PY': r'^(\+?595|0)9[9876]\d{7}$',
    'es-UY': r'^(\+598|0)9[1-9][\d]{6}$',
    'es-VE': r'^(\+?58)?(2|4)\d{9}$',
    'et-EE': r'^(\+?372)?\s?(5|8[1-4])\s?([0-9]\s?){6,7}$',
    'fa-IR': r'^(\+?98[\-\s]?|0)9[0-39]\d[\-\s]?\d{3}[\-\s]?\d{4}$',
    'fi-FI': r'^(\+?358|0)\s?(4(0|1|2|4|5|6)?|50)\s?(\d\s?){4,8}\d$',
    'fj-FJ': r'^(\+?679)?\s?\d{3}\s?\d{4}$',
    'fo-FO': r'^(\+?298)?\s?\d{2}\s?\d{2}\s?\d{2}$',
    'fr-CM': r'^(\+?237)6[0-9]{8}$',
    'fr-FR': r'^(\+?33|0)[67]\d{8}$',
    'fr-GF': r'^(\+?594|0|00594)[67]\d{8}$',
    'fr-GP': r'^(\+?590|0|00590)[67]\d{8}$',
    'fr-MQ': r'^(\+?596|0|00596)[67]\d{8}$',
    'fr-RE': r'^(\+?262|0|00262)[67]\d{8}$',
    'he-IL': r'^(\+972|0)([23489]|5[012345689]|77)[1-9]\d{6}$',
    'hu-HU': r'^(\+?36|06)(20|30|31|50|70)\d{7}$',
    'id-ID': r'^(\+?62|0)8(1[123456789]|2[1238]|3[1238]|5[12356789]|7[78]|9[56789]|8[123456789])([\s?|\d]{5,11})$',
    'it-IT': r'^(\+?39)?\s?3\d{2} ?\d{6,7}$',
    'it-SM': r'^((\+378)|(0549)|(\+390549)|(\+3780549))?6\d{5,9}$',
    'ja-JP': r'^(\+81[ \-]?(\(0\))?|0)[6789]0[ \-]?\d{4}[ \-]?\d{4}$',
    'ka-GE': r'^(\+?995)?(5|79)\d{7}$',
    'kk-KZ': r'^(\+?7|8)?7\d{9}$',
    'kl-GL': r'^(\+?299)?\s?\d{2}\s?\d{2}\s?\d{2}$',
    'ko-KR': r'^((\+?82)[ \-]?)?0?1([0|1|6|7|8|9]{1})[ \-]?\d{3,4}[ \-]?\d{4}$',
    'lt-LT': r'^(\+370|8)\d{8}$',
    'lv-LV': r'^(\+?371)2\d{7}$',
    'ms-MY': r'^(\+?6?01){1}(([0145]{1}(\-|\s)?\d{7,8})|([236789]{1}(\s|\-)?\d{7}))$',
    'mz-MZ': r'^(\+?258)?8[234567]\d{7}$',
    'nb-NO': r'^(\+?47)?[49]\d{7}$',
    'ne-NP': r'^(\+?977)?9[78]\d{8}$',
    'nl-BE': r'^(\+?32|0)4\d{8}$',
    'nl-NL': r'^(((\+|00)?31\(0\))|((\+|00)?31)|0)6{1}\d{8}$',
    'nn-NO': r'^(\+?47)?[49]\d{7}$',
    'pl-PL': r'^(\+?48)? ?[5-8]\d ?\d{3} ?\d{2} ?\d{2}$',
    'pt-BR': r'^((\+?55\ ?[1-9]{2}\ ?)|(\+?55\ ?\([1-9]{2}\)\ ?)|(0[1-9]{2}\ ?)|(\([1-9]{2}\)\ ?)|([1-9]{2}\ ?))((\d{4}\-?\d{4})|(9[2-9]{1}\d{3}\-?\d{4}))$',
    'pt-PT': r'^(\+?351)?9[1236]\d{7}$',
    'pt-AO': r'^(\+244)\d{9}$',
    'ro-RO': r'^(\+?4?0)\s?7\d{2}(\/|\s|\.|\-)?\d{3}(\s|\.|\-)?\d{3}$',
    'ru-RU': r'^(\+?7|8)?9\d{9}$',
    'si-LK': r'^(?:0|94|\+94)?(7(0|1|2|4|5|6|7|8)( |-)?)\d{7}$',
    'sl-SI': r'^(\+386\s?|0)(\d{1}\s?\d{3}\s?\d{2}\s?\d{2}|\d{2}\s?\d{3}\s?\d{3})$',
    'sk-SK': r'^(\+?421)? ?[1-9][0-9]{2} ?[0-9]{3} ?[0-9]{3}$',
    'sq-AL': r'^(\+355|0)6[789]\d{6}$',
    'sr-RS': r'^(\+3816|06)[- \d]{5,9}$',
    'sv-SE': r'^(\+?46|0)[\s\-]?7[\s\-]?[02369]([\s\-]?\d){7}$',
    'tg-TJ': r'^(\+?992)?[5][5]\d{7}$',
    'th-TH': r'^(\+66|66|0)\d{9}$',
    'tr-TR': r'^(\+?90|0)?5\d{9}$',
    'uk-UA': r'^(\+?38|8)?0\d{9}$',
    'uz-UZ': r'^(\+?998)?(6[125-79]|7[1-69]|88|9\d)\d{7}$',
    'vi-VN': r'^((\+?84)|0)((3([2-9]))|(5([25689]))|(7([0|6-9]))|(8([1-9]))|(9([0-9])))([0-9]{7})$',
    'zh-CN': r'^((\+|00)86)?(1[3-9]|9[28])\d{9}$',
    'zh-TW': r'^(\+?886\-?|0)?9\d{8}$',
    'dz-BT': r'^(\+?975|0)?(17|16|77|02)\d{6}$',
}

mobile_number_patterns['en-CA'] = mobile_number_patterns['en-US']
mobile_number_patterns['fr-CA'] = mobile_number_patterns['en-CA']
mobile_number_patterns['fr-BE'] = mobile_number_patterns['nl-BE']
mobile_number_patterns['zh-HK'] = mobile_number_patterns['en-HK']
mobile_number_patterns['zh-MO'] = mobile_number_patterns['en-MO']
mobile_number_patterns['ga-IE'] = mobile_number_patterns['en-IE']
mobile_number_patterns['fr-CH'] = mobile_number_patterns['de-CH']
mobile_number_patterns['it-CH'] = mobile_number_patterns['fr-CH']

__default_options: IsMobileNumberOptions = {
    'strict_mode': False
}


def is_mobile_number(
        input: str,
        locale: Tuple[List[Locals], Locals, 'any'] = 'any',
        options: IsMobileNumberOptions = {}
) -> bool:
    input = assert_string(input)

    options = merge(options, __default_options)

    if options['strict_mode'] and not input.startswith('+'):
        return False

    if locale == 'any':
        for item, pattern in mobile_number_patterns.items():
            if input.match(pattern):
                return True
        return False
    elif isinstance(locale, list):
        for item in locale:
            if pattern := mobile_number_patterns.get(item):
                if input.match(pattern):
                    return True
        return False
    elif pattern := mobile_number_patterns.get(locale):
        return input.match(pattern)
    raise Exception('Invalid locale provided: {}'.format(locale))
