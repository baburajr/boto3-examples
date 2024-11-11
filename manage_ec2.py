import boto3


def manage_ec2_instance(instance_id, action="start"):
    ec2 = boto3.client("ec2")
    if action == "start":
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting EC2 instance: {instance_id}")
    elif action == "stop":
        response = ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping EC2 instance: {instance_id}")
    else:
        print("Invalid action. Use 'start' or 'stop'.")

    return response


if __name__ == "__main__":
    manage_ec2_instance("i-0123456789abcdef0", action="start")
    # manage_ec2_instance('i-0123456789abcdef0', action='stop')
