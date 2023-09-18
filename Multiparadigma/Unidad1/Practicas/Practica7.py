#//7 Formateo y conversiones 

#Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
#YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
#del día de hoy en el formato seleccionado.

from datetime import datetime

opcion = input("Seleccione una opcion:\n1.- Imprimir YYYY/MM/DD\n2.- Imprimir MM/DD/YYYY\n")
hoy = datetime.now()
if opcion == "1":
    print(hoy.strftime("%Y/%m/%d"))
else:
    print(hoy.strftime("%m/%d/%Y"))