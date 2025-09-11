# app/lambda_handlers/kinesis_to_timestream.py
import json
import base64
import boto3
# import time

timestream = boto3.client('timestream-write')

DATABASE_NAME = 'BinanceTradesDB'
TABLE_NAME = 'trades'


def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(base64.b64decode(record['kinesis']['data']))

        # Convert timestamp (ms) to ISO 8601 format or leave as string in epoch ms
        timestamp = str(payload['T'])  # Timestream expects string in epoch milliseconds

        dimensions = [
            {'Name': 'pair', 'Value': payload['s']},
            {'Name': 'maker', 'Value': str(payload['m'])}
        ]

        measures = [
            {
                'Name': 'price',
                'Value': payload['p'],
                'Type': 'DOUBLE'
            },
            {
                'Name': 'quantity',
                'Value': payload['q'],
                'Type': 'DOUBLE'
            }
        ]

        record = {
            'Dimensions': dimensions,
            'MeasureName': 'trade',
            'MeasureValueType': 'MULTI',
            'Time': timestamp,
            'TimeUnit': 'MILLISECONDS',
            'MeasureValues': measures
        }

        try:
            timestream.write_records(
                DatabaseName=DATABASE_NAME,
                TableName=TABLE_NAME,
                Records=[record]
            )
        except Exception as e:
            print(f"Error writing to Timestream: {e}")
