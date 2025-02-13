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

# Interfaz de usuario con NiceGUI
with ui.row():
    numero1_input = ui.input(label='Número 1').props('type=number')
    operador_input = ui.input(label='Operador').props('type=text')
    numero2_input = ui.input(label='Número 2').props('type=number')
    resultado_label = ui.label('Resultado: ').style("font-size: 130%;")

def calcular():
    try:
        numero1 = float(numero1_input.value)
        operador = operador_input.value
        numero2 = float(numero2_input.value)
        resultado = realizar_operacion(operador, numero1, numero2)
        resultado_label.set_text(f'Resultado: {resultado}')
    except ValueError:
        resultado_label.set_text('Entrada no válida. Debes introducir números.')

ui.button('Calcular', on_click=calcular)

ui.run()