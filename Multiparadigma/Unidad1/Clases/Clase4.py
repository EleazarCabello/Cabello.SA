#SET sonmmutables e inmutables a la vez, loe lementos  no se pueden modificar los elemnetos , pero si las posiciones
s = (1,2,3,4,5,0,23,4)
print(s)

#CICLO WHYLE ,se basa a una condicion

x = 5
while x>0:
    x-=1
    print(x)
    
y = 0
while x>0 or y > 10:
    x-=1
    y+=1
    print(x,y)
else:   #Cuando todas las condiciones se cumplen
    print("Fin del ciclo")
    
#TRY EXCEP
try:
    pass
except Exception as e:  #La exeption es Exception
    print(e)

#FUNCIONES
def suma(): #sin parametros
    return 10 + 5
print(suma())


def sumaParametros(a,b): #con parametros
    return a + b
print(sumaParametros(a =10, b = 11))

def sumaParametros2(a : int,b:int) -> int: #con parametros
    return a + b
print(sumaParametros2(a=1,b=2))


x=10
y = 1
z = 2

def mmultiplicacion(a,b,c=1): # HACER QUE UN PARAMETRO TENGA UN VALOR POR DEFECTO
    return a*b*c
print(mmultiplicacion(a=x,b=y))

def algo():
    pass
print(help(print)) #es para buscar algo sobre una funcion

lista = [1,2,3,4]
def suma(*x):
    suma = 0
    for i in x:
        suma +=1
    return suma
print(suma*(1,2,34,5,6)) #python lo convierte a tupla, se yien que poner asterisco 

#INVESTIGAR COMO HACE UNA FUNCION QUE RECIVA N PARAMETROS, AEN PYTHON Y C#

