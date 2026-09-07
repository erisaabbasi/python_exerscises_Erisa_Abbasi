correct_user = "admin"
correct_pass = "1234"
attemps = 3
while attemps > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_user and password == correct_pass:
        print("Welcome " + username + "!")
        break
    else:
        attemps -= 1
        print("Wrong username or password!")
        print("remaining attemps: ", attemps)