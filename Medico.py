from Trabajador import Trabajador

class Medico(Trabajador):

    def __init__(self, nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso, especialidad):
            super().__init__(nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso)
            self._especialidad = especialidad

    def get_especialidad(self):
        return self._especialidad
    def set_especialidad(self,especialidad):
        self._especialidad = especialidad

    def generar_consulta():
        pass

    def mostrar_consultas():
         pass
    
    def __str__(self):
        return super ().__str__() + f"Especialidad: {self._especialidad}" 