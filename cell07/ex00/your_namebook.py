#!/usr/bin/python3


def array_of_names(dic):
    n = []
    for first_name in dic:
        last_name = dic[first_name]
        full_name = str(first_name) + " " + str(last_name)

        n.append(full_name.capitalize())
    return n
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
# print(persons)
# print(type(persons))
print(array_of_names((persons)))