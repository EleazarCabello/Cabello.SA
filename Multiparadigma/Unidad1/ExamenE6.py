
palabraBuscar = input("Ingrese la palabra que buscara: ")


texto = open('C:/xampp/htdocs/Cabello.SA/Multiparadigma/Unidad1/Texto.txt')
reader = texto.read()

listaRes = []
posicion = 1
repeticion = 0
contadorCaracter = 0
tamanoPalabra = 0

for i in palabraBuscar:
    tamanoPalabra += 1

for palabra in reader.split(" "):
    
    for caracter in palabra:
        contadorCaracter += 1
        
    if palabraBuscar == palabra:
        listaRes.append(contadorCaracter-tamanoPalabra)
        repeticion += 1
        
        
    posicion += 1
    #print(palabra)
    
print(f"La plabra {palabraBuscar} se repite: {repeticion}")

for i in listaRes:
    print(f"Posicion: {i}")

    
    