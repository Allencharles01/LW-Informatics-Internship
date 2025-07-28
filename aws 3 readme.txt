AWS Task 3: Access CloudWatch Logs using Boto3

Title: Fetching CloudWatch Logs with Boto3

Objective:
Use Python and Boto3 to access logs stored in AWS CloudWatch Logs.

Prerequisites:
- Install boto3:
    pip install boto3
- Configure AWS CLI:
    aws configure
- IAM user must have the following permissions:
    - logs:DescribeLogGroups
    - logs:DescribeLogStreams
    - logs:GetLogEvents

Sample Python Script:

import boto3

# Initialize the CloudWatch Logs client
client = boto3.client('logs')

# Replace with your actual log group and log stream
log_group_name = '/aws/lambda/your-log-group'
log_stream_name = '2025/07/27/[$LATEST]abcd1234example'

# Fetch log events
response = client.get_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name,
    startFromHead=True
)

# Print logs
for event in response['events']:
    print(f"{event['timestamp']} - {event['message']}")

Additional Commands:

1. List Log Groups:
log_groups = client.describe_log_groups()
for group in log_groups['logGroups']:
    print(group['logGroupName'])

2. List Log Streams:
streams = client.describe_log_streams(logGroupName=log_group_name)
for stream in streams['logStreams']:
    print(stream['logStreamName'])

Notes:
- Timestamps are in Unix epoch format.
- Use nextToken for pagination if the response is large.
- CloudWatch Logs are commonly used with AWS Lambda, ECS, EC2, and custom applications.

Conclusion:
With Boto3, you can automate the retrieval and processing of AWS CloudWatch Logs, enabling easier monitoring, alerting, and debugging of your cloud-based applications.
