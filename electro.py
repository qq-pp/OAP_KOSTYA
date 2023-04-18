import csv

with open('electro.csv') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        fio, *e = row
        e_1 = [int(x) for x in e]
        print(f'{fio} {sum(e_1)} KBt')