import unittest

from pyvalidator import *


class TestIsAlpha(unittest.TestCase):
    def valid_check(self, items, locale = None, options = {}):
        for item in items:
            try:
                self.assertTrue(is_alpha(item, locale, options))
            except Exception as e:
                print(f'failed for input: {item}')
                raise e

    def invalid_check(self, items, locale = None, options = {}):
        for item in items:
            try:
                self.assertFalse(is_alpha(item, locale, options))
            except Exception as e:
                print(f'failed for input: {item}')
                raise e

    def test_valid_alpha_strings(self):
        valid = [
            'abc',
            'ABC',
            'FoObar',
        ]

        self.valid_check(valid)
        print('OK - test_valid_alpha_strings')

    def test_invalid_alpha_strings(self):
        invalid = [
            'abc1',
            '  foo  ',
            'FÜübar',
            'Jön',
        ]

        self.invalid_check(invalid)
        print('OK - test_invalid_alpha_strings')

    def test_valid_alpha_strings_with_ignored_characters(self):
        valid = [
            'en-US',
            'this is a valid alpha string',
            'us/usa',
        ]
        self.valid_check(valid, 'en-US', { "ignore": '- /' })
        print('OK - test_valid_alpha_strings_with_ignored_characters')

    def test_invalid_alpha_strings_with_ignored_characters(self):
        invalid = [
            '1. this is not a valid alpha string',
            'this$is also not a valid.alpha string',
            'this is also not a valid alpha string.',
        ]
        self.invalid_check(invalid, 'en-US', { "ignore": '- /' })
        print('OK - test_invalid_alpha_strings_with_ignored_characters', 'en-US', { "ignore": '- /' })

    def test_should_throw_for_invalid_ignore_matcher(self):
        self.assertRaises(Exception, is_alpha, ['this is also not a valid alpha string.', 'en-US', { "ignore": 123 }])
        print('OK - test_should_throw_for_invalid_ignore_matcher')

    def test_valid_azerbaijani_string(self):
        valid = [
            'Azərbaycan',
            'Bakı',
            'üöğıəçş',
            'sizAzərbaycanlaşdırılmışlardansınızmı',
            'dahaBirDüzgünString',
            'abcçdeəfgğhxıijkqlmnoöprsştuüvyz',
        ]

        self.valid_check(valid, 'az-AZ')
        print('OK - test_valid_azerbaijani_alpha_strings')

    def test_invalid_azerbaijani_string(self):
        invalid = [
            'rəqəm1',
            '  foo  ',
            '',
            'ab(cd)',
            'simvol@',
            'wəkil',
        ]

        self.invalid_check(invalid, 'az-AZ')
        print('OK - test_invalid_azerbaijani_alpha_strings')

    def test_valid_bulgarian_string(self):
        valid = [
            'абв',
            'АБВ',
            'жаба',
            'яГоДа',
        ]

        self.valid_check(valid, 'bg-BG')
        print('OK - test_valid_bulgarian_alpha_strings')

    def test_invalid_bulgarian_string(self):
        invalid = [
            'abc1',
            '  foo  ',
            '',
            'ЁЧПС',
            '_аз_обичам_обувки_',
            'ехо!',
        ]

        self.invalid_check(invalid, 'bg-BG')
        print('OK - test_invalid_bulgarian_alpha_strings')

    def test_valid_czech_string(self):
        valid = [
            'žluťoučký',
            'KŮŇ',
            'Pěl',
            'Ďábelské',
            'ódy',
        ]

        self.valid_check(valid, 'cs-CZ')
        print('OK - test_valid_czech_alpha_strings')

    def test_invalid_czech_string(self):
        invalid = [
            'ábc1',
            '  fůj  ',
            '',
        ]

        self.invalid_check(invalid, 'cs-CZ')
        print('OK - test_invalid_czech_alpha_strings')

    def test_valid_slovak_string(self):
        valid = [
            'môj',
            'ľúbím',
            'mäkčeň',
            'stĹp',
            'vŕba',
            'ňorimberk',
            'ťava',
            'žanéta',
            'Ďábelské',
            'ódy',
        ]

        self.valid_check(valid, 'sk-SK')
        print('OK - test_valid_slovak_alpha_strings')

    def test_invalid_slovak_string(self):
        invalid = [
            '1moj',
            '你好世界',
            '  Привет мир  ',
            'مرحبا العا '
        ]

        self.invalid_check(invalid, 'sk-SK')
        print('OK - test_invalid_slovak_alpha_strings')

    def test_valid_danish_string(self):
        valid = [
            'aøå',
            'Ære',
            'Øre',
            'Åre',
        ]

        self.valid_check(valid, 'da-DK')
        print('OK - test_valid_danish_alpha_strings')

    def test_invalid_danish_string(self):
        invalid = [
            'äbc123',
            'ÄBC11',
            '',
        ]

        self.invalid_check(invalid, 'da-DK')
        print('OK - test_invalid_danish_alpha_strings')

    def test_valid_dutch_string(self):
        valid = [
            'Kán',
            'één',
            'vóór',
            'nú',
            'héél',
        ]

        self.valid_check(valid, 'nl-NL')
        print('OK - test_valid_dutch_alpha_strings')

    def test_invalid_dutch_string(self):
        invalid = [
            'äca ',
            'abcß',
            'Øre',
        ]

        self.invalid_check(invalid, 'nl-NL')
        print('OK - test_invalid_dutch_alpha_strings')

    def test_valid_german_string(self):
        valid = [
            'äbc',
            'ÄBC',
            'FöÖbär',
            'Heiß',
        ]

        self.valid_check(valid, 'de-DE')
        print('OK - test_valid_german_alpha_strings')

    def test_invalid_german_string(self):
        invalid = [
            'äbc1',
            '  föö  ',
            '',
        ]

        self.invalid_check(invalid, 'de-DE')
        print('OK - test_invalid_german_alpha_strings')

    def test_valid_hungarian_string(self):
        valid = [
            'árvíztűrőtükörfúrógép',
            'ÁRVÍZTŰRŐTÜKÖRFÚRÓGÉP',
        ]

        self.valid_check(valid, 'hu-HU')
        print('OK - test_valid_hungarian_alpha_strings')

    def test_invalid_hungarian_string(self):
        invalid = [
            'äbc1',
            '  fäö  ',
            'Heiß',
            '',
        ]

        self.invalid_check(invalid, 'hu-HU')
        print('OK - test_invalid_hungarian_alpha_strings')

    def test_valid_portuguese_string(self):
        valid = [
            'palíndromo',
            'órgão',
            'qwértyúão',
            'àäãcëüïÄÏÜ',
        ]

        self.valid_check(valid, 'pt-PT')
        print('OK - test_valid_portuguese_alpha_strings')

    def test_invalid_portuguese_string(self):
        invalid = [
            '12abc',
            'Heiß',
            'Øre',
            'æøå',
            '',
        ]

        self.invalid_check(invalid, 'pt-PT')
        print('OK - test_invalid_portuguese_alpha_strings')

    def test_valid_italian_string(self):
        valid = [
            'àéèìîóòù',
            'correnti',
            'DEFINIZIONE',
            'compilazione',
            'metró',
            'pèsca',
            'PÉSCA',
            'genî',
        ]

        self.valid_check(valid, 'it-IT')
        print('OK - test_valid_italian_alpha_strings')

    def test_invalid_italian_string(self):
        invalid = [
            'äbc123',
            'ÄBC11',
            'æøå',
            '',
        ]

        self.invalid_check(invalid, 'it-IT')
        print('OK - test_invalid_italian_alpha_strings')

    def test_valid_vietnamese_string(self):
        valid = [
            'thiến',
            'nghiêng',
            'xin',
            'chào',
            'thế',
            'giới',
        ]

        self.valid_check(valid, 'vi-VN')
        print('OK - test_valid_vietnamese_alpha_strings')

    def test_invalid_vietnamese_string(self):
        invalid = [
            'thầy3',
            'Ba gà',
            '',
        ]

        self.invalid_check(invalid, 'vi-VN')
        print('OK - test_invalid_vietnamese_alpha_strings')

    def test_valid_arabic_string(self):
        valid = [
            'أبت',
            'اَبِتَثّجً',
        ]

        self.valid_check(valid, 'ar')
        print('OK - test_valid_arabic_alpha_strings')

    def test_invalid_arabic_string(self):
        invalid = [
            '١٢٣أبت',
            '١٢٣',
            'abc1',
            '  foo  ',
            '',
            'ÄBC',
            'FÜübar',
            'Jön',
            'Heiß',
        ]

        self.invalid_check(invalid, 'ar')
        print('OK - test_invalid_arabic_alpha_strings')

    def test_valid_finnish_string(self):
        valid = [
            'äiti',
            'Öljy',
            'Åke',
            'testÖ',
        ]

        self.valid_check(valid, 'fi-FI')
        print('OK - test_valid_finnish_alpha_strings')

    def test_invalid_finnish_string(self):
        invalid = [
            'AİıÖöÇçŞşĞğÜüZ',
            'äöå123',
            '',
        ]

        self.invalid_check(invalid, 'fi-FI')
        print('OK - test_invalid_finnish_alpha_strings')

    def test_valid_polish_string(self):
        valid = [
            'kreską',
            'zamknięte',
            'zwykłe',
            'kropką',
            'przyjęły',
            'święty',
            'Pozwól',
        ]

        self.valid_check(valid, 'pl-PL')
        print('OK - test_valid_polish_alpha_strings')

    def test_invalid_polish_string(self):
        invalid = [
            '12řiď ',
            'blé!!',
            'föö!2!',
        ]

        self.invalid_check(invalid, 'pl-PL')
        print('OK - test_invalid_polish_alpha_strings')
