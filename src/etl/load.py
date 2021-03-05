from src.db_handlers import db_connection as db
from uuid import uuid4 as uuidgen


def load_into_db(conn, transform_data):
    for row in transform_data:
        date_and_time = row["Date-Time"]

        store = row["location"]
        store_uuid = db.fetch_entry(conn, "store", ["location"], [store])
        if store_uuid == None:
            store_uuid = str(uuidgen())
            db.insert_into_table(conn, "store", {"id": store_uuid, "location": store})
        else:
            store_uuid = store_uuid[0]

        items_ids = []
        for item in row["items"]:
            item_size = "Regular"
            if item["size"] != "":
                item_size = item["size"]
            item_type = None
            item_type_uuid = None
            if item["type"] != "":
                item_type = item["type"]
                item_type_uuid = db.fetch_entry(
                    conn, "product_type", ["name"], [item_type]
                )
                if item_type_uuid == None:
                    item_type_uuid = str(uuidgen())
                    db.insert_into_table(
                        conn, "product_type", {"id": item_type_uuid, "name": item_type}
                    )
                else:
                    item_type_uuid = item_type_uuid[0]
            item_name = item["name"]
            item_price = item["price"]
            product_uuid = db.fetch_entry(
                conn,
                "product",
                ["type_id", "name", "size", "price"],
                [item_type_uuid, item_name, item_size, item_price],
            )
            if product_uuid == None:
                product_uuid = str(uuidgen())
                db.insert_into_table(
                    conn,
                    "product",
                    {
                        "id": product_uuid,
                        "type_id": item_type_uuid,
                        "name": item_name,
                        "size": item_size,
                        "price": item_price,
                    },
                )
            else:
                product_uuid = product_uuid[0]
            items_ids.append(product_uuid)

        payment_type = row["payment_type"]

        total_amount = row["total_amount"]

        transaction_uuid = str(uuidgen())
        db.insert_into_table(
            conn,
            "transaction",
            {
                "id": transaction_uuid,
                "datetime": date_and_time,
                "store_id": store_uuid,
                "payment_type": payment_type,
                "total_amount": total_amount,
            },
        )

        for item_ordered in items_ids:
            basket_uuid = str(uuidgen())
            db.insert_into_table(
                conn,
                "basket",
                {
                    "id": basket_uuid,
                    "transaction_id": transaction_uuid,
                    "product_id": item_ordered,
                },
            )
