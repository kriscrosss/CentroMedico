from Medico import Medico
class MedicoEspecialista (Medico):
    def __init__(self, nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso, especialidad, operacionesRealizadas):
        super().__init__(nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso, especialidad)
        self._operacionesRealizadas= operacionesRealizadas
        self._asistentes= []

    def get_operacionesRealizadas(self):
        return self._operacionesRealizadas
    def set_operacionesRealizadas(self, operacionesRealizadas):
        self._operacionesRealizadas = operacionesRealizadas

    def operar():
        pass

    def mostrar_asistentes():
        pass
     
    #aumentar operaciones?
    def añadir_asistente():
        pass

    def eliminar_asistente():
        pass

    def __str__(self):
        return super().__str__()+f"Operaciones realizadas: {self._operacionesRealizadas}, Asistentes (enfermer@/anestesista): {self._asistentes}" 