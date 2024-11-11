import boto3


def scale_auto_scaling_group(asg_name, desired_capacity):
    autoscaling = boto3.client("autoscaling")
    response = autoscaling.update_auto_scaling_group(
        AutoScalingGroupName=asg_name, DesiredCapacity=desired_capacity
    )
    print(
        f"Auto Scaling Group '{asg_name}' scaled to desired capacity: {desired_capacity}."
    )
    return response


if __name__ == "__main__":
    scale_auto_scaling_group("my-auto-scaling-group", 3)
