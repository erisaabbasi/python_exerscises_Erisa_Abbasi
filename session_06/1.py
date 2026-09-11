products = {
"laptop" : 1200,
"phone" : 800,
"tablet" : 500,
"headphone" : 150,
"mouse" : 50
}
prices = []
for i in products:
    prices.append(products[i])
print("cheapest ---> ",min(prices))
print("the most expensive ---> ",max(prices))
print("average ---> ",sum(prices) / len(prices))
over_500 = []
for price in prices:
    if price > 500:
        over_500.append(price)
print("over 500 ---> ",over_500)
print("aggregate ---> ",sum(prices))