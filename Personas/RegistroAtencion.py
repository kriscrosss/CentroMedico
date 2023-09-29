class Registro_Atencion():
    def __init__(self, nombre, especialidad, fecha_atencion, diagnostico, costo):
        self._nombre = nombre
        self._especialidad = especialidad
        self._fecha_atencion = fecha_atencion
        self._diagnostico = diagnostico
        self._costo = costo 

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre 

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def get_fecha_atencion(self):
        return self._fecha_atencion

    def set_fecha_atencion(self, fecha_atencion):
        self._fecha_atencion = fecha_atencion

    def get_diagnostico(self):
        return self._diagnostico

    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def get_costo(self):
        return self._costo

    def set_costo(self, costo):
        self._costo = costo


    def generarRegistroAtencion(cls):
        nombre = input("Ingrese el nombre del Doctor: ")
        especialidad = input("Ingrese la especialidad: ")
        fecha_atencion = input("Ingrese la fecha de atención (dd/mm/aaaa): ")
        diagnostico = input("Ingrese el diagnóstico: ")
        costo = float(input("Ingrese el costo: "))
        return Registro_Atencion(nombre, especialidad, fecha_atencion, diagnostico, costo)
        

    def __str__(self):
        return f"Nombre doctor: {self._nombre}\nEspecialidad: {self._especialidad}\nFecha de atención: {self._fecha_atencion}\nDiagnostico: {self._diagnostico}\nCosto {self._costo}" 

