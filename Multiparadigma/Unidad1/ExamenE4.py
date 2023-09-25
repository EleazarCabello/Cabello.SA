
#
import csv

documento = input ("Nombre archivo: ")

with open(f"C:/xampp/htdocs/Cabello.SA/Multiparadigma/Unidad1/{documento}") as datos:
    reader = csv.reader(datos)
    
    print(reader)