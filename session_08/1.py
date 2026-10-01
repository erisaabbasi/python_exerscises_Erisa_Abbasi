def find_user(username:str,filename="users.txt"):
    """finds users with their username"""
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        if parts[0] == username:
            return parts
    return None

def add_user(username:str,code:str,status:str,filename="users.txt"):
    """adds new user and dose not add repetitive users"""
    if find_user(username,filename) is not None:
        print(f"user{username} already exists")
        return False
    with open(filename,"a") as f:
        f.write(username+","+code+","+status+"\n")
        print(f"user{username} added")
    return

def delete_user(username:str,filename="users.txt"):
    """deletes user"""
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("file dose not exist")
        return False
    new_lines = []
    found = False
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = line.split(",")
        if parts[0] == username:
            found = True
            continue
        new_lines.append(stripped)
    if not found:
        print("Username not found")
        return False
    with open(filename,"w") as f:
        for line in new_lines:
            f.write(line + "\n")
    print(f"user{username} deleted")
    return True

def generate_report(filename="users.txt"):
    """shows number of active and blocked users"""
    active_count = 0
    blocked_count = 0
    try:
        with open(filename,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("file dose not exist")
        return
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        parts = stripped.split(",")
        status = parts[2]
        if status == "active":
            active_count += 1
        elif status == "blocked":
            blocked_count += 1
    print("users report:")
    print(f"\tactive users: {active_count}")
    print(f"\tblocked users: {blocked_count}")

add_user("Ali","12345","active")
add_user("Sara","abc789","active")
add_user("Reza","45678","blocked")
print(find_user("Sara"))
generate_report()
delete_user("Reza")
print("after deleting reza:")
generate_report()

