first_color = input("What is your first color?: ")
second_color = input("What is your second color?: ")
third_color = input("What is your third color?: ")
if first_color == second_color or first_color == third_color or second_color == third_color:
    print("these are the same colors!")
else:
    print("these are not the same colors!")