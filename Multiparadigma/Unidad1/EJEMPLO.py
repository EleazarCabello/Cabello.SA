

def Voltear (palabra):
    
    listaPalabra = []


    for letra in palabra:
        listaPalabra.append(letra)

    listaPalabra.reverse()

    res = ""
    for i in listaPalabra:
        res += i
    
    return res


palabra = input("Ingresa palabra: ")

print(Voltear(palabra))
