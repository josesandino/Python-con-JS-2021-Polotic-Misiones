#Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área. 

import math

radio = float(input("Introduzca el valor del radio: "))

if radio < 0 :
    print("El valor del radio es incorrecto")
else:
    area = math.pi * radio ** 2
    print("El area del circulo es: ", round(area, 2))    