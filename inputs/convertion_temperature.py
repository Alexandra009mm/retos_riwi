print("\n------Temperature ideal in fahrenheit-------")

name = input("enter your name: ")

welcome = f"hello {name}"
print(welcome)
age = int(input("please, enter your age to calculate your temperature ideal: "))
celcius = int(input("Enter the temperature in Celsius to convert it to Fahrenheit: "))

igualacion = celcius * 9/5 
fahrenheit = igualacion + 32

#---------------------------------------------------------------------------------------------------------------
if age <0:
    print("\n")
    print("-"*30)
    print("enter age valide")
#---------------------------------------------------------------------------------------------------------------
elif age >=0 and age <=2:

    if 97.9 <= fahrenheit < 100.4:
          print("\n")
          print("-"*30)
          print(f"""the result of convertion is: {fahrenheit}°F.{name}, According to the result, you have hypothermia.""")

    elif fahrenheit < 97.0:
        print("\n")
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, your temperature is normal""")

    else:
        print("\n")
        print("-"*30)
        print(f"""The result of conversion is: {fahrenheit}°F. {name}, your temperature is high, you have a fever.""")
#---------------------------------------------------------------------------------------------------------------
elif 2 > age <= 12:
    if 97.0 > fahrenheit <= 99.5:
        print("\n")
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, your temperature is normal""")

    elif fahrenheit <= 97.0:
        print()
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, According to the result, you have hypothermia.""")

    else:
        print("\n")
        print("-"*30)
        print(f"""The result of conversion is: {fahrenheit}°F. {name}, your temperature is high, you have a fever.""")
#---------------------------------------------------------------------------------------------------------------
elif 13>= age <= 64:

    if 97.0 >= fahrenheit  <= 99.5:
        print("\n")
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, your temperature is normal""")

    elif fahrenheit <= 96.0:
        print("\n")
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, According to the result, you have hypothermia.""")

    else:
        print("\n")
        print("-"*30)
        print(f"""The result of conversion is: {fahrenheit}°F. {name}, your temperature is high, you have a fever.""")
#---------------------------------------------------------------------------------------------------------------
else:
    if 96.0 <= fahrenheit <= 98.5:
        print()
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, your temperature is normal""")
    
    elif fahrenheit <= 96.0:
        print()
        print("-"*30)
        print(f"""the result of convertion is: {fahrenheit}°F.{name}, According to the result, you have hypothermia.""")

    elif fahrenheit >= 99.5:
        print()
        print("-"*30)
        print(f"""The result of conversion is: {fahrenheit}°F. {name}, your temperature is high, you have a fever.""")

