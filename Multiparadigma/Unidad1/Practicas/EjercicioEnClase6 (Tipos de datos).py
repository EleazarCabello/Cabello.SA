#//Tipos de datos
#Una jugueteria tiene mucho exito en todos sus productos, payasos y muñecas se suele hacer la venta por correo
#y la empresa de lojistica suele cobrar por peso cada paquete, asi que hay que calcular el peso delos payasos
#y muñecas.
#cada payaso pesa 112 gr y cada muñeca 75gr
#Escribir un prgrama que lea el numero de payasos y muñecas vendidas en el ultimo pedido,calcule el peso total del
#paquete y calcular el precio total ,si por cada 100gr de payaso se cobra 3 pesos y por cada 100 gr de 
#muñera 2 pesos.

numeroPayasos = float(input("Ingrese el numero de payasos: "))
numeroMuñeca = float(input("Ingrese el numero de muñecas: "))

pesoPayasos = 112 * numeroPayasos
pesoMuñecas = 75 * numeroMuñeca

precioTotal = pesoPayasos / 100 * 3 + pesoMuñecas /100 * 2 
print(precioTotal)