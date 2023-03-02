import nose
import logging
import arrow
from brevetsmongo import insert_brevet, retrieve_brevet

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_insert_b():
    brevet_dist = 200
    start_time = "2023-01-01T00:00:00"
    control_list = [
        {"km": 0, "open": "2021-01-01T00:00", "close": "2023-01-01T01:00:00"},
        {"km": 50, "open": "2021-01-01T01:28", "close": "2023-01-01T03:30:00"},
        {"km": 100, "open": "2021-01-01T02:56", "close": "2023-01-01T06:40:00"},
        {"km": 150, "open": "2023-01-01T04:25", "close": "2023-01-01T10:00:00"},
        {"km": 200, "open": "2023-01-02T05:53", "close": "2023-01-01T13:30:00"}
    ]
    inserted_id = insert_brevet(brevet_dist, start_time, control_list)
    assert isinstance(inserted_id, str)

def test_retrieve_b():
    # Test retrieving the newest document
    brevet_dist = 200
    start_time = "2023-01-01T00:00"
    control_list = [
        {"km": 0, "open": "2021-01-01T00:00", "close": "2023-01-01T01:00"},
        {"km": 50, "open": "2021-01-01T01:28", "close": "2023-01-01T03:30"},
        {"km": 100, "open": "2021-01-01T02:56", "close": "2023-01-01T06:40"},
        {"km": 150, "open": "2023-01-01T04:25", "close": "2023-01-01T10:00"},
        {"km": 200, "open": "2023-01-02T05:53", "close": "2023-01-01T13:30"}
    ]
    inserted_id = insert_brevet(brevet_dist, start_time, control_list)
    assert isinstance(inserted_id, str)

    brevet_dist, start_time, control_list = retrieve_brevet()
    assert brevet_dist == 200
    assert start_time == "2023-01-01T00:00"
    assert control_list == [
        {"km": 0, "open": "2021-01-01T00:00", "close": "2023-01-01T01:00"},
        {"km": 50, "open": "2021-01-01T01:28", "close": "2023-01-01T03:30"},
        {"km": 100, "open": "2021-01-01T02:56", "close": "2023-01-01T06:40"},
        {"km": 150, "open": "2023-01-01T04:25", "close": "2023-01-01T10:00"},
        {"km": 200, "open": "2023-01-02T05:53", "close": "2023-01-01T13:30"}
    ]
