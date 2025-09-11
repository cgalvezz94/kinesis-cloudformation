# app/delivery/binance_event_handler.py

import logging
# from app.processing.duration_filter_tester import is_duration_valid
from app.processing.uptime_filter_tester import is_continuous
from app.producers.kinesis_publisher import publish_event

# Configuración de logging
logger = logging.getLogger("BinanceEventHandler")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Estado interno para comparar eventos consecutivos
_last_event = None


def handle_event(event: dict):
    """
    Procesa un evento validado desde Binance.
    Aplica filtros de duración y continuidad antes de publicar.
    """
    global _last_event
    trade_id = event.get("t", "unknown")

    # Filtro de duración
    # if _last_event and not is_duration_valid(_last_event, event):
    #    logger.warning(f"Evento descartado por duración inválida [tradeId={trade_id}]")
    #    return

    # Filtro de continuidad
    if _last_event and not is_continuous(_last_event, event):
        logger.warning(f"Gap detectado en tradeId [prev={_last_event['t']}, current={trade_id}]")

    # Publicar evento
    try:
        publish_event(event)
        logger.info(f"Evento publicado correctamente [tradeId={trade_id}]")
    except Exception as e:
        logger.error(f"Error al publicar evento [tradeId={trade_id}]: {e}")

    # Actualizar estado
    _last_event = event
