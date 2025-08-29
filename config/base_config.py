import os

BINANCE_STREAM_NAME = os.getenv("BINANCE_STREAM_NAME", "binance-trades")
REGION = os.getenv("REGION", "us-east-1")
PARTITION_KEY = os.getenv("PARTITION_KEY", "BTCUSDT")
