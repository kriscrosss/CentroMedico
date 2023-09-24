from Personas.Medico import Medico
from Personas.PacienteHabitual import Paciente_Habitual
from Personas.MedicosEspecialistas import MedicoEspecialista
from Personas.PacienteNoHabitual import Paciente_No_Habitual
from RegistroAtencion import Registro_Atencion
from Personas.Asistentes import Asistentes
 
class Clinica():
    def __init__(self, nombre, direccion, telefono, listaMedicos, listaAsistentes, listaPacientes):
        self._nombre = nombre
        self._direccion= direccion 
        self._telefono = telefono
        self._listaMedicos = []
        self._listaAsistentes = []
        self._listaPacientes = []

    