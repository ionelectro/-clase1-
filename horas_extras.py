""" CALCULAR SALARIO DE TRABAJADORES
Pediremos a un usuario las horas trabajadas, precio hora y los kilómetros
El trabajador tendrá horas extra a partir de la hora 36
Cada hora extra será 2€ más
Solamente mostraremos mensajes
Si el trabajador hace menos de 100 km las dietas son LOCALES
Si el trabajador hace entre 101km y 500 km las dietas son PROVINCIALES
Si hace más km, serán NACIONALES
Si el precio final es menor a 250€ SIN RETENCIONES
Si es entre 251 y 600, 20% retención
Si es mayor 40 % retención

Número horas: 40
Horas extra: 4
Precio hora: 20
Salario base: 36 * 20
Salario Extra: 4 * 22 """

# pedir al usuario las horas trabajadas, precio hora y los kilometros
print("Introduce las horas trabajadas")
horas_trabajadas = int(input())
print("Introduce el precio por hora")
precio_hora = int(input())
print("Introduce los kilometros")
kilometros = int(input())
print("-------------------------")

# calcular el salario base
salario_base = precio_hora * 36

# calcular las horas extra
horas_extra = 0
salario_extra = 0
if horas_trabajadas > 36:
    horas_extra = horas_trabajadas - 36
    salario_extra = horas_extra * (precio_hora + 2)
    
# calcular las dietas
dietas = ""
if kilometros < 100:
    dietas = "LOCALES"
elif kilometros >= 101 and kilometros <= 500:
    dietas = "PROVINCIALES"
else:
    dietas = "NACIONALES"
    
# calcular el salario bruto
salario_bruto = salario_base + salario_extra

# calcular la retencion
retencion = 0
if salario_bruto < 250:
    retencion = 0
elif salario_bruto >= 251 and salario_bruto <= 600:
    retencion = 20
else:
    retencion = 40
    
# calcular el salario neto
salario_neto = salario_bruto - (salario_bruto * retencion / 100)

# mostrar los resultados
print(f"El salario base es: {salario_base}")
print("-------------------------")
print(f"El salario extra es: {salario_extra}")
print("-------------------------")
print(f"Las dietas son: {dietas}")
print("-------------------------")
print(f"El salario bruto es: {salario_bruto}")
print("-------------------------")
print(f"La retencion es: {retencion}")
print("-------------------------")
print(f"El salario neto es: {salario_neto}")
print("-------------------------")
print("Fin del programa")