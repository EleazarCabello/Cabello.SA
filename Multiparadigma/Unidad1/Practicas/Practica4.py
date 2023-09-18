#//4 Entrada de datos y estructuración. 

#Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture 
#las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato 
#“{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de 
#todas las materias 

programa = {}

materias = input("Registre las materias en orden.\n").split()
creditos = input("Registre los creditos de cada materia en el mismo orden.\n").split()

for materia, credito in zip(materias,creditos):
    programa[materia] = credito
    
print(type(programa))
print(programa)