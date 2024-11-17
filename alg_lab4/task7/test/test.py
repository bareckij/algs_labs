import time
import tracemalloc
from alg_lab4.task7.src.task import sliding_window_maximum
from alg_lab4.task7.src.task import process_commands

import utils

def run_scarecrow_sort():
    """
    Функция для выполнения сортировки с измерением времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()
    n, arr, m = utils.read_data_from_file('alg_lab4/task7/textf/input.txt')
    # Получение результата
    result = sliding_window_maximum(arr, n, m)
    
    # Запись результата в output_file
    utils.write_data_to_file('alg_lab4/task7/textf/output.txt', result)
        # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")


def test_sliding_window_maximum():
    # Пример 1: Стандартный случай
    arr = [7, 7, 5, 6, 6, 2, 7, 3]
    n = 8
    m = 4
    expected_output = [7, 7, 6, 7, 7]  
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 2: Все элементы одинаковы
    arr = [4, 4, 4, 4, 4]
    n = 5
    m = 3
    expected_output = [4, 4, 4]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 3: Массив с одним элементом
    arr = [5]
    n = 1
    m = 1
    expected_output = [5]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 4: Массив с убывающими элементами
    arr = [9, 8, 7, 6, 5, 4]
    n = 6
    m = 3
    expected_output = [9, 8, 7, 6]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 5: Массив с возрастающими элементами
    arr = [1, 2, 3, 4, 5, 6]
    n = 6
    m = 2
    expected_output = [2, 3, 4, 5, 6]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 6: Строка с минимальными значениями
    arr = [0, 0, 0, 0, 0]
    n = 5
    m = 3
    expected_output = [0, 0, 0]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    # Пример 7: Максимальные значения в массиве
    arr = [100000, 99999, 99998, 100000]
    n = 4
    m = 2
    expected_output = [100000, 99999, 100000]
    result = sliding_window_maximum(arr, n, m)
    assert result == expected_output, f"Ошибка: ожидалось {expected_output}, но получено {result}"

    print("Все тесты прошли успешно!")

if __name__ == "__main__":
    # Запуск сортировки и измерений
    run_scarecrow_sort()

    # Запуск тестов
    test_sliding_window_maximum()
