from Persona import Persona
#Herencia persona
class Empleado(Persona):
    def __init__(self, nombre, edad,sueldo) -> None:
        super().__init__(nombre, edad)
        self._sueldo=sueldo
        
    def __str__(self) -> str:
        return f"{super().__str__()} Sueldo: {self._sueldo}"
    

miEmpleado = Empleado("Pedro",25,500)
print(miEmpleado)