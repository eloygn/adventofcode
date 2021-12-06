#!/usr/bin/env python3

file_in = open('input_03.txt')
data = file_in.read().splitlines()
file_in.close

oxy_data = data
co2_data = data


def find_most_common(index, data_list):
    zero = one = 0
    for i in data_list:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1
    if one >= zero:
        return 1
    else:
        return 0


def find_least_common(index, data_list):
    zero = one = 0
    for i in data_list:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1
    if one >= zero:
        return 0
    else:
        return 1


def remove_mismatch(reference, index, data_list):
    if len(data_list) > 1:
        new_data_list = [i for i in data_list if int(i[index]) == reference]
        return new_data_list
    else:
        return data_list


for x in range(12):
    oxy_data = remove_mismatch(find_most_common(x, oxy_data), x, oxy_data)
    co2_data = remove_mismatch(find_least_common(x, co2_data), x, co2_data)


print(int(co2_data[0], 2) * int(oxy_data[0], 2))
