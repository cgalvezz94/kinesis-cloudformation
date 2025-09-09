# tests/test_binance_ws_client.py

import pytest
import logging
import asyncio
from unittest.mock import AsyncMock, patch
from app.sources.binance_ws_client import connect

@pytest.fixture(autouse=True)
def setup_logger():
    logger = logging.getLogger("BinanceWS")
    logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

@patch("app.sources.binance_ws_client.parse_valid_events", return_value=[{"t": 123, "s": "BTCUSDT"}])
@patch("app.sources.binance_ws_client.websockets.connect")
@pytest.mark.asyncio
async def test_connect_receives_and_processes_event(mock_ws_connect, mock_parser, caplog):
    # Simular WebSocket con recv que devuelve un mensaje y luego lanza ConnectionClosed
    mock_ws = AsyncMock()
    mock_ws.recv.side_effect = [
        '{"e":"trade","t":123,"s":"BTCUSDT"}',
        asyncio.CancelledError()  # Simula interrupción del loop
    ]
    mock_ws_connect.return_value.__aenter__.return_value = mock_ws

    with caplog.at_level(logging.INFO):
        try:
            await connect()
        except asyncio.CancelledError:
            pass  # Esperado para cortar el loop

    assert "Conectado al WebSocket de Binance" in caplog.text
    assert "Evento recibido: {'t': 123, 's': 'BTCUSDT'}" in caplog.text
    mock_parser.assert_called_once()

