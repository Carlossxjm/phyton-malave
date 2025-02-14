#condicionales and y or
#and revisa que las dos condiciones sean verdaderas
#or revisa que al menos una de las condiciones sea verdadera
acceso_usario = True
acceso_admin = False
if acceso_usario and acceso_admin:
    print('acceso total')
elif acceso_usario:
    print('el usuario esta autenticado')
else:
    print('el usuario no  esta autenticado')