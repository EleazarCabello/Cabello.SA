#//CONDICIONALES
#Una pitzeriaofrece pitzas vegetarinas y no vegetarianas y aparece una lista de ingredientes vegetarianos y no
#vegetarianos

#ingredientes vegetarianos: pimiento y tofu
#ingredientes no vegetarianos: pepperoni, jamon y salami
#Escribir un programa que permita  al usuario si quiere una pitza vegetariana o no vegetariana
#en funcion d esu respuesta , mostrar el menu con los ingredientes, solo se puede elegir un ingrediente
#ademas de la motzarrela y el tomate que estan en todas las pitzas, al final mostrar un mensaje con todos los ingredientes de la pitza
#y el tipo de la pitza.

print("Ingredientes vegetarianos:\n - Pimiento \n - Tofu\nIngredientes No vegetarianos: \n - Pepperoni\n - jamon\n - Salami")
seleccionPitza = input("¿Desea una pitza vegetariana? si o no\n")

if seleccionPitza == "si":
    ingrediente = input("\nSeleccione un  ingrediente:\n 1. Pimiento \n 2. Tofu\n")
    
    if ingrediente == "1":
        print("INGREDIENTES - PITZA VEGETARIANA\n Motzarrela, Tomate, Pimiento")
    elif ingrediente == "2":
        print("INGREDIENTES - PITZA VEGETARIANA\n Motzarrela, Tomate, Tofu")
        
else:
    ingrediente = input("\nSeleccione un  ingrediente:\n 1. Pepperoni\n 2. jamon\n 3. Salami\n")
    
    if ingrediente == "1":
        print("INGREDIENTES - PITZA NO VEGETARIANA\n Motzarrela, Tomate, Pepperoni")
    elif ingrediente == "2":
        print("INGREDIENTES - PITZA NO VEGETARIANA\n Motzarrela, Tomate, Jamon")
    elif ingrediente == "3":
        print("INGREDIENTES - PITZA NO VEGETARIANA\n Motzarrela, Tomate, Salamino")

