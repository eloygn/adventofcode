#!/usr/bin/env python3
import statistics

lista=[16,1,2,0,4,2,7,1,2,14]

file1 = open("input_04.txt", "r")
lista1 = file1.readline()
lista1 = lista1[:-1]
lista = lista1.split(",")
lista = list(map(int,lista))
print(lista)

lista2 = file1.readlines()
lista2 = [s.rstrip() for s in lista2 if s != '\n']
print(lista2)
print(len(lista2))
file1.close()


#lista = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]






