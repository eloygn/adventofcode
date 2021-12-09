#!/usr/bin/env python3
import numpy as np

with open('input_09.txt') as f:
    cadena = f.read().splitlines()

for i in range(len(cadena)):
    res = [int(x) for x in str(cadena[i])]
    cadena[i] = res
#print(cadena)



def buscar_adyacentes(cadena,i,j):
    adyacentes = [9,9,9,9]     #superior,derecho,izquierdo,inferior
    margen_derecho = len(cadena)
    margen_inferior = len(cadena[i])
    print("buscando para i=",i,"y j=",j,"margen_dcho:",margen_derecho,"margen_inferior:",margen_inferior)
    #busco adyacente superior
    if i == 0:
        adyacentes[0] = 9
    else:
        adyacentes[0] = cadena[i-1][j]

    #busco adyacente derecho
    if j == margen_derecho - 1:
        adyacentes[1] = 9
    else:
        adyacentes[1] = cadena[i][j+1]

    #busco adyacente izquierdo
    if j == 0:
        adyacentes[2] = 9
    else:
        adyacentes[2] = cadena[i][j-1]

    #busco adyacente inferior
    if i == margen_inferior - 1:
        adyacentes[3] = 9
    else:
        adyacentes[3] = cadena[i+1][j]

    print("adyacentes:",adyacentes)
    menor_de_adyacentes = min(adyacentes)
    print("menor de adyacentes:",menor_de_adyacentes)
    print("------")
    return (menor_de_adyacentes)

risk_level = 0
for i in range(len(cadena)):
    for j in range(len(cadena[i])):
        height = cadena[i][j]
        print("el peso de i=",i,"j=",j,"es",height)
        menor_de_adyacentes = buscar_adyacentes(cadena,i,j)
        if height < menor_de_adyacentes:
            risk_level = risk_level + (1 + height)
print(risk_level)
