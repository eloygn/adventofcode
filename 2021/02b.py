#!/usr/bin/env python3

incremento_x = 0
incremento_y = 0
aim = 0

file1 = open('input_02.txt', 'r')
 
while True:
    line = file1.readline()
 
    # if line is empty, end of file is reached
    if not line:
        break
 
    if line.startswith('forward'):
        line = line.rstrip("\n")
        line = line.split(" ", 1)
        incremento_x = incremento_x + int(line[1])
        aim_calc = aim * int(line[1])
        incremento_y = incremento_y + aim_calc
    else:
        if line.startswith('up'):
            line = line.rstrip("\n")
            line = line.split(" ", 1)
            aim = aim - int(line[1])
        else:
            if line.startswith('down'):
                line = line.rstrip("\n")
                line = line.split(" ", 1)
                aim = aim + int(line[1])
file1.close()

total = abs(incremento_x * incremento_y)
print (total)

