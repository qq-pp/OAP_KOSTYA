'''
def square_tringle(sa,sb,sc):
    """

    :param sa:
    :param sb:
    :param sc:
    :return: square
    """


'''
#создать программу для вычисления площади треугольника, в основе программы запрашивать стороны площадь треугольника расчитывается в функции
'''
import math
def square_triangle(a,b,c):
    if a >= b + c or b >= a + c or c >= a + b:
        return 0
    p = (a + b + c) / 2.0
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
a=int(input('первая сторона '))
b=int(input('вторая сторона '))
c=int(input('третья сторона '))
print(square_triangle(a,b,c))
'''
'''
создать функцию которая по введенному ip адресу возвращает сетевой ip адрес 
в работе можно использовать следующие: s.split()-разделяет строки на элементы 
'''
