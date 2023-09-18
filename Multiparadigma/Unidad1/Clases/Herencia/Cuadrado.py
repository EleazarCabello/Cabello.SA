from Figura import Figura
from Color import Color
from Figura import *

class Cuadrado(Figura,Color):
    def __init__(self,color, lado):
        Figura.__init__(lado, lado)
        Color.__init__(self._color)
        
    def CalcularArea(self):
        return self.largo*self._ancho
    
    def __str__(self) -> str:
        return f"{Figura.__str__(self)} {Color.__str__(self)} AREA: {self.CalcularArea()}"


Cuadrado1 = Cuadrado("rojo",5)
print(Cuadrado1)