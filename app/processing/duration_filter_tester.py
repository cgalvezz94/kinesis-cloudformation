import logging

logger = logging.getLogger("DurationFilter")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def is_duration_valid(prev_event: dict, current_event: dict, min_ms: int = 1) -> bool:
    """
    Verify if duration between 2 events is greater or equall to minimun threshold
    """
    try:
        duration = current_event["T"] - prev_event["T"]
        trade_id = current_event.get("t", "unknown")
        
        if duration >= min_ms:
            return True
        else:
            logger.warning(
                f"Duracion invalida [tradeId={trade_id}] | "
                f"ΔT={duration} ms < {min_ms} ms"
            )
    except KeyError as e:
        logger.error(f"Falta campo en evento para calcular duracion: {e}")
        return False

