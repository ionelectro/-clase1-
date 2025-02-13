from nicegui import ui

# Diccionario de provincias
provincias = {
    "01": "Álava",
    "02": "Albacete",
    "03": "Alicante",
    "04": "Almería",
    "05": "Ávila",
    "06": "Badajoz",
    "07": "Baleares",
    "08": "Barcelona",
    "09": "Burgos",
    "10": "Cáceres",
    "11": "Cádiz",
    "12": "Castellón",
    "13": "Ciudad Real",
    "14": "Córdoba",
    "15": "La Coruña",
    "16": "Cuenca",
    "17": "Gerona",
    "18": "Granada",
    "19": "Guadalajara",
    "20": "Guipúzcoa",
    "21": "Huelva",
    "22": "Huesca",
    "23": "Jaén",
    "24": "León",
    "25": "Lérida",
    "26": "La Rioja",
    "27": "Lugo",
    "28": "Madrid",
    "29": "Málaga",
    "30": "Murcia",
    "31": "Navarra",
    "32": "Orense",
    "33": "Asturias",
    "34": "Palencia",
    "35": "Las Palmas",
    "36": "Pontevedra",
    "37": "Salamanca",
    "38": "Santa Cruz de Tenerife",
    "39": "Cantabria",
    "40": "Segovia",
    "41": "Sevilla",
    "42": "Soria",
    "43": "Tarragona",
    "44": "Teruel",
    "45": "Toledo",
    "46": "Valencia",
    "47": "Valladolid",
    "48": "Vizcaya",
    "49": "Zamora",
    "50": "Zaragoza",
    "51": "Ceuta",
    "52": "Melilla"
}

# Función para mostrar el diccionario
def mostrar_diccionario():
    with ui.column():
        for clave, valor in provincias.items():
            ui.label(f"Provincia {valor} con código {clave}")

# Función para recorrer solo las claves
def recorrer_claves():
    with ui.column():
        for clave in provincias.keys():
            ui.label(clave)

# Función para recorrer solo los valores
def recorrer_valores():
    with ui.column():
        for valor in provincias.values():
            ui.label(valor)

# Función para comprobar si una clave existe en el diccionario
def comprobar_clave():
    clave = clave_input.value
    if clave in provincias:
        ui.label(f"La clave {clave} existe en el diccionario")
    else:
        ui.label(f"La clave {clave} no existe en el diccionario")

# Función para borrar un elemento del diccionario
def borrar_elemento():
    clave = clave_input.value
    if clave in provincias:
        del provincias[clave]
        ui.label(f"Elemento con clave {clave} borrado")
    else:
        ui.label(f"La clave {clave} no existe en el diccionario")
    mostrar_diccionario()

# Función para insertar un elemento en el diccionario
def insertar_elemento():
    clave = clave_input.value
    valor = valor_input.value
    provincias[clave] = valor
    ui.label(f"Elemento con clave {clave} y valor {valor} insertado")
    mostrar_diccionario()

# Interfaz de usuario con NiceGUI
with ui.column():
    ui.button('Mostrar Diccionario', on_click=mostrar_diccionario)
    ui.button('Recorrer Claves', on_click=recorrer_claves)
    ui.button('Recorrer Valores', on_click=recorrer_valores)
    
    clave_input = ui.input(label='Clave').props('type=text')
    valor_input = ui.input(label='Valor').props('type=text')
    
    ui.button('Comprobar Clave', on_click=comprobar_clave)
    ui.button('Borrar Elemento', on_click=borrar_elemento)
    ui.button('Insertar Elemento', on_click=insertar_elemento)

ui.run()