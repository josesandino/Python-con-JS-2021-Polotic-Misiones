#Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista. Luego recorrer la lista y mostrar los números por pantalla. 

f = int(input("Escribe un número: "))
g = int(input("Escribe un número: "))
h = int(input("Escribe un número: "))
i = int(input("Escribe un número: "))
j = int(input("Escribe un número: "))

numeros = [f, g, h, i, j]

for i in numeros:
    print(i)
print(numeros)