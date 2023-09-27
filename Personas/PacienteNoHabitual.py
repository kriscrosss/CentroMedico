from Personas.Persona import Persona
from ..Validar import validar_rut

class Paciente_No_Habitual(Persona):
    def __init__(self, nombre, rut, edad, telefono, email,  diagnostico, ultimo_medico):
        super().__init__(nombre, edad, rut, telefono, email)
        self._diagnostico = diagnostico
        self._ultimo_medico = ultimo_medico

    def get_diagnostico (self):
        return self._diagnostico
    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def get_ultimo_medico (self):
        return self._ultimo_medico
    def set_ultimo_medico(self, ultimo_medico):
        self._ultimo_medico = ultimo_medico

    def generar_paciente():
        nombre = input("Ingrese el nombre del paciente: ")
        rut = validar_rut()
        edad = input("Ingrese la edad del paciente: ")
        telefono = input("Ingrese el telefono del paciente: ")
        email = input("Ingrese el email del paciente: ")
        diagnostico = input("Ingrese el diagnostico del paciente: ")
        ultimo_medico = input("Ingrese el ultimo medico del paciente: ")
        return Paciente_No_Habitual(nombre, rut, edad, telefono, email, diagnostico, ultimo_medico)
        
    
    def __str__(self):
        return super ().__str__()+f"Diagnostico: {self._diagnostico}, Médico: {self._ultimo_medico}" 