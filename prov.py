'''
в службе поддержки провайдера работает 4 сотрудника
каждому из них выставляется оценка клиентом после обращения в службу поддержки
проранжировать в порядке убывания средней оценки данных сотрудников (10 оценок от 0 до 5)
'''
from faker import Faker
fake = Faker('ru_RU')
from pprint import  pprint
from random import randint

lst=[]

lsta=[]
lstb=[]
lstc=[]
lstd=[]

for i in range(10):
    lsta.append(randint(0, 5))
    lstb.append(randint(0, 5))
    lstc.append(randint(0, 5))
    lstd.append(randint(0, 5))
for i in range(4):
    lst.append(fake.name())

lst1=sum(lsta)/len(lsta)
lst2=sum(lstb)/len(lstb)
lst3=sum(lstc)/len(lstc)
lst4=sum(lstd)/len(lstd)
sum1=[lst1,lst[0]]
sum2=[lst2,lst[1]]
sum3=[lst3,lst[2]]
sum4=[lst4,lst[3]]
suma=[sum1,sum2,sum3,sum4]
suma.sort()
suma.reverse()
pprint(suma)










