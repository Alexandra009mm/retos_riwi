print("hello, welcome to the program! ")
print()

name = (input("what is your name?: ")).strip()
 
print()

print(f"ok {name}, It's a pleasure to meet you!")
print("Now we're going to do some operations")
print()
print("""---------MENU-----------
      
      1. Add.
      2. Subtract.
      3. Multiply.
      4. Divide.""")
   

option = int(input("What do you want to do?: "))
print()
num1 = int(input("enter the first number: "))
print()
num2 = int(input("enter ther second number: "))


if option == 1:
    resultado = num1 + num2
    print()
    print("-"*30)
    print(f"Ok,The result of your sum is: {resultado}")
    

elif option == 2:
    resultado = num1 - num2
    print()
    print("-"*30)
    print(f"Ok,The result of your sub is: {resultado}")

elif option == 3:
    resultado = num1 * num2
    print()
    print("-"*30)
    print(f"Ok,The result of your multiply is: {resultado}")

elif option == 4:
    resultado = num1 / num2
    print()
    print("-"*30)
    print(f"Ok,The result of your divition is: {resultado:.2f}")

print()
print("-"*30)
print(f"see you later {name}!")
    
