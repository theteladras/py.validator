import unittest

from pyvalidator.is_jwt import is_jwt
from . import print_test_ok


class TestIsJwt(unittest.TestCase):

    def test_valid_jwt(self):
        for i in [
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb3JlbSI6Imlwc3VtIn0.ymiJSsMJXR6tMSr8G9usjQ15_8hKPDv_CArLhxw28MI',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2xvciI6InNpdCIsImFtZXQiOlsibG9yZW0iLCJpcHN1bSJdfQ.rRpe04zbWbbJjwM43VnHzAboDzszJtGrNsUxaqQ-GQ8',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqb2huIjp7ImFnZSI6MjUsImhlaWdodCI6MTg1fSwiamFrZSI6eyJhZ2UiOjMwLCJoZWlnaHQiOjI3MH19.YRLPARDmhGMC3BBk_OhtwwK21PIkVCqQe8ncIRPKo-E',
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ',
        ]:
            self.assertTrue(is_jwt(i))
        print_test_ok()

    def test_invalid_jwt(self):
        for i in [
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',
            '$Zs.ewu.su84',
            'ks64$S/9.dy$§kz.3sd73b',
        ]:
            self.assertFalse(is_jwt(i))
        print_test_ok()

    def test_fail_jwt(self):
        self.assertRaises(Exception, is_jwt, None)
        self.assertRaises(Exception, is_jwt, {})
        print_test_ok()
