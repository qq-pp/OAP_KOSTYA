'''
даны 2 списка list1 список фамилий, list2 содержит вложеные списки с оценками за экзамен (5 штук для каждого)
создать функцию для расчета среднего балла за экзамен           sr_bal
'''
def sr_bal(a, b, c, d, f):
    sred = (a + b + c + d + f)/5
    return sred

def sr_bal1(lst):
    sred = 0
    for ball in lst:
        sred += ball
    sred = sred / 5.0
    return sred

list1 = ('ivanov', 'popov')
list2 = [[4, 2, 3, 4, 5], [5, 5, 3, 4, 2]]
for i in range(0, len(list1)):
    sred = sr_bal(list2[i][0], list2[i][1], list2[i][2], list2[i][3], list2[i][4])
    print(f'{list1[i]} {sred}')