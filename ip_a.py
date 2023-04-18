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

ip_4 = input('Пример:(Парфехин ДГ): ')

for i,e in enumerate(ip_3):
    n = f'{e[0]} {e[1][:1]}{e[2][:1]}'
    if ip_4 == n:
        print(f'{e[0]} {e[1][:1]}{e[2][:1]} - {ip_2[i][-1]}')
