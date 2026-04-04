#17. Pide al usuario dos números y muestra si al menos uno es mayor que 10 (usar operador lógico or).

number_1 = int(input("Enter an integer number: "))
number_2 = int(input("Enter another integer number: "))

print(f"Is at least one number greater than 10? {number_1 > 10 or number_2 > 10}")