#!/usr/bin/python3
import sys
import re

l = sys.argv
l.pop(0)
if len(l) != 1:
    print("none")
else:
    count = len(re.findall("z",l[0]))
    if count == 0:
        print("none")
    else:
        for i in range(0,count):
            print("z", end="")
        print()

 