#Escribir un programa que le pida al usuario un numero entero N, N debe ser >= a 4
#y <= a 100
#generar una lista de longitud N de numeros aleatorios y crear una  donde se genere una matriz
#donde los elementos de la X sean los numeros de la lista, llenar los demas espacios con 0 ceros
#validar si no se puede hacer una X con la cantidad de N

#import random
#
#N = input("Ingrese el valor de N: ")
#matriz = []
#
#if N >= 4 and N <= 100:
#    
#    listaAleatoria = [10,11,12,13,14]
#    
#    if N-1 % 4 == 0:
#        
#        for i in range(0,int(N/2+0.5)):
#            
#            
#            
#            
#    elif N == 4:
#        matriz.append([listaAleatoria[0],listaAleatoria[1]])
#        matriz.append([listaAleatoria[2],listaAleatoria[3]])
#    else:
#        print("El valor de N no permite una X perfecta.")
#        
#else:
#    print("El valor de N debe ser mayor a 3 y menor que 101")
#    
#print(matriz)


#/////////////////
import random
matriz = []
while True:
    try:
        dato = input("Ingrese N: ")
        if dato != "0":
            n = int(dato)
            if n >=4 and n<=100:
                break
    except ValueError:
        print("Eso no es un valor entero.")
lista=[]
for i in range(n):
    lista.append(random.randint(1,100))
print("la lista es: ")
print(f"{lista}\nEl resultado es:")
def Convertir(lista):
    res = int((n+1)/2)
    val = int(res/2+1)
    x=0
    y= res-1
    valor=0
    valList=0
    for i in range(res):
        fila = []
        for j in range(res):
            valor=0
            if y == j and valList< n:
                valor = lista[valList]
                valList+=1
                if y > 0:
                    y-=1
            if j==i and valList < n and j!=val-1 and i!= val-1: 
                valor=lista[valList]
                valList+=1
                x+=1 
            fila.append(valor)
        matriz.append(fila)
    return matriz
def Convertir2(lista):
    res = int((n+1)/2)
    val = int(res/2+1)
    x=0
    y= res-1
    valor=0
    valList=0
    for i in range(res):
        fila = []
        for j in range(res):
            valor=0
            if y == j and valList< n:
                valor = lista[valList]
                valList+=1
                if y > 0:
                    y-=1
            if j==i and valList < n: 
                valor=lista[valList]
                valList+=1
                x+=1 
            fila.append(valor)
        matriz.append(fila)
    return matriz
if n % 2 != 0:
    resultado = Convertir(lista)
else:
    resultado = Convertir2(lista)
for i in resultado:
    print(i)







