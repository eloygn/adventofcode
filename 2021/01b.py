#!/usr/bin/env python3

#measurements = [199,200,208,210,200,207,240,269,260,263]
incremento = 0
i = 0
with open('input_01.txt') as f:
    measurements = list(map(int, f))

for i in range(len(measurements)):
    if sum(measurements[i:i+3]) < sum(measurements[i+1:i+4]):
        incremento= incremento + 1

print(incremento)
