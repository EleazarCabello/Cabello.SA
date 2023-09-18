def suma(*x):
    print(type(x))
    suma=0
    for i in x:
        suma+=1
    return suma

print(suma(1,2,3,4,5,6,7,8,9))

def resta(*x):
    print(type(x))
    resta=0
    for i in x:
        resta+=1
    return resta

print(resta(1,2,3,4,5,6,7,8,9))


def suma(**kwargs):
    suma = 0
    for key,value in kwargs.item():
        print(key,value)
        suma+=value
    return suma

print(suma(a=10,b=5,c=12,d=20))


di = {'a':10,'b':11,'c':12,'d':1} #enviando un diccionaria, se debe desenpacar 

suma(**di)

def mifuncion():
    print("entra")
    return
    print("sale")


def sumamedia(*x):
    suma = 0
    for n in x:
        suma+=n
    media= suma/len(x)
    return suma,media
resultado = sumamedia(1,2,3,4,5,3,2)
print(resultado)

def function(a,b,*arg,**kwargs):
    print ('a',a)
    print ('b',b)
    for i in arg:
        print('arg',i)
    for key,value in kwargs.items():
        print(key,'=',value)
        
function(1,0,'k',4,2,4,"hola",e=1,c=1,d=10)
        
        
numeros = list(range(1,101,1))

def suma2(*numeros):
    suma= 0
    for n in numeros:
        suma+=n
    return suma
print(suma(+numeros))

(lambda *n:print(sum(n)))(*list(range(1,101,1)))


def multiplicador(n):
    return lambda a:print(a*n)
duplicador = multiplicador(2)
triplicador = multiplicador(3)

print(duplicador(11))
print(triplicador(11))

#regreso al try catch

suma3 = None
try:
    suma=1+"1"
except Exception as e:
    print(e)
else: #solo se ejecuta cuando no hay errores
    print("esle",suma3)
finally: #se ejecuta siempre , con errores o sin errores
    print("finaly",suma3)