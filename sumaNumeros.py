# pedir al usuario un texto numerico y sumar cada caracter y mostrar el resultado

print("Suma de los números de un texto numérico")

print("Introduce un texto numérico:")
texto = input()
suma = 0
for i in range(len(texto)):
    if texto[i].isdigit():
        suma += int(texto[i])
print(f"La suma de los números del texto es {suma}")
print("Fin del programa.")

# explicacion del programa
""" En resumen, el programa solicita al usuario que introduzca un texto numérico, 
recorre cada carácter del texto, verifica si es un dígito y, si lo es, lo suma a una variable acumuladora. 
Finalmente, imprime la suma de todos los dígitos encontrados en el texto. """


# tratamiento con try y except
print("Suma de los números de un texto numérico")

print("Introduce un texto numérico:")
texto2 = input()
suma2 = 0
for i in range(len(texto2)):
    try:
        suma2 += int(texto2[i])
    except ValueError as e:
        pass
print(f"La suma de los números del texto es {suma2}")
print("Fin del programa.")