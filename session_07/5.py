logs = [
    ("Ali","LOGIN",200),
    ("Ali","DOWNLOAD",200),
    ("Sara","LOGIN",403),
    ("Reza","LOGIN",200),
    ("Sara","LOGIN",403),
    ("Sara","LOGIN",403)
]
def analyze_log(logs):
    success_logins = 0
    failed_logins = 0
    user_errors = {}
    user_operations = {}
    suspicious_users = []
    for name, action, status in logs:
        user_operations[name] = user_operations.get(name, 0) + 1
        if action == "LOGIN":
            if status == 200:
                success_logins += 1
            elif status == 403:
                failed_logins += 1
                user_errors[name] = user_errors.get(name, 0) + 1
    for name , count in user_errors.items():
        if count >= 3:
            suspicious_users.append(name)
    return {
        "success_logins": success_logins,
        "failed_logins": failed_logins,
        "user_errors": user_errors,
        "user_operations": user_operations,
    }
print(analyze_log(logs))
