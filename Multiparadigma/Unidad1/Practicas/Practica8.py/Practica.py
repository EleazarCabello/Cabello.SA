#8.2.-Realizar un programa que contenga el siguiente menú 1.- Registro
#2.- Inicio de sesión
#3.- Salida 
#La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase 
#exceptuando el atributo Rol que por defecto será rol cliente, no se permitirán usuarios con CURP 
#repetido en caso de mostrar mensaje de “El usuario ya existe” 
#La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas desplegar 
#en pantalla la información del usuario de lo contrario mostrar mensaje de “datos incorrectos“ 

#8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la 
#información de todos los usuarios registrados al momento.

from ClassUsuario import usuario

listaUsuariosCreados = []
administrador = usuario("Ele","123","Administrador","Eleazar","CASE","NL")
listaUsuariosCreados.append(administrador)

def Registro ():
    C = input("\nContraseña: ")
    U = input("Usuario: ")
    N = input("Nombre: ")
    R = input("Cliente: ")
    CU = input("Curp: ")
    CI = input("Ciudad: ")
    
    for miUsuario in listaUsuariosCreados:
        if miUsuario.CURP == CU:
            print("El usuario ya existe")
            return
        
    nuevoUsuario = usuario(U,C,R,N,CU,CI)
    listaUsuariosCreados.append(nuevoUsuario)
    
def ImprimirTodo():
    for miUsuario in listaUsuariosCreados:
        miUsuario.Imprimir()


while True:
    
    opcion = int(input("\n1.- Registro \n2.- Inicio de sesión\n3.- Salida "))
    
    if opcion == 1:
        Registro()
        
    elif opcion == 2:
        pedirUsuario = input("Ingrese su Usuario: ")
        pedirContraseña = input("Ingrese su Contraseña: ")
        encontrado = True
        
        for miUsuario in listaUsuariosCreados:
            if miUsuario.Usuario == pedirUsuario and miUsuario.Contraseña == pedirContraseña:
                if miUsuario.Rol == "Administrador":
                    ImprimirTodo()
                else:
                    miUsuario.Imprimir()
                encontrado = False
        if encontrado:
            print("Datos incorrectos")  
        
    else:
        break
    
    
