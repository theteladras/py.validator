import unittest
from validator import *

class TestIsEmail(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(is_email('foo@bar.com'))
        self.assertTrue(is_email('x@x.au'))
        self.assertTrue(is_email('foo@bar.com.au'))
        self.assertTrue(is_email('foo+bar@bar.com'))
        self.assertTrue(is_email('hans.m端ller@test.com'))
        self.assertTrue(is_email('hans@m端ller.com'))
        self.assertTrue(is_email('test|123@m端ller.com'))
        self.assertTrue(is_email('test123+ext@gmail.com'))
        self.assertTrue(is_email('some.name.midd.leNa.me.and.locality+extension@GoogleMail.com'))
        self.assertTrue(is_email('"foobar"@example.com'))
        self.assertTrue(is_email('"  foo  m端ller "@example.com'))
        self.assertTrue(is_email('"foo\\@bar"@example.com'))
        self.assertTrue(is_email("{}@{}.com".format(('a' * 64), ('a' * 63))))
        self.assertTrue(is_email("{}@{}.com".format(('a' * 64), ('a' * 63))))
        self.assertTrue(is_email("{}@gmail.com".format(('a' * 31))))
        self.assertTrue(is_email('test@gmail.com'))
        self.assertTrue(is_email('test.1@gmail.com'))
        self.assertTrue(is_email('test@1337.com'))
        print('OK - test_valid_email')

    def test_invalid_email(self):
        self.assertFalse(is_email('invalidemail@'))
        self.assertFalse(is_email('invalid.com'))
        self.assertFalse(is_email('@invalid.com'))
        self.assertFalse(is_email('foo@bar.com.'))
        self.assertFalse(is_email('somename@ｇｍａｉｌ.com'))
        self.assertFalse(is_email('foo@bar.co.uk.'))
        self.assertFalse(is_email('z@co.c'))
        self.assertFalse(is_email('ｇｍａｉｌｇｍａｉｌｇｍａｉｌｇｍａｉｌｇｍａｉｌ@gmail.com'))
        self.assertFalse(is_email("{}@{}.com".format('a' * 64, 'a' * 251)))
        self.assertFalse(is_email("{}@{}.com".format('a' * 65, 'a' * 250)))
        self.assertFalse(is_email("{}@{}.com".format('a' * 64, 'a' * 64)))
        self.assertFalse(is_email("{}@{}.{}.{}.{}.com".format('a' * 64, 'b' * 63, 'b' * 63, 'c' * 63, 'd' * 58)))
        self.assertFalse(is_email('test1@invalid.co m'))
        self.assertFalse(is_email('test2@invalid.co m'))
        self.assertFalse(is_email('test3@invalid.co m'))
        self.assertFalse(is_email('test4@invalid.co m'))
        self.assertFalse(is_email('test5@invalid.co m'))
        self.assertFalse(is_email('test6@invalid.co m'))
        self.assertFalse(is_email('test7@invalid.co m'))
        self.assertFalse(is_email('test8@invalid.co m'))
        self.assertFalse(is_email('test9@invalid.co m'))
        self.assertFalse(is_email('test10@invalid.co m'))
        self.assertFalse(is_email('test11@invalid.co m'))
        self.assertFalse(is_email('test12@invalid.co　m'))
        self.assertFalse(is_email('test13@invalid.co　m'))
        self.assertFalse(is_email('multiple..dots@stillinvalid.com'))
        self.assertFalse(is_email('test123+invalid! sub_address@gmail.com'))
        self.assertFalse(is_email('gmail...ignores...dots...@gmail.com'))
        self.assertFalse(is_email('ends.with.dot.@gmail.com'))
        self.assertFalse(is_email('multiple..dots@gmail.com'))
        self.assertFalse(is_email('wrong()[]",:;<>@@gmail.com'))
        self.assertFalse(is_email('"wrong()[]",:;<>@@gmail.com'))
        self.assertFalse(is_email('username@domain.com�'))
        self.assertFalse(is_email('username@domain.com©'))
        print('OK - test_invalid_email')

    def test_valid_domain_specific_email(self):
        self.assertTrue(is_email('foobar@gmail.com', { "domain_specific_validation": True }))
        self.assertTrue(is_email('foo.bar@gmail.com', { "domain_specific_validation": True }))
        self.assertTrue(is_email('foo.bar@googlemail.com', { "domain_specific_validation": True }))
        self.assertTrue(is_email('{}@gmail.com'.format('a' * 30), { "domain_specific_validation": True }))
        print('OK - test_valid_domain_specific_email')

    def test_invalid_domain_specific_email(self):
        self.assertFalse(is_email('test.1@gmail.com', { "domain_specific_validation": True }))
        self.assertFalse(is_email('.foobar@gmail.com', { "domain_specific_validation": True }))
        self.assertFalse(is_email("{}@gmail.com".format('s' * 31), { "domain_specific_validation": True }))
        print('OK - test_invalid_domain_specific_email')

    def test_valid_email_with_utf8_char_in_local_part(self):
        self.assertTrue(is_email('foo@bar.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('x@x.au', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('foo@bar.com.au', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('foo+bar@bar.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('hans@m端ller.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('test|123@m端ller.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('test123+ext@gmail.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('some.name.midd.leNa.me+extension@GoogleMail.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('"foobar"@example.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('"foo\\@bar"@example.com', { "allow_utf8_local_part": False }))
        self.assertTrue(is_email('"  foo  bar  "@example.com', { "allow_utf8_local_part": False }))
        print('OK - test_valid_email_with_utf8_char_in_local_part')

    def test_invalid_email_with_utf8_char_in_local_part(self):
        self.assertFalse(is_email('invalidemail@', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('invalid.com', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('@invalid.com', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('foo@bar.com.', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('foo@bar.co.uk.', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('somename@ｇｍａｉｌ.com', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('hans.m端ller@test.com', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('z@co.c', { "allow_utf8_local_part": False }))
        self.assertFalse(is_email('tüst@invalid.com', { "allow_utf8_local_part": False }))
        print('OK - test_invalid_email_with_utf8_char_in_local_part')

    def test_valid_email_with_display_name(self):
        self.assertTrue(is_email('foo@bar.com', { "allow_display_name": True }))
        self.assertTrue(is_email('x@x.au', { "allow_display_name": True }))
        self.assertTrue(is_email('foo@bar.com.au', { "allow_display_name": True }))
        self.assertTrue(is_email('foo+bar@bar.com', { "allow_display_name": True }))
        self.assertTrue(is_email('hans.m端ller@test.com', { "allow_display_name": True }))
        self.assertTrue(is_email('hans@m端ller.com', { "allow_display_name": True }))
        self.assertTrue(is_email('test|123@m端ller.com', { "allow_display_name": True }))
        self.assertTrue(is_email('test123+ext@gmail.com', { "allow_display_name": True }))
        self.assertTrue(is_email('some.name.midd.leNa.me+extension@GoogleMail.com', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <foo@bar.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <x@x.au>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <foo@bar.com.au>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <foo+bar@bar.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <hans.m端ller@test.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <hans@m端ller.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <test|123@m端ller.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <test123+ext@gmail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('\'Foo Bar, Esq\'<foo@bar.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Middle Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Name<some.name.midd.leNa.me+extension@GoogleMail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Some Name <foo@gmail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('Name🍓With🍑Emoji🚴‍♀️🏆<test@aftership.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('🍇🍗🍑<only_emoji@aftership.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('"<displayNameInBrackets>"<jh@gmail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('"\\"quotes\\""<jh@gmail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('"name;"<jh@gmail.com>', { "allow_display_name": True }))
        self.assertTrue(is_email('"name;" <jh@gmail.com>', { "allow_display_name": True }))
        print('OK - test_valid_email_with_display_name')

    def test_invalid_email_with_display_name(self):
        self.assertFalse(is_email('invalidemail@', { "allow_display_name": True }))
        self.assertFalse(is_email('invalid.com', { "allow_display_name": True }))
        self.assertFalse(is_email('@invalid.com', { "allow_display_name": True }))
        self.assertFalse(is_email('foo@bar.com.', { "allow_display_name": True }))
        self.assertFalse(is_email('foo@bar.co.uk.', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <invalidemail@>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <invalid.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <@invalid.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.com.>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.co.uk.>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name foo@bar.co.uk.>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.co.uk.', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name < foo@bar.co.uk >', { "allow_display_name": True }))
        self.assertFalse(is_email('Name foo@bar.co.uk', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name <some..name@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('Some Name<emoji_in_address🍈@aftership.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('invisibleCharacter\u001F<jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('<displayNameInBrackets><jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('\\"quotes\\"<jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('""quotes""<jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('name;<jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('    <jh@gmail.com>', { "allow_display_name": True }))
        self.assertFalse(is_email('"    "<jh@gmail.com>', { "allow_display_name": True }))
        print('OK - test_invalid_email_with_display_name')

    def test_valid_email_with_required_display_name(self):
        self.assertTrue(is_email('Some Name <foo@bar.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <x@x.au>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <foo@bar.com.au>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <foo+bar@bar.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <hans.m端ller@test.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <hans@m端ller.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <test|123@m端ller.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <test123+ext@gmail.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Some Middle Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Name <some.name.midd.leNa.me+extension@GoogleMail.com>', { "require_display_name": True }))
        self.assertTrue(is_email('Name<some.name.midd.leNa.me+extension@GoogleMail.com>', { "require_display_name": True }))
        print('OK - test_valid_email_with_required_display_name')

    def test_invalid_email_with_required_display_name(self):
        self.assertFalse(is_email('some.name.midd.leNa.me+extension@GoogleMail.com', { "require_display_name": True }))
        self.assertFalse(is_email('foo@bar.com', { "require_display_name": True }))
        self.assertFalse(is_email('x@x.au', { "require_display_name": True }))
        self.assertFalse(is_email('foo@bar.com.au', { "require_display_name": True }))
        self.assertFalse(is_email('foo+bar@bar.com', { "require_display_name": True }))
        self.assertFalse(is_email('hans.m端ller@test.com', { "require_display_name": True }))
        self.assertFalse(is_email('hans@m端ller.com', { "require_display_name": True }))
        self.assertFalse(is_email('test|123@m端ller.com', { "require_display_name": True }))
        self.assertFalse(is_email('test123+ext@gmail.com', { "require_display_name": True }))
        self.assertFalse(is_email('invalidemail@', { "require_display_name": True }))
        self.assertFalse(is_email('invalid.com', { "require_display_name": True }))
        self.assertFalse(is_email('@invalid.com', { "require_display_name": True }))
        self.assertFalse(is_email('foo@bar.com.', { "require_display_name": True }))
        self.assertFalse(is_email('foo@bar.co.uk.', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <invalidemail@>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <invalid.com>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <@invalid.com>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.com.>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.co.uk.>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name foo@bar.co.uk.>', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name <foo@bar.co.uk.', { "require_display_name": True }))
        self.assertFalse(is_email('Some Name < foo@bar.co.uk >', { "require_display_name": True }))
        self.assertFalse(is_email('Name foo@bar.co.uk', { "require_display_name": True }))
        print('OK - test_invalid_email_with_required_display_name')

    def test_valid_emails_with_ip(self):
        self.assertTrue(is_email('email@[123.123.123.123]', { "allow_ip_domain": True }))
        self.assertTrue(is_email('email@255.255.255.255', { "allow_ip_domain": True }))
        print('OK - test_valid_emails_with_ip')

    def test_invalid_emails_with_ip(self):
        self.assertFalse(is_email('email@0.0.0.256', { "allow_ip_domain": True }))
        self.assertFalse(is_email('email@26.0.0.256', { "allow_ip_domain": True }))
        self.assertFalse(is_email('email@[266.266.266.266]', { "allow_ip_domain": True }))
        print('OK - test_invalid_emails_with_ip')

    def test_valid_emails_with_blacklisted_chars_in_name(self):
        self.assertTrue(is_email('emil@gmail.com', { "blacklisted_chars": 'abc' }))
        self.assertTrue(is_email('ssss@gmail.com', { "blacklisted_chars": 'abc' }))
        self.assertFalse(is_email('today@yahoo.com', { "blacklisted_chars": 'time' }))
        print('OK - test_valid_emails_with_blacklisted_chars_in_name')

    def test_invalid_emails_with_blacklisted_chars_in_name(self):
        self.assertFalse(is_email('email@gmail.com', { "blacklisted_chars": 'abc' }))
        self.assertFalse(is_email('ssss@gmail.com', { "blacklisted_chars": 's' }))
        self.assertFalse(is_email('ssss@gmail.com', { "blacklisted_chars": 'ssss' }))
        self.assertFalse(is_email('today@yahoo.com', { "blacklisted_chars": 'day' }))
        print('OK - test_invalid_emails_with_blacklisted_chars_in_name')

    def test_valid_long_emails(self):
        self.assertTrue(is_email('Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX@example.com', { "ignore_max_length": True }))
        print('OK - test_valid_long_emails')

    def test_invalid_long_emails(self):
        self.assertFalse(is_email('Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX@example.com', { "ignore_max_length": False }))
        self.assertFalse(is_email('Deleted-user-id-19430-Team-5051deleted-user-id-19430-team-5051XXXXXX-blablabla-blablabla-blablabla-blablabla-blablabla-blablabla@example.com', { "ignore_max_length": False }))
        print('OK - test_invalid_long_emails')

    def test_valid_emails_with_denied_domains(self):
        self.assertTrue(is_email('sample@test.com', { "host_blacklist": ['web.com', 'test.domain.com'] }))
        self.assertTrue(is_email('sample@domain.com', { "host_blacklist": ['web.com', 'test.domain.com'] }))
        print('OK - test_valid_emails_with_denied_domains')

    def test_invalid_emails_with_denied_domains(self):
        self.assertFalse(is_email('gosn@web.com', { "host_blacklist": ['web.com', 'test.domain.com'] }))
        self.assertFalse(is_email('gosn@test.domain.com', { "host_blacklist": ['web.com', 'test.domain.com'] }))
        print('OK - test_invalid_emails_with_denied_domains')