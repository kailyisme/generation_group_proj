import src.etl.extract as ex


def cleaning_csv(df):
    df = [
        {
            key: line[key]
            for key in line
            if key != "customer_name" and key != "card_details"
        }
        for line in df
    ]
    return df


def transform(df):
    for dic in df:
        dic["items"] = dic["items"].split(",")
        new_items = []
        repeat = len(dic["items"]) // 3
        for i in range(repeat):
            product = dic["items"][1].split(" - ")
            if len(product) > 1:  # if there's a type for product
                product_type = product[0]
                name = product[1]
            else:
                product_type = ""
                name = product[0]
            new_items.append(
                {
                    "size": dic["items"][0],
                    "type": product_type,
                    "name": name,
                    "price": dic["items"][2],
                }
            )
            del dic["items"][0:3]
        dic["items"] = new_items
    return df


def transform_run(extract):
    df = cleaning_csv(extract)
    transform_data = transform(df)
    return transform_data


# if __name__ == "__main__":
#     print(transform(cleaning_csv(ex.extract_csv(ex.filename)))[:3])