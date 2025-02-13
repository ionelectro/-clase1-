print("Tuplas en Python")

# Las tuplas son secuencias inmutables de objetos, es decir, no se pueden modificar una vez creadas.
# Se definen mediante paréntesis y los elementos se separan por comas.
# Las tuplas pueden contener cualquier tipo de objeto, incluso otras tuplas.

# Crear una tupla
productos = ("Camiseta", 20.0, "Pantalón", 50.0, "Zapatos", 70.0)

# contando elementos de la tupla
numeroDeElementos = len(productos)
print(f"La tupla tiene {numeroDeElementos} elementos.")

# recorrer elementos de la tupla
for i in range(len(productos)):
    prod = productos[i]
    print(f"Producto {i}: {prod}")
    
# recorrer con enumerate 
# enumerate() devuelve una tupla con el índice y el elemento correspondiente
for i, prod in enumerate(productos):
    print(f"Producto {i}: {prod}")