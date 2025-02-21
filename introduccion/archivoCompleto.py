import os

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Este es el contenido inicial del archivo.\n")
        print(f"archivo {nombre_archivo} creado exitosamente")

def leer_archivos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read() # Leer todo el contenido
            print(contenido) # Imprimir el contenido del archivo creado arriba
    except FileNotFoundError:
        print(f"el archivo {nombre_archivo} no existe.") # error si no existe el archivo

def agregar_linea(nombre_archivo, nueva_linea):
    with open(nombre_archivo, 'a') as archivo: # Esto les permirte y cerrar el archivo
        archivo.write(nueva_linea + '\n')
        print("Linea Agregada al archivo")

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f"archivo {nombre_archivo} eliminando")    
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

# Ejemplo de uso:
nombre_archivo = "poo/mi_archivo.txt"
crear_archivo(nombre_archivo)
leer_archivos(nombre_archivo)
agregar_linea(nombre_archivo, "ola")
# eliminar_archivo(nombre_archivo) # Descomenta esta linea para eliminar el archivo