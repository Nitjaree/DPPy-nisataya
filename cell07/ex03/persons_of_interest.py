#!/usr/bin/python3
# your method definition here
def famous_births(dic):
    sdic = dict(sorted(dic.items(), key=lambda item: item[1]["date_of_birth"]))
    # print(sdic)
    for i in sdic:
        item = sdic[i]
        print(item["name"] , "is a great scientist born in",item["date_of_birth"])
    return
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)