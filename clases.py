class Persona:
    nBrazos = 0
    nPiernas = 0
    cabello = True
    cCabello = "Defecto"
    hambre = 0

    def dormir(self):
        pass
    # self es como this in java
    def comer(self):
        self.hambre = 0

class Hombre:
    nombre = "Defecto"
    sexo = "M"

    def cambiarNombre(self, nombre):
        self.nombre = nombre;

class Mujer:
    nombre = "Defecto"
    sexo = "F"