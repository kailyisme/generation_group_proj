import psycopg2
import os
from dotenv import load_dotenv
from dotenv.main import get_key

HOST = os.environ.get("POSTGRES_HOST")
print(HOST)
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB = os.environ.get("POSTGRES_DB")
print(os.environ.get("POSTGRES_PORT"))
PORT = int(os.environ.get("POSTGRES_PORT"))

print(HOST)


def postgre_conn():
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
