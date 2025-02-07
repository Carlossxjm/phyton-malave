#ejercicio2
pregunta = input('agrega un número y te dire si es impar\r\n')
pregunta += '\r\n escribre "cerrar" para salir de la app \r\n'
preguntar = False

while preguntar:
    numero = input("agrega un número y te dire si es impar\r\n")
    if numero == "cerrar":
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f'tu número {numero} es par')
        else:
            print(f'tu número {numero} es impar')
    except ValueError:
        print("debes agregar un número")
        

