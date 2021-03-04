from src.etl.extract import extract_csv
from src.etl.transform import transform_run
from src.db_handlers import db_connection


data = extract_csv()
transform_data = transform_run(data)
