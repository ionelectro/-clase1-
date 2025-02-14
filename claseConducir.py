from claseDeportivo import Deportivo

print("Conduciendo mi coche deportivo")
car = Deportivo(marca="Ferrari", modelo="488")
opcion = -1


while opcion != 0:
    print("------------------")
    print("0.- Salir")
    print("1.- Arrancar")
    print("2.- Acelerar")
    print("3.- Frenar")
    print("4.- Activar turbo")
    print("Seleccione una opción")
    try:
        opcion = int(input())
    except ValueError:
        print("Por favor, introduzca un número válido.")
        continue

    if opcion == 1:
        car.arrancar()
    elif opcion == 2:
        car.acelerar()
    elif opcion == 3:
        car.frenar()
    elif opcion == 4:
        car.activar_turbo()
    elif opcion == 0:
        print("Saliendo del programa")
    else:
        print("Opción incorrecta")


print("Fin de programa")