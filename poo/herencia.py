# Herencia
# Se puede crear el hijo o una copia de otra, al heredar una clase
# Tendras todos los atributos y metodos de la clase padre
# Y podras agregar nuevos atributos y metodos

class Restaurante:

     def __init__(self, nombre, categoria, precio):
        print('yo me ejecuto automaticamente cuando creas un objeto de esta clase')
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
     def agregar_restauramte(self, nombre):
         self.nombre = nombre
         print(f"Se ha agregado un restaurante {self.nombre}.")
     
     def mostrar_informacion(self):
         print(f"El nombre del Establecimiento es: {self.nombre} y es de la categoria: {self.categoria}.")

# Instanciar la clase
restaurante = Restaurante("Pizza hut", "Comida rapida", 50)
restaurante.mostrar_informacion()

# Herencia
class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, numero_habitaciones):
        super().__init__(nombre, categoria, precio) # super() es una referencia a la clase padre
        self.numero_habitaciones = numero_habitaciones

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de habitaciones: {self.numero_habitaciones}")

# Instanciar la clase Restaurante
restaurante = Restaurante("Pizza hut", "Comida rapida", 50)
restaurante.mostrar_informacion()


# Instanciar la clase Hotel
hotel = Hotel("Hotel POO", "5 BITS", 200, 30)
hotel.mostrar_informacion()
hotel2 = Hotel("Hotel Pipol", "4 Estrellas", 200, 100)
hotel2.mostrar_informacion()

class Clinica:
    def __init__(self, nombre2, categoria2, precio2):
        self.nombre2 = nombre2
        self.categoria2 = categoria2
        self.precio2 = precio2

    def agregar_clinica(self, nombre2):
         self.nombre2 = nombre2
         print(f"Se ha agregado una Clinica {self.nombre2}.")
     
    def mostrar_informacion(self):
         print(f"El nombre de la Clinica es: {self.nombre2} y es de la categoria: {self.categoria2}.")

class clinica(Clinica):
    def __init__(self, nombre2, categoria2, precio2, numero_habitaciones2):
        super().__init__(nombre2, categoria2, precio2) # super() es una referencia a la clase padre
        self.numero_habitaciones2 = numero_habitaciones2

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de habitaciones: {self.numero_habitaciones2}")

# instanciar la clinica
clinica = Clinica("Clinica Calicanto", "3 Estrellas", 200)
clinica.mostrar_informacion()

class Medicos:
    def __init__(self, nombre3, categoria3, precio3):
        self.nombre3 = nombre3
        self.categoria3 = categoria3
        self.precio3 = precio3

    def agregar_medico(self, nombre3):
         self.nombre3 = nombre3
         print(f"Se ha agregado un medico {self.nombre3}.")
     
    def mostrar_informacion(self):
         print(f"El nombre del Medico es: {self.nombre3} y es de la Especialidad: {self.categoria3}.")

class medicos(Medicos):
    def __init__(self, nombre3, categoria3, precio3, numero_habitaciones3):
        super().__init__(nombre3, categoria3, precio3) # super() es una referencia a la clase padre
        self.numero_habitaciones3 = numero_habitaciones3

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de habitaciones: {self.numero_habitaciones3}")

# instaciar la clase medicos
medicos = Medicos("Jonathan", "Medico Cirujano", 200)
medicos.mostrar_informacion()