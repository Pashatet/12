person = {
    'pasha': 80,
    'sasha': 70,
    'vlad': 'green',
    'vladislav': 83,
}
print(person)

print('вес саши ' + str(person['sasha']))
print('цвет влада ' + person['vlad'])
person['papasha'] = 'jopa'
print(person)
print('--------------------------------')
person['papasha'] = '11'
print(person)
print('--------------------------------')
del person['papasha']
print(person)
print('--------------------------------')
person['pasha'] = person['pasha'] + 50
print(person)
