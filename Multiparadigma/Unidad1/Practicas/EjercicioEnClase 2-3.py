#Una chocolateria lanzara un nuevo producto el cual viene presentado en barras de Nsegmentos
#las barras N segmentos ,solo vienen en tamaños que son potencia de 2 (1,2,4,8,16)
#realizar un programa para realizar una prueba de calidad de dicho producto 
#pero para ello tines que probar M segmentos , el problema es que la barra solo se puede partir a la mitad
#dicho programa determinara el numero de veces que quebraras la barra 
#para obtener M segmentos exactamente, La salida sera el tam;ano minimo de la barra que se tendra que pedir para
# para probar cada segmento y el segundo numero es el numero de veces que tienes que partir la barra

Probar = int(input("Ingrese N: "))
potenciaR = 1

while Probar >= potenciaR:
    potenciaR = potenciaR * 2
    
print("Tableta de ",potenciaR)

PartesObtenidas = 0
VecesPartida = 0
Tempo = potenciaR

while Probar != PartesObtenidas:
    VecesPartida += 1
    Tempo = int(Tempo / 2)
    
    if Tempo + PartesObtenidas == potenciaR:
        break
    else:
        if Tempo + PartesObtenidas  < potenciaR:
            PartesObtenidas = PartesObtenidas +  Tempo
            print(PartesObtenidas)
            continue
        else:
            break
    
print("Veces partida: ",VecesPartida)