#arreglos o list en python
meses = ['octubre','febrero','marzo']
print(meses)

#ordena los elementos de la lista
meses.sort()
print(meses[0])#para imprimir la posicion en especifico
print(meses)

#obtener datos dentro de un arreglo
aprediendo =f'estamos en el mes de {meses[0]}'
print(aprediendo)

#reemplazar el valor de un arreglo
meses[2]= 'noviembre'
print(meses)

#agregar un valor a un arreglos
meses.append('julio')
print(meses)

#eliminar el valor de un arreglo
del meses[2]
print(meses)
