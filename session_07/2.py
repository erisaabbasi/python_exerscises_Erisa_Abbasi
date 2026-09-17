def process_order(customer,*products,**options):
    results = {"costomer":"","products":[],"discount":0,"tax":0,"shipping":0,"final_price":0}
    results["costomer"] = customer
    results["products"] = products
    results["discount"] = options.get("discount",0)
    results["shipping"] = options["shipping"]
    results["tax"] = options.get("tax",0)
    return results


print(process_order(
    "Ali",
    "laptop","mouse","keyboard",
    discount= 10,
    tax = 9,
    shipping = 200000))