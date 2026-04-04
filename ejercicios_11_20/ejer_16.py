#16. Pide al usuario dos números y muestra si ambos son mayores que 10 (usar operador lógico and).

number_1 = int(input("Enter an integer number: "))
number_2 = int(input("Enter another integer number: "))

print(f"Are both numbers greater than 10? {number_1 > 10 and number_2 > 10}")