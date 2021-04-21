class Perro:

    especie = "Canis lupus familiaris" #atributo clase

    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

    #def descripcion(self):
     #   return f"{self.nombre} tiene {self.edad} años"

    def ladrar(self, sonido):
        return f"{self.nombre} hace este sonido: {sonido}"

    # Describir la clase
    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    # Herencia

class DogoArgentino(Perro):
    raza = "Dogo Argentino"

class BullDogFrances(Perro):
    raza = "Bulldog Frances"