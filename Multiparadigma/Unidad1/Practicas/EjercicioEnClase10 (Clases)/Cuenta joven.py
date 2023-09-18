import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setter y Getter para bonificacion
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    # Método para verificar si el titular es mayor de edad y menor de 25 años
    def esTitularValido(self):
        # Suponemos que la edad está almacenada en el atributo "edad" del titular
        return self.titular.edad >= 18 and self.titular.edad < 25

    # Sobreescribir el método retirar para verificar si el titular es válido
    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero. El titular no es válido.")

    # Sobreescribir el método mostrar para incluir la bonificación
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.get_bonificacion()}%")