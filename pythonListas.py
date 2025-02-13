# crear una lista

print("Crear una lista en Python")

ListaNumeros = [1, 2, 3, 6, 5, 3]
print("Numero 0: ", ListaNumeros[0])
print("Numero 1: ", ListaNumeros[1])

listaNombres = ["Juan", "Pedro", "Maria", "Ana", "Luis"]
print("Nombre 2: ", listaNombres[2])
print("Nombre 4: ", listaNombres[4])


# sort() - Ordena los elementos de la lista
print("Ordenar elementos de la lista")
ListaNumeros.sort()
print(ListaNumeros)

# reverse() - Invierte el orden de los elementos de la lista
print("Invertir elementos de la lista")
ListaNumeros.reverse()
print(ListaNumeros)


# Metodos de listas en Python
print("Metodos de listas en Python")

# append() - Añade un elemento al final de la lista
listaNombres.append("Carlos")
print(listaNombres)

# insert() - Añade un elemento en una posición específica
listaNombres.insert(2, "Jose")
print("Nombre 2: ", listaNombres[2])

# remove() - Elimina un elemento de la lista
listaNombres.remove("Ana")
print(listaNombres)

# pop() - Elimina un elemento de la lista por su posición
listaNombres.pop(3)
print(listaNombres)

# del  - Elimina un elemento de la lista por su posición desde el indice hasta el final
del listaNombres[1:2]
print(listaNombres)

# recorrer elementos de la lista y mostrar su posicion

for i in range (len(listaNombres)):
    print(f"Nombre {i}: {listaNombres[i]}")
    
# clear() - Elimina todos los elementos de la lista
# listaNombres.clear()
# print(listaNombres)
    
# in - Verificar si un elemento está en la lista
if "Carlos" in listaNombres:
    print("Carlos está en la lista")
else:
    print("Carlos no está en la lista")
    

