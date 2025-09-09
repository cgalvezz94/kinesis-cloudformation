import json
import re
import logging
from app.utils.schema_validator import validate_event
from app.schemas.binance_trade_schema import BINANCE_TRADE_SCHEMA

logger = logging.getLogger("WebSocketParser")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def extract_payloads(raw_message: str) -> list:
    """
    Separates concatenated JSON objects from a raw WebSocket message.
    Returns a list of parsed dicts.
    """
    chunks = re.findall(r'\{.*?\}', raw_message)
    payloads = []

    for chunk in chunks:
        try:
            payload = json.loads(chunk)
            payloads.append(payload)
        except json.JSONDecodeError:
            logger.warning("Invalid JSON chunk discarded: %s", chunk)

    return payloads



def parse_valid_events(raw_message: str) -> list:
    """
    Extracts and validates events from a raw WebSocket message.
    Returns only those that pass schema validation.
    """
    events = []
    for payload in extract_payloads(raw_message):
        if validate_event(payload, BINANCE_TRADE_SCHEMA):
            events.append(payload)
        else:
            trade_id = payload.get("t", "unknown")
            logger.warning("Payload discarded: invalid schema [tradeId=%s]", trade_id)

    return events
