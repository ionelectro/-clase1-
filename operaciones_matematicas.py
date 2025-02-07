# operadores matematicos
# suma + , resta - , multiplicacion * , division / , division entera // , modulo % , potencia **
# pedir tres valores al usuario

print("Operaciones matematicas")

# pedir tres valores al usuario

print("Ingrese la operacion a realizar")
print("Operaciones validas: suma: +, resta: -, multiplicacion: *, division: /, division entera: //, modulo: %, potencia: **")

operacion = input()

print("Ingrese el primer valor")

valor1 = int(input())

print("Ingrese el segundo valor")

valor2 = int(input())

print("Ingrese el tercer valor")

valor3 = int(input())

# realizar la operacion

if operacion == "+":
    resultado = valor1 + valor2 + valor3
elif operacion == "-":
    resultado = valor1 - valor2 - valor3
elif operacion == "*":
    resultado = valor1 * valor2 * valor3
elif operacion == "/":
    resultado = valor1 / valor2 / valor3
elif operacion == "//":
    resultado = valor1 // valor2 // valor3
elif operacion == "%":
    resultado = valor1 % valor2 % valor3
elif operacion == "**":
    resultado = valor1 ** valor2 ** valor3
else:
    resultado = "Operacion no valida"
    
print(f"El resultado de la operacion {operacion} es {resultado}")


