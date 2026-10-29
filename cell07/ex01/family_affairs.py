#!/usr/bin/python3
def find_the_redheads(dic):
    n = []
    for first_name in dic:
        head = dic[first_name]
        if head == "red":
            n.append(first_name)

    return n

    
# your method definition here
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))