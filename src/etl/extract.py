import csv

filename = "./data/2021-02-23-isle-of-wight.csv"


def extract_csv(filename=filename):
    csv_data = []
    with open(filename) as file:
        data = csv.DictReader(
            file,
            [
                "Date-Time",
                "location",
                "customer_name",
                "items",
                "payment_type",
                "total_amount",
                "card_details",
            ],
        )
        for line in data:
            csv_data.append(line)
    return csv_data
