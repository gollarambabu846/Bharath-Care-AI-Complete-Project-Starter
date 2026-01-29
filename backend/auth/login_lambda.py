import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

def lambda_handler(event, context):

    body = json.loads(event["body"])

    userId = body["userId"]
    password = body["password"]

    response = table.get_item(
        Key={"userId": userId}
    )

    if "Item" not in response:
        return {
            "statusCode": 401,
            "body": json.dumps("User not found")
        }

    return {
        "statusCode": 200,
        "body": json.dumps("Login successful")
    }
