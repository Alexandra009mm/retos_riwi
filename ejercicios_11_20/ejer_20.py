#20. Pide al usuario un número entero y muestra si el número es divisible entre 5 (usar operador de módulo % y comparación).

number = int(input("Enter an integer number: "))

div = number % 5

print(f"Is it divisible by 5? {div == 0}")
print(f"Is it divisible by 5? {(number % 5) == 0}")