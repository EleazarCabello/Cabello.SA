#en el archivo exportador colocar los sigueintes metodos
#-Matricez a diccionario
#-tuplas a Matrizes
#-Set a listas

def Matriz_a_Diccionario(matriz):
    
    diccionario = {}
    contador = 0
    for fila in matriz:
        
            diccionario[fila[0]] = fila[1]
    return diccionario

def Tuplas_a_Matriz(*tuplas):
    
    Matriz = [tuplas]
    return Matriz

def Sets_a_Listas(*sets):
    #INTERESANTE> creas una lista que contenga un ciloc que recorra los set(conjuntos)
    Lista = [list(conjunto) for conjunto in sets]
    return Lista

    
