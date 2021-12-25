import unittest
from pyvalidator import *

class TestIsHash(unittest.TestCase):

    len_32 = [
        'd94f3f016ae679c3008de268209132f2',
        '751adbc511ccbe8edf23d486fa4581cd',
        '88dae00e614d8f24cfd5a8b3f8002e93',
        '0bf1c35032a71a14c2f719e5a14c1e96',
        'd94f3F016Ae679C3008de268209132F2',
        '88DAE00e614d8f24cfd5a8b3f8002E93',
    ]

    len_8 = [
        'd94f3f01',
        '751adbc5',
        '88dae00e',
        '0bf1c350',
        '88DAE00e',
        '751aDBc5',
    ]

    len_40 = [
        '3ca25ae354e192b26879f651a51d92aa8a34d8d3',
        'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d',
        'beb8c3f30da46be179b8df5f5ecb5e4b10508230',
        'efd5d3b190e893ed317f38da2420d63b7ae0d5ed',
        'AAF4c61ddCC5e8a2dabede0f3b482cd9AEA9434D',
        '3ca25AE354e192b26879f651A51d92aa8a34d8D3',
    ]

    len_48 = [
        '6281a1f098c5e7290927ed09150d43ff3990a0fe1a48267c',
        '56268f7bc269cf1bc83d3ce42e07a85632394737918f4760',
        '46fc0125a148788a3ac1d649566fc04eb84a746f1a6e4fa7',
        '7731ea1621ae99ea3197b94583d034fdbaa4dce31a67404a',
        '6281A1f098c5e7290927ed09150d43ff3990a0fe1a48267C',
        '46FC0125a148788a3AC1d649566fc04eb84A746f1a6E4fa7',
    ]

    len_64 = [
        '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
        '1d996e033d612d9af2b44b70061ee0e868bfd14c2dd90b129e1edeb7953e7985',
        '80f70bfeaed5886e33536bcfa8c05c60afef5a0e48f699a7912d5e399cdcc441',
        '579282cfb65ca1f109b78536effaf621b853c9f7079664a3fbe2b519f435898c',
        '2CF24dba5FB0a30e26E83b2AC5b9E29E1b161e5C1fa7425E73043362938b9824',
        '80F70bFEAed5886e33536bcfa8c05c60aFEF5a0e48f699a7912d5e399cdCC441',
    ]

    len_96 = [
        '3fed1f814d28dc5d63e313f8a601ecc4836d1662a19365cbdcf6870f6b56388850b58043f7ebf2418abb8f39c3a42e31',
        'b330f4e575db6e73500bd3b805db1a84b5a034e5d21f0041d91eec85af1dfcb13e40bb1c4d36a72487e048ac6af74b58',
        'bf547c3fc5841a377eb1519c2890344dbab15c40ae4150b4b34443d2212e5b04aa9d58865bf03d8ae27840fef430b891',
        'fc09a3d11368386530f985dacddd026ae1e44e0e297c805c3429d50744e6237eb4417c20ffca8807b071823af13a3f65',
        '3fed1f814d28dc5d63e313f8A601ecc4836d1662a19365CBDCf6870f6b56388850b58043f7ebf2418abb8f39c3a42e31',
        'b330f4E575db6e73500bd3b805db1a84b5a034e5d21f0041d91EEC85af1dfcb13e40bb1c4d36a72487e048ac6af74b58',
    ]

    len_128 = [
        '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043',
        '83c586381bf5ba94c8d9ba8b6b92beb0997d76c257708742a6c26d1b7cbb9269af92d527419d5b8475f2bb6686d2f92a6649b7f174c1d8306eb335e585ab5049',
        '45bc5fa8cb45ee408c04b6269e9f1e1c17090c5ce26ffeeda2af097735b29953ce547e40ff3ad0d120e5361cc5f9cee35ea91ecd4077f3f589b4d439168f91b9',
        '432ac3d29e4f18c7f604f7c3c96369a6c5c61fc09bf77880548239baffd61636d42ed374f41c261e424d20d98e320e812a6d52865be059745fdb2cb20acff0ab',
        '9B71D224bd62f3785D96d46ad3ea3d73319bFBC2890CAAdae2dff72519673CA72323C3d99ba5c11d7c7ACC6e14b8c5DA0c4663475c2E5c3adef46f73bcDEC043',
        '432AC3d29E4f18c7F604f7c3c96369A6C5c61fC09Bf77880548239baffd61636d42ed374f41c261e424d20d98e320e812a6d52865be059745fdb2cb20acff0ab',
    ]

    def test_valid_hash_md5(self):
        for hash in self.len_32:
            self.assertTrue(is_hash(hash, 'md5'))
        print('OK - test_valid_hash_md5')

    def test_invalid_hash_md5(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'md5'))
        self.assertFalse(is_hash('q94375dj93458w34', 'md5'))
        self.assertFalse(is_hash('q94375dj93458w34', 'md5'))
        self.assertFalse(is_hash('39485729348', 'md5'))
        self.assertFalse(is_hash('q943', 'md5'))
        self.assertFalse(is_hash('%&FHKJFvk', 'md5'))
        self.assertFalse(is_hash('39485729348', 'md5'))
        print('OK - test_invalid_hash_md5')

    def test_valid_hash_md4(self):
        for hash in self.len_32:
            self.assertTrue(is_hash(hash, 'md4'))
        print('OK - test_valid_hash_md4')

    def test_invalid_hash_md4(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'md4'))
        self.assertFalse(is_hash('q94375dj93458w34', 'md4'))
        self.assertFalse(is_hash('q94375dj93458w34', 'md4'))
        self.assertFalse(is_hash('39485729348', 'md4'))
        self.assertFalse(is_hash('q943', 'md4'))
        self.assertFalse(is_hash('%&FHKJFvk', 'md4'))
        self.assertFalse(is_hash('39485729348', 'md4'))
        print('OK - test_invalid_hash_md4')

    def test_valid_hash_ripemd128(self):
        for hash in self.len_32:
            self.assertTrue(is_hash(hash, 'ripemd128'))
        print('OK - test_valid_hash_ripemd128')

    def test_invalid_hash_ripemd128(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'ripemd128'))
        self.assertFalse(is_hash('q94375dj93458w34', 'ripemd128'))
        self.assertFalse(is_hash('q94375dj93458w34', 'ripemd128'))
        self.assertFalse(is_hash('39485729348', 'ripemd128'))
        self.assertFalse(is_hash('q943', 'ripemd128'))
        self.assertFalse(is_hash('%&FHKJFvk', 'ripemd128'))
        self.assertFalse(is_hash('39485729348', 'ripemd128'))
        print('OK - test_invalid_hash_ripemd128')

    def test_valid_hash_tiger128(self):
        for hash in self.len_32:
            self.assertTrue(is_hash(hash, 'tiger128'))
        print('OK - test_valid_hash_tiger128')

    def test_invalid_hash_tiger128(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'tiger128'))
        self.assertFalse(is_hash('q94375dj93458w34', 'tiger128'))
        self.assertFalse(is_hash('q94375dj93458w34', 'tiger128'))
        self.assertFalse(is_hash('39485729348', 'tiger128'))
        self.assertFalse(is_hash('q943', 'tiger128'))
        self.assertFalse(is_hash('%&FHKJFvk', 'tiger128'))
        self.assertFalse(is_hash('39485729348', 'tiger128'))
        print('OK - test_invalid_hash_tiger128')

    def test_valid_hash_crc32(self):
        for hash in self.len_8:
            self.assertTrue(is_hash(hash, 'crc32'))
        print('OK - test_valid_hash_crc32')

    def test_invalid_hash_crc32(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'crc32'))
        self.assertFalse(is_hash('q94375dj93458w34', 'crc32'))
        self.assertFalse(is_hash('q943', 'crc32'))
        self.assertFalse(is_hash('39485729348', 'crc32'))
        self.assertFalse(is_hash('%&FHKJFvk', 'crc32'))
        print('OK - test_invalid_hash_crc32')

    def test_valid_hash_crc32b(self):
        for hash in self.len_8:
            self.assertTrue(is_hash(hash, 'crc32b'))
        print('OK - test_valid_hash_crc32b')

    def test_invalid_hash_crc32b(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'crc32b'))
        self.assertFalse(is_hash('q94375dj93458w34', 'crc32b'))
        self.assertFalse(is_hash('q943', 'crc32b'))
        self.assertFalse(is_hash('39485729348', 'crc32b'))
        self.assertFalse(is_hash('%&FHKJFvk', 'crc32b'))
        print('OK - test_invalid_hash_crc32b')

    def test_valid_hash_sha1(self):
        for hash in self.len_40:
            self.assertTrue(is_hash(hash, 'sha1'))
        print('OK - test_valid_hash_sha1')

    def test_invalid_hash_sha1(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'sha1'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'sha1'))
        self.assertFalse(is_hash('q943', 'sha1'))
        self.assertFalse(is_hash('q94375dj93458w34', 'sha1'))
        self.assertFalse(is_hash('%&FHKJFvk', 'sha1'))
        print('OK - test_invalid_hash_sha1')

    def test_valid_hash_tiger160(self):
        for hash in self.len_40:
            self.assertTrue(is_hash(hash, 'tiger160'))
        print('OK - test_valid_hash_tiger160')

    def test_invalid_hash_tiger160(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'tiger160'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'tiger160'))
        self.assertFalse(is_hash('q943', 'tiger160'))
        self.assertFalse(is_hash('q94375dj93458w34', 'tiger160'))
        self.assertFalse(is_hash('%&FHKJFvk', 'tiger160'))
        print('OK - test_invalid_hash_tiger160')

    def test_valid_hash_sha256(self):
        for hash in self.len_64:
            self.assertTrue(is_hash(hash, 'sha256'))
        print('OK - test_valid_hash_sha256')

    def test_invalid_hash_sha256(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'sha256'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'sha256'))
        self.assertFalse(is_hash('q943', 'sha256'))
        self.assertFalse(is_hash('q94375dj93458w34', 'sha256'))
        self.assertFalse(is_hash('%&FHKJFvk', 'sha256'))
        print('OK - test_invalid_hash_sha256')

    def test_valid_hash_sha384(self):
        for hash in self.len_96:
            self.assertTrue(is_hash(hash, 'sha384'))
        print('OK - test_valid_hash_sha384')

    def test_invalid_hash_sha384(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'sha384'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'sha384'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjklololo', 'sha384'))
        self.assertFalse(is_hash('q943', 'sha384'))
        self.assertFalse(is_hash('q94375dj93458w34', 'sha384'))
        self.assertFalse(is_hash('%&FHKJFvk', 'sha384'))
        print('OK - test_invalid_hash_sha384')

    def test_valid_hash_sha512(self):
        for hash in self.len_128:
            self.assertTrue(is_hash(hash, 'sha512'))
        print('OK - test_valid_hash_sha512')

    def test_invalid_hash_sha512(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'sha512'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'sha512'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjklololo', 'sha512'))
        self.assertFalse(is_hash('q943', 'sha512'))
        self.assertFalse(is_hash('q94375dj93458w34', 'sha512'))
        self.assertFalse(is_hash('%&FHKJFvk', 'sha512'))
        print('OK - test_invalid_hash_sha512')

    def test_valid_hash_tiger192(self):
        for hash in self.len_48:
            self.assertTrue(is_hash(hash, 'tiger192'))
        print('OK - test_valid_hash_tiger192')

    def test_invalid_hash_tiger192(self):
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1', 'tiger192'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjk', 'tiger192'))
        self.assertFalse(is_hash('KYT0bf1c35032a71a14c2f719e5a14c1dsjkjkjkjkkjklololo', 'tiger192'))
        self.assertFalse(is_hash('q943', 'tiger192'))
        self.assertFalse(is_hash('q94375dj93458w34', 'tiger192'))
        self.assertFalse(is_hash('%&FHKJFvk', 'tiger192'))
        print('OK - test_invalid_hash_tiger192')
