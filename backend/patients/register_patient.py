import boto3, json, uuid


db = boto3.resource('dynamodb')
table = db.Table('Patients')


def lambda_handler(event, context):
data = json.loads(event['body'])


patient_id = str(uuid.uuid4())


table.put_item(Item={
'patient_id': patient_id,
'name': data['name'],
'age': data['age'],
'gender': data['gender']
})


return {
'statusCode': 200,
'body': json.dumps({'patient_id': patient_id})
}