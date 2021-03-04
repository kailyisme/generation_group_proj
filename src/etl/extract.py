import pandas as pd 

def extract_csv():
    df = pd.read_csv("./data/2021-02-23-isle-of-wight.csv", header=None)

    headings = ["Date-Time","location","customer_name","items","payment_type","total_amount","card_details"]
    df.columns= headings
    return df
