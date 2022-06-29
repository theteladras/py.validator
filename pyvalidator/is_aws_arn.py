from typing import Literal, Union

from .utils.assert_string import assert_string

AwsService = Union[
    Literal["connect"],
    Literal["iam"],
    Literal["iam-user"],
    Literal["iam-pollicy"],
    Literal["organizations"],
    Literal["ec2"],
    Literal["lambda"],
    Literal["lambda-function"],
    Literal["lambda-event-mapping"],
    Literal["lambda-layer"],
]

def is_aws_arn(input: str, service: AwsService) -> bool:
    input = assert_string(input)

    if service == "connect":
        return input.match(r"^arn:(aws|aws-cn|aws-us-gov):connect:\w+(?:-\w+)+:\d{12}:instance\/[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+$")

    if service == "iam-user" or service == "iam":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::user\/[a-zA-Z0-9]+$")
        if service != "iam":
            return result

    if service == "iam-pollicy" or service == "iam":
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:policy/.+$")
        if service != "iam":
            return result

    if service == "organizations":
        return input.match(r"^arn:(aws|aws-cn|aws-us-gov):organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}$")

    if service == "ec2":
        return input.match(r"^arn:(aws|aws-cn|aws-us-gov):ecs:\S+:\d+:\w+\/\S+$")

    if service == "lambda-function" or service == 'lambda':
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\w+(?:-\w+)+:\d{12}:function\/[A-Za-z0-9]+(:?\/[A-Za-z0-9]+)")
        if service != "lambda":
            return result

    if service == "lambda-event-mapping" or service == 'lambda':
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\w+(?:-\w+)+:\d{12}:event-source-mapping\/[A-Za-z0-9]+")
        if service != "lambda":
            return result

    if service == "lambda-layer" or service == 'lambda':
        result = input.match(r"^arn:(aws|aws-cn|aws-us-gov):lambda:\w+(?:-\w+)+:\d{12}:layer\/[A-Za-z0-9]+(:?\/\d+)")
        if service != "lambda":
            return result

    return False
	


