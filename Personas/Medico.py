# BEGIN: xz4d5f6g7h8j

from .Trabajador import Trabajador
from ..Validar import validar_rut
class Medico(Trabajador):

    def __init__(self, nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, consultas_hechas):
            super().__init__(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso)
            self._consultas_hechas = consultas_hechas

    def get_consultas_hechas(self):
        return self._consultas_hechas
    def set_consultas_hechas(self,consultas_hechas):
        self._consultas_hechas = consultas_hechas

    def generar_consulta():
        pass

    def mostrar_consultas():
         pass
    
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
# END: xz4d5f6g7h8j
