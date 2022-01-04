cities = ['homel', 'minsk', 'others', 'town']
print(cities)
print(len(cities))
cities[3] = 'Gomel'
cities.insert(0, 'mozir')
print(cities)

del cities[0]
print(cities)

cities.remove('homel')
print(cities)