from claseVehiculo import Vehiculo, Turbo

class Deportivo(Vehiculo, Turbo):
    def __init__(self, marca="", modelo=""):
        super().__init__(marca, modelo)
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10
        print(f"El coche está acelerando. Velocidad actual: {self.velocidad} km/h")

    def frenar(self):
        if self.velocidad == 0:
            print("El coche está detenido")
        else:
            self.velocidad -= 10
            print(f"El coche está frenando. Velocidad actual: {self.velocidad} km/h")

    def activar_turbo(self):
        super().activar_turbo()
        self.velocidad += 50
        print(f"Velocidad actual con turbo: {self.velocidad} km/h")