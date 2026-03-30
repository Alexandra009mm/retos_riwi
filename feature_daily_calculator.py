def daily_income(order_tuple):
    total = 0
    for i in order_tuple:
        total += i["subtotal"]
    print("Total daily income: $", total)