import boto3


client = boto3.client('rekognition')


def scan(image_bytes):
response = client.detect_text(Image={'Bytes': image_bytes})
return response['TextDetections']