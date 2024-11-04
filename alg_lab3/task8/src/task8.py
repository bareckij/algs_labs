def find_k_closest_points(n, k, points):
    # Вычисляем расстояния и сортируем точки
    points_with_distance = [(x, y, x * x + y * y) for x, y in points]
    
    # Сортируем по расстоянию (третьему элементу кортежа)
    points_with_distance.sort(key=lambda p: p[2])
    
    # Извлекаем K ближайших точек
    closest_points = [(p[0], p[1]) for p in points_with_distance[:k]]
    
    return closest_points