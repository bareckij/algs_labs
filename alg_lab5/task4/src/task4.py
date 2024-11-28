import utils

def min_heapify(arr, n, i, swaps):
    smallest = i  # Инициализируем наименьший элемент как текущий узел
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок существует и меньше текущего элемента
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Если правый потомок существует и меньше текущего элемента
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Если наименьший элемент не текущий, меняем местами и рекурсивно применяем heapify
    if smallest != i:
        # Перестановка
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))  # Сохраняем перестановку
        min_heapify(arr, n, smallest, swaps)

def build_min_heap(arr):
    n = len(arr)
    swaps = []  # Список для хранения свопов
    # Начинаем с последнего узла, который имеет потомков, и идем до корня
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i, swaps)
    return swaps

# Основная логика
if __name__ == "__main__":
    n = utils.read_data_from_file('alg_lab5/task4/textf/input.txt')[0]
    arr = utils.read_data_from_file('alg_lab5/task4/textf/input.txt')[1]
    swaps = build_min_heap(arr)    
    # Вывод результата
    utils.write_data_to_file('alg_lab5/task4/textf/output.txt', (len(swaps),'\n',swaps))