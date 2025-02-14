playlist = {}
playlist['canciones'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('como deseas nombrar tu playlist?\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    print ('agregando canciones a la playlist', playlist['nombre'])
    while True:
        cancion = input('ingresa el nombre de la cancion ( o "X" para salir): ')
        if cancion.lower() == 'x':
            break
        playlist['canciones'].append(cancion)
        print('cancion agregada:', cancion)
    print('¡Playlist creada!')
    print(playlist)

def eliminar_canciones():
    print('eliminando canciones de la playlist', playlist['nombre'])
    while True:
        cancion = input('ingresa el nombre de la cancion ( o "X" para salir): ')
        if cancion.lower() == 'x':
            break
        playlist['canciones'].remove(cancion)
        print('cancion eliminada:', cancion)
    print('¡Playlist actualizada!')
    print(playlist)
app()
