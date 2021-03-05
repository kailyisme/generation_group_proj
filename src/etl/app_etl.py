from src.etl.extract import extract_csv
from src.etl.transform import transform_run
from src.etl.load import load_into_db
from src.db_handlers import db_init


conn = db_init.init_db()


data = extract_csv()
transform_data = transform_run(data)
# for i, row in enumerate(transform_data):
#     print(f"{i}\n", row)
#     if i == 10:
#         break

load_into_db(conn, transform_data)
