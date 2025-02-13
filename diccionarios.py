# diccionarios esta compuesto por una clave y un valor,son mutables y se definen mediante llaves.

provincias =  dict()

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

for clave, valor in provincias.items():
    print(f"Provincia {valor} con código {clave}")
    
    
# solo recorrer las claves
print("Recorrer solo las claves")
for clave in provincias.keys():
    print(clave)
    
# solo recorrer los valores
print("Recorrer solo los valores")
for valor in provincias.values():
    print(valor)
    
    
# comprobar si una clave existe en el diccionario
if "28" in provincias:
    print("La clave 28 existe en el diccionario")
else:
    print("La clave 28 no existe en el diccionario")
    
# borrado de un elemento del diccionario
print("Borrado de un elemento del diccionario")
del provincias["52"]
for clave, valor in provincias.items():
    print(f"Provincia {valor} con código {clave}")
    
# inertar un elemento en el diccionario
print("Insertar un elemento en el diccionario")
provincias["52"] = "Melilla"
for clave, valor in provincias.items():
    print(f"Provincia {valor} con código {clave}")