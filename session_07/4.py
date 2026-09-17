def check_large_transactions(transactions):
    name, function, amount, time = transactions
    return amount > 100000000
def check_repeated_withdrawals(transactions):
    suspicious_transactions = []
    last_user = None
    withdraw_streak = 0
    for transaction in transactions:
        name, function, amount, time = transaction
        if function == "withdraw" and name == last_user:
            withdraw_streak += 1
        elif function == "withdraw":
            withdraw_streak = 1
        else:
            withdraw_streak = 0
        last_user = name
        if function == "withdraw" and withdraw_streak > 3:
            suspicious_transactions.append(transaction)
        return suspicious_transactions
def check_balance(transactions):
    suspicious_transactions = []
    balances = {}
    for transaction in transactions:
        name, function, amount, time = transaction
        if name not in balances:
            balances[name] = 0
        if function == "deposit":
            balances[name] += amount
        elif function == "withdraw":
            if amount > balances[name]:
                suspicious_transactions.append(transaction)
            else:
                balances[name] -= amount
    return suspicious_transactions
def generate_fraud_report(transactions):
    report = []
    large_list = []
    for transaction in transactions:
        if check_large_transactions(transaction):
            large_list.append(transaction)
    repeated_list = check_repeated_withdrawals(transactions)
    balance_list = check_balance(transactions)
    for transaction in transactions:
        reasons = []
        if transaction in large_list:
            reasons.append("large transaction")
        if transaction in repeated_list:
            reasons.append("repeated withdrawls")
        if transaction in balance_list:
            reasons.append("insufficient balance")
        if len(reasons) > 0:
            report.append({"transaction": transaction, "reasons": reasons})
    return report
def detect_fraud(transactions):
    return generate_fraud_report(transactions)
transactions = [
    ("Ali","deposit",50000000,10),
    ("Ali","withdraw",2000000,11),
    ("Ali","withdraw",3000000,12),
    ("Ali","withdraw",4000000,13),
    ("Ali","withdraw",5000000,14),
    ("Ali","withdraw",6000000,15),
    ("Sara","deposit",50000000,20),
    ("Sara","withdraw",60000000,21),
    ("Reza","deposit",150000000,30)
]
print(detect_fraud(transactions))


