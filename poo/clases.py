class Restaurant:
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"Agregando..{self.nombre}")
    def mostrar_informacion(self):
        print(f"El nombre del restaurante es: {self.nombre}")
    
class Carro:
    def agregar_carro(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        print(f"Carro: {self.marca} {self.modelo} {self.color}")


#Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurante("El pollo loco")
restaurant.mostrar_informacion()
print(f"El nombre del restaurante es: {restaurant.nombre}")

restaurant2 = Restaurant()
restaurant2.agregar_restaurante("Pizza hut")
restaurant2.mostrar_informacion()
print(f"El nombre del restaurante es: {restaurant2.nombre}")

