#!/usr/bin/python3
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    password = sys.argv[1]
    x=input("What was the parameter? ")
    if x == password:
        print("Good job!")
    else:
        print ("Nope, sorry...")