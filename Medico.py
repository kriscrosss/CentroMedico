from Persona import Persona

class Medico(Persona):
    def __init__(self,nombre,rut,telefono,especialidad):
        super ().__init__(nombre, rut, telefono)
        self._especialidad = especialidad

    def get_especialidad(self):
        return self._especialidad
    def set_especialidad(self,especialidad):
        self._especialidad = especialidad