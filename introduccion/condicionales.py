#operadores basicos
# == igual que
#!=: diferente de 
#<: menor que
#>: mayor que
#<=: menor igual que
#>=: mayor igual que

a = 5
b = 3
igual = a == b # igual es False
diferente = a != b # diferentes es True
mayor = a >= b # mayor es True

#condicional
ahorro = 500
if ahorro >=600:
    print("nos vamos de viaje")
else:
    print("no tenemos dinero")

#Revisamos si un valor es diferente en pyhon string
lenguaje = "python"
if not lenguaje == "python":
    print(f"super eres un crack de {lenguaje}")
else:
    print(f"no eres un crack de {lenguaje}")

#evaluacion boolean
usuario_autenticado = True
if usuario_autenticado:
    print("el usuario esta autenticado con exito")
else:
    print("el usuario no esta autenticado vuelve a intentarlo")

#codicionales con listas

superheroes = ["batman","superman","mujer maravilla" , "hercules"]
if "batman" in superheroes:
    print("batman es un superheroe")
else:
    print("tu superheroe no esta en la lista")

#condicionales anidados
acceso_usuario = True
acceso_admin = False

if acceso_usuario:
    print("acceso a la aplicacion")
    if acceso_admin:
        print("acceso total")
    else:
        print("el usuario no esta autenticado")