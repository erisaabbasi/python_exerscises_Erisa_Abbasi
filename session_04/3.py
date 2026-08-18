code = input("enter code: ")
valid = True
if len(code) != 8:
    print("Error:it should have 8 characters")
    valid = False
else:
    if not code[:4].isalpha():
        print("Error:it should have 4 letters")
        valid = False
    else:
        if not code[4:8].isdigit():
            print("Error:it should have 4 digits")
            valid = False
if valid:
    print("it's a valid code!")