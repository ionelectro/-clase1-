import random

class MesEnero:
    def __init__(self):
        self.nombre = "Enero"
        self.temperaturas_maximas = [random.uniform(10, 25) for _ in range(31)]
        self.temperaturas_minimas = [random.uniform(-5, 10) for _ in range(31)]

    def calcular_media(self):
        media_maxima = sum(self.temperaturas_maximas) / len(self.temperaturas_maximas)
        media_minima = sum(self.temperaturas_minimas) / len(self.temperaturas_minimas)
        media_total = (media_maxima + media_minima) / 2
        return media_total

    def mostrar_informacion(self):
        print(f"Mes: {self.nombre}")
        print(f"Temperaturas máximas: {self.temperaturas_maximas}")
        print(f"Temperaturas mínimas: {self.temperaturas_minimas}")
        print(f"Media de temperaturas del mes: {self.calcular_media():.2f}°C")

# Ejemplo de uso
enero = MesEnero()
enero.mostrar_informacion()