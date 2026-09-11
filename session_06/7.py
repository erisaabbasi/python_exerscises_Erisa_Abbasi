orders = [
    ("Ali","Laptop"),
    ("Sara","Phone"),
    ("Ali","Phone"),
    ("Reza","Laptop"),
    ("Sara","Laptop"),
    ("Ali","Tablet"),
    ("Reza","Phone"),
]
dictionary = {}
for customer,product in orders:
    if customer not in dictionary:
        dictionary[customer] = [product]
    else:
        dictionary[customer].append(product)
print(dictionary)