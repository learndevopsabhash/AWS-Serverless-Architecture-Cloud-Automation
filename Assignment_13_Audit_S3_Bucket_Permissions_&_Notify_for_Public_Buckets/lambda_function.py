import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'YOUR_SNS_TOPIC_ARN'


def lambda_handler(event, context):

    buckets = s3.list_buckets()['Buckets']

    public_buckets = []

    for bucket in buckets:

        bucket_name = bucket['Name']

        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)

            for grant in acl['Grants']:

                grantee = grant.get('Grantee', {})

                if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    public_buckets.append(bucket_name)

        except Exception as e:
            print(e)

    if public_buckets:

        message = "Public Buckets Found:\n\n"

        for bucket in public_buckets:
            message += bucket + "\n"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='Public S3 Bucket Alert',
            Message=message
        )

    return {
        'statusCode':200,
        'body':'Completed'
    }