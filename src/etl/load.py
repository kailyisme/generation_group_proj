from src.db_handlers import db_connection as db
from uuid import uuid4 as uuidgen


headings = ["Date-Time","location","items","payment_type","total_amount"]
{'size': '', 'type': '', 'name': 'Glass of milk', 'price': '0.7'}
{'size': 'Regular', 'type': 'Flavoured hot chocolate', 'name': 'Vanilla', 'price': '2.6'}

def load_into_db(conn, transform_data):
    for row in transform_data:
        date_and_time = row["Date-Time"]
        
        store = row["location"]
        store_uuid = db.fetch_entry(conn, "store", "location", store)
        if store_uuid == []:
            store_uuid = uuidgen()
            db.insert_into_table(conn, "store", {"id": store_uuid, "location": store})
        else:
            store_uuid = store_uuid[0]
        
        items_ids = []
        for item in row["items"]:
            item_size = "Regular"
            if item["size"] != '':
                item_size = item["size"]
            item_type = None
            item_type_uuid = None
            if item["type"] != '':
                item_type = item["type"]
                item_type_uuid = db.fetch_entry(conn, "product_type", "name", item_type)[0]
                if item_type_uuid == None:
                    item_type_uuid = uuidgen()
                    db.insert_into_table(conn, "product_type", {"id": item_type_uuid, "name": item_type})
            item_name = item["name"]
            item_price = item["price"]
            

        payment_type = row["payment_type"]
        
        total_amount = row["total_amount"]