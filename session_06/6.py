sales= (
("Ali","Laptop",1200) ,
("Sara","phone",800) ,
("Ali","Phone",800) ,
("Reza","Laptop",1200) ,
("Sara","Laptop",1200) ,
("Ali","Mouse",50)
)
# مقدار خرید هر مشتری
customers = {}
for sale in sales:
    customer = sale[0]
    price = sale[2]
    if customer in customers:
        customers[customer] += price
    else:
        customers[customer] = price
for customer in customers:
    print(customer,"---> ",customers[customer])
# مشتری با بیشترین خرید
best_customer = ""
max_purchase = 0
for customer in customers:
    if customers[customer] > max_purchase:
        max_purchase = customers[customer]
        best_customer = customer
print("Best customer: ",best_customer)
# تعداد فروش هر محصول
products = {}
for sale in sales:
    product = sale[1]
    if product in products:
        products[product] += 1
    else:
        products[product] = 1
print("product sales: ")
for product in products:
    print(product,"--->",products[product])
# مجموع درامد فروشگاه
total = 0
for sale in sales:
    total += sale[2]
print("total sales: ",total)