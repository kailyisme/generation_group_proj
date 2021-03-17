from src.db_handlers import db_connection
from src.db_handlers import db_tables


def init_db():
    conn = db_connection.postgre_conn()
    db_tables.init_tables(conn)
    return conn
