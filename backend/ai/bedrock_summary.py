import boto3


client = boto3.client('bedrock-runtime')


def summarize(text):
prompt = f"Summarize medical instructions: {text}"
response = client.invoke_model(
modelId='amazon.titan-text-lite-v1',
body=prompt
)
return response