#!/usr/bin/python3

def add_one(item):
    global value 
    value = item + 1
    # item = item+1
    return 
    
value = 42
print(f"Begin value {value}")
add_one(value)
print(f"Later value {value}")
