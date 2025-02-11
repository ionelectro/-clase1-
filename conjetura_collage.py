# Description: Programa que implementa la conjetura de Collatz

print("Conjetura de Collatz")

print("Introduce un número:")
numero = int(input())

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1
    print(numero)
print("Fin del programa.")
