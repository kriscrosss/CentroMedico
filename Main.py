from Clinica import Clinica
from Personas.PacienteHabitual import Paciente_Habitual
from Personas.PacienteNoHabitual import Paciente_No_Habitual
# Prueba
def main_menu():
    clinica = Clinica()
    opc = True
    while opc:
        print("-----°-----Bienvenido(a) a la consulta médica-----°-----")
        print("------------------------Autónoma------------------------")
        print("1. Ingresar Paciente (Habitual o No habitual)")
        print("2. Ingresar Médico (General o especialista)")
        print("3. Búsqueda de persona por rut")
        print("4. Mostrar Registros de pacientes")
        print("5. Crear nuevo registro a paciente habitual")
        print("6. Mostrar pacientes")
        print("7. Mostrar médicos")
        print("0. Salir")
        bandera = 1
        while bandera == 1:
            try:
                opcion = int(input("Ingresa una opción:\n"))
                if opcion >= 0 and opcion <= 7:
                    bandera = 0
                else:
                    print("Opción elegida equivocada")
            except ValueError:
                print("Ingrese una opción nuevamente entre 0 y 7")

        if opcion == 1: # Ingresar paciente
            clinica.crear_paciente()
        elif opcion == 2: # Ingresar medico
            clinica.crear_medico()
        elif opcion == 3: # Buscar persona por rut
           clinica.busqueda_por_rut()
        elif opcion == 4: # Mostrar registros de pacientes
            persona = clinica.busqueda_por_rut()
            if persona:
                if isinstance(persona, Paciente_Habitual):
                    paciente = persona
                    paciente.mostrar_historial_medico()
                elif  isinstance(persona, Paciente_No_Habitual):
                    print(persona)
                else:
                    print("Error el rut debe ser de un paciente.")
        elif opcion == 5: # Crear registro a paciente habitual
            persona = clinica.busqueda_por_rut()
            if persona:
                if isinstance(persona, Paciente_Habitual):
                    paciente = persona
                    paciente.generar_registro()
                else:
                    print("Error el rut debe ser de un paciente habitual.")     
        elif opcion ==6: # Mostrar los pacientes
            clinica.mostrar_pacientes()
        elif opcion ==7: # mostrar los medicos
            clinica.mostrar_medicos()
        elif opcion == 0: #  cerrar
            print("Hasta luego!")
            opc = False

main_menu()
