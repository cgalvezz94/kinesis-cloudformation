# app/producers/kinesis_publisher.py

import boto3
import json
import logging
from config import BINANCE_STREAM_NAME, REGION, PARTITION_KEY

logger = logging.getLogger("KinesisPublisher")
kinesis_client = boto3.client("kinesis", region_name=REGION)


def publish_event(event, stream_name=BINANCE_STREAM_NAME, partition_key=PARTITION_KEY):
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(event),
            PartitionKey=partition_key
        )
        logger.info(f"Evento publicado: {response['SequenceNumber']}")
    except Exception as e:
        logger.error(f"Error al publicar en Kinesis: {e}")

