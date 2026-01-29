import boto3, json


db = boto3.resource('dynamodb')
table = db.Table('MedicineTracking')


def lambda_handler(event, context):
data = json.loads(event['body'])


table.put_item(Item=data)


return {
'statusCode': 200,
'body': json.dumps({'status': 'Medicine recorded'})
}