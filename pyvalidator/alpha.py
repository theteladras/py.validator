alpha = {
  'en-US': '^[A-Z]+$',
  'az-AZ': '^[A-VXYZÇƏĞİıÖŞÜ]+$',
  'bg-BG': '^[А-Я]+$',
  'cs-CZ': '^[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+$',
  'da-DK': '^[A-ZÆØÅ]+$',
  'de-DE': '^[A-ZÄÖÜß]+$',
  'el-GR': '^[Α-ώ]+$',
  'es-ES': '^[A-ZÁÉÍÑÓÚÜ]+$',
  'fa-IR': '^[ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]+$',
  'fr-FR': '^[A-ZÀÂÆÇÉÈÊËÏÎÔŒÙÛÜŸ]+$',
  'it-IT': '^[A-ZÀÉÈÌÎÓÒÙ]+$',
  'nb-NO': '^[A-ZÆØÅ]+$',
  'nl-NL': '^[A-ZÁÉËÏÓÖÜÚ]+$',
  'nn-NO': '^[A-ZÆØÅ]+$',
  'hu-HU': '^[A-ZÁÉÍÓÖŐÚÜŰ]+$',
  'pl-PL': '^[A-ZĄĆĘŚŁŃÓŻŹ]+$',
  'pt-PT': '^[A-ZÃÁÀÂÄÇÉÊËÍÏÕÓÔÖÚÜ]+$',
  'ru-RU': '^[А-ЯЁ]+$',
  'sl-SI': '^[A-ZČĆĐŠŽ]+$',
  'sk-SK': '^[A-ZÁČĎÉÍŇÓŠŤÚÝŽĹŔĽÄÔ]+$',
  'sr-RS@latin': '^[A-ZČĆŽŠĐ]+$',
  'sr-RS': '^[А-ЯЂЈЉЊЋЏ]+$',
  'sv-SE': '^[A-ZÅÄÖ]+$',
  'th-TH': '^[ก-๐\s]+$',
  'tr-TR': '^[A-ZÇĞİıÖŞÜ]+$',
  'uk-UA': '^[А-ЩЬЮЯЄIЇҐі]+$',
  'vi-VN': '^[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴĐÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ]+$',
  'ku-IQ': '^[ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆھەیێيطؤثآإأكضصةظذ]+$',
  'ar': '^[ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٰ]+',
  'he': '^[א-ת]+',
  'fa': '^[\'آاءأؤئبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهةی\']+$',
  'hi-IN': '^[\u0900-\u0961]+[\u0972-\u097F]*$',
}

alphanumeric = {
  'en-US': '^[0-9A-Z]+$',
  'az-AZ': '^[0-9A-VXYZÇƏĞİıÖŞÜ]+$',
  'bg-BG': '^[0-9А-Я]+$',
  'cs-CZ': '^[0-9A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+$',
  'da-DK': '^[0-9A-ZÆØÅ]+$',
  'de-DE': '^[0-9A-ZÄÖÜß]+$',
  'el-GR': '^[0-9Α-ω]+$',
  'es-ES': '^[0-9A-ZÁÉÍÑÓÚÜ]+$',
  'fr-FR': '^[0-9A-ZÀÂÆÇÉÈÊËÏÎÔŒÙÛÜŸ]+$',
  'it-IT': '^[0-9A-ZÀÉÈÌÎÓÒÙ]+$',
  'hu-HU': '^[0-9A-ZÁÉÍÓÖŐÚÜŰ]+$',
  'nb-NO': '^[0-9A-ZÆØÅ]+$',
  'nl-NL': '^[0-9A-ZÁÉËÏÓÖÜÚ]+$',
  'nn-NO': '^[0-9A-ZÆØÅ]+$',
  'pl-PL': '^[0-9A-ZĄĆĘŚŁŃÓŻŹ]+$',
  'pt-PT': '^[0-9A-ZÃÁÀÂÄÇÉÊËÍÏÕÓÔÖÚÜ]+$',
  'ru-RU': '^[0-9А-ЯЁ]+$',
  'sl-SI': '^[0-9A-ZČĆĐŠŽ]+$',
  'sk-SK': '^[0-9A-ZÁČĎÉÍŇÓŠŤÚÝŽĹŔĽÄÔ]+$',
  'sr-RS@latin': '^[0-9A-ZČĆŽŠĐ]+$',
  'sr-RS': '^[0-9А-ЯЂЈЉЊЋЏ]+$',
  'sv-SE': '^[0-9A-ZÅÄÖ]+$',
  'th-TH': '^[ก-๙\s]+$',
  'tr-TR': '^[0-9A-ZÇĞİıÖŞÜ]+$',
  'uk-UA': '^[0-9А-ЩЬЮЯЄIЇҐі]+$',
  'ku-IQ': '^[٠١٢٣٤٥٦٧٨٩0-9ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆھەیێيطؤثآإأكضصةظذ]+$',
  'vi-VN': '^[0-9A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴĐÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ]+$',
  'ar': '^[٠١٢٣٤٥٦٧٨٩0-9ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٰ]+',
  'he': '^[0-9א-ת]+',
  'fa': '^[\'0-9آاءأؤئبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهةی۱۲۳۴۵۶۷۸۹۰\']+$',
  'hi-IN': '^[\u0900-\u0963]+[\u0966-\u097F]*$',
}

decimal = {
  'en-US': '.',
  'ar': '٫',
}


english_locales = ['AU', 'GB', 'HK', 'IN', 'NZ', 'ZA', 'ZM']

for i, locale in enumerate(english_locales):
    locale = "en-{}".format(english_locales[i])
    alpha[locale] = alpha['en-US']
    alphanumeric[locale] = alphanumeric['en-US']
    decimal[locale] = decimal['en-US']

arabic_locales = [
  'AE', 'BH', 'DZ', 'EG', 'IQ', 'JO', 'KW', 'LB', 'LY',
  'MA', 'QM', 'QA', 'SA', 'SD', 'SY', 'TN', 'YE',
]

for j, locale in enumerate(arabic_locales):
    locale = "ar-{}".format(arabic_locales[j])
    alpha[locale] = alpha['en-US']
    alphanumeric[locale] = alphanumeric['en-US']
    decimal[locale] = decimal['en-US']

farsi_locales = [
  'IR', 'AF',
]

for k, locale in enumerate(farsi_locales):
    locale = "fa-{}".format(farsi_locales[k])
    alpha[locale] = alpha['en-US']
    alphanumeric[locale] = alphanumeric['en-US']
    decimal[locale] = decimal['en-US']

dot_decimal = ['ar-EG', 'ar-LB', 'ar-LY']

for n, _ in enumerate(farsi_locales):
    decimal[dot_decimal[n]] = decimal['en-US']

comma_decimal = [
  'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-ZM', 'es-ES', 'fr-CA', 'fr-FR',
  'id-ID', 'it-IT', 'ku-IQ', 'hi-IN', 'hu-HU', 'nb-NO', 'nn-NO', 'nl-NL', 'pl-PL', 'pt-PT',
  'ru-RU', 'sl-SI', 'sr-RS@latin', 'sr-RS', 'sv-SE', 'tr-TR', 'uk-UA', 'vi-VN',
]

for m, _ in enumerate(comma_decimal):
    decimal[comma_decimal[m]] = decimal['en-US']

alpha['fr-CA'] = alpha['fr-FR']
alphanumeric['fr-CA'] = alphanumeric['fr-FR']

alpha['pt-BR'] = alpha['pt-PT']
alphanumeric['pt-BR'] = alphanumeric['pt-PT']
decimal['pt-BR'] = decimal['pt-PT']

alpha['pl-Pl'] = alpha['pl-PL']
alphanumeric['pl-Pl'] = alphanumeric['pl-PL']
decimal['pl-Pl'] = decimal['pl-PL']

alpha['fa-AF'] = alpha['fa']
