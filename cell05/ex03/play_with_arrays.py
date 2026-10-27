#!/usr/bin/python3

oArray = [2, 8, 9, 48, 8, 22, -12, 2]
nArray = []

for item in oArray:
    if item > 5:
        nArray.append(item+2)
        
nSet = set(nArray)

print(oArray)
print(nSet)

