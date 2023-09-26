class Persona():

    def __init__(self,nombre,rut,edad,telefono,email):
        self._nombre = nombre 
        self._rut = rut
        self._edad = edad
        self._telefono = telefono
        self._email = email

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre


    def get_rut(self):
        return self._rut
    def set_rut(self,rut):
        self._rut= rut

    def get_edad(self):
        return self._edad
    def set_edad(self,edad):
        self._edad=edad

    def get_telefono(self):
        return self._telefono
    def set_telefono(self,telefono):
        self._telefono = telefono

    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def __str__(self):
        return f"Nombre: {self._nombre}, RUT: {self._rut}, Edad: {self._edad}, Telefono: {self._telefono}, Email: {self._email}" 































        