transactions = [
    ("Ali","deposit",5000000),
    ("Ali","withdraw",1000000),
    ("Sara","deposit",8000000),
    ("Ali","withdraw",500000),
    ("Sara","withdraw",2000000),
    ("Reza","deposit",10000000)
]
def analyze_transactions(transactions):
    users = {}
    for name, function, amount in transactions:
        if name not in users:
            users[name] = {"deposits": 0, "withdrawls": 0, "transactions": 0, "balance_changes":0}
        if function == "deposit":
            users[name]["deposits"] += amount
        elif function == "withdraw":
            users[name]["withdrawls"] += amount
        users[name]["transactions"] += 1
        for name in users:
            users[name]["balance_changes"] = users[name]["deposits"] - users[name]["withdrawls"]
        max_withdraw_user = None
        max_withdraw_value = -1
        for name in users:
            if users[name]["deposits"] < users[name]["withdrawls"]:
                max_withdraw_value = users[name]["withdrawls"]
                max_withdraw_user = name
        max_deposit_user = None
        max_deposit_value = -1
        for name in users:
            if users[name]["withdrawls"] < users[name]["deposits"]:
                max_deposit_value = users[name]["deposits"]
                max_deposit_user = name
        most_active_user = None
        most_active_value = -1
        for name in users:
            if users[name]["transactions"] > most_active_value:
                most_active_value = users[name]["transactions"]
                most_active_user = name
    return {
        "users" : users,
        "max_deposit_user" : max_deposit_user,
        "max_withdraw_user" : max_withdraw_user,
        "most_active_user" : most_active_user,

    }
print(analyze_transactions(transactions))
