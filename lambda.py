people = [
    {"name": "John", "house": "ctg"},
    {"name": "trk", "house": "dhaka"},
    {"name": "rana", "house": "barisal"}
]

# 1st way to call a function
# def f(person):
#     return person["name"]

# people.sort(key=f)

# 2nd way to call a function


people.sort(key=lambda person: person["name"])


print(people)


# if im sorting like people.sort then python does not sort so we have to declare a function...
