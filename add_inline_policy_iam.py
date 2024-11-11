import boto3


def add_inline_policy_to_user(user_name, policy_name, policy_document):
    iam = boto3.client("iam")
    response = iam.put_user_policy(
        UserName=user_name, PolicyName=policy_name, PolicyDocument=policy_document
    )
    print(f"Policy '{policy_name}' added to user '{user_name}'.")
    return response


if __name__ == "__main__":
    policy_document = """
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": "*"
        }
    ]
    }
    """
    add_inline_policy_to_user("new_user", "S3FullAccess", policy_document)
