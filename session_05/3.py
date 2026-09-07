string = input("text: ")
letters = 0
upper = 0
lower = 0
digits = 0
spaces = 0
special = 0
for i in string:
    if i.isalpha():
        letters += 1
        if i.isupper():
            upper += 1
        else:
            lower += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        spaces += 1
    else:
        special += 1
print("letters:", letters)
print("upper:", upper)
print("lower:", lower)
print("digits:", digits)
print("spaces:", spaces)
print("special:", special)


