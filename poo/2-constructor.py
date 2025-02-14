#constructor es una funcion que se ejecuta automaticamente al crear un objeto

class Restaurant:
    def __init__(self,nombre, categoria): #constructor
        print('yo me ejecuto automaticamente al crear un objeto')
        self.nombre = nombre
        self.categoria = categoria
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"Agregando restaurante..{self.nombre}")
    def mostrar_informacion(self):
        print(f"El nombre del restaurante es: {self.nombre} y su categoria es: {self.categoria}")

restaurante = Restaurant('El pollo loco', 'Comida rapida')
restaurante.mostrar_informacion()