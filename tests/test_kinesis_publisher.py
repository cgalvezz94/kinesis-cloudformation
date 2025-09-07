import json
from unittest.mock import patch
from app.producers.kinesis_publisher import publish_event
from config import BINANCE_STREAM_NAME

@patch("app.producers.kinesis_publisher.kinesis_client.put_record")
def test_publish_event_success(mock_put_record):
    # Evento simulado
    event = {
        "t": 123456789,
        "p": "27000.00",
        "q": "0.01",
        "T": 1756827686939
    }

    # Ejecutar publisher
    publish_event(event)

    # Validar que se llamó a put_record con los datos esperados
    mock_put_record.assert_called_once()
    args, kwargs = mock_put_record.call_args

    # Validar contenido del record
    payload = json.loads(kwargs["Data"])
    assert payload["t"] == event["t"]
    assert kwargs["StreamName"] == BINANCE_STREAM_NAME  # Ajustá según tu config