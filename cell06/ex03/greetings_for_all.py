#!/usr/bin/python3
# your method definition here
def greetings(txt="noble stranger"):
    if type(txt) == int:
        print("Error! It was not a name.")
    else:
        print("Hello, " + txt + ".")
    return 




greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)