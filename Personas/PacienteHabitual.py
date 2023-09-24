from Personas.Persona import Persona
class Paciente_Habitual(Persona):
    def __init__(self, nombre, rut, edad,telefono,email, registro,prevision):
        super().__init__(nombre,rut,edad,telefono,email)
        self._registro = registro
        self._prevision = prevision
    
    def get_registro(self):
        return self._registro
    def set_registro(self,registro):
        self._registro= registro

    def get_prevision(self):
        return self._prevision
    def set_prevision(self, prevision):
        self._prevision = prevision

    def registrar_paciente():
        pass

    def convertir_paciente_habitual():
        pass

    def buscar_registro_medico():
        pass

    def mostrar_historial_medico ():
        pass

    def __str__(self):
        return super().__str__()+ f"Registro: {self._registro}, Prevision: {self._prevision}" 







