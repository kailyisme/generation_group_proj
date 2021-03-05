from src.db_handlers import db_connection as db
from uuid import uuid4 as uuidgen


headings = ["Date-Time","location","items","payment_type","total_amount"]
{'size': '', 'type': '', 'name': 'Glass of milk', 'price': '0.7'}
{'size': 'Regular', 'type': 'Flavoured hot chocolate', 'name': 'Vanilla', 'price': '2.6'}

def load_into_db(conn, transform_data):
    for row in transform_data:
        date_and_time = row["Date-Time"]
        location = row["location"]
        store_uuid = db.fetch_entry(conn, "store", "location", location)
        if store_uuid == []:
            store_uuid = uuidgen()
            db.insert_into_table(conn, "store", {"uuid": store_uuid, "location": location})
        else:
            store_uuid = store_uuid[0]
        
        
        payment_type = row["payment_type"]
        total_amount = row["total_amount"]