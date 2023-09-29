from Personas.Medico import Medico
from Personas.Validar import validar_rut
class MedicoEspecialista (Medico):
    def __init__(self, nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, especialidad, operacionesRealizadas):
        super().__init__(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, especialidad)
        self._operacionesRealizadas= operacionesRealizadas
        self._asistentes= []

    def get_operacionesRealizadas(self):
        return self._operacionesRealizadas
    def set_operacionesRealizadas(self, operacionesRealizadas):
        self._operacionesRealizadas = operacionesRealizadas

    def mostrar_asistentes():
        pass
     
    #aumentar operaciones?
    def añadir_asistente():
        pass

    def eliminar_asistente():
        pass
    
    def crear_medico_especialista():
        nombre = input("Ingrese el nombre del médico especialista: ")
        rut = validar_rut()
        edad = int(input("Ingrese la edad del médico especialista: "))
        telefono = input("Ingrese el teléfono del médico especialista: ")
        email = input("Ingrese el email del médico especialista: ")
        valor_por_hora = float(input("Ingrese el valor por hora del médico: "))
        horasTrabajadas = int(input("Ingrese las horas trabajadas del médico especialista: "))
        fechaIngreso = input("Ingrese la fecha de ingreso del médico especialista (en formato dd/mm/aaaa): ")
        especialidad = input("Ingrese la especialidad del médico especialista: ")
        operacionesRealizadas = int(input("Ingrese la cantidad de operaciones realizadas por el médico especialista: "))
        return MedicoEspecialista(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, especialidad, operacionesRealizadas)

    def __str__(self):
        return super().__str__()+f"Operaciones realizadas: {self._operacionesRealizadas}, Asistentes (enfermer@/anestesista): {self._asistentes}" 