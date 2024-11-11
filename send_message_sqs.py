import boto3


def send_message_to_sqs(queue_url, message_body):
    sqs = boto3.client("sqs")
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
    print(f"Message sent to SQS queue: {queue_url}")
    return response


if __name__ == "__main__":
    send_message_to_sqs(
        "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue",
        "Hello, this is a test message!",
    )
