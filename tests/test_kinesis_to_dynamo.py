# tests/test_kinesis_to_dynamo.py

import json
import base64
import boto3
import pytest
from moto import mock_dynamodb
from app.lambda_handlers.kinesis_to_dynamo import lambda_handler

@pytest.fixture
def kinesis_event():
    payload = {
        "e": "trade",
        "s": "BTCUSDT",
        "t": 123,
        "p": "27000.00",
        "q": "0.01",
        "T": 1756827686939,
        "m": False,
        "M": True
    }
    encoded = base64.b64encode(json.dumps(payload).encode("utf-8")).decode("utf-8")
    return {
        "Records": [
            {
                "kinesis": {
                    "data": encoded
                }
            }
        ]
    }

@mock_dynamodb
def test_lambda_handler_inserts_item(kinesis_event):
    # Setup DynamoDB mock
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    dynamodb.create_table(
        TableName="BinanceTrades",
        KeySchema=[
            {"AttributeName": "tradeId", "KeyType": "HASH"},
            {"AttributeName": "pair", "KeyType": "RANGE"}
        ],
        AttributeDefinitions=[
            {"AttributeName": "tradeId", "AttributeType": "N"},
            {"AttributeName": "pair", "AttributeType": "S"}
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    # Invoke Lambda
    lambda_handler(kinesis_event, None)

    # Verify item was inserted
    response = dynamodb.get_item(
        TableName="BinanceTrades",
        Key={
            "tradeId": {"N": "123"},
            "pair": {"S": "BTCUSDT"}
        }
    )
    assert "Item" in response
    assert response["Item"]["price"]["S"] == "27000.00"
    assert response["Item"]["maker"]["BOOL"] is False