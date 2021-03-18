import psycopg2
import os
from dotenv import load_dotenv
from dotenv.main import get_key

load_dotenv()

HOST = os.environ.get("HOST")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
DB = os.environ.get("DB")
PORT = os.environ.get("PORT")


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
            conn = psycopg2.connect(
                database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT
            )
            conn.autocommit = True
            return conn
        else:
            print(e)
            exit()


def commit(conn, sql, values=[]):
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
    conn.commit()


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


def fetch_entry(conn, table_name, column_names, entry_values):
    sql_query = f"SELECT * FROM {table_name} WHERE"
    for column_name in column_names:
        sql_query += f" {column_name} = %s AND"
    sql_query = sql_query[:-4]
    with conn.cursor() as cursor:
        cursor.execute(sql_query, entry_values)
        return cursor.fetchone()
    