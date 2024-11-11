import boto3


def list_rds_instances():
    rds = boto3.client("rds")
    response = rds.describe_db_instances()
    for db_instance in response["DBInstances"]:
        print(
            f"DBInstanceIdentifier: {db_instance['DBInstanceIdentifier']}, Status: {db_instance['DBInstanceStatus']}"
        )

    return response


if __name__ == "__main__":
    list_rds_instances()
