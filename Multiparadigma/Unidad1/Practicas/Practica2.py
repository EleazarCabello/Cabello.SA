#2 Manejo y manipulación de elementos de una lista 

#Escribir un programa que almacene el abecedario en una lista, elimine de la 
# lista las letras que ocupen posiciones múltiplos de 2, y muestre por pantalla
# la lista resultante

abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
multiplo = 0
decre = 0

for posicion in range(len(abcdario)):
    
    multiplo += 1
    if multiplo == 2:
        multiplo -= 2
        abcdario.remove(abcdario[posicion-decre])
        decre += 1
print(abcdario)