#tupla , conexiones ordenada e inmutable y permite datos duplucados

tupla= (1,2,3)
print(tupla)
print(type(tupla))

# no se pueden agregar mas elementos ni eliminarlos o modificarlos
#tupla[0] = 5

tupla = 1,2,('a','b'),3
print(tupla)
print(tupla[2][0])

tupla1 = 1,2,3
lista = list(tupla1)
lista.append(4)
tupla = tuple(lista)
print(tupla1)

for t in tupla1:
    print(t)
    
#x,y,z,a = tupla1
#print(x,y,z,a)


#tupla de un elemento
tupla2 = (2)
print(tupla2)
print(type(tupla2))

#metodos que se utilizan para las tuplas
tupla3 = (2,2,2,1,2,4,6)
print(tupla3.count(2))
#print(tupla3.index(0))

#LISTA , ES ORDENADA Y MUTABLE, PERMITE DUPLICADOS
lista = [1,2,3,4]
print(lista)
lista2=list("4567")
print(lista2)

#listas de listas
lista3 = [1,"2",["12",2,4]]
print(lista3[2][0])

print(lista3[-1])
lista3[2] = 10
print(lista3)

lista4 = [1,2,3,4,5,6,7]
print (lista4[0:2])
print(lista4[2:6])
lista4[0:3] = [0,0,0]
print(lista4)

#operaciones entre listas directamente
lista3 += lista4
print(lista3)

#ITERAR LISTA CICLO FOR
for l in lista3:
    print(l)
for index,l in enumerate(lista3):
    print(index,l)
    
lista5 = [1,2,3]
lista6 = ["A","B","C"]
for l1,l2 in zip(lista5,lista6):
    print(l1,l2)
    
for i in range(0,len(lista3)):
    print(lista3[i])

#METODOS DE LAS LISTAS

lista3.append(4)
lista3.extend([2,1])
lista3.insert(1,4) #inserta en cierta posicion y reocrre los demas
lista3.pop(1)
lista3.reverse() #inverte la lista
#lista3.sort() #ordena de ascendente o descendente
#lista3.sort(reverse=True) #el otro orden

#SET, COMO LISTAS PERO NO PERMITEN DUPLICADOS,es mutable e inmutable a la vez ,no se puede modificar lo que ya este escrito

#siempre estyan ordenados de manera ascendente
set={1,2,4,3}
print(set)
set.add(9)
print(set)


#set2 = set([2,3,4,5,1,2])
#print(set2)

listax = ["a","b","c"]

#for s in set2:
#    print(s)
#se pueden hacer union , interseccion etc
s1={1,2,3}
s2={3,5,6}
print(s1^ s2)

#metodos de los set
s1.add(1)
s1.remove(3) #elimina elementos si es que existe, o manda un error si no lo encuentra
s1.discard(7) #elimina , pero si no existe no hace nada
s1.pop() #elimin al azar 
s1.clear() #remueve todos los elementos
s1.union()
s1.intersection()