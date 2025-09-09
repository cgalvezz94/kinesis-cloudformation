#app/lambda_handlers/kinesis_to_dynamo.py
import json, base64, boto3

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(base64.b64decode(record['kinesis']['data']))
        item = {
            'tradeId': {'N': str(payload['t'])},
            'pair': {'S': payload['s']},
            'price': {'S': payload['p']},
            'quantity': {'S': payload['q']},
            'timestamp': {'N': str(payload['T'])},
            'maker': {'BOOL': payload['m']}
        }
        dynamodb.put_item(TableName='BinanceTrades', Item=item)
