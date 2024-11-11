import boto3


def add_ingress_rule_to_security_group(group_id, protocol, from_port, to_port, cidr_ip):
    ec2 = boto3.client("ec2")
    response = ec2.authorize_security_group_ingress(
        GroupId=group_id,
        IpPermissions=[
            {
                "IpProtocol": protocol,
                "FromPort": from_port,
                "ToPort": to_port,
                "IpRanges": [{"CidrIp": cidr_ip}],
            }
        ],
    )
    print(
        f"Ingress rule added to Security Group '{group_id}': {protocol} from {from_port} to {to_port} for {cidr_ip}"
    )
    return response


if __name__ == "__main__":
    add_ingress_rule_to_security_group(
        "sg-0123456789abcdef0", "tcp", 22, 22, "0.0.0.0/0"
    )
