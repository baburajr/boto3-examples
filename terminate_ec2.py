import boto3


def terminate_ec2_instance(instance_id):
    ec2 = boto3.client("ec2")
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminating EC2 instance: {instance_id}")
    return response


if __name__ == "__main__":
    terminate_ec2_instance("i-0123456789abcdef0")
