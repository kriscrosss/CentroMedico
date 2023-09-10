from Persona import Persona
class Paciente_Habitual(Persona):
    def __init__(self, nombre, rut, telefono,registro,prevision):
        super().__init__(nombre, rut, telefono)
        self._registro = registro
        self._prevision = prevision
    
    def get_registro(self):
        return self._registro
    def set_registro(self,registro):
        self._registro= registro








class Paciente_No_Habitual(Persona):
    def __init__(self, nombre, rut, telefono, diagnostico, ultimo_medico):
        super().__init__(nombre, rut, telefono)
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
        