people = [
    ["Tom",29],
    ["Alice", 33],
    ["Bob", 27]
]

person = list()
person.append("Bill")
person.append(41)

people.append(person)
print(people[-1])

people[-1].append("+89324177411")
print(people[-1])

people[-1].pop()
print(people[-1])

people[0] = ["Sam", 18]
print(people)

for person in people:
    for item in person:
        print(item,end=" /|\ ")