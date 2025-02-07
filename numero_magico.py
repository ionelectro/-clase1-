import math
import random

# pedimos al usuario dos numeros y le decimos cual es el mayor

print("Ingrese dos numeros para saber cual es mayor")

print("Ingrese el primer numero")
numero1 = int(input())

print("Ingrese el segundo numero")
numero2 = int(input())

if numero1 > numero2:
    print(f"El numero {numero1} es mayor que el numero {numero2}")
elif numero1 < numero2:
    print(f"El numero {numero2} es mayor que el numero {numero1}")
else:
    print(f"Los numeros {numero1} y {numero2} son iguales")