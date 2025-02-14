#iteradores corren un determinado numero de veces un pieza de codigo

meses = ["octubre", "febrero", "marzo"]

#ciclo for
for mes in meses:
    print(meses[1])
    print(f"estoy viajando por el mundo en el mes de {mes}")

    #imprimir numeros

for numero in range (0,25,5):
    print(numero)

usuarios = [{'usuario': 31583184, 'clave': '1234'}, {'usuario': 31583185, 'clave': '1235'}, {'usuario': 31583186, 'clave': '1236'}]
usuario_buscado = 31583184
def buscar_usuario(usuario_buscado):
    return usuario_buscado['usuario'] == usuario_buscado

resultado = list(filter(buscar_usuario, usuarios))
print(resultado)

for usuario in usuarios:
    if usuario['usuario'] == usuario_buscado:
        print(usuario)
        break