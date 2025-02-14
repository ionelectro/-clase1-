class Vehiculo:
    def __init__(self, marca="", modelo=""):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"{self.marca} {self.modelo} ha arrancado.")
        
    def acelerar(self):
        print(f"{self.marca} {self.modelo} ha acelerado.")
        
    def getVelocidadMaxima(self):
        print("Velocidad máxima: 140 km/h")
        return 140

class Turbo:
    def activar_turbo(self):
        print("¡Turbo activado!")