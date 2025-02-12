# debemos mostrar el menu con estas operaciones: suma, resta, multiplicacion, division, salir.
# tendremos tres funciones return para cada una de las opciones del menu.

print ("Programa calculadora con funciones de retorno")

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

def menu():
    print("Calculadora:")
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

print("-------------------------")

# Programa principal
menu()
print("-------------------------")

opcion = int(input("Introduce una opción: "))
if opcion >= 5:
    print("Fin del programa.")
else:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    
    if opcion == 1:
        resultado = suma(numero1, numero2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = resta(numero1, numero2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = multiplicacion(numero1, numero2)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4: 
        resultado = division(numero1, numero2)
        round(resultado, 2)
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Opción no válida.")
    print("Fin del programa.")