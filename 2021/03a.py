#!/usr/bin/env python3

i = 0
gamma = []
epsilon = []
power_consumption = 0

with open('input_03.txt') as f:
    binary_list = list(map(list, f))

length_list = len(binary_list)
length_string = len(binary_list[0]) - 1

for i in range(length_string):
    count = 0
    for elem_list in range(len(binary_list)):
        str1 = binary_list[elem_list]
        count = count + int(str1[i])
    if count / length_list > 0.5:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma2 = ''.join(gamma)
epsilon2 = ''.join(epsilon)
gamma3 = int(gamma2,2)
epsilon3 = int(epsilon2,2)
power_consumption = gamma3 * epsilon3
print (power_consumption)

