'''
Определить жанр, лидирующий по продажам в каждом регионе
'''
import csv
from pprint import pprint


def sorted_genre(d):

    sorted_tuple = sorted(d.items(), key=lambda x: x[1],reverse=True)
    return dict(sorted_tuple)

genre = {}
us = {}
eu = {}
jp = {}
ot = {}
with open('games.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        g = row[3]
        if g not in us.keys() and \
                g not in eu.keys() and \
                g not in jp.keys() and \
                g not in ot.keys():
            us[g] = float(row[4])
            eu[g] = float(row[5])
            jp[g] = float(row[6])
            ot[g] = float(row[7])
        else:
            us[g] = us[g] + float(row[4])
            eu[g] = eu[g] + float(row[5])
            jp[g] = jp[g] + float(row[6])
            ot[g] = ot[g] + float(row[7])
print('-'*80)
pprint(sorted_genre(us))
pprint(sorted_genre(eu))
pprint(sorted_genre(jp))
pprint(sorted_genre(ot))
print('-'*80)
print(f'US - {list(sorted_genre(us).keys())[0]}')
print(list(sorted_genre(eu).keys())[0])
print(list(sorted_genre(jp).keys())[0])
print(list(sorted_genre(ot).keys())[0])

