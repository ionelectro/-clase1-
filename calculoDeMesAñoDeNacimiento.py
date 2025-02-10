# calculo de dia de la semana de nacimiento

# pedimos al usuario el dia ,mes y año de nacimiento
dia = int(input("Introduce el dia de nacimiento: "))
mes = int(input("Introduce el mes de nacimiento: "))
anyo = int(input("Introduce el año de nacimiento: "))
# si es enero o febrero se considera que es el mes 13 y 14
if mes == 1 or mes == 2:
    mes = mes + 12
    anyo = anyo - 1
# calculo el dia de la semana
k = anyo % 100
j = anyo // 100
# formula de Zeller
diaSemana = (dia + 13*(mes + 1)//5 + k + k//4 + j//4 + 5*j) % 7
# mostrar el dia de la semana
if diaSemana == 0:
    print("El dia de la semana es sabado")
elif diaSemana == 1:
    print("El dia de la semana es domingo")
elif diaSemana == 2:
    print("El dia de la semana es lunes")
elif diaSemana == 3:
    print("El dia de la semana es martes")
elif diaSemana == 4:
    print("El dia de la semana es miercoles")
elif diaSemana == 5:
    print("El dia de la semana es jueves")
elif diaSemana == 6:
    print("El dia de la semana es viernes")
else:
    print("Error en el calculo del dia de la semana")
    
print("Fin del programa")