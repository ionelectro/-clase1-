import random

def generar_ISBN():
    """
    Función que genera un número ISBN-10 válido.
    :return: str
    """
    # Generar los primeros 9 dígitos aleatorios
    isbn = [random.randint(0, 9) for _ in range(9)]
    
    # Calcular el dígito de control
    suma = sum((10 - i) * isbn[i] for i in range(9))
    digito_control = 11 - (suma % 11)
    
    if digito_control == 10:
        isbn.append('X')
    elif digito_control == 11:
        isbn.append(0)
    else:
        isbn.append(digito_control)
    
    # Convertir la lista de dígitos a una cadena
    return ''.join(map(str, isbn))

# Generar y mostrar un ISBN-10 válido
isbn_valido = generar_ISBN()
print(f"ISBN-10 generado: {isbn_valido}")