import unittest

from pyvalidator.is_aws_arn import is_aws_arn
from . import print_test_ok


class TestIsAWSArn(unittest.TestCase):

    def test_valid_aws_arn(self):
        for i in [
			'arn:aws:iam::123456789012:user/someName1',
			'arn:aws:iam::123456789012:user/someName2',
			'arn:aws:iam::123456789012:user/user@mail.com',
			'arn:aws:iam::123456789012:user/*',
			'arn:aws:iam::123456789012:user/Development/product_1234/*',
			'arn:aws:iam::123456789012:group/groupName1',
			'arn:aws:iam::123456789012:group/groupName2',
			'arn:aws:iam::123456789012:group/*',
			'arn:aws:iam::123456789012:group/Development/product_1234/*',
			'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_A/Developers',
			'arn:aws:iam::123456789012:group/Developers',
			'arn:aws:iam::123456789012:role/TestRole',
			'arn:aws:iam::123456789012:role/*',
			'arn:aws:iam::123456789012:role/app/*',
			'arn:aws:iam::123456789012:role/application_abc/component_xyz/RDSAccess',
			'arn:aws:iam::123456789012:role/aws-service-role/access-analyzer.amazonaws.com/AWSServiceRoleForAccessAnalyzer',
			'arn:aws:iam::123456789012:role/service-role/QuickSightAction',
			'arn:aws:iam::123456789012:policy/division_abc/subdivision_xyz/UsersManageOwnCredentials',
			'arn:aws:iam::123456789012:policy/UsersManageOwnCredentials',
			'arn:aws-cn:organizations::123456789012:organization/o-123123123123',
			'arn:aws-cn:organizations::123456789012:ou/o-123123123123/ou-1234567890123',
			'arn:aws:sts::123456789012:assumed-role/demo/TestAR',
			'arn:aws:sqs:us-west-2:123456789012:mySQSqueue',
			'arn:aws:sqs:us-east-2:123456789012:mystack-myqueue-15PG5C2FC1CW8'
        ]:
            self.assertTrue(is_aws_arn(i))
        print_test_ok()

    def test_invalid_aws_arn(self):
        for i in [
            'arn:aws:iam::1234567890123:user/someName2',
			'arn:aws:iam::123456789012:user/Development//product_1234/*',
			'arn:aws:iam::123456789012:group//Development/product_1234/*',
			'arn:aws:iam::123456789012:group//Development/*/product_1234/*',
			'arn:aws:iam::1234567890123:role/role',
        ]:
            self.assertFalse(is_aws_arn(i))
        print_test_ok()

    def test_valid_aws_arn_iam_user(self):
        for i in [
			'arn:aws:iam::123456789012:user/someName1',
			'arn:aws:iam::123456789012:user/someName2',
			'arn:aws:iam::123456789012:user/user@mail.com',
			'arn:aws:iam::123456789012:user/*',
			'arn:aws:iam::123456789012:user/Development/product_1234/*'
        ]:
            self.assertTrue(is_aws_arn(i, "iam-user"))
        print_test_ok()

    def test_invalid_aws_arn_iam_user(self):
        for i in [
            'arn:aws:iam::1234567890123:user/someName2',
            'arn:aws:iam::123456789012:group/someName2',
			'arn:aws:iam::123456789012:user/Development//product_1234/*',
        ]:
            self.assertFalse(is_aws_arn(i, "iam-user"))
        print_test_ok()

    def test_valid_aws_arn_iam_group(self):
        for i in [
			'arn:aws:iam::123456789012:group/groupName1',
			'arn:aws:iam::123456789012:group/groupName2',
			'arn:aws:iam::123456789012:group/*',
			'arn:aws:iam::123456789012:group/Development/product_1234/*',
			'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_A/Developers',
			'arn:aws:iam::123456789012:group/Developers'
        ]:
            self.assertTrue(is_aws_arn(i, "iam-group"))
        print_test_ok()

    def test_invalid_aws_arn_iam_group(self):
        for i in [
            'arn:aws:iam::1234567890123:group/groupName1',
            'arn:aws:iam::123456789012:user/groupName1',
			'arn:aws:iam::123456789012:group//Development/product_1234/*',
			'arn:aws:iam::123456789012:group//Development/*/product_1234/*'
        ]:
            self.assertFalse(is_aws_arn(i, "iam-group"))
        print_test_ok()

    def test_valid_aws_arn_iam_role(self):
        for i in [
			'arn:aws:iam::123456789012:role/TestRole',
			'arn:aws:iam::123456789012:role/*',
			'arn:aws:iam::123456789012:role/app/*',
			'arn:aws:iam::123456789012:role/application_abc/component_xyz/RDSAccess',
			'arn:aws:iam::123456789012:role/aws-service-role/access-analyzer.amazonaws.com/AWSServiceRoleForAccessAnalyzer',
			'arn:aws:iam::123456789012:role/service-role/QuickSightAction'
        ]:
            self.assertTrue(is_aws_arn(i, "iam-role"))
        print_test_ok()

    def test_invalid_aws_arn_iam_role(self):
        for i in [
            'arn:aws:iam::1234567890123:role/role',
            'arn:aws:iam::123456789012:role',
			'arn:aws:iam::123456789012:group',
			'arn:aws:iam::123456789012:role//',
			'arn:aws:iam::123456789012:role/*/*',
			'arn:aws:iam::123456789012:role/*/application',
			'arn:aws:iam::123456789012:role/*/application/*',
        ]:
            self.assertFalse(is_aws_arn(i, "iam-role"))
        print_test_ok()

    def test_valid_aws_arn_iam_policy(self):
        for i in [
			'arn:aws:iam::123456789012:policy/UsersManageOwnCredentials',
			'arn:aws-cn:iam::123456789012:policy/UsersManageOwnCredentials',
			'arn:aws:iam::123456789012:policy/division_abc/subdivision_xyz/UsersManageOwnCredentials',
        ]:
            self.assertTrue(is_aws_arn(i, "iam-policy"))
        print_test_ok()

    def test_invalid_aws_arn_iam_policy(self):
        for i in [
            'arn:aws:iam::123456789012:role/TestRole',
			'arn:aws:iam::123456789012:policy'
			'arn:aws:iam::123456789012:policy/'
			'arn:aws:iam::123456789012:policy/*'
        ]:
            self.assertFalse(is_aws_arn(i, "iam-policy"))
        print_test_ok()

    def test_valid_aws_arn_organizations(self):
        for i in [
			'arn:aws:organizations::123456789012:account/o-123123123asd/123456789012',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/invite/h-123456789012',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/enable_all_features/h-123456789012',
			'arn:aws-cn:organizations::123456789012:organization/o-123123123123',
			'arn:aws:organizations::123456789012:ou/o-123123123asd/ou-123456789asd',
			'arn:aws-cn:organizations::123456789012:ou/o-123123123123/ou-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/aiservices_opt_out_policy/p-1234567890123',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs"))
        print_test_ok()

    def test_invalid_aws_arn_organizations(self):
        for i in [
			'',
			'123',
			'asd',
			'arn:aws:iam::123456789012:policy',
			'not:an:arn::123456789012:ou/o-123457890asd/ou-123456789asd'
			'arn:aws:organizations',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/inviteee/h-123456789012',
			'arn:aws:iam::123456789012:role/*',
			'arn:aws:organizations::123456789012:organization/123123123asd',
			'arn::organizations::123456789012:account/o-123123123asd/123456789012',
			'arn:aws:organizations::123456789012:policy/o-123123123asd/asd/p-1234567890123',
        ]:
            self.assertFalse(is_aws_arn(i, "orgs"))
        print_test_ok()

    def test_valid_aws_arn_organizations_account(self):
        for i in [
			'arn:aws:organizations::123456789012:account/o-123123123asd/123456789012',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs-account"))
        print_test_ok()

    def test_invalid_aws_arn_organizations_account(self):
        for i in [
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/invite/h-123456789012',
			'arn:aws:iam::123456789012:role/*',
			'arn:aws:organizations::123456789012:account/o-123123123asd/12345678901',
			'arn:aws:organizations::123456789012:account/o-123123123asd/1234567890123',
			'arn:aws-cn:organizations::123456789012:account/o-123456789/123456789012',
        ]:
            self.assertFalse(is_aws_arn(i, "orgs-account"))
        print_test_ok()

    def test_valid_aws_arn_organizations_handshake(self):
        for i in [
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/invite/h-123456789012',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/enable_all_features/h-123456789012',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/enable_all_features/h-123456789012ASD',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/approve_all_features/h-123456789012',
			'arn:aws:organizations::123456789012:handshake/o-123123123asd/add_organizations_service_linked_role/h-123456789012',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs-handshake"))
        print_test_ok()

    def test_invalid_aws_arn_organizations_handshake(self):
        for i in [
            'arn:aws:organizations::123456789012:organization/o-123/invite/h-123456789012',
            'arn:aws:organizations::123456789012:organization/o-123123123asd/asd/h-123456789012'
            'arn:aws:organizations::1234567890:organization/o-123123123asd/invite/h-123456789012'
        ]:
            self.assertFalse(is_aws_arn(i, "orgs-handshake"))
        print_test_ok()

    def test_valid_aws_arn_organizations_organization(self):
        for i in [
			'arn:aws:organizations::123456789012:organization/o-123123123asd',
			'arn:aws-cn:organizations::123456789012:organization/o-123123123123',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs-org"))
        print_test_ok()

    def test_invalid_aws_arn_organizations_organization(self):
        for i in [
            'arn:aws:organizations::123456789012:organization/o-123456789',
            'arn:aws:organizations::12345678901:organization/o-123456789012',
            'arn:aws:organizations::123456789012:organization/o-123456789asd/',
            'arn:aws:organizations::123456789012:organization/o-123123123asd/asd',
            'arn:aws:organizations::123456789012:organization/123123123asd'
        ]:
            self.assertFalse(is_aws_arn(i, "orgs-org"))
        print_test_ok()

    def test_valid_aws_arn_organizations_organization_units(self):
        for i in [
			'arn:aws:organizations::123456789012:ou/o-123123123asd/ou-123456789asd',
			'arn:aws-cn:organizations::123456789012:ou/o-123123123123/ou-1234567890123',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs-unit"))
        print_test_ok()

    def test_invalid_aws_arn_organizations_organization_units(self):
        for i in [
            'arn:aws:organizations::123456789012:ou/o-123123123asd',
			'arn:aws-cn:organizations::123456789012:ou/o-123123123123/o-1234567890123',
			'arn:aws:organizations::123456789012:organization/o-123123123asd/ou-123456789asd'
        ]:
            self.assertFalse(is_aws_arn(i, "orgs-unit"))
        print_test_ok()

    def test_valid_aws_arn_organizations_policy(self):
        for i in [
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/aiservices_opt_out_policy/p-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/tag_policy/p-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/SERVICE_CONTROL_POLICY/p-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/backup_policy/p-1234567890123',
        ]:
            self.assertTrue(is_aws_arn(i, "orgs-policy"))
        print_test_ok()

    def test_invalid_aws_arn_organizations_policy(self):
        for i in [
			'arn:aws:organizations::123456789012:policy/o-123123123asd/asd/p-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123/aiservices_opt_out_policy/p-1234567890123',
			'arn:aws-cn:organizations::123456789012:policy/o-123123123asd/aiservices_opt_out_policy/1234567890123',
			'arn:aws-cn:organizations::123456789012:ou/o-123123123asd/aiservices_opt_out_policy/p-1234567890123',
        ]:
            self.assertFalse(is_aws_arn(i, "orgs-policy"))
        print_test_ok()

    def test_valid_aws_arn_s3(self):
        for i in [
			'arn:aws:s3:::my_corporate_bucket/*',
			'arn:aws:s3:::my_corporate_bucket/Development/*',
			'arn:aws:s3:::john/User image.png',
			'arn:aws:s3:::john',
			'arn:aws:s3:::test-bucket',
        ]:
            self.assertTrue(is_aws_arn(i, "s3"))
        print_test_ok()

    def test_invalid_aws_arn_s3(self):
        for i in [
			'arn:aws:s2:::john',
			'arn:aw:s3:::john',
			'arn:aws:s3::123456789012:john',
			'arn:aws:s3:::john/dir/img.jpg',
        ]:
            self.assertFalse(is_aws_arn(i, "s3"))
        print_test_ok()

    def test_valid_aws_arn_ecs(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:container-instance/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance/cluster-name/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service/cluster-name/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:task/f9cc75bb-0c94-46b9-bf6d-49d320bc1551'
        ]:
            self.assertTrue(is_aws_arn(i, "ecs"))
        print_test_ok()

    def test_invalid_aws_arn_ecs(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:container-instance/asd/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance',
			'arn:aws:ecs:us-west-2:012345678910:service/asd/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service',
        ]:
            self.assertFalse(is_aws_arn(i, "ecs"))
        print_test_ok()

    def test_valid_aws_arn_ecs_instance(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:container-instance/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance/cluster-name/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
        ]:
            self.assertTrue(is_aws_arn(i, "ecs-instance"))
        print_test_ok()

    def test_invalid_aws_arn_ecs_instance(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:container-instance/asd/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance'
        ]:
            self.assertFalse(is_aws_arn(i, "ecs-instance"))
        print_test_ok()

    def test_valid_aws_arn_ecs_service(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:service/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service/cluster-name/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
        ]:
            self.assertTrue(is_aws_arn(i, "ecs-service"))
        print_test_ok()

    def test_invalid_aws_arn_ecs_service(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:service/asd/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service'
        ]:
            self.assertFalse(is_aws_arn(i, "ecs-service"))
        print_test_ok()

    def test_valid_aws_arn_ecs_task(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:task/f9cc75bb-0c94-46b9-bf6d-49d320bc1551'
        ]:
            self.assertTrue(is_aws_arn(i, "ecs-task"))
        print_test_ok()

    def test_invalid_aws_arn_ecs_task(self):
        for i in [
			'arn:aws:ecs:us-west-2:012345678910:service/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:task/asd/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:container-instance/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service'
        ]:
            self.assertFalse(is_aws_arn(i, "ecs-task"))
        print_test_ok()

    def test_valid_aws_arn_ec2(self):
        for i in [
			'arn:aws:ec2:us-east-1:4575734578134:instance/i-054dsfg34gdsfg38',
			'arn:aws:ec2:us-west-2:12345:instance/i-060d319e74305c009'
        ]:
            self.assertTrue(is_aws_arn(i, "ec2"))
        print_test_ok()

    def test_invalid_aws_arn_ec2(self):
        for i in [
			'arn:aws:ec2:us-west-2:12345:instanc/i-060d319e74305c009',
			'arn:aws:ec2:us-west-2:12345:instance/n-060d319e74305c009'
        ]:
            self.assertFalse(is_aws_arn(i, "ec2"))
        print_test_ok()

    def test_valid_aws_arn_lambda(self):
        for i in [
			'arn:aws:lambda:aws-region:123456789012:function:helloworld:42',
			'arn:aws:lambda:aws-region:123456789012:function:source_lambda',
			'arn:aws:lambda:us-west-2:123456789012:event-source-mapping/f0acb93d',
			'arn:aws:lambda:us-east-2:123456789012:layer:my-layer',
			'arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1'
        ]:
            self.assertTrue(is_aws_arn(i, "lambda"))
        print_test_ok()

    def test_invalid_aws_arn_lambda(self):
        for i in [
			'arn:aws:iam:us-west-2:123456789012:function:my-function:1',
			'arn:aws:lambda:us-west-2:123456789012:function:my-function:prod:asd',
			'arn:aws:lambda:us-east-2:123456789012:laye:my-layer:1',
			'arn:aws:ec2:us-east-1:4575734578134:instance/i-054dsfg34gdsfg38',
			'arn:aws:ec2:us-west-2:12345:instance/i-060d319e74305c009',
			'arn:aws:ecs:us-west-2:012345678910:service/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:ecs:us-west-2:012345678910:service/cluster-name/f9cc75bb-0c94-46b9-bf6d-49d320bc1551',
			'arn:aws:iam::123456789012:role/aws-service-role/access-analyzer.amazonaws.com/AWSServiceRoleForAccessAnalyzer',
			'arn:aws:iam::123456789012:role/service-role/QuickSightAction',
			'arn:aws:iam::123456789012:group/division_abc/subdivision_xyz/product_A/Developers',
			'arn:aws:iam::123456789012:group/Developers'
        ]:
            self.assertFalse(is_aws_arn(i, "lambda"))
        print_test_ok()

    def test_valid_aws_arn_lambda_function(self):
        for i in [
			'arn:aws:lambda:us-west-2:123456789012:function:my-function:1',
			'arn:aws:lambda:aws-region:123456789012:function:helloworld:42',
			'arn:aws:lambda:aws-region:123456789012:function:source_lambda',
			'arn:aws:lambda:us-west-2:123456789012:function:my-function:prod'
        ]:
            self.assertTrue(is_aws_arn(i, "lambda-function"))
        print_test_ok()

    def test_invalid_aws_arn_lambda_function(self):
        for i in [
			'arn:aws:iam:us-west-2:123456789012:function:my-function:1',
			'arn:aws:lambda:us-west-2:123456789012:function:my-function:prod:asd',
			'arn:aws:lambda:us-west-2:123456789012:function:my-$function:prod',
			'arn:aws:lambda:us-west-2:1234567890123:functio/n:my-function:prod',
        ]:
            self.assertFalse(is_aws_arn(i, "lambda-function"))
        print_test_ok()

    def test_valid_aws_arn_lambda_event_mapping(self):
        for i in [
			'arn:aws:lambda:us-west-2:123456789012:event-source-mapping/f0acb93d',
        ]:
            self.assertTrue(is_aws_arn(i, "lambda-event-mapping"))
        print_test_ok()

    def test_invalid_aws_arn_lambda_event_mapping(self):
        for i in [
			'arn:aws:lambda:us-west-2:123456789012:event-mapping/f0acb93d',
			'arn:aws:lambd:us-west-2:123456789012:event-source-mapping/f0acb93d',
			'arn:aws:lambda:us-west-2:1234567890123:event-source-mapping/f0acb93d',
			'arn:aws:iam:us-west-2:123456789012:function:my-function:1',
        ]:
            self.assertFalse(is_aws_arn(i, "lambda-event-mapping"))
        print_test_ok()

    def test_valid_aws_arn_lambda_layer(self):
        for i in [
			'arn:aws:lambda:us-east-2:123456789012:layer:my-layer',
			'arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1'
        ]:
            self.assertTrue(is_aws_arn(i, "lambda-layer"))
        print_test_ok()

    def test_invalid_aws_arn_lambda_layer(self):
        for i in [
			'arn:aws:lambda:us-east-2:123456789012:layer:my-layer:asd',
			'arn:aws:lambda:us-east-2:123456789012:laye:my-layer:1',
			'arn:aws:lambda:us-west-2:123456789012:event-mapping/f0acb93d',
        ]:
            self.assertFalse(is_aws_arn(i, "lambda-layer"))
        print_test_ok()

    def test_valid_aws_arn_lambda_sts(self):
        for i in [
			'arn:aws:sts::123456789012:federated-user/Paulo',
			'arn:aws:sts::123456789012:assumed-role/Accounting-Role/Mary',
			'arn:aws:sts::123456789012:assumed-role/demo/TestAR'
        ]:
            self.assertTrue(is_aws_arn(i, "sts"))
        print_test_ok()

    def test_invalid_aws_arn_lambda_layer(self):
        for i in [
			'arn:aws:sts::123456789012:assumed-role/Accounting-Role/Mary/asd',
			'arn:aws:lambda::123456789012:assumed-role/Accounting-Role/Mary'
        ]:
            self.assertFalse(is_aws_arn(i, "sts"))
        print_test_ok()

    def test_valid_aws_arn_sqs(self):
        for i in [
			'arn:aws:sqs:us-west-2:123456789012:mySQSqueue',
			'arn:aws:sqs:us-east-2:123456789012:mystack-myqueue-15PG5C2FC1CW8',
        ]:
            self.assertTrue(is_aws_arn(i, "sqs"))
        print_test_ok()

    def test_invalid_aws_arn_sqs(self):
        for i in [
			'arn:aws:sqs:us-east-2:123456789012:mystack-myqueue-15PG5C2FC1CW8/asd',
			'arn:aws:sts:us-east-2:123456789012:mystack-myqueue-15PG5C2FC1CW8',
			'arn:aws:sts:us-east-2:123456789012:mystack-myqueue-15PG5C2FC1CW8/',
        ]:
            self.assertFalse(is_aws_arn(i, "sqs"))
        print_test_ok()
