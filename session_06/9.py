products = {
    "p01": ("Laptop",1200,5),
    "p02": ("Phone",800,0),
        "p03": ("Tablet",500,12),
    "p04": ("Mouse",50,25),
    "p05": ("Keyboard",100,0),
}
# محصولات موجود
print("Available products:")
for code in products:
    name = products[code][0]
    stock = products[code][2]
    if stock > 0:
        print(name)
# محصولات ناموجود
print("Unavailable products:")
for code in products:
    name = products[code][0]
    stock = products[code][2]
    if stock == 0:
        print(name)
# ارزش موجودی هر محصول
print("Inventory value:")
values = {}
for code in products:
    name = products[code][0]
    price = products[code][1]
    stock = products[code][2]
    value = price * stock
    values[name] = value
    print(name,"--->",value)
# محصول با بیشتزین ارزش موجودی
max_value = 0
best_product = ""
for name in values:
    if values[name] > max_value:
        max_value = values[name]
        best_product = name
print("highest inventory value: ",best_product,"value ---> ",max_value)
# ارزش کل انبار
total = 0
for name in values:
    total += values[name]
print("total value: ",total)