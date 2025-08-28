# app/sources/binance_ws_client.py

import asyncio
import websockets
import json
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

# Configuración de logging
logger = logging.getLogger("BinanceWS")
logger.setLevel(logging.INFO)

# URL del WebSocket de Binance
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

# Buffer local para eventos
event_buffer = []

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=10))
async def connect():
    async with websockets.connect(BINANCE_WS_URL, ping_interval=20, ping_timeout=10) as ws:
        logger.info("Conectado al WebSocket de Binance")
        while True:
            try:
                message = await ws.recv()
                data = json.loads(message)
                handle_event(data)
            except websockets.ConnectionClosed:
                logger.warning("Conexión cerrada. Reintentando...")
                raise
            except Exception as e:
                logger.error(f"Error inesperado: {e}")
                continue

def handle_event(event):
    # Simulación: guardar en buffer e imprimir
    event_buffer.append(event)
    print(json.dumps(event, indent=2))

def run():
    try:
        asyncio.run(connect())
    except Exception as e:
        logger.error(f"Fallo al conectar: {e}")

if __name__ == "__main__":
    run()