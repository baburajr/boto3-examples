import boto3


def create_rds_instance(
    db_instance_identifier,
    db_instance_class,
    db_engine,
    master_username,
    master_password,
):
    rds = boto3.client("rds")
    response = rds.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        AllocatedStorage=20,
        DBInstanceClass=db_instance_class,
        Engine=db_engine,
        MasterUsername=master_username,
        MasterUserPassword=master_password,
        BackupRetentionPeriod=7,
        MultiAZ=False,
    )
    print(f"RDS instance '{db_instance_identifier}' is being created.")
    return response


if __name__ == "__main__":
    create_rds_instance("mydb", "db.t2.micro", "mysql", "admin", "password123")
