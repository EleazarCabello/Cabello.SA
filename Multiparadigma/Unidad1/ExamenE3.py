class Locacion:
    def __init__(self,nombre,porcentaje,items) -> None:
        self._nombre=nombre
        self._porcentaje=porcentaje
        self._items=items
        
        def __str__(self) -> str:
            return f"Nombre: {self._nombre}, Porcentaje: {self._porcentaje}, Items: {self._items}"
        
        def CalcularTotal(self):
            Total = 0
            for n in items:
                Total += n.precio           
            return print(f'El total es: {Total}')

        
class Item:
    def __init__(self,nombre,cantidad,precio) -> None:
        self._nombre=nombre
        self._cantidad=cantidad
        self._precio=precio
        
        def __str__(self) -> str:
            return f"Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"
        
ListaItems = []
opcion = 0
try:
    NombreL = input("\nIntroduzca el nombre de la locación: ")
    Porcentaje = float(input("\nIntroduzca la porcentaje del IVA: "))
    while opcion == 0:
        opcion = int(input("\nSeleccione una opción: \n1.-Crear Items \n2.-Añadir items a Locación \n3.- Sumar el total \n4.- Salida \nRespuesta: "))
        if opcion == 1:
            NombreI = input("\nIntroduzca el nombre: ")
            Cantidad = int(input("Introduzca la cantidad: "))
            Precio = Porcentaje*(float(input("Introduzca el precio: ")))
            if ListaItems == []:
                 miItem=Item(NombreI,Cantidad,Precio)
                 ListaItems.append(miItem)
                 print("\Item registrado\n")
                 opcion = 0
            else:
                 for obj in ListaItems:
                      if obj._nombre == NombreI:
                           print("\nEl Item ya existe\n")
                           opcion = 0
                           break
                      else:
                           miItem=Item(NombreI,Cantidad,Precio)
                           ListaItems.append(miItem)
                           print("\Item registrado\n")
                           opcion = 0
        elif opcion == 2:
            Items = ListaItems
            miLocacion=Locacion(NombreL,Porcentaje,Items)
            print("\nLocación registrada\n")
        elif opcion == 3:
             Locacion.CalcularTotal()
        elif opcion == 4:
            break
        else:
             print("\nOpción no válida\n")
             opcion = 0
    print("\nHasta luego!")
except:
     print('Ocurrió un error')