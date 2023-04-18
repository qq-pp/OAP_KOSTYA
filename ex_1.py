'''
доно 2 списка из n элементов значения которых генерировано случайным образом диапозон от 0 до 50
необходими вернуть список состоящий из элементов общих этих 2 списков

создать из 2 списков новые 2 списка
в 1 содержатся нечетные числа из обоих списков
в 2 содержатся четные числа из обеих списков

дан список из n чисел и число k больше 10000
создать список из элементов исходного списка которые являются делителями числа k
'''

'''
from random import randint
n = int(input('n='))
lst = []
lst1 = []
lst2 = []
lst3 = []
lst_a = []
lst_b = []
for i in range(n):
    lst1.append(randint(0, 50))
    lst2.append(randint(0, 50))
for i in lst1:
    if i in lst2:
        if i not in lst:
            lst.append(i)


for i in lst1:
    if i not in lst3:
        lst3.append(i)
for i in lst2:
    if i not in lst3:
        lst3.append(i)

for i in lst3:
    d = i % 2
    if d == 0:
        lst_a.append(i)
    else:
        lst_b.append(i)



def unique(lst):
    result = []
    for elem in lst:
        if elem in result:
            continue
        else:
            result.append(elem)
    return result

#t=unique(lst)
#print(lst1)
#print(lst2)
#print(lst)
#print(t)

print(lst_a)
print(lst_b)
'''


























