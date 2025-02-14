from nicegui import ui
from claseFebrero import MesFebrero

# Crear una instancia de MesFebrero
febrero = MesFebrero()

# Función para mostrar la información del mes de febrero
def mostrar_informacion():
    ui.label(f"Mes: {febrero.nombre}")
    ui.label(f"Temperaturas máximas: {febrero.temperaturas_maximas}")
    ui.label(f"Temperaturas mínimas: {febrero.temperaturas_minimas}")
    ui.label(f"Media de temperaturas del mes: {febrero.calcular_media():.2f}°C")

# Interfaz de usuario con NiceGUI
with ui.column():
    ui.button('Mostrar Información de Febrero', on_click=mostrar_informacion)

ui.run()