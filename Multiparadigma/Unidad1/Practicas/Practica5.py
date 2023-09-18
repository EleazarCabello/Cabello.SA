#//5 Manejo de información 

#Escribir una función que reciba n parámetros de llave valor e imprima la información en formato 
#“{valor}”: “{llave}” 

def Imprimir (**n):
    contador = 0
    for llave,valor in n.items():
        contador += 1
        print(f"{contador}.- {valor} : {llave}")
        
        
Imprimir(Nombre = "Eleazar", Apellido = "Cabello", NoControl = "19100114")