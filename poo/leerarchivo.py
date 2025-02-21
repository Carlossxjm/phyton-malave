def App():
    archivo = open('poo/archivo.txt', 'r') # w: write, r: read, a: append
    #leer archivo
    for contenido in archivo:
        print(contenido.rstrip())
    archivo.close() # Cerrar el Archivo
App()