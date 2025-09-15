# app/sources/binance_ws_client.py

import asyncio
import websockets
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from utils.websocket_payload_parser import parse_valid_events
from delivery.binance_event_handler import handle_event  # o donde tengas tu handler

# Configuración de logging
logger = logging.getLogger("BinanceWS")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# URL del WebSocket de Binance
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
async def connect():
    async with websockets.connect(BINANCE_WS_URL, ping_interval=20, ping_timeout=10) as ws:
        logger.info("Conectado al WebSocket de Binance")
        while True:
            try:
                raw_message = await ws.recv()
                valid_events = parse_valid_events(raw_message)
                for event in valid_events:
                    logger.info(f"Evento recibido: {event}")
                    handle_event(event)
            except websockets.ConnectionClosed:
                logger.warning("Conexión cerrada. Reintentando...")
                raise
            except Exception as e:
                logger.error(f"Error inesperado: {e}")
                continue


def run():
    try:
        asyncio.run(connect())
    except KeyboardInterrupt:
        print("🛑 Interrupción por teclado. Cerrando conexión...")
    except Exception as e:
        logger.error(f"Fallo al conectar: {e}")


if __name__ == "__main__":
    run()
