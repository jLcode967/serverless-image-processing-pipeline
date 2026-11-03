import os
import boto3
from PIL import Image
import io

s3 = boto3.client('s3')
DEST_BUCKET = os.environ['DEST_BUCKET']

def lambda_handler(event, context):
    try:
        # Check if triggered by an S3 Event Notification or a Direct Payload
        if 'Records' in event:
            record = event['Records'][0]
            source_bucket = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
        else:
            source_bucket = event.get('source_bucket')
            object_key = event.get('object_key')

        # Download image from source S3 bucket
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        image_content = response['Body'].read()

        # Open image and resize using Pillow
        image = Image.open(io.BytesIO(image_content))
        resized_image = image.resize((200, 200))

        # Save resized image to buffer
        buffer = io.BytesIO()
        # Determine the correct image format
        file_format = image.format if image.format else 'JPEG'
        resized_image.save(buffer, format=file_format)
        buffer.seek(0)

        # Upload resized image to destination S3 bucket
        dest_key = f"thumbnail-{object_key}"
        s3.put_object(
            Bucket=DEST_BUCKET,
            Key=dest_key,
            Body=buffer,
            ContentType=response['ContentType']
        )

        return {
            "statusCode": 200,
            "body": f"Successfully resized {object_key} and saved as {dest_key}"
        }
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise e