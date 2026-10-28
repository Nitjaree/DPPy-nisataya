#!/usr/bin/python3
import sys
def downcase_it(txt):
    return txt.lower()

l = sys.argv
l.pop(0)
if len(l)==0:
    print("none")
else:
    for item in l:
        print(downcase_it(item)) 