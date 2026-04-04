def customer_register (customer_dic):
    keep_register = "yes"
    while keep_register == "yes":

        customer_ID = 0
        while customer_ID <= 0 :
                     
            try:
                customer_ID = int(input("Enter an ID: "))   

                if customer_ID <= 0:
                    print ("Error, the ID must be a positive integer")
            except ValueError:
                print("Error, the ID must be a numeric value")

        customer_name = ""
        while customer_name == "" :

            customer_name = input("Enter the customer name: ")
            if customer_name == "":
                print("Error, this field must be filled")

        customer_email = ""
        while customer_email == "":

            customer_email = input("Enter the customer e-mail: ")
            if customer_email == "":
                print("Error, this field must be filled")


        customer_dic[customer_ID] = {
        "id" : customer_ID,
        "name": customer_name,
        "email": customer_email
        }


        keep_register = input("Do you want to register another customer? yes/no ").lower()
        

























