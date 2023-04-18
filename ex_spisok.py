'''
дан список из n элементов значения котрого генерируются случайным образом в диапозоне от 0 до 30
подсчитать среднее арефметическое элементов значения которых больше 15
вывести среднее и эти элементы
'''
from random import randint
n = int(input('n='))
lst = []
chisla = []
for i in range(n):
    lst.append(randint(0, 30))

def sred(lst):
    a=0
    b=0
    for i in lst:
        if i > 15:
            a += i
            chisla.append(i)
            b += 1
    c = a/b
    return c, chisla
print(lst)
print(sred(lst))



