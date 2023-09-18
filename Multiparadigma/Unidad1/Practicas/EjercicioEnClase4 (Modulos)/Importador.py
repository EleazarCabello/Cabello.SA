#en el archivo importador 
#-matriz a diccionario
#-listas a Set
#-Matriz a tuplas

def Diccionario_a_Matriz(Diccionario):
    
    Matriz = [list([llave,valor]) for llave,valor in Diccionario.items()]
    return Matriz

#Ayuda a quitar todos los elementos iguales
def Listas_a_Set(Lista):
    conjunto = set(Lista)
    return conjunto 

def Matriz_a_Tuplas(matriz):
    tuplas = [tuple(fila) for fila in matriz]
    return tuplas


