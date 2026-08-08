string = input("enter a string: ")
x = len(string)
if x % 2 == 0:
    y = x // 2
    print(string[:y])
elif x % 2 != 0:
    y = x // 2
    print(string[y:])