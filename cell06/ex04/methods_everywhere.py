#!/usr/bin/python3
import sys

def shrink(txt):
    result = txt[:8]
    return result

def enlarge(txt):
    i=len(txt)
    result = txt
    for j in range (i,8):
        result += "Z"
    return result
    

l = sys.argv
l.pop(0)
if len(l) <= 0:
    print("none")
else:
    for item in l:
        if len(item) < 8:
            print(enlarge(item))
        elif len(item) > 8:
            print(shrink(item))
        else:
            print(item)
