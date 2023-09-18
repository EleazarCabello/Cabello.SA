#1 Funciones con n parámetro
#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y 
# calcule el producto total y su suma total

def ProductoSumaTotal (*valores):
    resultadoMul = 1
    resultadoSum = 0
    
    for v in valores:
        resultadoMul *= v
        resultadoSum += v
    return resultadoMul,resultadoSum

print(ProductoSumaTotal(1,2,3,4))
    