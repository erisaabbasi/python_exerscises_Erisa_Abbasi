distance = int(input("distance: "))
if distance < 2:
    payment = 20
else:
    x = (distance - 2) * 5
    payment = 20 + x
print(payment)

