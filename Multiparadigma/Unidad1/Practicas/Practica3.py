#3 Entrada de datos y manipulación.

#Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de 
#manera inversa letra por letra intercalando una letra minuscula a una mayuscula ejemplo Luis : L u I s

nombreCompleto = input("Ingrese su nombre completo. ")
nombreCompleto = nombreCompleto.upper()
intercalar = False
resultado = ""


for l in nombreCompleto:
    print(l)
    if intercalar:
        resultado = resultado + l.swapcase()
        intercalar = False
    else:
        intercalar = True
        resultado = resultado + l
        
print(resultado)