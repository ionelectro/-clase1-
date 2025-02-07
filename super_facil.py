import random
import math

# pedimos un numero al ususraio e indicamos si es positivo o negativo

print("Ingrese un numero para saber si es positivo o negativo")
numero = int(input())

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")