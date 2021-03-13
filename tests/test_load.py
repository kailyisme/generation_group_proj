from unittest.mock import patch, Mock
from src.etl.load import (
    add_temp_id,
    store_load,
    type_load,
    product_data,
    transcation,
    basket,
)


def test_add_temp_id():
    fake_data = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
        }
    ]
    expected = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
            "temp_id": 1,
        }
    ]
    actual = add_temp_id(fake_data)
    assert actual == expected


@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_store_load(mock_insert, mock_fetch):
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
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
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
                {"size": "Large", "type": "", "name": "Chai latte", "price": "2.6"},
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
            "temp_id": 1,
        }
    ]
    actual = type_load(mock_conn, mock_data)
    assert actual == expected


@patch("src.db_handlers.db_connection.fetch_entry")
@patch("src.db_handlers.db_connection.insert_into_table")
def test_product_data(mock_insert, mock_fetch):
    mock_fetch.return_value = ["e8980e54-91bf-4132-93d2-10919142f434"]
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
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

    mock_uuid = Mock()
    mock_uuid.return_value = "e8980e54-91bf-4132-93d2-10919142f434"
    mock_data = [
        {
            "Date-Time": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "items": [
                {"size": "Large", "type": "", "name": "Hot chocolate", "price": "2.9"},
            ],
            "payment_type": "CASH",
            "total_amount": "8.40",
            "temp_id": 1,
        }
    ]
    mock_conn = []
    expected = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]

    actual = transcation(mock_conn, mock_data, mock_uuid)
    print(actual)
    assert actual == expected


@patch("src.db_handlers.db_connection.insert_into_table")
def test_basket(mock_insert):

    mock_trans_data = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    mock_conn = []
    mock_item_id = [
        {"product_uuid": "a7aeb15f-61a8-418d-abda-3ab2e0b1ff3e", "temp_id": 1}
    ]
    expected = [
        {"transaction_uuid": "e8980e54-91bf-4132-93d2-10919142f434", "temp_id": 1}
    ]
    actual = basket(mock_conn, mock_item_id, mock_trans_data)
    assert actual == expected
