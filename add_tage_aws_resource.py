import boto3


def add_tag(resource_id, key, value):
    ec2 = boto3.client("ec2")
    response = ec2.create_tags(
        Resources=[resource_id], Tags=[{"Key": key, "Value": value}]
    )
    print(f"Tag added to resource: {resource_id}, Key: {key}, Value: {value}")
    return response


if __name__ == "__main__":
    add_tag("i-0123456789abcdef0", "Environment", "Production")
