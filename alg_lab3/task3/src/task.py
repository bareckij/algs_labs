import utils 
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

if __name__ == '__main__':
    data = utils.read_data_from_file('alg_lab3/task3/textf/input.txt')
    n, k = data[0]  # первое число - количество элементов n, второе - количество групп k
    sizes = data[1]  # второй элемент - сам список с размерами

    # Выполнение алгоритма
    if scarecrow_sort(n, k, sizes):
        result = "Yes"
    else:
        result = "No"

    # Запись результатов в файл
    utils.write_data_to_file('alg_lab3/task3/textf/output.txt', result)
    print('Задание 3\n',  utils.read_data_from_file('alg_lab3/task3/textf/output.txt'))