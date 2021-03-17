import csv

def extract_csv(file):
    csv_data = []
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
