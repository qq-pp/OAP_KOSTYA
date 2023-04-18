'''
даны три списка одинаковой длинны :
фамилии менеджеров магазина
список выручки каждого менаджера за месяц(от 10 до 50 тыс)
список премии

вывести список сатрудников и зарплату с начислиной премией (премия 15% если выручка больше 30 тыс)
'''


from faker import Faker
fake = Faker('ru_RU')
from pprint import  pprint

from random import randint
list = []
list1 = []
list2 = [30000] * 1.15
n = int(input('число менеджеров '))
for i in range(n):
    list.append(fake.name())
    list1.append(randint(10000, 50000))
def zp(list1):
    for i in range(list1):
        if i > 30000:




pprint(list)
pprint(list1)