# mostrar la tabla de multiplicar ,segun numero introducido por el usuario

print("Tabla de Multiplicar segun número introducido por el usuario")

print("Introduce un número:")
numero = int(input())
print("------------------")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    print("------------------")
print("Fin del programa.")
