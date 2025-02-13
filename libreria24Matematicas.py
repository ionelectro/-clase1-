from nicegui import ui

# Funciones para las operaciones básicas
def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    if numero2 == 0:
        return "Error: División por cero"
    return numero1 / numero2

# Función para realizar operaciones
def realizar_operacion(operador, num1, num2):
    if operador == "+":
        return suma(num1, num2)
    elif operador == "-":
        return resta(num1, num2)
    elif operador == "*":
        return multiplicacion(num1, num2)
    elif operador == "/":
        return division(num1, num2)
    else:
        return "Operación no válida"