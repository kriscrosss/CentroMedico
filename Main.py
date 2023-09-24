def main_menu():
    opc=True
    while opc:
        print("-----°-----Bienvenido(a) a la consulta médica-----°-----")
        print("------------------------Autónoma------------------------")
        print("Ingresar un:")
        print("1.Paciente ")
        print("2.Médico ")
        print("3.Otra operacion")
        print("0.Salir")
        opcion = int(input("Ingresa una opción:\n"))

        if opcion ==1:
            pass
        elif opcion ==2:
            pass
        elif opcion ==3:
            subopcion = 1
            while subopcion > 0 and subopcion < 5:
                
                print("1.Busqueda por rut")
                print("2.Registros")
                print("3.Mostrar pacientes")
                print("4.Mostrar médicos")
                print("5.Volver")
                subopcion= int(input("Ingresa una opción:")) 
                
                if subopcion == 1:
                    pass
                elif subopcion == 2:
                    pass
                elif subopcion == 3:
                    pass
                elif subopcion == 4:
                    pass
                elif subopcion == 5:
                    break
                
        elif opcion ==0:
            print("chao conchetumare")
            opc=False
main_menu()

