def count_successful_logins(filename="logs.txt"):
    "counts code 200"
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
    count = 0
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = stripped.split(",")
        action = parts[1]
        code = parts[2]
        if action == "LOGIN" and code == "200":
            count += 1
    return count
def count_failed_logins(filename="logs.txt"):
    "counts all codes except 200"
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
    count = 0
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = stripped.split(",")
        action = parts[1]
        code = parts[2]
        if action == "LOGIN" and code != "200":
            count += 1
    return count
def find_suspicious_users(filename="logs.txt"):
    "finds users who have recived code 403 more than 3 times"
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
    usernames = []
    error_counts = []
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = stripped.split(",")
        username = parts[0]
        action = parts[1]
        code = parts[2]
        if action == "Login" and code == "403":
            index = -1
            for i in range(len(usernames)):
                if usernames[i] == username:
                    index = i
                    break
            if index == -1:
                usernames.append(username)
                error_counts.append(1)
            else:
                error_counts[index] += 1
    suspicious = []
    for i in range(len(usernames)):
        "return number of actions for each user"
        if error_counts[i] >= 3:
            suspicious.append(usernames[i])
        return suspicious
def user_operation_counts(filename="logs.txt"):
    """counts each users operations"""
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
    usernames = []
    counts = []
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = stripped.split(",")
        username = parts[0]
        index = -1
        for i in range(len(usernames)):
            if usernames[i] == username:
                index = i
                break
        if index == -1:
            usernames.append(username)
            counts.append(1)
        else:
            counts[index] += 1
    return usernames , counts
def generate_report(filename="logs.txt"):
    success = count_successful_logins(filename)
    failed = count_failed_logins(filename)
    suspicious = find_suspicious_users(filename)
    usernames,counts = user_operation_counts(filename)
    print("final report:")
    print(f"\tsuccessfull logins: ",success)
    print(f"\tfailed logins: ",failed)
    print(f"\tsuspicious: ",suspicious)
    print("each users activities: ")
    for i in range(len(usernames)):
        print(f"\t{usernames[i]}: {counts[i]}")
generate_report()