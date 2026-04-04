#18. Pide al usuario dos números y muestra si el primero NO es igual al segundo (usar operador lógico not combinado con comparación).

number_1 = int(input("Enter an integer number: "))
number_2 = int(input("Enter another integer number: "))

print(f"Is the first number NOT equal to the second? {not (number_1 == number_2)}")
print(f"Is the first number not equal to the second? {number_1 != number_2}")