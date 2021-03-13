from unittest.mock import patch
from src.etl.extract import extract_csv


@patch("csv.DictReader")
@patch("builtins.open")
def test_extract_csv(mock_open, mock_csv_dic):
    mock_filename = "mock path"
    mock_csv_dic.return_value = [
        {
            "Date-": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "customer_name": "Morgan Berka",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
            "card_details": "None",
        }
    ]

    expected = [
        {
            "Date-": "2021-02-23 09:00:48",
            "location": "Isle of Wight",
            "customer_name": "Morgan Berka",
            "items": "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9",
            "payment_type": "CASH",
            "total_amount": "8.40",
            "card_details": "None",
        }
    ]

    actual = extract_csv(mock_filename)
    assert actual == expected
