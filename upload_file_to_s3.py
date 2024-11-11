import boto3


def upload_file_to_s3(bucket_name, file_name, object_name=None):
    s3 = boto3.client("s3")
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")


if __name__ == "__main__":
    upload_file_to_s3("my-automation-bucket", "my_file.txt")
