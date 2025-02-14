from clasePersona import Persona

print("Prueba de la clase PersonaObjeto")

# creamos un objeto de la clase Persona
persona1 = Persona()
print(persona1.pais)
persona1.pais = "España"
print(persona1.pais)
persona1.nombre = "Juan"
persona1.apellidos = "Perez"
persona1.anyonacimiento = 1980
print(persona1.getNombreCompleto())
print(persona1.getEdad(2020))
print(persona1.pais)
print(persona1.nombre)
print(persona1.apellidos)
print(persona1.anyonacimiento)
print(persona1.descripcion)
print(persona1.edad)
print(persona1.nombreCompleto)
print(persona1) 
print(persona1.getDescripcion("es un buen amigo"))