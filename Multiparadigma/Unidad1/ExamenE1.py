import random

n = int(input("Ingrese el valor de N: "))

if n >= 2 and n <= 10:
    matrizA = []

    for fila in range(0,n):
        
        fila = []
        for columna in range(0,n):
            fila.append(random.randint(0,99))
            
        matrizA.append(fila)

    print(matrizA)
    matrizOrdenar = []
    
    for i in matrizA:
        for j in i:
            matrizOrdenar.append(j)
        
    matrizOrdenar.sort()
    print(matrizOrdenar)
    
    MatrizB = []
    for fila in range(0,n):
        
        fila = []
        for columna in range(0,n):
            fila.append(0)
        MatrizB.append(fila)





    vueltas = 0
    Contador = 0
    Bool = False
            
    while Contador < n*n-1:
        #print(Contador)
        #fila 0
        lista1 = []
        for columna1 in range(vueltas,n-vueltas):
            MatrizB[vueltas][columna1] = matrizOrdenar[Contador]
            if Contador >= n*n-1:
                Bool = True
                break
            Contador += 1
            
        if Bool:
            break


        #lista1 = []
        for fila1 in range(1+vueltas,n-vueltas):
            #print(fila1)
            MatrizB[fila1][n-1-vueltas] = matrizOrdenar[Contador]
            if Contador == n*n-1:
                Bool = True
                break
            Contador += 1
        if Bool:
            break
            
            
        for columna2 in range(n-2-vueltas,-1+vueltas,-1):
            #print (columna2)
            MatrizB[n-1-vueltas][columna2] = matrizOrdenar[Contador]
            if Contador == n*n-1:
                Bool = True
                break
            Contador += 1
        if Bool:
            break


        if Contador <= n*n-1:

            for fila2 in range(n-2-vueltas,vueltas,-1):
                MatrizB[fila2][vueltas] = matrizOrdenar[Contador]
                if Contador == n*n-1:
                    Bool = True
                    break
                Contador += 1
            if Bool:
                break

            if Contador+1 >= n*n:
                MatrizB[int((n-1)/2)][int((n-1)/2)] = matrizOrdenar[n*n-1]

            vueltas += 1

        else:
            break
            
    for X in MatrizB:

            print(X)
        
    
else:
    print("El valor de N debe ser entre mayor que 1 y menor que 11")