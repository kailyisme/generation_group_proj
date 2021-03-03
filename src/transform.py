import pandas as pd 
import uuid
import tabulate



df = pd.read_csv("2021-02-23-isle-of-wight.csv", header=None)


headings = ["Date-Time","location","customer_name","items","payment_type","total_amount","card_details"]
df.columns= headings
df.drop(columns=["customer_name","card_details"], inplace=True) 

df["items"] = df["items"].str.split(",")
df["temp_id"] = range(len(df["Date-Time"]))


store_table = df[["location","temp_id"]].copy()
transaction_table = df[["Date-Time","payment_type","total_amount","temp_id"]].copy()
# store_table = pd.Series(df["location"])
# x = store_table["location"].values


def split_item(df):
    products = []
    cl="items"
    
    
    for i in range(len(df[cl])):
        new_item =(df[cl].iloc[i])
        temp_id = df["temp_id"].iloc[i]
        repeat = int(len(new_item)/3)
        for i in range(repeat):
            products.append({"temp_id":temp_id,"size":new_item[0],"product":new_item[1],"price":new_item[2]}) 
            del new_item[0:3]
            
    # print(products)
    
# ---------------------------
    
    for dic in products:
        
        if dic["size"]=="":
            dic["size"]= "NaN" 
            
        if "-" in dic["product"]:
            two_fields = [x.strip() for x in dic["product"].split("-")]
            dic["type"] = two_fields[0]
            dic["product"] = two_fields[1]
            
        else:
            dic["type"]= "NaN"
            
    # print(products)
 
    return products




        
    
def type_table(data):
    all_types = []
    
    for dic in data:
        all_types.append(dic["type"])
           
    all_types = list(set(all_types))
    all_types.remove("NaN")
    
    types = []
    for i in all_types:
     types.append((uuid.uuid4(),i))   
    
    return types


def size_table(data):
    all_sizes = []
    
    for dic in data:
        all_sizes.append(dic["size"])
           
    all_sizes = list(set(all_sizes))
    all_sizes.remove("NaN")
    
    sizes = []
    for i in all_sizes:
     sizes.append((uuid.uuid4(),i))   
    
    print(tabulate.tabulate(sizes))
    return sizes



def store_table(data):
    all_stores = []
    
    for i in range(len(df["location"])):
        all_stores.append(df["location"].iloc[i])
       
    all_stores = list(set(all_stores))
    
    stores = []
    for i in all_stores:
        stores.append((uuid.uuid4(),i))
        
    return stores

def product_table(products_raw,type_table_data,size_table_data):
    
    for dic in products_raw:
        # if dic["product"] == 
        



products_raw = split_item(df)    

type_table_data = type_table(products_raw)
size_table_data = size_table(products_raw)
store_location_data = store_table(df)

print(tabulate.tabulate(type_table_data))
print(tabulate.tabulate(size_table_data))
print(tabulate.tabulate(store_location_data))