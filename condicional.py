#condicional el if ifel else
tipo = 'estudiante'

if tipo == 'estudiante':
    print('Tienes 50% de descuento')
elif tipo == 'profesor':
    print('Tienes 80% de descuento')
elif tipo == 'invitado':    
    print('Tienes 10% de descuento')
else:
    print('No tienes descuento')

usuario = 'romanlg'
tipoUsuario = 'admin'
tiposUsuarios = ['admin', 'superAdmin', 'usuario']

if tipoUsuario in tiposUsuarios and usuario == 'romanlg':
    print(f'puedes entrar {tipoUsuario}')
else:
    print('el usuario no puede entrar al sistema')


tipo = 'estudiante'

if tipo == 'estudiante':
    print('tienes acceso a la clase')
elif tipo == 'profesor':
    print('tienes acceso a modficar la clase')
elif tipo == 'invitado':    
    print('tienes acceso a ver la clase')
else:
    print('No tienes acceso a la clase')

verificarClave = '1234'

if verificarClave == '1234':
    print('clave correcta')
else:
    print('clave incorrecta')
