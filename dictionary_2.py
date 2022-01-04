person = {
    'pasha': 80,
    'sasha': 70,
    'vladislav': 83,
}

person_color = {
    'pasha': 'red',
    'sasha': 'yellow',
    'vladislav': ['blue', 'red', 'grean']
}

all_person = []

# all_person.append(person.copy())
# all_person.append(person_color.copy())
# print(all_person)
sss='----------------------------------------------------------------------------------------------------------'

print(sss)

for x in range(0, 3):
    all_person.append(person.copy())
    all_person.append(person_color.copy())
for x in all_person:
    print(x)

print(sss)
all_person[2]['pasha'] = [111,121]
all_person[0]['sasha'] = 'grean'
for x in all_person:
    print(x)