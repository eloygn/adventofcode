#!/usr/bin/env python3

file_in = open('input_03.txt')
data = file_in.read().splitlines()
file_in.close

binary_list = data
co2_list = data

length_list = len(binary_list)
length_string = len(binary_list[0])

def mostcommonvalue(i, lista):
    zero = one = 0
    for j in lista:
        if int(j[i]) == 0:
            zero += 1
        else:
            one += 1
    if one >= zero:
        return 1
    else:
        return 0


def leastcommonvalue(i, lista):
    zero = one = 0
    for j in lista:
        if int(j[i]) == 0:
            zero += 1
        else:
            one += 1
    if one >= zero:
        return 0
    else:
        return 1

def elegirvalores(i,lista,empiezapor):
    if len(lista) > 1:
        nuevalista = [x for x in lista if int(x[i])==empiezapor]
        return(nuevalista)
    else:
        return(lista)

for i in range(12):
    binary_list = elegirvalores(i,binary_list,mostcommonvalue(i,binary_list))
    co2_list = elegirvalores(i,co2_list,leastcommonvalue(i,co2_list))

print(int(co2_list[0], 2))
print(int(binary_list[0], 2))

print(int(co2_list[0], 2) * int(binary_list[0], 2))

