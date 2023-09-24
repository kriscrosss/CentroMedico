from Personas.Persona import Persona

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

    def __str__(self):
        return super ().__str__()+f"Diagnostico: {self._diagnostico}, Médico: {self._ultimo_medico}" 