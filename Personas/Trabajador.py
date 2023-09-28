from Personas.Persona import Persona 

class Trabajador (Persona):
    def __init__(self, nombre, rut, edad, telefono, email, valor_por_hora, horasTrabajadas, fechaIngreso):
        super().__init__(nombre, rut, edad, telefono, email)
        self._valor_por_hora = valor_por_hora
        self._horasTrabajadas = horasTrabajadas
        self._fechaIngreso = fechaIngreso

    def get_valor_por_hora(self):
        return self._valor_por_hora
    def set_sueldo(self,valor_por_hora):
        self._valor_por_hora=valor_por_hora
    
    def get_horasTrabajadas (self):
        return self._horasTrabajadas
    def set_horasTrabajadas(self, horasTrabajadas):
        self._horasTrabajadas = horasTrabajadas

    def get_fechaIngreso(self):
        return self._fechaIngreso
    def set_fechaIngreso (self, fechaIngreso):
        self._fechaIngreso= fechaIngreso

    def generar_sueldo(self):
        sueldo = self._valor_por_hora *self._horasTrabajadas
        print("El monto a pagar por el total de horas trabajadas es de:", sueldo)
        return sueldo

        
    def __str__(self):
        return super ().__str__()+f"Valor por hora $: {self._valor_por_hora}, Horas Trabajadas: {self._horasTrabajadas}, Fecha de Ingreso: {self._fechaIngreso}, Sueldo:{self.generar_sueldo}" 
        


