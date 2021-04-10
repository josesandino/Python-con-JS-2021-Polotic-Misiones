#Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuantas veces aparece la letra A (mayuscula y minúscula)

cadena = input("Escribe una frase: ")
cadena = cadena.upper()

longCad = len(cadena)
letraA = cadena.count("A")
tildeA = cadena.count("Á")

print ("El tamaño de la cadena es: ", longCad)
print ("En la cadena hay ", letraA, " letras a.")
print ("Hay ", letraA+tildeA, "letras a en total.")