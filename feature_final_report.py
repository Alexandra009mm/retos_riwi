def final_report(order_tuple):
    print("FINAL REPORT".center(60, "*"))
    
    # 1 - Total de pedidos
    print("Total orders:", len(order_tuple))
    
    # 2 - Total de ingresos
    total = 0
    for i in order_tuple:
        total += i["subtotal"]
    print("Total income: $", total)
    
    # 3 - Pedidos por cliente
    print("Orders by customer:".center(60, "-"))
    for i in order_tuple:
        print("Customer:", i["name"])
        print("Product:", i["product"])
        print("Quantity:", i["quantity"])
        print("Subtotal: $", i["subtotal"])
        print("-" * 40)
    
    # 4 - Productos vendidos
    print("Products sold:".center(60, "-"))
    for i in order_tuple:
        print("Product:", i["product"], "| Quantity:", i["quantity"])