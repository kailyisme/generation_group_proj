from src.etl.extract import extract_csv
from src.etl.transform import transform_run
from src.etl.load import load_db
from src.db_handlers import db_init

conn = db_init.init_db()

data = extract_csv()
transform_data = transform_run(data)
load_db(conn, transform_data)
