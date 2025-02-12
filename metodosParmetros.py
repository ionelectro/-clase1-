def saludar(nombre):
    print("Bienvenido a Python " + nombre)
    
    
def despedir(nombre,dia):
    print("Hasta mañana " + nombre + " que tengas un buen " + dia)
    
print("Metodos con parametros")
nombre = input("Introduce tu nombre: ")
dia = "miercoles"
saludar(nombre)
despedir(nombre,dia)
print("Fin del programa.")