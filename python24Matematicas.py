from nicegui import ui
import libreria24Matematicas as mate


# Interfaz de usuario con NiceGUI
with ui.row():
    numero1_input = ui.input(label='Número 1').props('type=number')
    operador_input = ui.input(label='Operador').props('type=text')
    numero2_input = ui.input(label='Número 2').props('type=number')
    resultado_label = ui.label('Resultado: ').style("font-size: 130%;")
    
    
# llamadas a metodos de la libreria24Matematicas

def calcular():
    try:
        numero1 = float(numero1_input.value)
        operador = operador_input.value
        numero2 = float(numero2_input.value)
        resultado = mate.realizar_operacion(operador, numero1, numero2)
        resultado_label.set_text(f'Resultado: {resultado}')
    except ValueError:
        resultado_label.set_text('Entrada no válida. Debes introducir números.')
        
ui.button('Calcular', on_click=calcular)

ui.run()

""" En resumen, este código crea una calculadora simple utilizando nicegui para la interfaz gráfica y una biblioteca personalizada libreria24Matematicas para realizar las operaciones matemáticas. 
La interfaz permite al usuario introducir dos números y un operador, y muestra el resultado de la operación cuando se hace clic en el botón "Calcular". """