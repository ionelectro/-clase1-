# metodos para comprobar la validez de un ISBN y un DNI
# el ISBN devolvera True si es correcto y False si no lo es
# el DNI devolvera una letra
# estas funciones se pueden usar en cualquier programa que necesite validar un ISBN o un DNI



# Método para comprobar la validez de un ISBN-10
def validar_ISBN(isbn):
    """
    Verifica si un ISBN-10 es válido.
    :param isbn: str
    :return: bool
    """
    if len(isbn) != 10:
        return False
    
    suma = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        suma += int(isbn[i]) * (10 - i)
    
    if isbn[9] == 'X':
        suma += 10
    elif isbn[9].isdigit():
        suma += int(isbn[9])
    else:
        return False
    
    return suma % 11 == 0

# Método para calcular la letra del DNI
def calcular_letra_DNI(dni):
    """
    Calcula la letra correspondiente a un número de DNI.
    :param dni: int
    :return: str
    """
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[dni % 23]

# Ejemplos de uso
if __name__ == "__main__":
    # Validar ISBN
    isbn = "0471958697"
    if validar_ISBN(isbn):
        print(f"El ISBN {isbn} es válido.")
    else:
        print(f"El ISBN {isbn} no es válido.")
    
    # Calcular letra del DNI
    dni = 12345678
    letra = calcular_letra_DNI(dni)
    print(f"La letra del DNI {dni} es {letra}.")
 