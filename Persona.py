class Persona():
    def __init__(self,nombre,rut,telefono):
        self._nombre = nombre 
        self._rut = rut
        self._telefono = telefono

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre


    def get_rut(self):
        return self._rut
    def set_rut(self,rut):
        self._rut= rut


    def get_telefono(self):
        return self.get_telefono
    def set_telefono(self,telefono):
        self._telefono = telefono

    def __str__(self):
        return f"Nombre: {self._nombre}, RUT: {self._rut}, Telefono: {self._telefono}" 































        