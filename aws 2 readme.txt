AWS Task 2: Launch and Terminate EC2 Instance using Boto3

Title: Automating EC2 Instance Management with Boto3

Objective:
Use the Boto3 library in Python to launch and terminate an EC2 instance.

Prerequisites:
- AWS account with programmatic access (Access Key & Secret Key)
- IAM role with EC2 permissions (ec2:RunInstances, ec2:TerminateInstances)
- Install boto3:
    pip install boto3
- Configure AWS credentials:
    aws configure

Step 1: Launch an EC2 Instance

Python Code:
import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-keypair-name'       # Replace with your key pair name
)

print("Launched Instance ID:", instance[0].id)

Step 2: Terminate an EC2 Instance

Python Code:
import boto3

ec2 = boto3.resource('ec2')

instance_id = 'i-0abc1234567890def'  # Replace with your actual instance ID

instance = ec2.Instance(instance_id)
response = instance.terminate()

print("Termination response:", response)

Notes:
- Use ec2.describe_instances() to list current EC2 instances.
- Always terminate unused instances to avoid charges.
- AMI IDs are region-specific.

Summary:

| Action     | Function                    | Key Parameters                         |
|------------|-----------------------------|----------------------------------------|
| Launch     | ec2.create_instances()      | AMI ID, Instance Type, Key Pair, Count |
| Terminate  | ec2.Instance(id).terminate()| Instance ID                            |

Conclusion:
Using Boto3, you can automate the lifecycle of EC2 instances—launching and terminating them programmatically, saving time and reducing manual effort.
