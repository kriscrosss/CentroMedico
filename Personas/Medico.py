# BEGIN: xz4d5f6g7h8j

from Personas.Trabajador import Trabajador
from Personas.Validar import validar_rut

class Medico(Trabajador):

    def __init__(self, nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, consultas_hechas):
            super().__init__(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso)
            self._consultas_hechas = consultas_hechas

    def get_consultas_hechas(self):
        return self._consultas_hechas

    def set_consultas_hechas(self,consultas_hechas):
        self._consultas_hechas = consultas_hechas

    def generar_medico():
        nombre = input("Ingrese el nombre del médico: ")
        rut = validar_rut()
        edad = input("Ingrese la edad del médico: ")
        telefono = input("Ingrese el teléfono del médico: ")
        email = input("Ingrese el email del médico: ")
        valor_por_hora = float(input("Ingrese el valor por hora del médico: "))
        horasTrabajadas = int(input("Ingrese las horas trabajadas del médico: "))
        fechaIngreso = input("Ingrese la fecha de ingreso del médico: ")
        consultas_hechas = input("Ingrese la consultas hechas del médico: ")
        return Medico(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, consultas_hechas)

    def __str__(self):
        return f"Nombre: {self._nombre}\nRUT: {self._rut}\nEdad: {self._edad}\nTeléfono: {self._telefono}\nEmail: {self._email}\nValor por hora: {self._valor_por_hora}\nHoras trabajadas: {self._horasTrabajadas}\nFecha de ingreso: {self._fechaIngreso}\nConsultas hechas: {self._consultas_hechas}"
# END: xz4d5f6g7h8j
    