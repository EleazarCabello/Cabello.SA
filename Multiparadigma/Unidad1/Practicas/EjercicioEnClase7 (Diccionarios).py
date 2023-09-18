#//Diccionarios
#Escribir un programa que guarde en un diccionario los precios de las frutas de la sigueinte manera
#Fruta    , Precio
#Platano     1.35
#Manzana     0.80
#Pera        0.85
#Naranja     0.7

#Guardar el nombre de las frutas en mayusculas en el diccionario, preguntar a l usuario por una fruta
#y el numero de Kilos, mostrar en pantalla el calculo y si la fruta no esta en el diccionario mostrar un mensaje 
#de ello.

Precios = {"PLATANO":1.35,"MANZANA":0.80,"PERA":0.85,"NARANJA":0.70}

fruta = input("Selecciona una fruta:\n -PLATANO \n -MANZANA \n -PERA \n -NARANJA\n")
kilos = float(input("¿Cuantos kilos? "))
res = 0

for clave,valor in Precios.items():
    
    if fruta == clave:
        res = kilos * valor
        
if res == 0:
    print("La fruta no esta en el diccionario.")
else:
    print("Precio:", res)



