import boto3

# Create a connection to the EC2 service
ec2_client = boto3.client('ec2', region_name='eu-west-2')

# Define parameters for the EC2 instance
instance_params = {
    'ImageId': 'ami-09744628bed84e434',
    'InstanceType': 't2.micro',
    'MinCount': 1,
    'MaxCount': 1
}

# Create the EC2 instance
response = ec2_client.run_instances(**instance_params)

# Get the Instance ID of the created EC2 instance
instance_id = response['Instances'][0]['InstanceId']

print("EC2 instance created with Instance ID:", instance_id)
