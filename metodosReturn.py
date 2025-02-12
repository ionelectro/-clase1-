# metodos return

def convertiraMayusculas(texto):
    return texto.upper()

def convertiraMinusculas(texto):
    return texto.lower()

def concatenar(texto1, texto2):
    resultado = texto1 + " " + texto2
    return resultado

# metodos de accion

def mostrarMenu():
    print("Selecciona una opción:")
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Concatenar textos")
    print("4. Salir")
    
# programa principal
print("Ejemplo de métodos con return en Python")
print("========================================")
print("introduce un texto:")
texto1 = input()
mostrarMenu()
opcion = int(input())

if opcion == 1:
    resultado = convertiraMayusculas(texto1)
    print(resultado)
elif opcion == 2:
    resultado = convertiraMinusculas(texto1)
    print(resultado)

elif opcion == 3:
    print("Introduce otro texto:")
    texto2 = input()
    resultado = concatenar(texto1, texto2)
    print(resultado)
else:
    opcion == 4
    
print("Fin del programa.")