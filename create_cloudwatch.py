import boto3


def create_cloudwatch_alarm(alarm_name, instance_id, threshold):
    cloudwatch = boto3.client("cloudwatch")
    response = cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        MetricName="CPUUtilization",
        Namespace="AWS/EC2",
        Statistic="Average",
        Period=300,
        EvaluationPeriods=1,
        Threshold=threshold,
        ComparisonOperator="GreaterThanThreshold",
        AlarmActions=["arn:aws:sns:us-east-1:123456789012:my-topic"],
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
    )
    print(f"CloudWatch alarm '{alarm_name}' created successfully.")
    return response


if __name__ == "__main__":
    create_cloudwatch_alarm("HighCPUAlarm", "i-0123456789abcdef0", 80)
