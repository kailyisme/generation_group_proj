from unittest.mock import patch
from src.etl.load import (
    add_temp_id,
    store_load,
    type_load,
    product_data,
    transcation,
    basket,
)


def test_add_temp_id():
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
        }
    ]
    expected = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    actual = add_temp_id(mock_data)
    assert actual == expected

@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_store_load(mock_insert, mock_fetch):
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    actual = store_load(mock_conn, mock_data)
    assert actual == expected

@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_type_load(mock_insert, mock_fetch):
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "loation": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    actual = type_load(mock_conn, mock_data)
    assert actual == expected

@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_product_data(mock_insert, mock_fetch):
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [{"product_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}]
    actual = product_data(mock_conn, mock_data)
    assert actual == expected

@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_transcation(mock_insert, mock_fetch):
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:01:45",
            "location": "Isle of Wight",
            "items": [{"size": "Large", "type": "", "name": "Latte", "price": "2.45"}],
            "payment_type": "CARD",
            "total_amount": 2.45,
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    actual = transcation(mock_conn, mock_data)
    assert actual == expected

@patch("src.db_handlers.db_connection.insert_into_table")
def test_basket(mock_insert):
    mock_trans_data = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    mock_conn = []
    mock_item_id = [
        {"product_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    expected = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    actual = basket(mock_conn, mock_item_id, mock_trans_data)
    assert actual == expected
