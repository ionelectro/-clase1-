from math import floor, ceil, trunc

numero1 = 8
numero2 = 3

division = numero1 / numero2

print("....................................................")

print(f"Division: {division}")

print("....................................................")

# redondear hacia abajo
redondear_hacia_abajo = floor(division)
print(f"Redondear hacia abajo: {redondear_hacia_abajo}")

print("....................................................")

# redondear hacia arriba
redondear_hacia_arriba = ceil(division)
print(f"Redondear hacia arriba: {redondear_hacia_arriba}")

print("....................................................")

# truncar
truncar = trunc(division)
print(f"Truncar: {truncar}")

print("....................................................")

print("Fin del programa")