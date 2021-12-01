#!/usr/bin/env python3

#measurements = [199,200,208,210,200,207,240,269,260,263]
incremento = 0

with open('input_01.txt') as f:
    #measurements = f.read().splitlines()
    measurements = list(map(int, f))

for i in range(1, len(measurements)):
    if measurements[i - 1] < measurements [i]:
        incremento = incremento + 1
        print (i,measurements[i],measurements[i - 1],"+1")
    else:
        print (i,measurements[i],measurements[i - 1])

print(incremento)
