# tests/test_binance_event_handler.py

import pytest
import logging
from app.delivery import binance_event_handler
from app.delivery.binance_event_handler import handle_event
from unittest.mock import patch

@pytest.fixture(autouse=True)
def reset_state():
    # Resetear estado interno antes de cada test
    binance_event_handler._last_event = None

@pytest.fixture(autouse=True)
def setup_logger():
    logger = logging.getLogger("BinanceEventHandler")
    logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

@patch("app.delivery.binance_event_handler.publish_event")
def test_event_published_successfully(mock_publish, caplog):
    event = {
        "e": "trade", "s": "BTCUSDT", "t": 100, "p": "27000.00",
        "q": "0.01", "T": 1756827686939, "m": False, "M": True
    }

    with caplog.at_level(logging.INFO):
        handle_event(event)

    mock_publish.assert_called_once_with(event)
    assert "Evento publicado correctamente [tradeId=100]" in caplog.text

@patch("app.delivery.binance_event_handler.publish_event")
def test_gap_logged_when_trade_id_not_continuous(mock_publish, caplog):
    prev = {
        "e": "trade", "s": "BTCUSDT", "t": 100, "p": "27000.00",
        "q": "0.01", "T": 1756827686939, "m": False, "M": True
    }
    current = {
        "e": "trade", "s": "BTCUSDT", "t": 105, "p": "27001.00",
        "q": "0.02", "T": 1756827687000, "m": True, "M": False
    }

    binance_event_handler._last_event = prev

    with caplog.at_level(logging.WARNING):
        handle_event(current)

    assert "Gap detectado en tradeId [prev=100, current=105]" in caplog.text
    mock_publish.assert_called_once_with(current)

@patch("app.delivery.binance_event_handler.publish_event", side_effect=Exception("Error simulado"))
def test_publish_failure_logged(mock_publish, caplog):
    event = {
        "e": "trade", "s": "BTCUSDT", "t": 101, "p": "27000.00",
        "q": "0.01", "T": 1756827686939, "m": False, "M": True
    }

    with caplog.at_level(logging.ERROR):
        handle_event(event)

    assert "Error al publicar evento [tradeId=101]: Error simulado" in caplog.text
