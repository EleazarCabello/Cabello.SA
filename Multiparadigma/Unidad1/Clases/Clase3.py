#DICCIONARIO , se parece a un json, no ordenadas, no indexadas (no contien 0,1,2,3,4,5)
#son mutables, como los elemntos y las llaves

dic = {
    "nombre":"Rocio",
    "Edad":24,
    "Promedio":10.0
    }

#utliza una lista de tuplas para crear un diccionario
print(dic("Promedio":))
dic=dict

#asiganr una llave nueva
dic{"Nacionalidad"} = "Mexaicano"
dic{"Edad"} = 25

#iteracion de diccionario

for d in dic:
    print(d)
    
for e in dic:
    print(dic{e})
    
# metodos
.items

#obetener el valor de un objeto del diccionario
print(dic.get) # Cuando el item no existe no manda un NULL, sirve para probar si esta  y si no existe regresa un valor que se puede configurar

# nulo en python en NONE

#METODOS DE DICCIONARIO
print(list:dic{"Nombre"})
 #limpiar un diccionario CLEAR 
 dic.pop #elimina un dato dandole el nombre
 dic.popitem #elimina un elemento al azar 
 
 
 
 #IF Y ELSE
 a = 5
 if a == 5 :
     print(a)
 else:
    print("falso")
 
 b = 5

 if b == 5 :
     print(a)
 elif b > 0:
    print("falso")
 else:
     print("otro")
 
 
 #if en linea
 if b == 5 : print(a) ; print(b)
 
 
 #operador ternario
print("No es 5" if a ==5 else "No esfalsa")

c = 10 if c==5 else c

#for
cadena = " ser"
for t in cadena:
    print(t)
    
#empieza en el 0 , hasta el 100, de 2 en 2
for t in cadena(0,100,2):
    print(t)
    
#fro anidados
tupla = (2,1),(3,6)
for i in tupla:
    for j in i:
        print(j)
        
#palabra reservada , para evitar errores en el if y for usar PASS
for i in tupla:
    pass
print(tupla)

#CONTINUE, pasar a la sigueinte iteracion sin romper el ciclo
#BREAK ,si rompe el ciclo
for i in range(0,10):
    if i == 0:
        break
print(tupla)

for i in range(0,10):
    if i == 3:
        continue
print(tupla)

