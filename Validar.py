def verificador_rut():
    def calcular_digito_verificador(rut_sin_dv):
        multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5]
        suma = sum(int(digito) * multiplicador for digito, multiplicador in zip(rut_sin_dv[::-1], multiplicadores))
        resto = suma % 11
        dv = 11 - resto if resto <= 10 else 'K'
        return str(dv)

    def validar_rut(rut):
        rut = rut.replace("-", "").replace(".", "")  # Eliminar guiones y puntos
        rut_sin_dv = rut[:-1]
        dv_ingresado = rut[-1].upper()

        dv_calculado = calcular_digito_verificador(rut_sin_dv)

        if dv_calculado == dv_ingresado:
            return dv_ingresado
        else:
            return False

    while True:
        rut_ingresado = input("Ingresa tu RUT (sin puntos y con guión): ")
        if validar_rut(rut_ingresado):
            print("El RUT es válido.")
            return rut_ingresado
            #break  # Rompe el bucle si el RUT es válido
        else:
            print("El RUT no es válido. Inténtalo nuevamente.")
