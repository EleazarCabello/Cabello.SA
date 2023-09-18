
#//MODULOS
#Generar 3 archivos
#el primero llamado exportador
#el segundo llamado inportador
#y el tercero llamado pruebas

#en el archivo exportador colocar los sigueintes metodos
#-Matricez a diccionario
#-tuplas a Matrizes
#-Set a listas

#en el archivo importador 
#-matriz a diccionario
#-listas a Set
#-Matriz a tuplas

#Archvo de purebas
#-va a mandar a llamar ambos modulos

from Exportador import Matriz_a_Diccionario,Tuplas_a_Matriz,Sets_a_Listas
from Importador import *

print(Matriz_a_Diccionario([["Nombre", "Eleazar"],["Apellido","Cabello"],["Edad",23]]))
print(Tuplas_a_Matriz((1,2,3,4),("Buenas","Tardes")))
print(Sets_a_Listas({1, 2, 3},{4, 5, 6},{7, 8, 9}))

print(Diccionario_a_Matriz({'Nombre': 'Eleazar', 'Apellido': 'Cabello', 'Edad': 23}))
print(Listas_a_Set([3,5,3,6,3,5,2]))
print(Matriz_a_Tuplas([[1,1,1],[2,2,2,2],[3,3]]))

