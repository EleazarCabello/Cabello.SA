class Figura:
    def __init__(self,ancho,lado) -> None:
        self._lado=lado
        self._ancho=ancho
        
    def __str__(self) -> str:
        return f"Ancho:{self._ancho} Largo: {self._lado}"