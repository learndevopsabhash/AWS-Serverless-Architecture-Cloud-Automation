# AWS-Serverless-Architecture-Cloud-Automation

Assignment On AWS Serverless Architecture

## Assignments Completed

### Assignment 1

   Automated EC2 start/stop based on tags.

### Assignment 2

   Automated S3 Bucket Cleanup.

### Assignment 5

   Automated Tagging EC2 Instances on Launch.

### Assignment 13

   Automated Audit S3 Bucket Permissions & Notify for Public Buckets

## Technologies Used

* AWS Lambda
* EC2
* IAM Policy
* Python 3.x
* Boto3
* EventBridge
* SNS
<br><br>
---

<br><br>

## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

### Objective

Automate EC2 instance start and stop operations based on tags.

### Steps Performed

1. Created two EC2 instances.
2. Added tags:

   * Action=Auto-Stop
   * Action=Auto-Start
3. Created IAM Role for Lambda.
4. Attached AmazonEC2FullAccess and AWSLambdaBasicExecutionRole.
5. Created Lambda function.
6. Implemented Boto3 automation.
7. Invoked Lambda manually.
8. Verified EC2 state changes.
9. Verified CloudWatch logs.

### Result

Lambda successfully stopped instances tagged Auto-Stop and started instances tagged Auto-Start.

---

## Assignment 2: Automated S3 Bucket Cleanup Using Lambda and Boto3.

### Objective

Detect S3 buckets objects via Lambda function.

### Steps Performed

1. Created test S3 buckets.
2. Created IAM Role for Lambda.
3. Attached AmazonS3FullAccess.
4. Developed Lambda function using Boto3.
5. Invoked Lambda manually.
6. Verified CloudWatch logs.

### Observation

AWS currently enables SSE-S3 encryption by default on newly created buckets. All test buckets were detected as encrypted.

### Result

Lambda successfully Delete objects into the bucket.

---

## Assignment 5: Auto Tagging EC2 Instances

### Objective

Automatically tag newly launched EC2 instances.

### Steps Performed

1. Create IAM Role for Lambda
3. Developed Lambda function.
4. Write the Lambda Code.
5. Create EventBridge rule.
6. Add Lambda as Target
7. Check Launched a new EC2 instance.
8. Verified automatic tagging.
9. Verify CloudWatch Logs

### Tags Added

* LaunchDate = 2026-06-28 (or current date)
* Environment = Development

### Result

New EC2 instances were automatically tagged upon launch.

---

## Assignment 13: Audit S3 Bucket Permissions and Notify for Public Buckets

### Objective

Automatically audit S3 bucket permissions and send notifications if any buckets have public read or write permissions.

### Steps Performed

1. Create two bucket public and Private.
   1. In First buckert - Disable - Block Public Access
   2. In second buckert - Enable - Block Public Access
2. Create an SNS Topic Under this Create Email Subscription.
3. Create/Update IAM Role for Lambda
4. Created Lambda function with code.
5. Configured SNS notifications.
6. Created EventBridge daily schedule.
7. Tested alert functionality.

### Result

It list all s3 bucket, mail send for public bucket via SNS 

---

## Region
ap-south-1

## AWS Services used
This repository contains solutions for AWS Serverless Architecture assignments using:

* AWS Lambda
* Amazon EC2
* Amazon S3
* Amazon SNS
* Amazon EventBridge
* IAM
* Python (Boto3)

## Conclusion

Successfully implemented serverless automation solutions using AWS Lambda, Boto3, EventBridge, SNS, S3, IAM and EC2 services.
