import unittest
from validator import *

class TestIsJwt(unittest.TestCase):

    def test_valid_jwt(self):
        self.assertTrue(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI'))
        self.assertTrue(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb3JlbSI6Imlwc3VtIn0.ymiJSsMJXR6tMSr8G9usjQ15_8hKPDv_CArLhxw28MI'))
        self.assertTrue(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2xvciI6InNpdCIsImFtZXQiOlsibG9yZW0iLCJpcHN1bSJdfQ.rRpe04zbWbbJjwM43VnHzAboDzszJtGrNsUxaqQ-GQ8'))
        self.assertTrue(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqb2huIjp7ImFnZSI6MjUsImhlaWdodCI6MTg1fSwiamFrZSI6eyJhZ2UiOjMwLCJoZWlnaHQiOjI3MH19.YRLPARDmhGMC3BBk_OhtwwK21PIkVCqQe8ncIRPKo-E'))
        self.assertTrue(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'))
        print('OK - test_valid_jwt')

    def test_invalid_jwt(self):
        self.assertFalse(is_jwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'))
        self.assertFalse(is_jwt('$Zs.ewu.su84'))
        self.assertFalse(is_jwt('ks64$S/9.dy$§kz.3sd73b'))
        print('OK - test_invalid_jwt')

    def test_fail_jwt(self):
        self.assertRaises(Exception, is_jwt, None)
        self.assertRaises(Exception, is_jwt, {})
