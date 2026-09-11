inventory = {
    "appel" : 20,
    "banana" : 5,
    "orange" : 0,
    "milk": 12,
    "bread": 0
}
available = []
out_of_stock = []
for i in inventory:
    if inventory[i] > 0:
        available.append(i)
    else:
        out_of_stock.append(i)
print(f'''
Available items:
{available} ---> {len(available)}
Out of stock:
{out_of_stock} ---> {len(out_of_stock)}''')
