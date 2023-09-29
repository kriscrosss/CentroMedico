from Personas.Persona import Persona
from Personas.Validar import validar_rut
from Personas.RegistroAtencion import Registro_Atencion
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
        nombre = input("Ingrese el nombre del paciente:")
        rut = validar_rut()
        edad = input("Ingresa tu edad:")
        telefono = input("Ingresa tu telefono:")
        email = input("Ingresa tu email:")
        registro = []
        prevision= input("Ingresa tu prevision")

        return Paciente_Habitual(nombre, rut, edad, telefono, email, registro, prevision)
    
    def mostrar_historial_medico (self):
        for i in self.get_registro():
            print(i, "\n")

    def generar_registro(self):
        fecha = input("Ingrese la fecha de la atención (dd/mm/aaaa): ")
        hora = input("Ingrese la hora de la atención (hh:mm): ")
        medico = input("Ingrese el nombre del médico que atendió: ")
        diagnostico = input("Ingrese el diagnóstico de la atención: ")
        
        registro = Registro_Atencion(fecha, hora, medico, diagnostico)
    
        self._registro.append(registro)
    def __str__(self):
        return super().__str__()+ f"Registro: {self._registro}, Prevision: {self._prevision}" 

