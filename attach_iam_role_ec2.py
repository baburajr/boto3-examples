import boto3


def attach_iam_role_to_ec2(instance_id, role_name):
    ec2 = boto3.client("ec2")
    response = ec2.associate_iam_instance_profile(
        IamInstanceProfile={"Name": role_name}, InstanceId=instance_id
    )
    print(f"Attached IAM role '{role_name}' to EC2 instance: {instance_id}")
    return response


if __name__ == "__main__":
    attach_iam_role_to_ec2("i-0123456789abcdef0", "my-ec2-role")
