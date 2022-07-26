from typing import Literal, Union

from .utils.assert_string import assert_string

AwsResource = Union[
	Literal["any"],
    Literal["connect"],
    Literal["iam"],
    Literal["iam-user"],
    Literal["iam-group"],
    Literal["iam-role"],
    Literal["iam-policy"],
    Literal["orgs"],
    Literal["orgs-account"],
    Literal["orgs-handshake"],
    Literal["orgs-org"],
    Literal["orgs-unit"],
    Literal["ecs"],
    Literal["ecs-instance"],
    Literal["ecs-service"],
    Literal["ec2"],
    Literal["lambda"],
    Literal["lambda-function"],
    Literal["lambda-event-mapping"],
    Literal["lambda-layer"],
    Literal["s3"],
    Literal["sts"],
    Literal["sqs"],
]

def is_aws_arn(input: str, resource: AwsResource = "any") -> bool:
    input = assert_string(input)

    if resource == "connect" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):connect:\w+(?:-\w+)+:\d{12}:instance\/[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+$")
        if resource != "any" or result:
            return result

    if resource == "iam-user" or resource == "iam" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:user((\/[^\s\/]+)+)?(?:\/\*)?$")
        if not (resource == "iam" or resource == "any") or result:
            return result

    if resource == "iam-group" or resource == "iam" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:group((\/[^\s\/]+)+)?(?:\/\*)?$")
        if not (resource == "iam" or resource == "any") or result:
            return result

    if resource == "iam-role" or resource == "iam" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role(((\/[^\s\/\*]+))|(?:\/\*)$)+")
        if not (resource == "iam" or resource == "any") or result:
            return result

    if resource == "iam-policy" or resource == "iam" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:policy((\/[^\s\/\*]+)+)$")
        if not (resource == "iam" or resource == "any") or result:
            return result

    if resource == "orgs-account" or resource == "orgs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}$")
        if not (resource == "orgs" or resource == "any") or result:
            return result

    if resource == "orgs-handshake" or resource == "orgs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:handshake\/o-[a-z0-9]{10,32}\/(invite|INVITE|enable_all_features|ENABLE_ALL_FEATURES|approve_all_features|APPROVE_ALL_FEATURES|add_organizations_service_linked_role|ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE)\/h-[a-zA-Z0-9]+$")
        if not (resource == "orgs" or resource == "any") or result:
           return result

    if resource == "orgs-org" or resource == "orgs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:organization\/o-[a-z0-9]{10,32}$")
        if not (resource == "orgs" or resource == "any") or result:
           return result

    if resource == "orgs-unit" or resource == "orgs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[a-z0-9]{10,32}$")
        if not (resource == "orgs" or resource == "any") or result:
           return result

    if resource == "orgs-policy" or resource == "orgs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:policy\/o-[a-z0-9]{10,32}\/(AISERVICES_OPT_OUT_POLICY|aiservices_opt_out_policy|BACKUP_POLICY|backup_policy|SERVICE_CONTROL_POLICY|service_control_policy|TAG_POLICY|tag_policy)\/p-[a-z0-9]{10,32}$")
        if not (resource == "orgs" or resource == "any") or result:
           return result

    if resource == "ecs-instance" or resource == "ecs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):ecs:\S+:\d+:container-instance(\/cluster-name)?\/[a-zA-Z0-9\-]{10,}$")
        if not (resource == "ecs" or resource == "any") or result:
           return result

    if resource == "ecs-service" or resource == "ecs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):ecs:\S+:\d+:service(\/cluster-name)?\/[a-zA-Z0-9\-]{10,}$")
        if not (resource == "ecs" or resource == "any") or result:
           return result

    if resource == "ecs-task" or resource == "ecs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):ecs:\S+:\d+:task(\/cluster-name)?\/[a-zA-Z0-9\-]{10,}$")
        if not (resource == "ecs" or resource == "any") or result:
           return result

    if resource == "ec2" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):ec2:\S+:\d+:instance\/i-[a-z0-9]{10,32}$")
        if resource != "any" or result:
           return result

    if resource == "lambda-function" or resource == "lambda" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\S+:\d{12}:function:[A-Za-z0-9\-\_\.]+(:?[A-Za-z0-9\-\_\.]+)$")
        if not (resource == "lambda" or resource == "any") or result:
            return result

    if resource == "lambda-event-mapping" or resource == "lambda" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\S+:\d{12}:event-source-mapping\/[A-Za-z0-9]+$")
        if not (resource == "lambda" or resource == "any") or result:
            return result

    if resource == "lambda-layer" or resource == "lambda" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\S+:\d{12}:layer:([A-Za-z0-9\-\_\.]+(:\d+)?)$")
        if not (resource == "lambda" or resource == "any") or result:
            return result

    if resource == "sts" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):sts::\d{12}:[A-Za-z0-9\-\_\.]+\/([A-Za-z0-9\-\_\.]+(\/[A-Za-z0-9\-\_\.]+)?)$")
        if resource != "any" or result:
            return result

    if resource == "s3" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):s3:::[a-zA-Z0-9_\-]+((\/.[^\/]+){1})?(?:\/\*)?$")
        if resource != "any" or result:
            return result

    if resource == "sqs" or resource == "any":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):sqs:\S+:\d{12}:[a-zA-Z0-9\-\_\.]+$")
        if resource != "any" or result:
            return result

    return False
	


