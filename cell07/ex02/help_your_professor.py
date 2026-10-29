#!/usr/bin/python3
# your method definition here
def average(dic):
    sum=0
    for item in dic:
        sum = sum + float(dic[item])
    avg = sum/len(dic)   
    return avg

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13,
"aa": 20
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")