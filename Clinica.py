from Medico import Medico
from PacienteHabitual import Paciente_Habitual
from MedicosEspecialistas import MedicoEspecialista
from PacienteNoHabitual import Paciente_No_Habitual
from RegistroAtencion import Registro_Atencion
from Asistentes import Asistentes
from Validar import verificador_rut

class Clinica():
    def __init__(self):
        self._nombre = "Autónoma"
        self._direccion = "Avenida Pedro de Valdivia 311"
        self._telefono = "600 656 0240"
        self._listaMedicos = []
        self._listaAsistentes = []
        self._listaPacientes = []
        self._listaPacientesNoHabituales=[]

    def crear_paciente(self):
        nombre = input("Ingrese el nombre del paciente:")
        rut = verificador_rut()  # Supongo que esto verifica el RUT
        edad = input("Ingresa tu edad:")
        telefono = input("Ingresa tu telefono:")
        email = input("Ingresa tu email:")
        registro=input("#########################")
        prevision= input("Ingresa tu prevision")
        paciente = Paciente_Habitual(nombre, rut, edad, telefono, email, registro, prevision)
        self._listaPacientes.append(paciente)
        print("Pacientes registrados:")
        for paciente in self._listaPacientes:
            print(paciente)

    def crear_medico(self):
        nombre = input("Ingrese el nombre del médico:")
        rut = verificador_rut()  # Supongo que esto verifica el RUT
        edad = input("Ingresa tu edad:")
        telefono = input("Ingresa tu telefono:")
        email = input("Ingresa tu email:")
        especialidad = input("Ingresa especialidad:")
        valor_por_hora = input("Ingresa tu valor por hora $:")
        horasTrabajadas = input("Ingresa tus horas laborales")
        fechaIngreso = input("Agrega tu fecha de ingreso en formato MM/dd/aaaa:")
        medico = Medico(nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso, especialidad)
        self._listaMedicos.append(medico)
        print("Médicos registrados:")
        for medico in self._listaMedicos:
            print(medico)

    def mostrar_pacientes(self):
        print("Lista de pacientes Habituales:")
        for paciente in self._listaPacientes:
            print (f"Nombre:{paciente.get_nombre()}, Rut: {paciente.get_rut()}, Registro: {paciente.get_registro()}, Previsión: {paciente.get_prevision()}")

        print("Lista de pacientes No habituales:")
        for paciente in self._listaPacientesNoHabituales:
            print(f"Nombre:{paciente.nombre}")

    def mostrar_medicos(self):
        print("Lista de médicos:", self._listaMedicos)
        for medico in self._listaMedicos:
            print("shjad")

    def busqueda_por_rut(self):
        rut=input("Ingresa Rut:")
        encontrado = False

        #busca en la lista de pacientes habituales
        for paciente in self._listaPacientes:
            if paciente.get_rut()==rut:
                print("Paciente Habitual encontrado:")
                print(f"Nombre: {paciente.get_nombre()}, Rut: {paciente.get_rut()}")
                encontrado=True

        #busca en la lista de pacientes no habituales
        for paciente in self._listaPacientesNoHabituales:
            if paciente.get_rut()==rut:
                print("Paciente no habitual encontrado:")
                print(f"Nombre: {paciente.get_nombre()}, Rut{paciente.get_rut()}")
                encontrado = True

        #busca en la lista de medico
        for medico in self._listaMedicos:
            if medico.get_rut()==rut:
                print("Médico encontrado:")
                print(f"Nombre:{medico.get_nombre()}, Rut: {medico.get_rut()}, Especialidad: {medico.get_especialidad()}" )
                encontrado= True
        
        if not encontrado:
            print(f"No se encontró ningún paciente o médico con el rut: {rut}")