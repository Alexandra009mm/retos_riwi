from show_resummary import show_resummary

def add_product(items):

    keep_register = "yes"
    while keep_register:
        try:
            a = True
            while a:
                    product_name = input("enter the product name: ").strip()
                    if not product_name:
                        print("Try again, enter a name")
                        continue
                    else:
                        a = False
            
            b = True
            while b:
                try:
                    price = float(input("enter price: "))
                    if price <= 0:
                        print("enter a valid number")
                        continue
                    else:
                        b = False
                except ValueError:
                    print("enter a number...")

            c = True
            while c:
                try:    
                    quantity = int(input("enter quantity: "))
                    if quantity <= 0:
                       print("enter a quantity valid")
                       continue
                    else:
                        c = False
                except ValueError:
                    print("Try again. enter a quantity valid ")
            
                   
        except TypeError:
            print("Error, try again")

        subtotal = price * quantity

            
        sales ={
            "product name": product_name,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal
        }

        items.append(sales)

        keep_register = input("do you want ot add another sale? yes/no: ").lower().strip()

        if keep_register == "no":
            print("Okay, the summary of the day will be shown below => \n")
            keep_register = False
        else:
            continue

    show_resummary(items)





