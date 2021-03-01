
# assuming got data in a state 


def cleaning(state):
    for dic in state:
        dic.pop("customer_name"),dic.pop("bank_details")
    return state

    