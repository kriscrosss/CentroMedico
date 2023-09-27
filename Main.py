from Clinica import Clinica


def main_menu():
    clinica = Clinica()
    opc = True
    while opc:
        print("-----°-----Bienvenido(a) a la consulta médica-----°-----")
        print("------------------------Autónoma------------------------")
        print("Ingresar:")
        print("1. Paciente ")
        print("2. Médico ")
        print("3. Otra operación")
        print("0. Salir")
        bandera = 1
        while bandera == 1:
            try:
                opcion = int(input("Ingresa una opción:\n"))
                if opcion >= 0 and opcion <= 3:
                    bandera = 0
                else:
                    print("Opción elegida equivocada")
            except ValueError:
                print("Ingrese una opción nuevamente entre 0 y 3")

        if opcion == 1:
            clinica.crear_paciente()
        elif opcion == 2:
            clinica.crear_medico()
        elif opcion == 3:
            subopcion = 1
            while subopcion > 0 and subopcion < 5:
                print("1. Búsqueda por rut")
                print("2. Registros")
                print("3. Mostrar pacientes")
                print("4. Mostrar médicos")
                print("5. Volver")
                subopcion = int(input("Ingresa una opción:"))
                
                if subopcion == 1:
                    clinica.busqueda_por_rut
                elif subopcion == 2:
                    pass
                elif subopcion == 3:
                    clinica.mostrar_pacientes
                elif subopcion == 4:
                    clinica.mostrar_medicos
                elif subopcion == 5:
                    break
        elif opcion == 0:
            print("bai")
            opc = False

main_menu()
