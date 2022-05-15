import unittest

from pyvalidator.is_email import is_email
from . import print_test_ok


class TestIsEmail(unittest.TestCase):

    def test_valid_email(self):
        for i in [
            'foo@bar.com',
            'x@x.au',
            'foo@bar.com.au',
            'foo+bar@bar.com',
            'hans.m端ller@test.com',
            'hans@m端ller.com',
            'test|123@m端ller.com',
            'test123+ext@gmail.com',
            'some.name.midd.leNa.me.and.locality+extension@GoogleMail.com',
            '"foobar"@example.com',
            '"  foo  m端ller "@example.com',
            '"foo\\@bar"@example.com',
            "{}@{}.com".format(('a' * 64), ('a' * 63)),
            "{}@{}.com".format(('a' * 64), ('a' * 63)),
            "{}@gmail.com".format(('a' * 31)),
            'test@gmail.com',
            'test.1@gmail.com',
            'test@1337.com',
        ]:
            self.assertTrue(is_email(i))
        print_test_ok()

    def test_invalid_email(self):
        for i in [
            'invalidemail@',
            'invalid.com',
            '@invalid.com',
            'foo@bar.com.',
            'somename@ｇｍａｉｌ.com',
            'foo@bar.co.uk.',
            'z@co.c',
            'ｇｍａｉｌｇｍａｉｌｇｍａｉｌｇｍａｉｌｇｍａｉｌ@gmail.com',
            "{}@{}.com".format('a' * 64, 'a' * 251),
            "{}@{}.com".format('a' * 65, 'a' * 250),
            "{}@{}.com".format('a' * 64, 'a' * 64),
            "{}@{}.{}.{}.{}.com".format('a' * 64, 'b' * 63, 'b' * 63, 'c' * 63, 'd' * 58),
            'test1@invalid.co m',
            'test2@invalid.co m',
            'test3@invalid.co m',
            'test4@invalid.co m',
            'test5@invalid.co m',
            'test6@invalid.co m',
            'test7@invalid.co m',
            'test8@invalid.co m',
            'test9@invalid.co m',
            'test10@invalid.co m',
            'test11@invalid.co m',
            'test12@invalid.co　m',
            'test13@invalid.co　m',
            'multiple..dots@stillinvalid.com',
            'test123+invalid! sub_address@gmail.com',
            'gmail...ignores...dots...@gmail.com',
            'ends.with.dot.@gmail.com',
            'multiple..dots@gmail.com',
            'wrong()[]",:;<>@@gmail.com',
            '"wrong()[]",:;<>@@gmail.com',
            'username@domain.com�',
            'username@domain.com©',
        ]:
            self.assertFalse(is_email(i))
        print_test_ok()

    def test_valid_domain_specific_email(self):
        for i in [
            'foobar@gmail.com',
            'foo.bar@gmail.com',
            'foo.bar@googlemail.com',
            '{}@gmail.com'.format('a' * 30),
        ]:
            self.assertTrue(is_email(i, {"domain_specific_validation": True}))
        print_test_ok()

    def test_invalid_domain_specific_email(self):
        for i in [
            'test.1@gmail.com',
            '.foobar@gmail.com',
            "{}@gmail.com".format('s' * 31),
        ]:
            self.assertFalse(is_email(i, {"domain_specific_validation": True}))
        print_test_ok()

    def test_valid_email_with_utf8_char_in_local_part(self):
        for i in [
            'foo@bar.com',
            'x@x.au',
            'foo@bar.com.au',
            'foo+bar@bar.com',
            'hans@m端ller.com',
            'test|123@m端ller.com',
            'test123+ext@gmail.com',
            'some.name.midd.leNa.me+extension@GoogleMail.com',
            '"foobar"@example.com',
            '"foo\\@bar"@example.com',
            '"  foo  bar  "@example.com',
        ]:
            self.assertTrue(is_email(i, {"allow_utf8_local_part": False}))
        print_test_ok()

    def test_invalid_email_with_utf8_char_in_local_part(self):
        for i in [
            'invalidemail@',
            'invalid.com',
            '@invalid.com',
            'foo@bar.com.',
            'foo@bar.co.uk.',
            'somename@ｇｍａｉｌ.com',
            'hans.m端ller@test.com',
            'z@co.c',
            'tüst@invalid.com',
        ]:
            self.assertFalse(is_email(i, {"allow_utf8_local_part": False}))
        print_test_ok()

    def test_valid_email_with_display_name(self):
        for i in [
            'foo@bar.com',
            'x@x.au',
            'foo@bar.com.au',
            'foo+bar@bar.com',
            'hans.m端ller@test.com',
            'hans@m端ller.com',
            'test|123@m端ller.com',
            'test123+ext@gmail.com',
            'some.name.midd.leNa.me+extension@GoogleMail.com',
            'Some Name <foo@bar.com>',
            'Some Name <x@x.au>',
            'Some Name <foo@bar.com.au>',
            'Some Name <foo+bar@bar.com>',
            'Some Name <hans.m端ller@test.com>',
            'Some Name <hans@m端ller.com>',
            'Some Name <test|123@m端ller.com>',
            'Some Name <test123+ext@gmail.com>',
            '\'Foo Bar, Esq\'<foo@bar.com>',
            'Some Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Some Middle Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Name<some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Some Name <foo@gmail.com>',
            'Name🍓With🍑Emoji🚴‍♀️🏆<test@aftership.com>',
            '🍇🍗🍑<only_emoji@aftership.com>',
            '"<displayNameInBrackets>"<jh@gmail.com>',
            '"\\"quotes\\""<jh@gmail.com>',
            '"name;"<jh@gmail.com>',
            '"name;" <jh@gmail.com>',
        ]:
            self.assertTrue(is_email(i, {"allow_display_name": True}))
        print_test_ok()

    def test_invalid_email_with_display_name(self):
        for i in [
            'invalidemail@',
            'invalid.com',
            '@invalid.com',
            'foo@bar.com.',
            'foo@bar.co.uk.',
            'Some Name <invalidemail@>',
            'Some Name <invalid.com>',
            'Some Name <@invalid.com>',
            'Some Name <foo@bar.com.>',
            'Some Name <foo@bar.co.uk.>',
            'Some Name foo@bar.co.uk.>',
            'Some Name <foo@bar.co.uk.',
            'Some Name < foo@bar.co.uk >',
            'Name foo@bar.co.uk',
            'Some Name <some..name@gmail.com>',
            'Some Name<emoji_in_address🍈@aftership.com>',
            'invisibleCharacter\u001F<jh@gmail.com>',
            '<displayNameInBrackets><jh@gmail.com>',
            '\\"quotes\\"<jh@gmail.com>',
            '""quotes""<jh@gmail.com>',
            'name;<jh@gmail.com>',
            '    <jh@gmail.com>',
            '"    "<jh@gmail.com>',
        ]:
            self.assertFalse(is_email(i, {"allow_display_name": True}))
        print_test_ok()

    def test_valid_email_with_required_display_name(self):
        for i in [
            'Some Name <foo@bar.com>',
            'Some Name <x@x.au>',
            'Some Name <foo@bar.com.au>',
            'Some Name <foo+bar@bar.com>',
            'Some Name <hans.m端ller@test.com>',
            'Some Name <hans@m端ller.com>',
            'Some Name <test|123@m端ller.com>',
            'Some Name <test123+ext@gmail.com>',
            'Some Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Some Middle Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Name <some.name.midd.leNa.me+extension@GoogleMail.com>',
            'Name<some.name.midd.leNa.me+extension@GoogleMail.com>',
        ]:
            self.assertTrue(is_email(i, {"require_display_name": True}))
        print_test_ok()

    def test_invalid_email_with_required_display_name(self):
        for i in [
            'some.name.midd.leNa.me+extension@GoogleMail.com',
            'foo@bar.com',
            'x@x.au',
            'foo@bar.com.au',
            'foo+bar@bar.com',
            'hans.m端ller@test.com',
            'hans@m端ller.com',
            'test|123@m端ller.com',
            'test123+ext@gmail.com',
            'invalidemail@',
            'invalid.com',
            '@invalid.com',
            'foo@bar.com.',
            'foo@bar.co.uk.',
            'Some Name <invalidemail@>',
            'Some Name <invalid.com>',
            'Some Name <@invalid.com>',
            'Some Name <foo@bar.com.>',
            'Some Name <foo@bar.co.uk.>',
            'Some Name foo@bar.co.uk.>',
            'Some Name <foo@bar.co.uk.',
            'Some Name < foo@bar.co.uk >',
            'Name foo@bar.co.uk',
        ]:
            self.assertFalse(is_email(i, {"require_display_name": True}))
        print_test_ok()

    def test_valid_emails_with_ip(self):
        for i in [
            'email@[123.123.123.123]',
            'email@255.255.255.255',
        ]:
            self.assertTrue(is_email(i, {"allow_ip_domain": True}))
        print_test_ok()

    def test_invalid_emails_with_ip(self):
        for i in [
            'email@0.0.0.256',
            'email@26.0.0.256',
            'email@[266.266.266.266]',
        ]:
            self.assertFalse(is_email(i, {"allow_ip_domain": True}))
        print_test_ok()

    def test_valid_emails_with_blacklisted_chars_in_name(self):
        for i in [
            ['emil@gmail.com', {"blacklisted_chars": 'abc'}],
            ['ssss@gmail.com', {"blacklisted_chars": 'abc'}],
        ]:
            self.assertTrue(is_email(*i))
        for i in [
            ['today@yahoo.com', {"blacklisted_chars": 'time'}],
        ]:
            self.assertFalse(is_email(*i))
        print_test_ok()

    def test_invalid_emails_with_blacklisted_chars_in_name(self):
        for i in [
            ['email@gmail.com', {"blacklisted_chars": 'abc'}],
            ['ssss@gmail.com', {"blacklisted_chars": 's'}],
            ['ssss@gmail.com', {"blacklisted_chars": 'ssss'}],
            ['today@yahoo.com', {"blacklisted_chars": 'day'}],
        ]:
            self.assertFalse(is_email(*i))
        print_test_ok()

    def test_valid_long_emails(self):
        for i in [
            'Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX@example.com',
        ]:
            self.assertTrue(is_email(i, {"ignore_max_length": True}))
        print_test_ok()

    def test_invalid_long_emails(self):
        for i in [
            'Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX@example.com',
            'Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX-blablabla-blablabla-blablabla-blablabla-blablabla-blablabla@example.com',
        ]:
            self.assertFalse(is_email(i, {"ignore_max_length": False}))
        print_test_ok()

    def test_valid_emails_with_denied_domains(self):
        for i in [
            ['sample@test.com', {"host_blacklist": ['web.com', 'test.domain.com']}],
            ['sample@domain.com', {"host_blacklist": ['web.com', 'test.domain.com']}],
        ]:
            self.assertTrue(is_email(*i))
        print_test_ok()

    def test_invalid_emails_with_denied_domains(self):
        for i in [
            ['gosn@web.com', {"host_blacklist": ['web.com', 'test.domain.com']}],
            ['gosn@test.domain.com', {"host_blacklist": ['web.com', 'test.domain.com']}],
        ]:
            self.assertFalse(is_email(*i))
        print_test_ok()
