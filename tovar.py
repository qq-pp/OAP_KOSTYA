from pprint import pprint

with open('tovar.txt', encoding='utf8') as f:
    tovar_input = []
    for line in f:
        tovar_input.append(line[:-1])

tovar_lst =[]
for t in tovar_input:
    tovar_lst.append(t.split(' '))
#pprint((tovar_lst))
quest = 'живая_рыба'
sum_total = 0
country = set()
for i in tovar_lst:
    if quest in i [0]:
        sum_total += float(i[1])
        country.add(i[2])
pprint(f'Товара "{quest}" экспортировано \ {sum_total} в {country}')