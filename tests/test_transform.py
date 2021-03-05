from unittest.mock import Mock, patch
import pandas as pd 
from src.etl.transform import cleaning_csv,transform,transform_run


@patch("pandas.DataFrame.drop")
def test_cleaning_csv(mock_drop):
    fake_df = pd.DataFrame({"test":["test_answer"],"customer_name":["kat"],"card_details":["123test"]}, columns=["test","customer_name","card_details"])
    expected = pd.DataFrame({"test":["test_answer"]},columns=["test"])
    actual = cleaning_csv(fake_df)

    
def test_transform():
    fake_df = pd.DataFrame({'Date-Time': ['2021-02-23 09:00:48'], 'location': ['Isle of Wight'], 'items': ['Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9'], 'payment_type': ['CASH'], 'total_amount': [8.4]})
    expected = [{'Date-Time': ['2021-02-23 09:00:48'], 'location': ['Isle of Wight'], 'items': [[{'size': 'Large', 'type': '', 'name': 'Hot chocolate', 'price': '2.9'}, {'size': 'Large', 'type': '', 'name': 'Chai latte', 'price': '2.6'}, {'size': 'Large', 'type': '', 'name': 'Hot chocolate', 'price': '2.9'}]], 'payment_type': ['CASH'], 'total_amount': [8.4]}]
    actual = transform(fake_df)
    
def test_transform_run():
        fake_df = pd.DataFrame({"customer_name":["kat"],"card_details":["123test"],'Date-Time': ['2021-02-23 09:00:48'], 'location': ['Isle of Wight'], 'items': ['Large,Hot chocolate,2.9,Large,Chai latte,2.6,Large,Hot chocolate,2.9'], 'payment_type': ['CASH'], 'total_amount': [8.4]})
        expected = [{'Date-Time': ['2021-02-23 09:00:48'], 'location': ['Isle of Wight'], 'items': [[{'size': 'Large', 'type': '', 'name': 'Hot chocolate', 'price': '2.9'}, {'size': 'Large', 'type': '', 'name': 'Chai latte', 'price': '2.6'}, {'size': 'Large', 'type': '', 'name': 'Hot chocolate', 'price': '2.9'}]], 'payment_type': ['CASH'], 'total_amount': [8.4]}]
        actual = transform(fake_df)

