'''
заполнить текстовый файл числовыми значениями сгенерированный датчиком случайных чисел
просумировать все элементы данного файла
'''

import random
def sum_nuber_in_file(file_input):
    """
    нахождение суммы
    :param file_input: имя файла с числами
    :return:
    """
    s = 0
    with open(file_input) as f:
        for line in f:
            b = int(line)
            s += b
        return(s)
n = 10
from random import randint
with open('ex_files_02.txt','w') as f:
    for i in range(n):
        f.write(str(random.randint(0,100))+'\n')
print(f'сумма всех элементов файла равна \
{sum_nuber_in_file("ex_files_02.txt")}')













