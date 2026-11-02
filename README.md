# Serverless Image Processing Pipeline

An event-driven serverless architecture built on AWS that automatically resizes images uploaded to an Amazon S3 bucket using AWS Lambda, orchestrated via AWS Step Functions, and exposed externally through an API Gateway endpoint.

## Architecture Diagram
[ API Gateway ] --> [ Step Functions State Machine ] --> [ Lambda Function (Pillow) ] --> [ Destination S3 Bucket ]

## Prerequisites
- An active AWS Account.
- Python 3.11+ installed locally (for code editing reference).
- Pillow library layer configured on the AWS Lambda function.

## Detailed Deployment Instructions

### 1. Amazon S3 Buckets Setup
- Create a source bucket for raw images: `serverless-pipeline-source-bucket`
- Create a destination bucket for thumbnails: `serverless-pipeline-dest-bucket`

### 2. Lambda Function Configuration
- Create a Lambda function named `ResizeImage` using Python 3.11.
- Attach a Pillow layer to support image manipulation.
- Configure an environment variable `DEST_BUCKET` pointing to your destination S3 bucket.
- Paste the source code from `lambda_function.py`.

### 3. Step Functions Workflow
- Create a Standard State Machine named `ImageProcessingWorkflow`.
- Use the provided ASL definition pointing to your `ResizeImage` Lambda function ARN.
- Ensure the automatically generated IAM execution role permits Lambda invocation.

### 4. API Gateway Integration
- Create a REST API (`ImageProcessingAPI`) with a POST method targeting the Step Functions `StartExecution` action.

## Testing
Upload a test `.jpg` or `.png` image to your source S3 bucket, trigger the execution ## Prerequisites
- An active AWS Account.
- Python 3.11+ installed locally (for code editing reference).
- Pillow library layer configured on the AWS Lambda function.

## Detailed Deployment Instructions

### 1. Amazon S3 Buckets Setup
- Create a source bucket for raw images: `serverless-pipeline-source-bucket`
- Create a destination bucket for thumbnails: `serverless-pipeline-dest-bucket`

### 2. Lambda Function Configuration
- Create a Lambda function named `ResizeImage` using Python 3.11.
- Attach a Pillow layer to support image manipulation.
- Configure an environment variable `DEST_BUCKET` pointing to your destination S3 bucket.
- Paste the source code from `lambda_function.py`.

### 3. Step Functions Workflow
- Create a Standard State Machine named `ImageProcessingWorkflow`.
- Use the provided ASL definition pointing to your `ResizeImage` Lambda function ARN.
- Ensure the automatically generated IAM execution role permits Lambda invocation.

### 4. API Gateway Integration
- Create a REST API (`ImageProcessingAPI`) with a POST method targeting the Step Functions `StartExecution` action.

## Testing
Upload a test `.jpg` or `.png` image to your source S3 bucket, trigger the execution ## Prerequisites
- An active AWS Account.
- Python 3.11+ installed locally (for code editing reference).
- Pillow library layer configured on the AWS Lambda function.

## Detailed Deployment Instructions

### 1. Amazon S3 Buckets Setup
- Create a source bucket for raw images: `serverless-pipeline-source-bucket`
- Create a destination bucket for thumbnails: `serverless-pipeline-dest-bucket`

### 2. Lambda Function Configuration
- Create a Lambda function named `ResizeImage` using Python 3.11.
- Attach a Pillow layer to support image manipulation.
- Configure an environment variable `DEST_BUCKET` pointing to your destination S3 bucket.
- Paste the source code from `lambda_function.py`.

### 3. Step Functions Workflow
- Create a Standard State Machine named `ImageProcessingWorkflow`.
- Use the provided ASL definition pointing to your `ResizeImage` Lambda function ARN.
- Ensure the automatically generated IAM execution role permits Lambda invocation.

### 4. API Gateway Integration
- Create a REST API (`ImageProcessingAPI`) with a POST method targeting the Step Functions `StartExecution` action.

## Testing
Upload a test `.jpg` or `.png` image to your source S3 bucket, trigger the execution ## Prerequisites
- An active AWS Account.
- Python 3.11+ installed locally (for code editing reference).
- Pillow library layer configured on the AWS Lambda function.

## Detailed Deployment Instructions

### 1. Amazon S3 Buckets Setup
- Create a source bucket for raw images: `serverless-pipeline-source-bucket`
- Create a destination bucket for thumbnails: `serverless-pipeline-dest-bucket`

### 2. Lambda Function Configuration
- Create a Lambda function named `ResizeImage` using Python 3.11.
- Attach a Pillow layer to support image manipulation.
- Configure an environment variable `DEST_BUCKET` pointing to your destination S3 bucket.
- Paste the source code from `lambda_function.py`.

### 3. Step Functions Workflow
- Create a Standard State Machine named `ImageProcessingWorkflow`.
- Use the provided ASL definition pointing to your `ResizeImage` Lambda function ARN.
- Ensure the automatically generated IAM execution role permits Lambda invocation.

### 4. API Gateway Integration
- Create a REST API (`ImageProcessingAPI`) with a POST method targeting the Step Functions `StartExecution` action.

## Testing
Upload a test `.jpg` or `.png` image to your source S3 bucket, trigger the execution via Step Functions or API Gateway, and verify that the corresponding resized thumbnail appears in your destination S3 bucket.
