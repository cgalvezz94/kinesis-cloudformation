# app/processing/uptime_filter_tester.py
import logging

logger = logging.getLogger("UptimeFilter")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def is_continuous(prev_event: dict, current_event: dict) -> bool:
    """
    Verifica si el tradeId es consecutivo, indicando continuidad en el stream.
    """
    try:
        prev_id = prev_event["t"]
        current_id = current_event["t"]
        expected = prev_id + 1

        if current_id == expected:
            return True
        else:
            logger.warning(
                f"Gap detectado [prev={prev_id},"
                f"current={current_id}] | Esperado={expected}"
            )
            return False

    except KeyError as e:
        logger.error(f"Falta campo en evento para verificar continuidad: {e}")
        return False
