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

suma = 0
for i in range(len(lista)):
    distancia = abs(int(lista[i]) - mediana)
    suma = suma + distancia 
    print(lista[i],distancia,suma)
print(suma)
