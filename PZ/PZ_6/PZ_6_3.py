# Дано множество А из N точек на плоскости и точка В (точки заданы своими
# координатами х, у). Найти точку из множества А, наиболее близкую к точке В.
# Расстожше R между точками с координатами (XI, у) и (м, у) вычисляется по формуле: R = 4х2 - х1)2 + (у2 - у1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй — для хранения ординат.
import math


def find_closest_point(A, x, y):
    min_distance = float('inf')
    closest_point = None

    for point in A:
        distance = math.sqrt((point[0] - x) ** 2 + (point[1] - y) ** 2)

        if distance < min_distance:
            min_distance = distance
            closest_point = point

    return closest_point



points = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(points)
target_x = int(input("Ввести значение Х: "))
target_y = int(input("Ввести значение Y: "))

closest = find_closest_point(points, target_x, target_y)
print(closest)