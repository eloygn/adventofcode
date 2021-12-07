#!/usr/bin/env python3
import statistics

lista=[16,1,2,0,4,2,7,1,2,14]

file1 = open("input_07.txt", "r")
lista1 = file1.read()
lista1 = lista1[:-1]
lista = lista1.split(",")
file1.close()

print(lista)
mediana = statistics.median(list(map(int,lista)))
print(int(mediana))

nuevamediana = 0
nuevalista = []
print(max(lista))

def calc_distancia(medianatest,lista):
    suma = 0
    for i in range(len(lista)):
        distancia = abs(int(lista[i]) - medianatest)
        suma = suma + (distancia * ( distancia + 1) / 2 )
    return(suma)

for j in range(int(max(lista))):
    nuevalista.append(calc_distancia(j,lista))

k = int(min(nuevalista))
print(k)

