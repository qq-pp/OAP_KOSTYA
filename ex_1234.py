'''
записать в файл f N челых чисел полученых с помощью генератора целых чисел
из файла f получить файл g исключив повторное вхождение чисел
в файле g подсчитать сумму нечетных элементов значения которых превышает среднее по этому файлу
'''
import random

def chislo_1 (file_f, file_g):
    a = []
    with open(file_f) as f:
        for line in f:
            b = line
            if b in a:

                continue
            else:

                a.append(b)
    with open(file_g, 'w') as g:
        g.writelines(a)


n=10

with open('f.txt', 'w') as f:
    for i in range(n):
        f.write(str(random.randint(0, 10))+'\n')

chislo_1("f.txt", "g.txt")

def summa(file_g):
    b=[]

    with open(file_g) as g:
        for line in g:
            b.append(int(line[:-1]))

    a = sum(b)/n
    print(f'сруднее значение файла: {a}')
    c=0

    for i in b:
        if i % 2 == 0:
            continue
        else:
            if i > a:
                c += i

    print(f'сумма чисел больше значения файла: {c}')