price = int(input("price: "))
if price > 1000000:
    price = price * 75/100
elif 500000 < price < 1000000:
    price = price * 90/100
elif price < 500000:
    price = price
print(price)