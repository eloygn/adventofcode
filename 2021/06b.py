#!/usr/bin/env python3

lista=[3,4,3,1,2]

file1 = open("input_06.txt", "r")
lista1 = file1.read()
lista1 = lista1[:-1]
lista = lista1.split(",")
file1.close()

lista0 = sum(map(lambda i : int(i) == 0, lista))
lista1 = sum(map(lambda i : int(i) == 1, lista))
lista2 = sum(map(lambda i : int(i) == 2, lista))
lista3 = sum(map(lambda i : int(i) == 3, lista))
lista4 = sum(map(lambda i : int(i) == 4, lista))
lista5 = sum(map(lambda i : int(i) == 5, lista))
lista6 = sum(map(lambda i : int(i) == 6, lista))
lista7 = sum(map(lambda i : int(i) == 7, lista))
lista8 = sum(map(lambda i : int(i) == 8, lista))

print(lista0,lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8)

i=0
for i in range(256):
    antiguos = lista0
    lista0 = lista1
    lista1 = lista2
    lista2 = lista3
    lista3 = lista4
    lista4 = lista5
    lista5 = lista6
    lista6 = lista7 + antiguos
    lista7 = lista8
    lista8 = antiguos

print(lista0+lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8)
