def order_creation(customer_dic, products_tuple, order_tuple):
    keep_register = "yes"
    while keep_register == "yes":
        
        # Mostrar lista de clientes disponibles
        for i in customer_dic.values():
            print("id", i["id"])
            print("name", i["name"])
        
        # Mostrar lista de productos disponibles
        for number, i in enumerate(products_tuple):
            print(number, i[0], i[1], i[2])

        # Buscar cliente por ID
        search_id = 0
        while search_id <= 0:
            try:
                search_id = int(input("Enter the customer id: "))
                if search_id <= 0:
                    print("Error, the ID must be a positive integer")
            except ValueError:
                print("Error, the ID must be a numeric value")
        
        selected_customer = None
        for i in customer_dic.values():
            if search_id == i["id"]:
                print("User selected")
                selected_customer = i
        if selected_customer is None:
            print("Error, the user doesn't exist")
            continue

        # Buscar producto por ID
        search_product = 0
        while search_product <= 0:
            try:
                search_product = int(input("Select a product by ID: "))
                if search_product <= 0:
                    print("Error, the ID must be a positive integer")
            except ValueError:
                print("Error, the ID must be a numeric value")

        selected_product = None
        for i in products_tuple:
            if search_product == i[0]:
                print("Product selected")
                selected_product = i
        if selected_product is None:
            print("Error, the product doesn't exist")
            continue

        # Cantidad y subtotal
        product_quantity = 0
        while product_quantity <= 0:
            try:
                product_quantity = int(input("Enter the product quantity: "))
                if product_quantity <= 0:
                    print("Error, quantity must be a positive integer")
            except ValueError:
                print("Error, the quantity must be a numeric value")

        subtotal = product_quantity * selected_product[2]

        order_dic = {
            "name": selected_customer["name"],
            "product": selected_product[1],
            "quantity": product_quantity,
            "subtotal": subtotal
        }

        order_tuple += (order_dic,)
        keep_register = input("Do you want to register another order? yes/no: ").lower()

    return order_tuple