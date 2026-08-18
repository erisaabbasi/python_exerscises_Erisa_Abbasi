import random
choices = ["rock", "paper", "scissors"]
while True:
    computer = random.choice(choices)
    person = input("rock, paper, or scissors? (type Exit to quit): ")
    if person == "rock" and computer == "scissors" or person == "paper" and computer == "rock" or person == "scissors" and computer == "paper":
        print(f"You won! results --> computer:{computer} you:{person}")
    elif computer == "rock" and person == "scissors" or computer == "paper" and person == "rock" or computer == "scissors" and person == "paper":
        print(f"computer won! results --> computer:{computer} you:{person}")
    elif person == computer:
        print(f"equal! results --> computer:{computer} you:{person}")
    elif person == "Exit":
        break
    else:
        print("Sorry, that's not a valid option.")