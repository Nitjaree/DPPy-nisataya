#!/usr/bin/python3
x = input("Give me a number: ")
f = float(x)
i = int(f)
if f%i == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
