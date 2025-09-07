# tests/test_uptime_filter_tester.py

import pytest
import logging
from app.processing.uptime_filter_tester import is_continuous

@pytest.fixture(autouse=True)
def reset_logger():
    # Evita duplicación de handlers en tests repetidos
    logger = logging.getLogger("UptimeFilter")
    logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def test_continuous_trade_id(caplog):
    prev = {"t": 100}
    current = {"t": 101}
    with caplog.at_level(logging.INFO):
        assert is_continuous(prev, current) is True
        assert "Gap detectado" not in caplog.text

def test_gap_in_trade_id(caplog):
    prev = {"t": 100}
    current = {"t": 105}
    with caplog.at_level(logging.WARNING):
        assert is_continuous(prev, current) is False
        assert "Gap detectado [prev=100, current=105]" in caplog.text

def test_missing_trade_id(caplog):
    prev = {"t": 100}
    current = {"p": "27000.00"}  # Falta "t"
    with caplog.at_level(logging.ERROR):
        assert is_continuous(prev, current) is False
        assert "Falta campo en evento para verificar continuidad" in caplog.text