# tests/test_websocket_payload_parser.py

import pytest
from app.utils.websocket_payload_parser import parse_valid_events

def test_single_valid_event():
    raw = '{"e":"trade","E":1756827686939,"s":"BTCUSDT","t":123,"p":"27000.00","q":"0.01","T":1756827686939,"m":false,"M":true}'
    events = parse_valid_events(raw)
    assert len(events) == 1
    assert events[0]["t"] == 123

def test_multiple_concatenated_events():
    raw = (
        '{"e":"trade","E":1756827686939,"s":"BTCUSDT","t":1,"p":"27000.00","q":"0.01","T":1756827686939,"m":false,"M":true}'
        '{"e":"trade","E":1756827686940,"s":"BTCUSDT","t":2,"p":"27001.00","q":"0.02","T":1756827686940,"m":true,"M":false}'
    )
    events = parse_valid_events(raw)
    assert len(events) == 2
    assert events[0]["t"] == 1
    assert events[1]["t"] == 2

def test_malformed_json_skipped():
    raw = (
        '{"e":"trade","E":1756827686939,"s":"BTCUSDT","t":1,"p":"27000.00","q":"0.01","T":1756827686939,"m":false,"M":true}'
        '{"e":"trade","E":1756827686940,"s":"BTCUSDT","t":2,"p":"27001.00","q":"0.02","T":1756827686940,"m":true,"M":false'  # falta cierre
    )
    events = parse_valid_events(raw)
    assert len(events) == 1  # solo el primero es válido

def test_empty_message():
    raw = ''
    events = parse_valid_events(raw)
    assert events == []