
matrizA = [[1,2,3],[4,5,6]]

matrizB = [[-1,0],[0,1],[1,1]]

tuplaResultado = []

for mA in matrizA:
    
    resultadoTemp1 = 0
    posicionMA = 0
    for mB in matrizB:
        resultadoTemp1 = resultadoTemp1 + mA[posicionMA] * mB[0]
        posicionMA += 1
    print(resultadoTemp1)
    
    
    resultadoTemp2 = 0
    posicionMA = 0
    for mB in matrizB:
        
        resultadoTemp2 = resultadoTemp2 + mA[posicionMA] * mB[1]
        posicionMA += 1
    print(resultadoTemp2)
    
    tupla = (resultadoTemp1,resultadoTemp2)
    tuplaResultado.append(tupla)
    
print(f"R ={tuplaResultado[0]} \n   {tuplaResultado[1]}")

    
    

    
