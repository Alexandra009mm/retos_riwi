from retos_riwi.inputs.inventoy.calculate_total import calculate_total as ctl

def show_resummary(items):
             
    print("\n------resummary-------\n")

    for i in items:
        print(i["product name"])
        print(i["price"])
        print(i["quantity"])
        print(i["subtotal"])


    total = ctl(items)
        
    print("\n")
    print("total:",total)

    


    