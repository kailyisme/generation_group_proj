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

            item_type = "Unidentified"
            item_type_uuid = None
            if item["type"] != "":
                item_type = item["type"]
            item_type_uuid = db.fetch_entry(conn, "product_type", ["name"], [item_type])
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


# --------added------
def add_temp_id(transform_data):
    temp_id = 1
    for dic in transform_data:
        dic["temp_id"] = temp_id
        temp_id += 1
    return transform_data


# -------ended------


def store_load(conn, transform_data):

    for row in transform_data:

        store = row["location"]
        store_uuid = db.fetch_entry(conn, "store", ["location"], [store])

        if store_uuid == None:
            store_uuid = str(uuidgen())
            db.insert_into_table(conn, "store", {"id": store_uuid, "location": store})
        else:
            store_uuid = store_uuid[0]
    return transform_data


def type_load(conn, transform_data):

    for row in transform_data:

        for item in row["items"]:

            item_type = "Unidentified"
            item_type_uuid = None
            if item["type"] != "":
                item_type = item["type"]
            item_type_uuid = db.fetch_entry(conn, "product_type", ["name"], [item_type])
            if item_type_uuid == None:
                item_type_uuid = str(uuidgen())
                db.insert_into_table(
                    conn, "product_type", {"id": item_type_uuid, "name": item_type}
                )
            else:
                item_type_uuid = item_type_uuid[0]

    return transform_data


def product_data(conn, transform_data):
    items_ids = []
    for row in transform_data:

        for item in row["items"]:

            item_size = "Regular"
            if item["size"] != "":
                item_size = item["size"]

            item_name = item["name"]
            item_price = item["price"]

            #   added --from big boy--------------------
            item_type = "Unidentified"
            if item["type"] != "":
                item_type = item["type"]
            item_type_uuid = db.fetch_entry(conn, "product_type", ["name"], [item_type])
            # ended-------------------------------------

            product_uuid = db.fetch_entry(
                conn,
                "product",
                ["type_id", "name", "size", "price"],
                [item_type_uuid[0], item_name, item_size, item_price],
            )
            if product_uuid == None:
                product_uuid = str(uuidgen())
                db.insert_into_table(
                    conn,
                    "product",
                    {
                        "id": product_uuid,
                        "type_id": item_type_uuid[0],
                        "name": item_name,
                        "size": item_size,
                        "price": item_price,
                    },
                )
            else:
                product_uuid = product_uuid[0]

            items_ids.append({"product_uuid": product_uuid, "temp_id": row["temp_id"]})
    return items_ids


def transcation(conn, transform_data):

    transaction_uuid_out = []

    for row in transform_data:

        date_and_time = row["Date-Time"]
        payment_type = row["payment_type"]
        total_amount = row["total_amount"]

        # ----added---from big boy---------------
        store = row["location"]
        store_uuid = db.fetch_entry(conn, "store", ["location"], [store])
        # ----------ended-----------------------
        transaction_uuid = str(uuidgen())

        db.insert_into_table(
            conn,
            "transaction",
            {
                "id": transaction_uuid,
                "datetime": date_and_time,
                "store_id": store_uuid[0],
                "payment_type": payment_type,
                "total_amount": total_amount,
            },
        )

        transaction_uuid_out.append(
            {"transaction_uuid": transaction_uuid, "temp_id": row["temp_id"]}
        )
    return transaction_uuid_out


def basket(conn, items_ids, transaction_uuid_out):

    # ----------added-----------
    for dic in transaction_uuid_out:

        for item in items_ids:
            if item["temp_id"] == dic["temp_id"]:
                # ---------ended-------------

                basket_uuid = str(uuidgen())

                db.insert_into_table(
                    conn,
                    "basket",
                    {
                        "id": basket_uuid,
                        "transaction_id": dic["transaction_uuid"],
                        "product_id": item["product_uuid"],
                    },
                )


def load_db(conn, transform_data):

    transform_data = add_temp_id(transform_data)
    store_load(conn, transform_data)
    type_load(conn, transform_data)
    items_id = product_data(conn, transform_data)
    transaction_uuid_out = transcation(conn, transform_data)
    basket(conn, items_id, transaction_uuid_out)