class Rectangulo:

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):      
        return self.longitud*self.ancho

lado = float(input("Ingrese la longitud del rectangulo: "))
ancho = float(input("Ingrese el ancho del rectangulo: "))
r1 = Rectangulo(lado, ancho)
print("Area: ", r1.area())

        