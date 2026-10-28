#!/usr/bin/python3
x = input("Give me a number: ")
if x.isnumeric():
    f = float(x)
    if f.is_integer:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("This is not numeric.")

