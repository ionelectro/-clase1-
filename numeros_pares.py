print("Rango Pares")

print("Introduce el número de inicio:")
inicio = int(input())
print("Introduce el número final:")
final = int(input())

for i in range(inicio, final +1):
    if i % 2 == 0:
        print(f"El número {i} es par.")
    else:
        print(f"El número {i} es impar.")
print("Fin del programa.")