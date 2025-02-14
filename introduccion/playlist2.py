playlist = {}

def crear_playlist():
    nombre_playlist = input('Ingrese el nombre de la playlist:\n')
    playlist[nombre_playlist] = []
    return nombre_playlist

def agregar_canciones(playlist_nombre):
    print('agregando canciones a la playlist:', playlist_nombre)
    while True:
        cancion = input('Ingrese el nombre de la cancion o "X" para salir:')
        if cancion.lower == 'x':
            break
        playlist[playlist_nombre].append(cancion)
        print('cancion agregada', cancion)

def eliminar_canciones(playlist_nombre):
    print('eliminando canciones de la playlist:',playlist_nombre)
    while True:
        cancion_eliminar = input('Ingrese el nombre de la cancion a eliminar o "X" para salir: ')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist[playlist_nombre]:
            playlist[playlist_nombre].remove(cancion_eliminar)
            print('cancion eliminada:', cancion_eliminar)
        else:
            print('La cancion no se encuentra en la playlist')
def mostrar_playlist():
    if not playlist:
        print("No hay playlist creadas")
    else:
        for nombre, canciones in playlist.items():
            print(f"Playlist: {nombre}")
            for cancion in canciones:
                print(f"- {cancion}")
def app():
    while True:
        print("\nMenu:")
        print("1. Crear una nueva Playlist")
        print("2. Agregar canciones a una playlist")
        print("3. Eliminar canciones de una playlist")
        print("4. Mostrar todas las playlist")
        print("5. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_canciones(nombre_playlist)
        elif opcion == '2':
            nombre_playlist = input("¿A que playlist desea agregar canciones?")
            if nombre_playlist in playlist:
                agregar_canciones(nombre_playlist)
            else:
                print("La playlist no existe")
        elif opcion == '3':
            nombre_playlist = input("¿De que playlist desea eliminar canciones?")
            if nombre_playlist in playlist:
                eliminar_canciones(nombre_playlist)
            else:
                print("La playlist no existe")
        elif opcion == '4':
            mostrar_playlist()
        elif opcion == '5':
            break
        else:
            print('Opcion invalida')
    
app()
