print("Programa calculadora con funciones de retorno")

# Funciones para las operaciones básicas
def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    if numero2 == 0:
        return "Error: División por cero"
    return numero1 / numero2

# Función para mostrar el menú
def menu():
    print("\nCalculadora:")
    print("Selecciona una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

# Función para realizar operaciones
def realizar_operacion(operador, num1, num2):
    if operador == "+":
        return suma(num1, num2)
    elif operador == "-":
        return resta(num1, num2)
    elif operador == "*":
        return multiplicacion(num1, num2)
    elif operador == "/":
        return division(num1, num2)
    else:
        return "Operación no válida"

# Programa principal
while True:
    menu()
    opcion = input("Introduce una opción (1-5): ")

    if opcion == "5":
        print("Fin del programa.")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida. Inténtalo de nuevo.")
        continue

    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Entrada no válida. Debes introducir números.")
        continue

    # Realizar la primera operación según la opción seleccionada
    if opcion == "1":
        resultado = suma(numero1, numero2)
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = resta(numero1, numero2)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(numero1, numero2)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        resultado = division(numero1, numero2)
        if isinstance(resultado, str):  # Verificar si hubo un error
            print(resultado)
            continue
        print(f"El resultado de la división es: {round(resultado, 2)}")

    # Solicitar un tercer número y realizar otra operación
    try:
        numero3 = float(input("Introduce un tercer número: "))
        operacion = input("Introduce la operación a realizar (+, -, *, /): ")
    except ValueError:
        print("Entrada no válida. Debes introducir números.")
        continue

    nuevo_resultado = realizar_operacion(operacion, resultado, numero3)
    if isinstance(nuevo_resultado, str):  # Verificar si hubo un error
        print(nuevo_resultado)
    else:
        print(f"El resultado final es: {round(nuevo_resultado, 2)}")