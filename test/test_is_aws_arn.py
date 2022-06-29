import unittest

from pyvalidator.is_aws_arn import is_aws_arn
from . import print_test_ok


class TestIsAWSArn(unittest.TestCase):

    def test_valid_aws_arn(self):
        for i in [
            'arn:aws:gamelift:us-west-2:123456789012:fleet/fleet-as',
			'arn:aws:iam::442149722351:user/test@mail.com',
			'arn:aws:iam::AWS-account-ID:user/**user-name-1**',
			'arn:aws:iam::AWS-account-ID:user/**user-name-2**',
			'arn:aws:ec2:us-east-1:AWS-account-ID:instance/**InstanceIdOne**',
			'arn:aws:lambda:us-west-2:123456789012:function:my-function:1',
			'arn:aws:lambda:us-west-2:123456789012:event-source-mapping:fa123456-14a1-4fd2-9fec-83de64ad683de6d47',
			'arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1'
        ]:
            self.assertTrue(is_aws_arn(i))
        print_test_ok()

    def test_invalid_aws_arn(self):
        for i in [
            '',
        ]:
            self.assertFalse(is_aws_arn(i))
        print_test_ok()
