import boto3


def create_vpc(cidr_block):
    ec2 = boto3.client("ec2")
    response = ec2.create_vpc(CidrBlock=cidr_block)
    vpc_id = response["Vpc"]["VpcId"]
    print(f"VPC created with ID: {vpc_id}")
    return response


if __name__ == "__main__":
    create_vpc("10.0.0.0/16")
