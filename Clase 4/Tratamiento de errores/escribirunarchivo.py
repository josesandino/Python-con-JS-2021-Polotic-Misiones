try:
    f = open("miarchivo.txt","w")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
except:
    print("Algo malo paso al intentar abrir el archivo.")
finally:
    print("El try y except finalizo")