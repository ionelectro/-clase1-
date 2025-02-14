

class Persona :
    nombre = ""
    apellidos = ""
    email = ""
    anyonacimiento = 0
    pais = ""
    descripcion = dict()
    
    def __init__(self):
        self.pais = "Francia"
    
    def getNombreCompleto(self):
        self.nombreCompleto = self.nombre + " " + self.apellidos
        return self.nombreCompleto
        
        
    def getEdad(self, anyoactual):
        self.edad = anyoactual - self.anyonacimiento
        return self.edad
    
    def __str__(self):
        return self.apellidos + ", " + self.nombre + ", " + self.pais
    
    def getDescripcion(self,description):
        return self.nombreCompleto + " " + description