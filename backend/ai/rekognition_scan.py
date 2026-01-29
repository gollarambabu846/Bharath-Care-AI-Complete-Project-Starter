import json
import boto3

rekognition = boto3.client("rekognition")

def lambda_handler(event, context):

    body = json.loads(event["body"])

    bucket = body["bucket"]
    image = body["image"]

    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": image
            }
        },
        MaxLabels=10,
        MinConfidence=80
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response["Labels"])
    }
