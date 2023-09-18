#///BUCLES
#Escribir un programa en el que se pregunten por una frase y una letra y se muestre un mensaje
#que muestre el numero de veces que aparece una letra en la frase.

frase = input("Ingrese un menaje\n")
letra = input("Inrgese la letra que quiere buscar.\n")
frecuencia = 0

for l in frase:
    if letra == l:
        frecuencia += 1
print(f"La letra aparece {frecuencia} veces.")