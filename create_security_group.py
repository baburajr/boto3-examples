import boto3


def create_security_group(vpc_id, group_name, description):
    ec2 = boto3.client("ec2")
    response = ec2.create_security_group(
        GroupName=group_name, Description=description, VpcId=vpc_id
    )
    group_id = response["GroupId"]
    print(f"Security Group '{group_name}' created with ID: {group_id}")
    return response


if __name__ == "__main__":
    create_security_group(
        "vpc-0123456789abcdef0", "my-security-group", "Allow SSH and HTTP"
    )
