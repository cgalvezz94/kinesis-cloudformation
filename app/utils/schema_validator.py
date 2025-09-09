import json
import logging
from app.schemas.binance_trade_schema import BINANCE_TRADE_SCHEMA

# Configuración del logger
logger = logging.getLogger("BinanceWS")
logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

def validate_event(event: dict, schema: dict = BINANCE_TRADE_SCHEMA) -> bool:
    """
    Valida que el evento cumpla con el esquema esperado.
    Verifica que todas las claves requeridas estén presentes.
    """
    try:
        required_keys = schema.get("required", [])
        if not all(k in event for k in required_keys):
            logger.warning(f"Evento inválido: faltan claves requeridas. Recibido: {json.dumps(event)}")
            return False
        return True
    except Exception as e:
        logger.error(f"Error en validación de esquema: {e}")
        return False
