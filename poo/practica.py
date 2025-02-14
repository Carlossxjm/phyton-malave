class Medicos:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def agregar_medico(self, nombre):
        self.nombre = nombre
        print(f"medico: {self.nombre} {self.especialidad}")

    def mostrar_informacion(self):
        print(f"El nombre del medico es: {self.nombre} y su especialidad es: {self.especialidad}")

medico = Medicos('Dr. Juan', 'Pediatra')
medico.mostrar_informacion()