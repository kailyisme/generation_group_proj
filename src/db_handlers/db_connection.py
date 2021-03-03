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


def commit(conn, sql, values=[]):
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(sql, values)