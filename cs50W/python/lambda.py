people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Mike", "house" : "Melton"},
    {"name": "Bill", "house" : "Kicks"}
]


# def f(person):
#     return person["name"]
# people.sort(key=f)

people.sort(key=lambda person: ["name"]) # Function that takes a person as input and returns their name

print(people)