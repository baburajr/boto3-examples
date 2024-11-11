import boto3


def publish_sns_message(topic_arn, message, subject):
    sns = boto3.client("sns")
    response = sns.publish(TopicArn=topic_arn, Message=message, Subject=subject)
    print(f"Message published to SNS topic: {topic_arn}")
    return response


if __name__ == "__main__":
    publish_sns_message(
        "arn:aws:sns:us-east-1:123456789012:my-topic",
        "This is a test notification",
        "Test Subject",
    )
