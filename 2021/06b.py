#!/usr/bin/env python3

lista=[3,4,3,1,2]

file1 = open("input_06.txt", "r")
lista1 = file1.read()
lista1 = lista1[:-1]
lista = lista1.split(",")
file1.close()
print(lista)

for i in range(256):
    for j in range(len(lista)):
        #print(lista[j])
        lista[j] = int(lista[j]) - 1
        if lista[j] < 0:
            lista[j] = 6
            lista.append(8)
print(len(lista))
