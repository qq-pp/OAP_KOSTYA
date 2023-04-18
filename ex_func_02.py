'''
создать программу для вычисления площадей треугольников, стороны которых хранятся в списке list_side
'''
import math
def square_triangle(a,b,c):
    if a >= b + c or b >= a + c or c >= a + b:
        return 0
    p = (a + b + c) / 2.0
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
list_side = [[3, 4, 5], [5, 8, 10], [12, 15, 7], [10, 2, 3], ['a', 'b','c']]
for triangle in list_side:
    print(f'стороны текущего треугольника {triangle}')
    square = square_triangle(triangle[0], triangle[1], triangle[2])
    if square:
        print(f'площадь треугольника равна {square:.2f}')
    else:
        print(f'треугольник не существует')