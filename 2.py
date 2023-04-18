'''
даны 2 отрезка a1 b1   a1 b2
вывести отрезок пересечение данного отрезка
'''
import random
from random import randint
a1=random.randint(0,10)
b1=random.randint(0,10)
a2=random.randint(0,10)
b2=random.randint(0,10)
print(a1,b1,a2,b2)
if (a2>b1) or (a1>b2):
    print('отрезки не перечекаются')
elif (a2>=a1) and (b2>=b1):
    print(f'пересечение отрезков[{a2},{b1}]')
elif (a1>=a2) and (b2>=b1):
    print(f'пересечение отрезков[{a2},{b1}]')
elif (a2>=a1) and (b2<=b1):
    print(f'пересечение отрезков[{a2},{b2}]')
