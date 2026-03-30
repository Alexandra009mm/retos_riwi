def product_register(products_tuple):
    
    keep_register = "yes"
    while keep_register == "yes":

        product_ID = 0
        while product_ID <= 0 :
            try:
                product_ID = int(input("Enter an ID: "))   
            
                if product_ID <= 0:
                    print ("Error, the ID must be a positive integer")
            except ValueError:
                print("Error, the ID must be a numeric value")

#*-----------------------------------------------------------------------------
        product_name = ""
        while product_name == "" :

            product_name = input("Enter the product name: ")
            if product_name == "":
                print("Error, this field must be filled")
#---------------------------------------------------------------------------

        product_price = 0
        while product_price <= 0 :
            
            try:
                product_price = int(input("Enter product price: "))   

                if product_price <= 0:
                    print ("Error, the price must be a positive integer")

            except ValueError:
                print("Error, the price must be a numeric value")

        products_tuple += ((product_ID, product_name, product_price),)

        keep_register = input("Would you like to register another product? yes/no: ").lower()
    return products_tuple

    
