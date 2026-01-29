import boto3


client = boto3.client('comprehendmedical')


def extract(text):
return client.detect_entities_v2(Text=text)