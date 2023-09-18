#//Dividir un cierto entero en N veces, por otro entero M, hasta N=1 
#obteniendo una secuencia de numeros, cada numero de una secuencia almacenado en una lista
#la secuencia hay que cumplir hasta llegar a N=1
#si N=1 imprimir la secuencia entera
#en caso contrio, imprmir"Secuencia entera", caso contrario "Secuencia invalida"

n = input("Ingrese N: ")
m = input("Ingrese M: ")

try:
    resultados=[]
    resultados.append(int(n))
    
    while n!=1:
        n = n / m
    resultados.append(int(n))

    resultados.reverse()
    if resultados[0] == 1:
        print("Secuencia entera")
    else:
        print("Secuencia invalida")
    
    print(resultados)
except:
    print("Solo permite numeros enteros")



