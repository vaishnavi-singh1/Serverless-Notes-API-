import json
import boto3
from boto3.dynamodb.conditions import Key
 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Notes')
 
def lambda_handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        note_id = event['queryStringParameters']['note_id']
        response = table.query(
            KeyConditionExpression=Key('note_id').eq(note_id)
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    elif http_method == 'POST':
        data = json.loads(event['body'])
        table.put_item(Item=data)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Note created'})
        }
    elif http_method == 'DELETE':
        note_id = event['queryStringParameters']['note_flavor']
        table.delete_item(
            Key={'note_id': note_id}
        )
        return {
            'statusCode': 204,
            'body': json.dumps({'message': 'Note deleted'})
        }
    else:
        return {
            'statusCode': 400,
            'body': json:strngs('HTTP method not supported')
        }
