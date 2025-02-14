directorio = {}

def negocios():
    nombre_negocio = input('Ingrese el nombre del negocio: ')
    directorio[nombre_negocio] = []
    return nombre_negocio

def agregar_negocios(negocio_nombre):
    print('agregaando negocios al directorio:', negocio_nombre)
    while True:
        negocio = input('Ingrese el nombre del negocio o "X" para salir: ')
        if negocio.lower() == 'x':
            break
        directorio[negocio_nombre].append(negocio)
        print('negocio agregado:', negocio)

def eliminar_negocios(nombre_negocio):
    print('eliminando negocios del directorio:', nombre_negocio)
    while True:
        negocios_eliminar = input('Ingrese el nombre del negocio a eliminar o "X" para salir: ')
        if negocios_eliminar.lower() == 'x':
            break
        if negocios_eliminar in directorio[nombre_negocio]:
            directorio[nombre_negocio].remove(negocios_eliminar)
            print('negocio eliminado:', negocios_eliminar)
        else:
            print('El negocio no se encuentra en el directorio')

def mostrar_directorio():
    if not directorio:
        print('No hay negocios creados')
    else:
        for nombre, negocios in directorio.items():
            print(f"Negocio: {nombre}")
            for negocio in negocios:
                print(f"- {negocio}")

def app():
    while True:
        print('\nMenu:')
        print('1. Crear un nuevo Directorio')
        print('2. Agregar negocios al directorio')
        print('3. Eliminar negocios del directorio')
        print('4. Mostrar todos los negocios')
        print('5. Salir')

        opcion = input('Ingrese una opcion: ')

        if opcion == '1':
            nombre_negocio = negocios()
            agregar_negocios(nombre_negocio)
        elif opcion == '2':
            nombre_negocio = input('¿A que directorio desea agregar negocios? ')
            if nombre_negocio in directorio:
                agregar_negocios(nombre_negocio)
            else:
                print('El directorio no existe')
        elif opcion == '3':
            nombre_negocio = input('¿De que directorio desea eliminar negocios? ')
            if nombre_negocio in directorio:
                eliminar_negocios(nombre_negocio)
            else:
                print('El directorio no existe')
        elif opcion == '4':
            mostrar_directorio()
        elif opcion == '5':
            break
        else:
            print('Opcion no valida')

app()

        




