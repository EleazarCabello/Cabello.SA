#8 Resumen y multi-solución
#8.1.-Definir una clase usuario que contenga como atributos: Usuario
#Contraseña
#Rol
#Nombre
#CURP
#Ciudad

class usuario:
    def __init__ (self,Usuario,Contraseña,Rol,Nombre,CURP,Ciudad):
        self.Usuario = Usuario
        self.Contraseña = Contraseña
        self.Rol = Rol
        self.Nombre = Nombre
        self.CURP = CURP
        self.Ciudad = Ciudad
        
    def Imprimir(self):
        print(f"\nUsuario:{self.Usuario} , Contraseña:{self.Contraseña}\n Rol:{self.Rol}, Nombre:{self.Nombre}\n Curp:{self.CURP}, Ciudad: {self.Ciudad}")