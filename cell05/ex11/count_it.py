#!/usr/bin/python3
import sys

l = sys.argv
l.pop(0)
if len(l) <= 0:
    print("none")
else:
    print(f"parameters: {len(l)}")
    for item in l:
        print(f"{item}: {len(item)}")
