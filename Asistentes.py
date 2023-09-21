from Trabajador import Trabajador
#enfermer@s y anestesistas
class Asistentes(Trabajador):
    def __init__(self, nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso, medico_a_cargo, pacientes_atendidos):
        super().__init__(nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso)
        self._medico_a_cargo = medico_a_cargo
        self._pacientes_atendidos = pacientes_atendidos

    def get_medico_a_cargo(self):
        return self._medico_a_cargo
    def set_medico_a_cargo(self, medico_a_cargo):
        self._medico_a_cargo = medico_a_cargo

    def get_pacientes_atendidos(self):
        return self._pacientes_atendidos
    def set_pacientes_atendidos(self, pacientes_atendidos):
        self._pacientes_atendidos = pacientes_atendidos
        
    def mostrar_jefe():
        pass

    def pacientes_atendidos():
        pass
    
    def __str__(self):
        return super().__str__()+f"Médico a cargo: {self._medico_a_cargo}, Pacientes atendidos: {self._pacientes_atendidos}" 
