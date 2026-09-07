password = input("enter password: ")
errors = []
if len(password) < 8:
    errors.append("password must be at least 8 characters")
has_upper = False
for i in password:
    if i.isupper():
        has_upper = True
        break
if not has_upper:
    errors.append("password must contain at least one uppercase letter")
has_lower = False
for i in password:
    if i.islower():
        has_lower = True
        break
if not has_lower:
    errors.append("password must contain at least one lowercase letter")
has_number = False
for i in password:
    if i.isdigit():
        has_number = True
        break
if not has_number:
    errors.append("password must contain at least one number")
has_symbol = False
for i in password:
    if i in "@#$%":
        has_symbol = True
        break
if not has_symbol:
    errors.append("password must contain at least one symbol")
if errors:
    print("Password is Invalid!")
    for error in errors:
        print(error)
else:
    print("Password is Valid!")