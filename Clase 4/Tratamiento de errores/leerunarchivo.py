try:
    f = open("milog.txt","r")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
    f = open("milog.txt","r")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
finally:
    print("El try y except finalizo")