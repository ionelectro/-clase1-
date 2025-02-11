# Comprobacion de un ISBN
""" print("Comprobación de un ISBN")

print("Introduce un ISBN:")
isbn = input()
suma = 0
for i in range(len(isbn)):
    if isbn[i].isdigit():
        suma += int(isbn[i]) * (i + 1)
if suma % 11 == 0:
    print("El ISBN es válido.")
else:
    print("El ISBN no es válido.")
    
print("Fin del programa.") """

""" En resumen, el programa solicita al usuario que introduzca un ISBN,
recorre cada carácter del ISBN, verifica si es un dígito y, si lo es, 
lo multiplica por su posición en la cadena y lo suma a una variable acumuladora. 
Luego, verifica si la suma es divisible por 11 para determinar si el ISBN es válido o no. """


# segunda forma incluye isbn de 13 digitos

def calcular_checksum_isbn10(isbn):
    """Calcula el checksum para un ISBN-10."""
    suma = 0
    for i, char in enumerate(isbn[:9]):
        if not char.isdigit():
            return -1  # Carácter no válido
        suma += int(char) * (i + 1)
    # Manejar el último carácter (puede ser 'X')
    ultimo_caracter = isbn[9]
    if ultimo_caracter == 'X':
        suma += 10
    elif not ultimo_caracter.isdigit():
        return -1  # Carácter no válido
    else:
        suma += int(ultimo_caracter)
    return suma


def calcular_checksum_isbn13(isbn):
    """Calcula el checksum para un ISBN-13."""
    suma = 0
    for i, char in enumerate(isbn):
        if not char.isdigit():
            return -1  # Carácter no válido
        factor = 1 if i % 2 == 0 else 3
        suma += int(char) * factor
    return suma


def es_isbn_valido(isbn):
    """Verifica si un ISBN es válido."""
    isbn = isbn.replace("-", "").replace(" ", "").upper()  # Eliminar guiones y espacios
    
    if len(isbn) == 10:  # ISBN-10
        checksum = calcular_checksum_isbn10(isbn)
        if checksum == -1:
            return False
        return checksum % 11 == 0
    elif len(isbn) == 13:  # ISBN-13
        checksum = calcular_checksum_isbn13(isbn)
        if checksum == -1:
            return False
        return checksum % 10 == 0
    else:
        return False


# Programa principal
print("Comprobación de un ISBN")
isbn = input("Introduce un ISBN (10 u 13 dígitos): ")

if es_isbn_valido(isbn):
    print("El ISBN es válido.")
else:
    print("El ISBN no es válido.")

print("Fin del programa.")

""" Explicación de las mejoras:
Funciones modulares :
calcular_checksum_isbn10: Calcula el checksum para un ISBN-10.
calcular_checksum_isbn13: Calcula el checksum para un ISBN-13.
es_isbn_valido: Verifica si el ISBN es válido llamando a las funciones anteriores según la longitud del ISBN.
 Validación de entrada :
Se eliminan guiones (-) y espacios en blanco automáticamente.
Se convierte todo a mayúsculas para manejar el caso especial del caracter "X" en los ISBN-10.
 Compatibilidad con ISBN-10 e ISBN-13 :
El programa ahora puede manejar tanto ISBN-10 como ISBN-13, dependiendo de la longitud de la entrada.
 Manejo de errores :
Si el ISBN contiene caracteres no válidos o no tiene la longitud correcta, el programa lo detectará y devolverá que no es válido.
 Claridad y legibilidad :
El código está dividido en funciones pequeñas y específicas, lo que facilita su lectura y mantenimiento.
 Con estas mejoras, el programa es más robusto, versátil y fácil de entender. """