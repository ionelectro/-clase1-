from nicegui import ui
from claseMesEnero import MesEnero

# Crear una instancia de MesEnero
enero = MesEnero()

# Función para mostrar la información del mes de enero
def mostrar_informacion():
    ui.label(f"Mes: {enero.nombre}")
    ui.label(f"Temperaturas máximas: {enero.temperaturas_maximas}")
    ui.label(f"Temperaturas mínimas: {enero.temperaturas_minimas}")
    ui.label(f"Media de temperaturas del mes: {enero.calcular_media():.2f}°C")

# Interfaz de usuario con NiceGUI
with ui.column():
    ui.button('Mostrar Información de Enero', on_click=mostrar_informacion)

ui.run()