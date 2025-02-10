# calculo de letra de dni

# pedir al usuario el dni
dni = int(input("Introduce el dni: "))

# calcular la letra del dni
# letra = "TRWAGMYFPDXBNJZSQVHLCKE"[dni % 23]

equivalencia_de_calculo_de_letra = {
    0: "T",
    1: "R",
    2: "W",
    3: "A",
    4: "G",
    5: "M",
    6: "Y",
    7: "F",
    8: "P",
    9: "D",
    10: "X",
    11: "B",
    12: "N",
    13: "J",
    14: "Z",
    15: "S",
    16: "Q",
    17: "V",
    18: "H",
    19: "L",
    20: "C",
    21: "K",
    22: "E"
}

# mostrar la letra del dni
# print(f"La letra del dni es: {letra}")
print(f"La letra del dni es: {equivalencia_de_calculo_de_letra[dni % 23]}")

print("Fin del programa")