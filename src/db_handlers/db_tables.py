from src.db_handlers import db_connection


with open("src/db_handlers/tables.sql") as sql_file:
    sql_file_string = sql_file.read()


def init_tables(conn):
    db_connection.commit(conn, sql_file_string)
