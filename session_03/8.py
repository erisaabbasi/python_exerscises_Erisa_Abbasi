balance = int(input("How much balance do you have?: "))
withdrawl = int(input("How much do you want to withdraw?: "))
if withdrawl > 0 :
    if withdrawl <= balance :
        balance -= withdrawl
        print("done!current balance is:", balance)
    else:
        print("you don't have enough money!")
else:
    print("Error!Wrong number!")