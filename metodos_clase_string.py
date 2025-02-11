# metodos de clase string
# 1. mayusculas y minusculas

""" print("Mayúsculas y minúsculas")
print("Introduce una palabra:")
palabra = input()
print(f"En mayúsculas: {palabra.upper()}")
print(f"En minúsculas: {palabra.lower()}") """

# 2. contar caracteres
""" print("Contar caracteres")
print("Introduce una palabra:")
palabra2 = input()
print(f"La palabra tiene {len(palabra2)} caracteres.")
 """
# acceder a cada caracter de un texto mediante un metodo de clase string
""" print("Acceder a cada caracter de un texto")
print("Introduce una palabra:")
palabra3 = input()
for i in range(len(palabra3)):
    print(f"El caracter {i+1} es {palabra3[i]}") """
    
    
# metodo find
""" print("Método find")
print("Introduce una palabra:")
palabra4 = input()
print("Introduce una letra:")
letra = input()
print(f"La letra {letra} está en la posición {palabra4.find(letra)}") """

# metodo refind
""" print("Método rfind")
print("Introduce una palabra:")
palabra5 = input()
print("Introduce una letra:")
letra2 = input()
print(f"La letra {letra2} está en la posición {palabra5.rfind(letra2)}") """

# startwith
""" print("Método startswith")
print("Introduce una palabra:")
palabra6 = input()
print("Introduce una letra:")
letra3 = input()
print(f"La palabra {palabra6} empieza por {letra3}: {palabra6.startswith(letra3)}") """

# endswith
""" print("Método endswith")
print("Introduce una palabra:")
palabra7 = input()
print("Introduce una letra:")
letra4 = input()
print(f"La palabra {palabra7} termina por {letra4}: {palabra7.endswith(letra4)}") """


# replace
""" print("Método replace")
print("Introduce una palabra:")
palabra8 = input()
print("Introduce una letra:")
letra5 = input()
print("Introduce otra letra:")
letra6 = input()
print(f"La palabra {palabra8} reemplazando {letra5} por {letra6} es {palabra8.replace(letra5, letra6)}") """

# count
""" print("Método count")
print("Introduce una palabra:")
palabra9 = input()
print("contar cuantas veces se repite una letra:")
letra7 = input()
print(f"La letra {letra7} se repite {palabra9.count(letra7)} veces") """

# slicing
""" print("Método slicing")
print("Introduce una palabra:")
palabra10 = input()
print("Introduce el inicio:")
inicio = int(input())
print("Introduce el final:")
final = int(input())
print(f"La palabra {palabra10} desde {inicio} hasta {final} es {palabra10[inicio:final]}") """

texto = "Primer programa en Python"
print(texto)
print(texto.upper())
print(texto.lower())
print(len(texto))
print(texto[0])
print(texto.find("P"))
print(texto.find("Z"))
print("find sobrecargado")
print(texto.find("P", 1))
print(texto.rfind("P"))
print("rfind sobrecargado")
print(texto.rfind("p", 1))
print(texto.startswith("P"))
print(texto.endswith("n"))
print(texto.replace("P", "p"))
print(texto.count("P"))
print(texto[0:6])


# metodos de contenido is
""" print("Métodos de contenido")
print("Introduce una palabra:")
palabra11 = input()
print(palabra11.isalnum())
print(palabra11.isalpha())
print(palabra11.isdigit())
print(palabra11.islower())
print(palabra11.isupper())
print(palabra11.isspace())
print(palabra11.istitle()) """

# metodo slicing
""" print("Método slicing")
print("Introduce una palabra:")
palabra12 = input()
print("Introduce el inicio:")
inicio = int(input())
print("Introduce el final:")
final = int(input())
print(f"La palabra {palabra12} desde {inicio} hasta {final} es {palabra12[inicio:final]}") """


# recuperar una subcadena
subtexto = texto[0:6]
print("texto [0:6] = ", subtexto)

# bucle con rango indicando posicion
longitud = len(texto)
for i in range(longitud):
    print(f"El caracter {i+1} es {texto[i]}")
    
# comprobar que el usuario ha introducido un número y si es negativo
print("Introduce un número:")
numero = input()
if numero.isdigit():
    numero = int(numero)
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número es positivo.")
else:
    print("No has introducido un número.")