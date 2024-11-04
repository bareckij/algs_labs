def scarecrow_sort(n, k, sizes):
    # Создаем список групп
    groups = [[] for _ in range(k)]
    
    # Заполняем группы
    for i in range(n):
        groups[i % k].append(sizes[i])
    
    # Сортируем каждую группу
    for group in groups:
        group.sort()
    
    # Собираем отсортированный массив
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])
    
    # Проверяем, совпадает ли отсортированный массив с оригинальным
    return sorted_sizes == sorted(sizes)