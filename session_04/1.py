import random
x = random.randint(1, 1000)
while True:
    number = int(input("what's your guess?"))
    if number > x :
        print("too high...try lower numbers")
    elif number < x :
        print("too low...try higher numbers")
    elif number == x:
        print("congratulations, you got it!")
        break