def App():
    archivo = open('poo/archivo.txt', 'w') # w: write, r: read, a: append
    #escribir en el archivo
    for i in range(0, 10):
        archivo.write(f"Esta es la Linea {i}\n")
    archivo.write("Aprediendo en python\n")
    archivo.close() # cerrar el archivo
App()


    # 'r':  Solo lectura (Modo por defecto)
    # 'w':  Solo Escritura (Sobreescribe el archivo existente)
    # 'a':  Añadir (Añade al final del archivo)
    # 'x':  Crear (Crea un nuevo archivo, si ya existe, lanza un error)
    # 'b':  Binario (Para abrir archivos binarios)
    # '+':  Leer y escribir
