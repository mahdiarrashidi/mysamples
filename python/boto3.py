#boto3 Script To Retrieve EMR Master IP


import boto3
import json

boto_client_emr = boto3.client("emr")
cluster_id = "j-DFGDSFGREWG"

def get_emr_master_pvt_ip(boto_client_emr, cluster_id):
    emr_list_instance_rep = boto_client_emr.list_instances(
        ClusterId=cluster_id,
        InstanceGroupTypes=[
            'MASTER',
        ],
        InstanceStates=[
            'RUNNING',
        ]
    )
  
    return emr_list_instance_rep["Instances"][0]["PrivateIpAddress"]

emr_master_ip = get_emr_master_pvt_ip(boto_client_emr, cluster_id)

print("EMR master IP is" + " " + emr_master_ip)
