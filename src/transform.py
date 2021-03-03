import pandas as pd 
import uuid
import tabulate



df = pd.read_csv("./data/2021-02-23-isle-of-wight.csv", header=None)


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
            
    return products




        
    
def type_table(data):
    all_types = []
    
    for dic in data:
        all_types.append(dic["type"])
           
    all_types = list(set(all_types))
    all_types.remove("NaN")
    
    types = []
    for i in all_types:
     types.append({"id":uuid.uuid4(),"type":i})   
    
    return types


def size_table(data):
    all_sizes = []
    
    for dic in data:
        all_sizes.append(dic["size"])
           
    all_sizes = list(set(all_sizes))
    all_sizes.remove("NaN")
    
    sizes = []
    for i in all_sizes:
     sizes.append({"id":uuid.uuid4(),"size":i})   
    
    return sizes



def store_table(data):
    all_stores = []
    
    for i in range(len(df["location"])):
        all_stores.append(df["location"].iloc[i])
       
    all_stores = list(set(all_stores))
    
    stores = []
    for i in all_stores:
        stores.append({"id":uuid.uuid4(),"store":i})
        
    return stores

def product_table(products_raw,type_table_data,size_table_data):
    
    product = []
    product_true = []
    for dic in products_raw:

        size_temp = dic["size"]
        type_temp = dic["type"]
        
        
        size_id = size_temp
        type_id = type_temp
        
        for s in size_table_data:
            
            if s["size"] == size_temp:
                size_id = s["id"] 
                
        for t in type_table_data:
            
            if t["type"] == type_temp:
                type_id = t["id"] 
           
        product.append({"id":uuid.uuid4(),"type_id":type_id,"product":dic["product"],"size_id":size_id,"price":dic["price"]})        
        product.append({"id":uuid.uuid4(),"type_id":type_id,"product":dic["product"],"size_id":size_id,"price":dic["price"],"temp_id":dic["temp_id"]})

        x = list(set
    return product 


def transaction(df,store_data):
    store_loca = []
    for i in range(len(df["Date-Time"])):
        
        
        date_time = (df["Date-Time"].iloc[i])
        payment_type = (df["payment_type"].iloc[i])
        total_amount = (df["total_amount"].iloc[i])

        temp_id = (df["temp_id"].iloc[i])
        
        temp_store = (df["location"].iloc[i])
        
        for dic in store_data:
            
            if dic["store"] == temp_store:
                store_id = dic["id"]
                
        store_loca.append({"id":uuid.uuid4(),"date_time":date_time,"store_id":store_id,"payment_type":payment_type,"total":total_amount,"temp_id":temp_id})
                
    return store_loca
    
        
def basket(transaction_data,product_table_data):   
    basket = []
    for ids in transaction_data:
        temp_trans_id = ids["id"]
        
        for dic in product_table_data:
            if dic["temp_id"] == ids["temp_id"]:
            
                basket.append({"id":uuid.uuid4(),"transaction_id":temp_trans_id,"product_id":dic["id"]})
    
    return basket
    
    
    
    
    

products_raw = split_item(df)    

type_table_data = type_table(products_raw)

size_table_data = size_table(products_raw)

store_location_data = store_table(df)

product_table_data = product_table(products_raw,type_table_data,size_table_data)

transaction_data = transaction(df,store_location_data)

basket_data = basket(transaction_data,product_table_data)

# print(tabulate.tabulate(type_table_data, headers="keys"))

# print(tabulate.tabulate(size_table_data, headers="keys"))

# print(tabulate.tabulate(store_location_data, headers="keys"))

# print(tabulate.tabulate(product_table_data, headers="keys"))

# print(tabulate.tabulate(transaction_data, headers="keys"))

# print(tabulate.tabulate(basket_data, headers="keys"))
