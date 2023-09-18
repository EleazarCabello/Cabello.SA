#//Archivos
#En base al siguiente csv realizar lo siguiente, crear una funcion que ordene un dicionario por nombre
#crear otra funcion que ordene por numero de control y una funcion que ordene por calificacion

import csv

diccionario = {}
listaControl = []
listaNombre = []
listaCalificacion = []
contador = 0
with open('C:/Users/Eleazar/Documents/Multiparadigma/Unidad1/Practicas/EjercicioEnClase9(Archivos)/Entrada.csv') as datos:
    reader = csv.reader(datos)
    
    for row in reader:
        if contador != 0:
            listaControl.append(row[0])
            listaNombre.append(row[1])
            listaCalificacion.append(row[2])
            
        contador = 1
    
    diccionario = {"No.Control":listaControl,"Nombre":listaNombre,"Cailificacion":listaCalificacion}
    


#def OrdenarNombre(diccionario):
#    listaControl = []
#    listaNombre = []
#    listaCalificacion = []
#    nuevoDiccionario = {}
#
#    #nuevoDiccionario = sorted(diccionario.items())
#    
#    print(diccionario)
#    
#def OrdenarNumeroControl():
#    pass
#def OrdenarCalificacion():
#    pass
#
#OrdenarNombre(diccionario)