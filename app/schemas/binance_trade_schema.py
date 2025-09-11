# app/schemas/binance_trade_schema.py

BINANCE_TRADE_SCHEMA = {
    "type": "object",
    "properties": {
        "e": {"type": "string"},
        "E": {"type": "integer"},
        "s": {"type": "string"},
        "t": {"type": "integer"},
        "p": {"type": "string"},
        "q": {"type": "string"},
        "T": {"type": "integer"},
        "m": {"type": "boolean"},
        "M": {"type": "boolean"}
    },
    "required": ["e", "E", "s", "t", "p", "q", "T", "m", "M"]
}
