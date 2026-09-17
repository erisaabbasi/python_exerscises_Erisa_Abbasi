def process_order(customer, *products, discount = 0, tax = 0, shipping = 0, options):
    # قیمت فرضی است
    base_price = len(products) * 10000
    price_after_discount = base_price - (base_price * discount / 100)
    price_after_tax = price_after_discount + (price_after_discount * tax / 100)
    final_price = price_after_tax + shipping
    return {
        "customer": customer,
        "products": list(products),
        "discount": discount,
        "tax": tax,
        "shipping": shipping,
        "final_price": final_price,
    }


print(process_order(
    "Ali",
    "laptop","mouse","keyboard",
    discount= 10,
    tax = 9,
    shipping = 200000))