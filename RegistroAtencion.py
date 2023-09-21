class Registro_Atencion ():
    def __init__(self, nombre, especialidad,fecha_atencion, diagnostico, costo):
        self._nombre = nombre
        self._especialidad = especialidad
        self._fecha_atencion = fecha_atencion
        self._diagnostico = diagnostico
        self._costo = costo 

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre 

    def get_especialidad (self):
        return self._especialidad
    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def get_fecha_atencion(self):
        return self._fecha_atencion
    def set_fecha_atencion(self, fecha_atencion):
        self._fecha_atencion = fecha_atencion

    def get_diagnostico (self):
        return self._diagnostico
    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def get_costo(self):
        return self._costo
    def set_costo(self,costo):
        self._costo=costo

    def generarRegistroAtencion ():
        pass

    def __str__(self) -> str:
        pass
 