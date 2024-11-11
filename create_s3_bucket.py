import boto3


def create_s3_bucket(bucket_name, region="us-east-1"):
    s3 = boto3.client("s3", region_name=region)
    response = s3.create_bucket(
        Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
    )
    print(f"Bucket '{bucket_name}' created successfully.")
    return response


if __name__ == "__main__":
    create_s3_bucket("my-automation-bucket")
