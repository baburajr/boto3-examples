import boto3


def create_load_balancer(lb_name, subnet_ids, security_group_ids):
    elb = boto3.client("elb")
    response = elb.create_load_balancer(
        LoadBalancerName=lb_name,
        Listeners=[
            {
                "Protocol": "HTTP",
                "LoadBalancerPort": 80,
                "InstanceProtocol": "HTTP",
                "InstancePort": 80,
            }
        ],
        Subnets=subnet_ids,
        SecurityGroups=security_group_ids,
        Scheme="internet-facing",
    )
    print(f"Load Balancer '{lb_name}' created successfully.")
    return response


if __name__ == "__main__":
    create_load_balancer(
        "my-load-balancer", ["subnet-0123456789abcdef0"], ["sg-0123456789abcdef0"]
    )
