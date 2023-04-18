from pprint import pprint

with open('ip_a.txt', "r", encoding='utf8') as f:
    ip_1 = []
    for line in f:
        ip_1.append(line[:-1])

ip_2 =[]
for t in ip_1:
    ip_2.append(t.split('\t'))

ip_3=[]
for i in ip_2:
    ip_3.append(i[0].split())

IP=[]
for i in ip_2:
    IP.append(i[1].split('.'))
ip_4=[]
Ip1=input('Пример:(Парфехин ДГ): ')
Ip2=input('Пример:(Кунец СТ): ')

for i,e in enumerate(ip_3):
    n = f'{e[0]} {e[1][:1]}{e[2][:1]}'
    if Ip1==n:
        ip_3=int(IP[i][2])
    elif Ip2==n:
        ip_4 = int(IP[i][2])

if ip_3==1:
    print('accept')
else:
    if ip_3 == 2 and  ip_4==1 or 4 or 5:
        print('dineid')
    elif ip_3 == 2 and  ip_4==1 or 2 or 5:
        print('dineid')
    elif ip_3 == 3 and  ip_4== 1 or 5:
        print('dineid')
    elif ip_3 == 5 and  ip_4== 4 or 5:
        print('dineid')