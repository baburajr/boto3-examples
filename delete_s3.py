import boto3


def delete_s3_bucket(bucket_name):
    s3 = boto3.client("s3")

    objects = s3.list_objects_v2(Bucket=bucket_name).get("Contents", [])
    if objects:
        for obj in objects:
            s3.delete_object(Bucket=bucket_name, Key=obj["Key"])
            print(f"Deleted object: {obj['Key']} from bucket '{bucket_name}'")

    response = s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
    return response


if __name__ == "__main__":
    delete_s3_bucket("my-automation-bucket")
