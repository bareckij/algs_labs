import time
import tracemalloc
from alg_lab3.task1.src.task1 import randomized_quick_sort
import utils

def run_sorting():
    """
    Функция для выполнения сортировки и измерения времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Чтение входных данных
    n, arr = utils.read_data_from_file('alg_lab3/task1/textf/input.txt')

    # Сортировка массива
    sorted_arr = randomized_quick_sort(arr, 0, n - 1)

    # Запись результатов в файл
    utils.write_data_to_file('alg_lab3/task1/textf/output.txt', sorted_arr)

    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")

def test_randomized_quick_sort():
    """
    Функция для тестирования алгоритма сортировки.
    """
    # Пример 1: Простая сортировка
    test_arr = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]
    assert randomized_quick_sort(test_arr, 0, len(test_arr) - 1) == expected, "Тест 1 не пройден!"

    # Пример 2: Пустой список
    test_arr = []
    expected = []
    assert randomized_quick_sort(test_arr, 0, len(test_arr) - 1) == expected, "Тест 2 не пройден!"

    # Пример 3: Уже отсортированный список
    test_arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert randomized_quick_sort(test_arr, 0, len(test_arr) - 1) == expected, "Тест 3 не пройден!"

    # Пример 4: Список с одинаковыми элементами
    test_arr = [7, 7, 7, 7, 7]
    expected = [7, 7, 7, 7, 7]
    assert randomized_quick_sort(test_arr, 0, len(test_arr) - 1) == expected, "Тест 4 не пройден!"

    print("Все тесты прошли успешно!")

if __name__ == "__main__":
    # Запуск сортировки и измерений
    run_sorting()

    # Запуск тестов
    test_randomized_quick_sort()