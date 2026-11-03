# Serverless Image Processing Pipeline

An event-driven serverless application built on AWS that automatically resizes uploaded images into thumbnails. The workflow integrates an **API Gateway** endpoint to trigger an **AWS Step Functions** state machine, which orchestrates a Python **AWS Lambda** function utilizing **Pillow** to process and save images between two **Amazon S3** buckets.

---

## Architecture Overview

```text
[ API Gateway (POST /process) ] 
       │
       ▼
[ Step Functions (ImageProcessingPipeline) ]
       │
       ▼
[ Lambda Function (ResizeImage) ] ──> Reads from Source S3 Bucket
       │
       ▼
[ Destination S3 Bucket ] (Saves thumbnail-<filename>)

```

---

## Project Resources & Configuration

* **Source S3 Bucket:** `serverless-pipeline-source-jliu-2026` (Stores raw, original images)
* **Destination S3 Bucket:** `serverless-pipeline-dest-bucket` *(or your custom destination bucket name)* (Stores resized 200x200 thumbnails)
* **Lambda Function:** `ResizeImage` (Python 3.11 with Pillow layer attached and `DEST_BUCKET` environment variable configured)
* **Step Functions State Machine:** `ImageProcessingPipeline` (Standard workflow containing task invocation, choice state validation, success, and fail states)
* **API Gateway:** `ImageProcessingAPI` (REST API with a `POST /process` method mapped to trigger Step Functions via `StartExecution`)

---

## Repository Contents

* `lambda_function.py` — The Python code for the resizing Lambda function, built to handle both direct JSON payloads and event triggers robustly.
* `state-machine.json` — The Amazon States Language (ASL) JSON definition for the Step Functions workflow.

---

## Setup & Deployment Steps

### 1. Amazon S3 Buckets Setup

1. Create a source S3 bucket to hold your original raw images.
2. Create a destination S3 bucket to hold the processed thumbnails.

### 2. Lambda Function Configuration

1. Create a Python 3.11 Lambda function named `ResizeImage`.
2. Attach a Pillow layer to support image manipulation.
3. Add an environment variable named `DEST_BUCKET` and set its value to your destination bucket's name.
4. Paste the code from `lambda_function.py` into the code editor and click **Deploy**.

### 3. Step Functions Workflow

1. Create a Standard State Machine named `ImageProcessingPipeline`.
2. Choose **Edit in code editor** and paste the contents of `state-machine.json`, replacing the placeholder Lambda ARN with your actual `ResizeImage` Lambda function ARN.
3. Allow Step Functions to auto-generate or link its IAM execution role with permissions to invoke Lambda.

### 4. API Gateway Integration

1. Create a REST API named `ImageProcessingAPI` with a resource path `/process` and a `POST` method.
2. Configure **AWS Service Integration** pointing to Step Functions (`StartExecution`).
3. Set up an IAM role (`APIGatewayToStepFunctionsRole`) with explicit `states:StartExecution` permissions on your state machine and proper trust relationships for API Gateway.
4. Add a mapping template for application/json passing the input payload:
```json
{
  "input": "$util.escapeJavaScript($input.body)",
  "stateMachineArn": "arn:aws:states:us-east-1:YOUR_ACCOUNT_ID:stateMachine:ImageProcessingPipeline"
}

```

5. Deploy the API to a `prod` stage.

---

## Testing the Application

1. In the API Gateway console under the **Test** tab for your `POST /process` method, send a test payload:
```json
{
    "source_bucket": "serverless-pipeline-source-jliu-2026",
    "object_key": "test-image.jpg"
}

```

2. Confirm you receive a `200 OK` response with a valid execution ARN.
3. Check your AWS Step Functions console to verify the execution finished with a green **Succeeded** status.
4. Open your destination S3 bucket to verify that the resized file (`thumbnail-test-image.jpg`) has been successfully created.
