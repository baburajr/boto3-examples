import boto3


def create_iam_user(user_name):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=user_name)
    print(f"IAM User '{user_name}' created successfully.")
    return response


if __name__ == "__main__":
    create_iam_user("new_user")
