from Persona import Persona 

class Trabajador (Persona):
    def __init__(self, nombre, rut, edad, telefono, email, sueldo, horasTrabajadas, fechaIngreso):
        super().__init__(nombre, rut, edad, telefono, email)
        self._sueldo = sueldo
        self._horasTrabajadas = horasTrabajadas
        self._fechaIngreso = fechaIngreso

    def get_sueldo(self):
        return self._sueldo
    def set_sueldo(self,sueldo):
        self._sueldo=sueldo
    
    def get_horasTrabajadas (self):
        return self._horasTrabajadas
    def set_horasTrabajadas(self, horasTrabajadas):
        self._horasTrabajadas = horasTrabajadas

    def get_fechaIngreso(self):
        return self._fechaIngreso
    def set_fechaIngreso (self, fechaIngreso):
        self._fechaIngreso= fechaIngreso

    def generar_sueldo():
        pass 
        
    def __str__(self):
        return super ().__str__()+f"Sueldo: {self._sueldo}, Horas Trabajadas: {self._horasTrabajadas}, Fecha de Ingreso: {self._fechaIngreso}" 
        


