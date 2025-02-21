class Carro:
    def __init__(self, marca, modelo, color):
        self.__marca = marca # _ significa que es protegido
        self.__modelo = modelo # __ significa que es privado
        self.color = color # no tiene nada, es publico
        self.encendido = False
    
#gatters y setters son metodos que nos permiten acceder a los atributos de una clase

    def get_marca(self):
        print(self.__marca)

    def set_marca(self, marca): # se utiliza para modificar el valor de un atributo
        self.__marca = marca

    def encender(self):
        self.encendido = True
        print(f"El carro ha encendido({self.__marca}, {self.__modelo})")
    
    def apagar(self):
        self.encendido = False
        print(f"El carro ha apagado({self.__marca}, {self.__modelo})")
    
    def acelerar(self):
        if self.encendido:
            print("El carro esta acelerando.")
        else:
            print("El carro esta apagado.")

mi_carro = Carro("Toyota", "Corolla", "Rojo")
mi_carro.marca="Nissan" # no se puede modificar el valor de un atributo privado
mi_carro.set_marca("Nissan") # se utiliza el metodo set_marca para modificar el valor de un atributo privado

print(mi_carro.marca) # no se puede acceder a un atributo privado

mi_carro.encender()
mi_carro.acelerar()

# Encapsulamiento: es una forma de proteger los atributos de una clase, para que no puedan ser modificados directamente desde fuera de la clase. Se utiliza para proteger los datos de la clase y para que no puedan ser modificados por error.
# Diferencia entre atributos publicos, protegidos y privados:
# Publicos: se pueden acceder y modificar desde cualquier parte del codigo.
# Protegidos: se pueden acceder y modificar desde la misma clase y desde las clases hijas.
# Privados: solo se pueden acceder y modificar desde la misma clase.

mi_carro2 = Carro("volkswagen", "Jetta", "Azul")
mi_carro2.marca="volkswagen"
mi_carro2.set_marca("volkswagen")

print(mi_carro2.marca)

mi_carro2.encender()
mi_carro2.acelerar()