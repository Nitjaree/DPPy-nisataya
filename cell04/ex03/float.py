#!/usr/bin/python3
x = input("Give me a number: ")
f = float(x)
i = int(f)
if f%i == 0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")

# if type(x) == int:
#     print("This number is an integer.")
# elif type(x) == float:
#     print("This number is a decimal.")
# else:
#     print("Error!")