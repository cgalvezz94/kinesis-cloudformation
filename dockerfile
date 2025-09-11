FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Solo copiar lo necesario
COPY app/delivery/ ./delivery
COPY app/processing/ ./processing
COPY app/producers/ ./producers
COPY app/utils/ ./utils
COPY app/schemas/ ./schemas
COPY app/sources/ ./sources
COPY config/ ./config

CMD ["python", "app/sources/binance_ws_client.py"]