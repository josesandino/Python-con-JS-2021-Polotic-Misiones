#Escribe un programa Python que imprima “Hola Mundo”, si a es mayor que b.

a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))


if a > b:
    print("Hola Mundo")
elif a == b:
    print("A es igual a B")
else:
    print("A no es mayor a B")