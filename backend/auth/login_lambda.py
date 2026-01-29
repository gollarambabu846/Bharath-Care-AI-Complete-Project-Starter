import json


def lambda_handler(event, context):
body = json.loads(event['body'])


if body['username'] == 'admin' and body['password'] == 'admin123':
return {
'statusCode': 200,
'body': json.dumps({'message': 'Login successful'})
}


return {
'statusCode': 401,
'body': json.dumps({'message': 'Invalid credentials'})
}