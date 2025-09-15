FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Solo copiar lo necesario
COPY app/ ./app
COPY config/ ./config

CMD ["python", "sources/binance_ws_client.py"]