from nicegui import ui
from mesesCompletos import MesEnero, MesFebrero, MesMarzo, MesAbril, MesMayo, MesJunio, MesJulio, MesAgosto, MesSeptiembre, MesOctubre, MesNoviembre, MesDiciembre

# Crear instancias de cada mes
meses = {
    "Enero": MesEnero(),
    "Febrero": MesFebrero(),
    "Marzo": MesMarzo(),
    "Abril": MesAbril(),
    "Mayo": MesMayo(),
    "Junio": MesJunio(),
    "Julio": MesJulio(),
    "Agosto": MesAgosto(),
    "Septiembre": MesSeptiembre(),
    "Octubre": MesOctubre(),
    "Noviembre": MesNoviembre(),
    "Diciembre": MesDiciembre()
}

# Función para mostrar la información del mes seleccionado
def mostrar_informacion():
    mes = mes_selector.value
    info = meses[mes].mostrar_informacion()
    info_label.set_text(info)

# Interfaz de usuario con NiceGUI
with ui.column():
    ui.label("Seleccione un mes para ver la información:")
    mes_selector = ui.select(options=list(meses.keys()), label="Mes")
    ui.button('Mostrar Información', on_click=mostrar_informacion)
    info_label = ui.label("")

ui.run()