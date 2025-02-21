class Clinica:

     def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
     def agregar_restauramte(self, nombre):
         self.nombre = nombre
         print(f"Se ha agregado una clinica {self.nombre}.")
     
     def mostrar_informacion(self):
         print(f"El nombre del Establecimiento es: {self.nombre} y es de la categoria: {self.categoria}.")

     def mostrar_informacion2(self):
         print(f"El nombre del medico es: {self.nombre} y es de la Especialidad: {self.categoria} ")

# Herencia
class Medicos(Clinica):
    def __init__(self, nombre, categoria, sueldo, pacientes):
        super().__init__(nombre, categoria, sueldo) # super() es una referencia a la clase padre
        self.pacientes = pacientes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Numero de Pacientes: {self.pacientes}")

# Instanciar la clase Clinica
clinica = Clinica("Las delicias", "General", 50)
clinica.mostrar_informacion()


# Instanciar la clase medicos
medicos = Medicos("Jonathan", "Neurologia", 200, 30)
medicos.mostrar_informacion2()