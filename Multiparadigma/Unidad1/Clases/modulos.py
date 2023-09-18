import csv
import random
from csv import DictReader #Solo traer una parte del modulo o libreria


numRandom = random.randint(0,100)

while True:
    numero = int(input("cual sera el numero entre 0 y 100:"))
    if numero == numRandom:
        break
    if numero > numRandom:
        print("El numero es mayor")
    else:
        print("El numero es menor")
print("El numero era {numRandom}")

#Utilizar with y buscar explicacion
#EJEMPLO CALSE 5
def pslit(inputFile,):
    with,open(Input(File,'f')) as file:
        header = file.readLine().string()
        outPutFile.None