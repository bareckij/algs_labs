import time
import tracemalloc
from alg_lab3.task3.src.task import scarecrow_sort
import utils

def run_scarecrow_sort():
    """
    Функция для выполнения сортировки с измерением времени и памяти.
    """
    tracemalloc.start() 
    t_start = time.perf_counter()

    # Чтение входных данных
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

    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")


def test_scarecrow_sort():
    """
    Функция для тестирования алгоритма scarecrow_sort.
    """
    # Пример 1: Обычный случай
    sizes = [2, 1, 3]
    n = 3
    k = 2
    expected = False  # Мы ожидаем False, так как невозможно отсортировать
    assert scarecrow_sort(n, k, sizes) == expected, "Тест 1 не пройден!"

    # Пример 2: Пустой список
    sizes = []
    n = 0
    k = 1
    expected = True  # Пустой список всегда отсортирован
    assert scarecrow_sort(n, k, sizes) == expected, "Тест 2 не пройден!"

    # Пример 3: Все элементы одинаковые
    sizes = [7, 7, 7, 7]
    n = 4
    k = 2
    expected = True  # Список из одинаковых элементов всегда отсортирован
    assert scarecrow_sort(n, k, sizes) == expected, "Тест 3 не пройден!"

    # Пример 4: Сортировка должна быть ложной
    sizes = [3, 1, 4, 2]
    n = 4
    k = 2
    expected = False  # Невозможно отсортировать с разбиением на 2 группы
    assert scarecrow_sort(n, k, sizes) == expected, "Тест 4 не пройден!"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    # Запуск сортировки и измерений
    run_scarecrow_sort()

    # Запуск тестов
    test_scarecrow_sort()
