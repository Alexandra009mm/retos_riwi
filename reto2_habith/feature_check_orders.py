def check_orders (order_tuple):
    print(" REGISTERED ORDERS".center(60, "*"))

    for i in order_tuple:
        print("customer", i ["name"])
        print("product", i ["product"])
        print("quantity", i["quantity"])
        print("subtotal", i["subtotal"])
        print("-" * 40)