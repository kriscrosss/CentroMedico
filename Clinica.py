from Personas.Medico import Medico
from Personas.PacienteHabitual import Paciente_Habitual
from Personas.MedicosEspecialistas import MedicoEspecialista
from Personas.PacienteNoHabitual import Paciente_No_Habitual
from RegistroAtencion import Registro_Atencion
from Personas.Asistentes import Asistentes
from Validar import validar_rut

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

        paciente_habitual = input("¿Desea ingresar a un paciente habitual o un paciente nuevo? (s/n)")

        paciente = None

        while paciente_habitual.lower() != "s" and paciente_habitual.lower() != "n":
            paciente_habitual = input("Intentalo denuevo, debe ingresar s (Sí) o n (No): ")
            
        if paciente_habitual.lower() == "s":
            paciente = Paciente_Habitual.registrar_paciente()
        else:
            paciente = Paciente_No_Habitual.registrar_paciente()
        

        self._listaPacientes.append(paciente)
        
        print("Pacientes registrados:")
        i = 0
        for paciente in self._listaPacientes:
            i += 1
            print(f"{i}.{paciente.get_nombre()}")

    def crear_medico(self):
        nombre = input("Ingrese el nombre del médico:")
        rut = validar_rut()  # Supongo que esto verifica el RUT
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