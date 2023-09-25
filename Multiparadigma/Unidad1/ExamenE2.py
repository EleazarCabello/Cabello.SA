
valor1 = int(input("Ingrese el primer valor: "))

valor2 = int(input("Ingrese el segundo valor: "))

listaV1 = []
listaV2 = []

for numero in range(0,1):
    
    temporal = valor1%10
    valor1 = int(valor1/10)
    listaV1.append(temporal)
    
    temporal = valor1%10
    valor1 = int(valor1/10)
    listaV1.append(temporal)
    
    temporal = valor1%10
    valor1 = int(valor1/10)
    listaV1.append(temporal)
    
    temporal = valor2%10
    valor2 = int(valor2/10)
    listaV2.append(temporal)
    
    temporal = valor2%10
    valor2 = int(valor2/10)
    listaV2.append(temporal)
    
    temporal = valor2%10
    valor2 = int(valor2/10)
    listaV2.append(temporal)
    
    
    valor1 = 0
    valor2 =0
    contador1 = 0
    contador2 = 0
    for i in listaV1:
        
        valor1 += i
        contador1 += 1
        if contador1 != 3:
            valor1 = valor1*10
        
        
    for i in listaV2:
        valor2 += i
        contador2 += 1
        if contador2 != 3:
            valor2 = valor2*10
       
        
    if valor1 > valor2:
        print(valor1)
    else:
        print(valor2)

