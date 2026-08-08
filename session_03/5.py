function = input("choose(+,-,*,/): ")
x = int(input("enter first number: "))
y = int(input("enter second number: "))
if function == "+":
    print(x + y)
elif function == "-":
    print(x - y)
elif function == "*":
    print(x * y)
elif function == "/":
    print(x / y)