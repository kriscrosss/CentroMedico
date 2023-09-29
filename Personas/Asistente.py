from Personas.Trabajador import Trabajador
#enfermer@s y anestesistas
class Asistente(Trabajador):
    def __init__(self, nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso, pacientes_atendidos):
        super().__init__(nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso)

        self._pacientes_atendidos = pacientes_atendidos


    def get_pacientes_atendidos(self):
        return self._pacientes_atendidos
    def set_pacientes_atendidos(self, pacientes_atendidos):
        self._pacientes_atendidos = pacientes_atendidos

    def __str__(self):
        return super().__str__()+f"Médico a cargo: {self._medico_a_cargo}, Pacientes atendidos: {self._pacientes_atendidos}" 
