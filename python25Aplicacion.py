from nicegui import ui
import python25LibreriaValidacionISBNYDNI as lib

# Interfaz de usuario con NiceGUI para validar ISBN y DNI
with ui.row():
    isbn_input = ui.input(label='ISBN-10').props('type=text')
    isbn_result = ui.label('').style('font-size: 130%;')

with ui.row():
    dni_input = ui.input(label='DNI').props('type=number')
    dni_result = ui.label('').style('font-size: 130%;')

def validar_isbn():
    isbn = isbn_input.value
    if lib.validar_ISBN(isbn):
        isbn_result.set_text('ISBN válido')
    else:
        isbn_result.set_text('ISBN no válido')

def validar_dni():
    dni = dni_input.value
    letra_dni = lib.calcular_letra_DNI(int(dni))
    dni_result.set_text(f'Letra del DNI: {letra_dni}')

ui.button('Validar ISBN', on_click=validar_isbn)
ui.button('Validar DNI', on_click=validar_dni)

ui.run()