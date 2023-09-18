#//Matrizes
#
#En una matriz de 5 x 4 pedirle al usuario los valores, , si es multiplo de 3 guardar un 2, 
#si el numeor es un multiplo de 5 guardar un 3 y guardar un 4 si es multiplo de 3 y 5 a la vez,
#si no se cumple ninguna de las reglas guardar un 0 

import random

matriz = []
resultado=[]

for fila in range(0,5):
    
    lista = []
    for columna in range(0,4):
        tem = random.randint(0,10)
        lista.append(tem)
        
    matriz.append(lista)
    
filas = len(matriz)
columnas = len(matriz[0])

for fila2 in range(0,filas):
    
    lista = []
    for columna2 in range(0,columnas):
        
        if matriz[fila2][columna2] % 3 == 0 and matriz[fila2][columna2] % 5 == 0:
            lista.append(4)
        elif matriz[fila2][columna2] % 5 == 0:
            lista.append(3)
        elif matriz[fila2][columna2] % 3 == 0:
            lista.append(2)
        else:
            lista.append(0)
            
    resultado.append(lista)
    
print(f"Matriz ORIGINAL\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}\n{matriz[4]}")
print(f"\nMatriz RESULTADO\n{resultado[0]}\n{resultado[1]}\n{resultado[2]}\n{resultado[3]}\n{resultado[4]}")