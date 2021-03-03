from src.db_handlers import db_connection


with open("src/db_handlers/tables.sql") as sql_file:
    sql_file_string = sql_file.read()


# making sure tables already exist
conn = db_connection.postgre_conn()


def init_tables():
    db_connection.commit(conn, sql_file_string)


if __name__ == "__main__":
    init_tables()