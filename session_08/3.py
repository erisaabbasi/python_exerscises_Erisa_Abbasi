def read_lines(filename="transactions.txt"):
    with open(filename,"r") as f:
        lines = f.readlines()
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped != "":
            result.append(stripped)
    return result
def total_deposits(username:str,filename="transactions.txt"):
    """total deposits of user"""
    total = 0
    for line in read_lines(filename):
        parts = line.split(",")
        if parts[0] == username and parts[1] == "deposit":
            total += int(parts[2])
    return total
def total_withdrawals(username:str,filename="transactions.txt"):
        """total withdrawals of user"""
        total = 0
        for line in read_lines(filename):
            parts = line.split(",")
            if parts[0] == username and parts[1] == "withdraw":
                total += int(parts[2])
        return total
def calculate_balance(username:str,filename="transactions.txt"):
    """calculate balance of user"""
    return total_deposits(username,filename)-total_withdrawals(username,filename)
def find_invalid_transactions(username:str,filename="transactions.txt"):
    """transactions where withdraw amount is  more than balance"""
    invalid = []
    balance = 0
    for line in read_lines(filename):
        parts = line.split(",")
        name = parts[0]
        t_type = parts[1]
        amount = int(parts[2])
        if name != username:
            continue
        if t_type == "deposit":
            balance += amount
        elif t_type == "withdraw":
            if amount > balance:
                invalid.append(line)
            else:
                balance -= amount
    return invalid
def get_all_usernames(filename="transactions.txt"):
    usernames = []
    for line in read_lines(filename):
        parts = line.split(",")
        name = parts[0]
        found = False
        for user in usernames:
            if user == name:
                found = True
                break
        if not found:
            usernames.append(name)
    return usernames
def generate_report(filename="transactions.txt"):
    usernames = get_all_usernames(filename)
    print("final report:")
    for username in usernames:
        deposits = total_deposits(username,filename)
        withdrawals = total_withdrawals(username,filename)
        balance = calculate_balance(username,filename)
        invalid = find_invalid_transactions(username,filename)
        print(f"name: {username}")
        print(f"total deposits: {deposits}")
        print(f"total withdrawals: {withdrawals}")
        print(f"balance: {balance}")
        print(f"invalid transactions: {invalid}")
generate_report()
