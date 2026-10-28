#!/usr/bin/python3
import sys
listA = sys.argv
newList = []
if len(listA) == 1: 
    print("none")
else:
    listA.pop(0)
    for i in listA:
        newList.insert(0,i)
for i in newList :
    print(i)