#Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + nn + nnn

num = int(input("Introduzca un numero entero: "))
result = num + num ** 2 + num ** 3
print ("El resultado de la operación es : ", result)