import json
import csv
import boto3
from src.etl import extract as ex
from src.etl import transform as tr
from src.etl.load import load_db
from src.db_handlers import db_init

from dotenv import load_dotenv
from dotenv.main import get_key

def execute(event, context):
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]
        s3_res = boto3.resource("s3")
        s3_object = s3_res.Object(bucket_name, key)
        raw = s3_object.get()["Body"].read().decode("utf-8").splitlines()
    except Exception as e:
        print(e)

    PORT = os.environ.get("POSTGRES_PORT")
    print(PORT)
    DB = os.environ.get("POSTGRES_DB")
    print(DB)
    
    print("no get after this ")
    
    PORT1 = os.environ.("POSTGRES_PORT")
    DB1 = os.environ["POSTGRES_DB"]
    print(PORT1)
    print(db1)
    
    df = ex.extract_csv(raw)
    df = tr.transform_run(df)
    print(df[1])
    conn = db_init.init_db()
    load_db(conn, df)
    
    # print(df[:3])