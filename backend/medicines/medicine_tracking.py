import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Medicines")

def lambda_handler(event, context):

    body = json.loads(event["body"])

    medicine = {
        "medicineId": str(uuid.uuid4()),
        "patientId": body["patientId"],
        "medicineName": body["medicineName"],
        "time": body["time"],
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=medicine)

    return {
        "statusCode": 200,
        "body": json.dumps("Medicine reminder added")
    }
