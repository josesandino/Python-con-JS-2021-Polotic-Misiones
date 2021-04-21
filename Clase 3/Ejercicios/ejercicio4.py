#Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]), iterarla y mostrar números divisibles por cinco, y si encuentra un número mayor que 150, detenga la iteración del bucle.

lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in lista1:
    if i > 150:
        break
    if i % 5 == 0:
        print(i)



