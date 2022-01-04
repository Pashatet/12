""" x = 10
if (x == 1):
    print('hellp')
elif (x > 3 and x < 5):
    print('pasha')
else:
    x='you are next'
    print(x)

print('ASDASD') """

cars = ['lada', 'bmw', 'mersede', 'volfswagen', 'toyota', 'audi', 'seat']
germans_cars = ['bmw', 'mersedes', 'volfswagen', 'audi']
for x in cars:
    if x in germans_cars:
        print(x + ' is german car')
    else:
        print(x + ' not german car')
