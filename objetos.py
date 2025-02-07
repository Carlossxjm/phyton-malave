#objetos
#un objeto como ya sbemos es similar a un array, te permite agrupar contenido
#diferentes tipos de datos
#aqui se conocen como diccionarios

cancion = {
    'artista': 'ricado arjona',
    'nombre': 'el problema',
}

#acceder a los valores de un diccionario
print(cancion['artista'])
artista = cancion['artista']
print(artista)

#agregar un key al diccionario
cancion['playlist_id'] = 'romantica'   
print(cancion)

#eliminar un key del diccionario
del cancion['playlist_id']
print(cancion)

print("··   (ºº.)//    ··")

ciudad = {
    'nombre': 'maracay',
    'pais': 'venezuela',
    'estado': 'aragua'
}
print(ciudad['nombre'])
pais = ciudad['pais']
print(pais)

ciudad['urbanizacion'] = 'las acacias'
print(ciudad)

del ciudad['urbanizacion']
print(ciudad)