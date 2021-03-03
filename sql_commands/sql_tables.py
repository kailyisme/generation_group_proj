import psycopg2
import os
from dotenv import load_dotenv
from dotenv.main import get_key

load_dotenv()

HOST = os.environ.get("POSTGRES_HOST")
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB = os.environ.get("POSTGRES_DB")
PORT = (os.environ.get("POSTGRES_PORT"))


def postgre_conn():
    try:
        return psycopg2.connect(
            database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
        )
    except psycopg2.OperationalError as e:
        if e.args[0] == f'FATAL:  database "{DB}" does not exist\n':
            conn = psycopg2.connect(
                user=USER, password=PASSWORD, host=HOST, port=PORT
                )
            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {DB}")
            return psycopg2.connect(
                database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
                )


print(postgre_conn())

# create tables commands
SQL_store_table = "CREATE TABLE IF NOT EXISTS store (\
    store_uuid UUID PRIMARY KEY,\
    store_location VARCHAR(255)\
    );"

SQL_size = "CREATE TABLE IF NOT EXISTS product_size (\
    product_size_id SERIAL PRIMARY KEY,\
    product_size_name VARCHAR(255)\
    );"


SQL_type = "CREATE TABLE IF NOT EXISTS product_type (\
    product_type_id SERIAL PRIMARY KEY,\
    product_type_name VARCHAR(255)\
    );"


SQL_product = "CREATE TABLE IF NOT EXISTS product (\
    product_uuid UUID PRIMARY KEY,\
    product_type_id INTEGER REFERENCES product_type(product_type_id),\
    product_name VARCHAR(255),\
    product_size_id INTEGER REFERENCES product_size(product_size_id),\
    product_price MONEY\
    );"


SQL_transaction = "CREATE TABLE IF NOT EXISTS transaction (\
    transaction_uuid UUID PRIMARY KEY,\
    transaction_datetime TIMESTAMP,\
    store_uuid UUID REFERENCES store(store_uuid),\
    transaction_paymenttype VARCHAR(4),\
    transaction_totalamount MONEY\
    );"


SQL_basket = "CREATE TABLE IF NOT EXISTS basket (\
    basket_id UUID PRIMARY KEY,\
    transaction_uuid UUID REFERENCES transaction(transaction_uuid),\
    product_uuid UUID REFERENCES product(product_uuid)\
    );"


# db variable types
DB_VARIABLE_TYPES = {
    "id": "INTEGER",
    "uuid": "UUID",
    "name": "VARCHAR(255)",
    "datetime": "TIMESTAMP",
    "paymenttype": "VARCHAR(4)",
    "totalamount": "MONEY",
    "location": "VARCHAR(255)",
    "price": "MONEY",
}
