# vamos a realizar un program que nos permita comparar tres numeros
# pedimos los numeros al usuario

print("Introduce tres numeros y te dire cual es el mayor")
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
numero3 = int(input("Introduce el tercer numero: "))
# comparar los numeros
if numero1 > numero2 and numero1 > numero3:
    print(f"El numero mayor es: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero mayor es: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El numero mayor es: {numero3}")
else:
    print("Los numeros son iguales")

# tambien mostrar el numero menor
if numero1 < numero2 and numero1 < numero3:
    print(f"El numero menor es: {numero1}")
elif numero2 < numero1 and numero2 < numero3:
    print(f"El numero menor es: {numero2}")
elif numero3 < numero1 and numero3 < numero2:
    print(f"El numero menor es: {numero3}")
else:
    print("Los numeros son iguales")



# con la funcion max y min
print("Introduce tres numeros y te dire cual es el mayor")
numero4 = int(input("Introduce el primer numero: "))
numero5 = int(input("Introduce el segundo numero: "))
numero6 = int(input("Introduce el tercer numero: "))

# comparar los numeros
mayor = max(numero4, numero5, numero6)
menor = min(numero4, numero5, numero6)
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")

print("Fin del programa")

