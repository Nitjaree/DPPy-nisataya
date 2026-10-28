#!/usr/bin/python3
import sys


l = sys.argv
l.pop(0)
x = []
if len(l) != 2:
    print("none")
else:

    if l[0].isnumeric() and l[1].isnumeric:
        for i in range (int(l[0]),int(l[1])+1):
            x.append(i)

    else:
        print("Please input two number.")


print (x) 