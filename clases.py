
class Persona:
    def __init__(self, nombre, edad, trabajo):
        self.nombre = nombre
        self.edad = edad
        self.trabajo = trabajo
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años, y mi trabajo es {self.trabajo}")


# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30, "fotografo")
persona2 = Persona("Paco", 20, "carpintero")


# Acceder a los atributos de la instancia
print(persona1.nombre)  # Output: Juan
print(persona1.edad)    # Output: 30

# Llamar a un método de la instancia
persona1.saludar()  # Output: Hola, mi nombre es Juan y tengo 30 años.
persona2.saludar()


area = 0

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def area(self):
        area = self.ancho * self.largo
        print(f"Area : {area} m2")
            
    def dartamaño(self):
        print(f"El tamaño rectangulo es : {self.largo} x {self.ancho}")

rectangulo1 = Rectangulo(20, 30)

rectangulo1.dartamaño()

rectangulo1.area()





