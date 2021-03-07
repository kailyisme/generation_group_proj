from unittest.mock import patch
import pandas as pd
from src.etl.extract import extract_csv

@patch("pandas.read_csv")
def test_extract_csv(mock_extract):
    expected = pd.DataFrame(
        {
            "Date-Time": ["2021-02-23 09:00:48"],
            "location": ["Isle of Wight"],
            "customer_name": ["kat"],
            "items": [
                "Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9"
            ],
            "payment_type": ["CASH"],
            "total_amount": [8.4],
            "card_details": ["discover,6011446267942513"],
        }
    )
    actual = extract_csv()