card = input("card_number: ")
x = card[0:5]
if x == "6037":
    print("this is for bank A")
elif x == "8090":
    print("this is for bank B")
else:
    print("invalid card number")