#!/usr/bin/python3
import sys


l = sys.argv
l.pop(0)
if len(l) == 0:
    print("none")
else:
    for i in l:
       if not(i.endswith("ism")):
           print(f"{i}ism")
    
 