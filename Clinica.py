from Medico import Medico
from PacienteHabitual import Paciente_Habitual
from MedicosEspecialistas import MedicoEspecialista
from PacienteNoHabitual import Paciente_No_Habitual
from RegistroAtencion import Registro_Atencion
from Asistentes import Asistentes
 
class Clinica():
    def __init__(self, nombre, direccion, telefono, listaMedicos, listaAsistentes, listaPacientes):
        self._nombre = nombre
        self._direccion= direccion 
        self._telefono = telefono
        self._listaMedicos = []
        self._listaAsistentes = []
        self._listaPacientes = []

    