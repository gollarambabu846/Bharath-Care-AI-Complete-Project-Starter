import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Patients")

def lambda_handler(event, context):

    body = json.loads(event["body"])

    patient = {
        "patientId": str(uuid.uuid4()),
        "name": body["name"],
        "age": body["age"],
        "gender": body["gender"],
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=patient)

    return {
        "statusCode": 200,
        "body": json.dumps(patient)
    }
