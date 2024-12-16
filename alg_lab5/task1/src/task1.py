import utils

def is_non_decreasing_heap(n, arr):
    # Проверяем каждый элемент массива (кроме последнего уровня)
    for i in range(n // 2):
        # Проверка на левого потомка
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return "NO"
        # Проверка на правого потомка
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    print('lab5/task1')
    # Чтение входных данных
    n = utils.read_data_from_file('alg_lab5/task1/textf/input.txt')[0]
    arr = utils.read_data_from_file('alg_lab5/task1/textf/input.txt')[1]

    # Проверка на неубывающую пирамиду
    result = is_non_decreasing_heap(n, arr)
    print(result)
    # Вывод результата
    utils.write_data_to_file('alg_lab5/task1/textf/output.txt', result)