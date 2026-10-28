#!/usr/bin/python3

def add_one(item):
    return item+1
    
i = [2,4,5,7,8,2, 8, 9, 48, 8, 22, -12, 2]
for item in i:
    print(f"Pass {item} to function add_one and it returns {add_one(item)} result")

# test input