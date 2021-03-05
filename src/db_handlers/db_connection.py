import psycopg2
import os
from dotenv import load_dotenv
from dotenv.main import get_key

load_dotenv()

HOST = os.environ.get("POSTGRES_HOST")
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB = os.environ.get("POSTGRES_DB")
PORT = os.environ.get("POSTGRES_PORT")


def postgre_conn():
    try:
        return psycopg2.connect(
            database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
        )
    except psycopg2.OperationalError as e:
        if e.args[0] == f'FATAL:  database "{DB}" does not exist\n':
            conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT)
            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {DB}")
            return psycopg2.connect(
                database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
            )
        else:
            print(e)
            exit()


def commit(conn, sql, values=[]):
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
    conn.autocommit = False


def query(conn, sql, values=[]):
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        return cursor.fetchall()


def insert_into_table(conn, table_name, to_insert:dict):
    sql_query = f"INSERT INTO {table_name}("
    query_values = ""
    values = []
    for key in to_insert:
        query_values += "%s,"
        sql_query += f"{key},"
        values.append(to_insert[key])
    sql_query = sql_query[:-1]  # Remove trailing comma
    sql_query += ") VALUES ("
    sql_query += f"{query_values[:-1]})"
    commit(conn, sql_query, tuple(values))


def fetch_entry(conn, table_name, column_name, entry_value):
    sql_query = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
    with conn.cursor() as cursor:
        cursor.execute(sql_query, entry_value)
        return cursor.fetchone()