""" Validar Email ,si esta mal y su razon 
sin bucles ,todo con metodos
-que el email contenga arroba y punto
-que el email no tenga arroba ni al principio ni al final
-que el email no tenga punto al principio ni al final
-que el email solo tenga un punto despues del arroba 
-el dominio debe ser de 2 a 3 caracteres
-que el email solo tenga un arroba  """

def contiene_un_arroba(email):
    """Verifica que el email contenga exactamente un arroba."""
    return email.count("@") == 1

def contiene_un_punto(email):
    """Verifica que el email contenga al menos un punto."""
    return email.count(".") >= 1

def arroba_no_al_extremo(email):
    """Verifica que el arroba no esté al principio ni al final."""
    return not email.startswith("@") and not email.endswith("@")

def punto_no_al_extremo(email):
    """Verifica que el punto no esté al principio ni al final."""
    return not email.startswith(".") and not email.endswith(".")

def punto_despues_de_arroba(email):
    """Verifica que el punto esté después del arroba."""
    indice_arroba = email.find("@")
    indice_punto = email.rfind(".")
    return indice_arroba != -1 and indice_punto != -1 and indice_punto > indice_arroba

def dominio_valido(email):
    """Verifica que el dominio tenga entre 2 y 3 caracteres."""
    dominio = email.split(".")[-1]
    return 2 <= len(dominio) <= 3

def validar_email(email):
    """Valida el email según todas las reglas."""
    if not contiene_un_arroba(email):
        return "El email debe contener exactamente un arroba (@)."
    if not contiene_un_punto(email):
        return "El email debe contener al menos un punto (.)."
    if not arroba_no_al_extremo(email):
        return "El email no puede empezar ni terminar con '@'."
    if not punto_no_al_extremo(email):
        return "El email no puede empezar ni terminar con '.'."
    if not punto_despues_de_arroba(email):
        return "El punto debe estar después del arroba (@)."
    if not dominio_valido(email):
        return "El dominio debe tener entre 2 y 3 caracteres."
    return "El email es válido."

# Programa principal
print("Validación de email")
email = input("Introduce tu email: ")

resultado = validar_email(email)
print(resultado)
print("Fin del programa.")



""" Funciones Modulares :
Cada regla de validación se encapsula en una función independiente (contiene_un_arroba, contiene_un_punto, etc.). Esto hace que el código sea más fácil de leer, depurar y extender.
La función validar_email actúa como el punto central que llama a todas las funciones de validación.
 Mensajes de Error Más Detallados :
Cada función devuelve un mensaje específico sobre qué está mal en el email, lo que facilita la identificación del problema.
 Reutilización de Métodos :
Se utilizan métodos como str.count, str.startswith, str.endswith, str.find, str.rfind y str.split de manera eficiente para realizar las validaciones.
 Validación del Dominio :
La función dominio_valido verifica que el dominio tenga entre 2 y 3 caracteres, incluso si hay múltiples puntos en el email (por ejemplo, usuario@ejemplo.co.uk).
 Código Más Legible :
Al dividir el código en funciones pequeñas y específicas, se mejora significativamente la claridad y el mantenimiento. """