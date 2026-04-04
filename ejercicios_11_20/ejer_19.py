#19. Pide al usuario tres números, calcula el promedio y muestra el resultado.

number_1 = int(input("Enter an integer number: "))
number_2 = int(input("Enter another integer number: "))
number_3 = int(input("Enter another integer number: "))

s = number_1 + number_2 + number_3
r = s / 3

k = (number_1 + number_2 + number_3) / 3

print(f"The average is: {r}")
print(f"The average is: {k}")