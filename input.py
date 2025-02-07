nombre = input('¿Cuál es tu nombre?\r\n')
print(f'Hola como estas, {nombre}!')
#leer los datos cuando sean numeros podemos hacer un if
#nota las entradas de datos siempre vienen en string
edad = input('¿Cuál es tu edad?\r\n')
try:
    if int(edad) >= 18:
        print(f'Eres mayor de edad, puedes votar')
    elif int(edad) <= 0:
        print(f'ingresa un numero valido para la edad')
    else:
        print(f'Lo sentimos aun eres un bebe')
except  ValueError:
    print('Por favor, ingresa un número valido para la edad')

