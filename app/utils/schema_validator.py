import json
import logging
from schemas.binance_trade_schema import BINANCE_TRADE_SCHEMA
from utils.schema_validator import validate_event

# Configuración del logger
logger = logging.getLogger("BinanceWS")
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def handle_event(event):
    """
    Procesa un evento recibido desde Binance WebSocket.
    Valida el esquema antes de imprimir o publicar.
    """
    if validate_event(event, BINANCE_TRADE_SCHEMA):
        logger.info("Evento válido recibido")
        print(json.dumps(event, indent=2))
        # Aquí podrías publicar a Kinesis o persistir en DynamoDB
    else:
        logger.warning("Evento descartado por esquema inválido")