import math

def find_k_nearest_points(points, k):
    # Сортируем точки по расстоянию до начала координат
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]

