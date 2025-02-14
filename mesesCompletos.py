
import random

class Mes:
    def __init__(self, nombre, dias):
        self.nombre = nombre
        self.dias = dias
        self.temperaturas_maximas = [random.randint(10, 25) for _ in range(dias)]
        self.temperaturas_minimas = [random.randint(-5, 10) for _ in range(dias)]

    def calcular_media(self):
        media_maxima = sum(self.temperaturas_maximas) / len(self.temperaturas_maximas)
        media_minima = sum(self.temperaturas_minimas) / len(self.temperaturas_minimas)
        media_total = (media_maxima + media_minima) / 2
        return media_total

    def mostrar_informacion(self):
        return (f"Mes: {self.nombre}\n"
                f"Temperaturas máximas: {self.temperaturas_maximas}\n"
                f"Temperaturas mínimas: {self.temperaturas_minimas}\n"
                f"Media de temperaturas del mes: {self.calcular_media():.2f}°C")

class MesEnero(Mes):
    def __init__(self):
        super().__init__("Enero", 31)

class MesFebrero(Mes):
    def __init__(self):
        super().__init__("Febrero", 28)

class MesMarzo(Mes):
    def __init__(self):
        super().__init__("Marzo", 31)

class MesAbril(Mes):
    def __init__(self):
        super().__init__("Abril", 30)

class MesMayo(Mes):
    def __init__(self):
        super().__init__("Mayo", 31)

class MesJunio(Mes):
    def __init__(self):
        super().__init__("Junio", 30)

class MesJulio(Mes):
    def __init__(self):
        super().__init__("Julio", 31)

class MesAgosto(Mes):
    def __init__(self):
        super().__init__("Agosto", 31)

class MesSeptiembre(Mes):
    def __init__(self):
        super().__init__("Septiembre", 30)

class MesOctubre(Mes):
    def __init__(self):
        super().__init__("Octubre", 31)

class MesNoviembre(Mes):
    def __init__(self):
        super().__init__("Noviembre", 30)

class MesDiciembre(Mes):
    def __init__(self):
        super().__init__("Diciembre", 31)