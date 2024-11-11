import boto3


def list_objects_in_s3(bucket_name):
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"Object: {obj['Key']}, Size: {obj['Size']}")
    else:
        print(f"No objects found in bucket '{bucket_name}'")

    return response


if __name__ == "__main__":
    list_objects_in_s3("my-automation-bucket")
