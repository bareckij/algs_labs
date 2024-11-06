def h_index(citations):
    # Сортируем список цитирований по убыванию
    citations.sort(reverse=True)
    
    # Ищем индекс Хирша
    h = 0
    for i, c in enumerate(citations):
        # Если количество цитирований больше или равно индексу, увеличиваем h
        if c >= i + 1:
            h = i + 1
        else:
            break  # Если условие не выполняется, дальше искать не нужно
    
    return h
