import boto3
import zipfile


def create_lambda_function(
    function_name, role_arn, handler, zip_file_path, runtime="python3.9"
):
    lambda_client = boto3.client("lambda")

    # Read the zip file content
    with open(zip_file_path, "rb") as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={"ZipFile": zipped_code},
        Timeout=300,
        MemorySize=128,
    )

    print(f"Lambda function '{function_name}' created successfully.")
    return response


if __name__ == "__main__":
    create_lambda_function(
        "my-lambda-function",
        "arn:aws:iam::123456789012:role/my-lambda-role",
        "my_module.my_handler",
        "function.zip",
    )
