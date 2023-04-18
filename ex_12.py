'''
вычеслить расстояние между двумя точками с заданными координатами (x1,y1) и (x2,y2)
вычисление расстояния должно быть выполнено в функции point_distance
'''
import math
def point_distance(x1, y1, x2, y2):
    s = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return s
point_list = [[1, 2, 3, 4], [2, 5, 3, 7]]
for points in point_list:
    print(f'переменные {points}')
    distance = point_distance(points[0], points[1], points[2], points[3])
    print(f'расстояние {distance:.2f}')