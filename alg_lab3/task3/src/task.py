def scarecrow_sort(n, k, sizes):
    # Создание групп
    groups = [[] for _ in range(k)]
    
    # Разделение элементов на группы по индексу % k
    for i in range(n):
        groups[i % k].append(sizes[i])
    
    # Сортировка каждой группы
    for group in groups:
        group.sort()
    
    # Пересборка отсортированного массива
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])
    
    # Проверка, совпадает ли итоговый массив с отсортированным
    return sorted_sizes == sorted(sizes)
