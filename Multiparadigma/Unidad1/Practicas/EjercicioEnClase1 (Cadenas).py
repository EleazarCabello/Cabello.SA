#/Escribir un programa que reciva una cadena de caracteres
# y devuelva un diccionario con cada palabra que contenga y su frecuencia/#

Cadena = "Hola mucho gusto hola eso eso"

palabras = Cadena.split()

dic = {}

for i in palabras:
    print(i)
    if i in dic:
        dic[i] += 1 
    else:
        dic[i] = 1
        
print(dic)