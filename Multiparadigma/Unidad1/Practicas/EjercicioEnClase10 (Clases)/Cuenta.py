class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad  # Usamos __cantidad como atributo privado

    # Setter y Getter para cantidad
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.get_cantidad()}")

    # Método para ingresar dinero en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        # Permitir retiradas incluso si la cantidad es negativa
        self.__cantidad -= cantidad

