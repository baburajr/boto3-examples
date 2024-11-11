import boto3


def create_ec2_instance(image_id, instance_type, key_name, security_group):
    ec2 = boto3.resource("ec2")
    instance = ec2.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group],
        MinCount=1,
        MaxCount=1,
    )
    print(f"EC2 instance created with ID: {instance[0].id}")
    return instance[0]


if __name__ == "__main__":
    create_ec2_instance(
        "ami-0abcdef1234567890", "t2.micro", "my-key-pair", "sg-0123456789abcdef0"
    )
