from src.db_handlers import db_connection


# create tables commands
SQL_store_table = "CREATE TABLE IF NOT EXISTS store (\
    uuid UUID PRIMARY KEY,\
    location VARCHAR(255)\
    );"

SQL_size = "CREATE TABLE IF NOT EXISTS product_size (\
    id SERIAL PRIMARY KEY,\
    name VARCHAR(255)\
    );"


SQL_type = "CREATE TABLE IF NOT EXISTS product_type (\
    id SERIAL PRIMARY KEY,\
    name VARCHAR(255)\
    );"


SQL_product = "CREATE TABLE IF NOT EXISTS product (\
    uuid UUID PRIMARY KEY,\
    type_id INTEGER REFERENCES product_type(id),\
    name VARCHAR(255),\
    size_id INTEGER REFERENCES product_size(id),\
    price MONEY\
    );"


SQL_transaction = "CREATE TABLE IF NOT EXISTS transaction (\
    uuid UUID PRIMARY KEY,\
    datetime TIMESTAMP,\
    store_uuid UUID REFERENCES store(uuid),\
    paymenttype VARCHAR(4),\
    totalamount MONEY\
    );"


SQL_basket = "CREATE TABLE IF NOT EXISTS basket (\
    id UUID PRIMARY KEY,\
    transaction_uuid UUID REFERENCES transaction(uuid),\
    product_uuid UUID REFERENCES product(uuid)\
    );"

tables_list = [
    SQL_store_table,
    SQL_size,
    SQL_type,
    SQL_product,
    SQL_transaction,
    SQL_basket,
]

# making sure tables already exist
conn = db_connection.postgre_conn()


def init_tables():
    for table in tables_list:
        db_connection.commit(conn, table)


if __name__ == "__main__":
    init_tables()