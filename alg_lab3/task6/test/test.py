import time
import tracemalloc
from alg_lab3.task6.src.task import sum_of_every_tenth_product
import utils

def run_sum_of_every_tenth_product():
    """
    Функция для выполнения вычисления суммы каждого десятого произведения с измерением времени и памяти.
    """
    # Начинаем отслеживание памяти
    tracemalloc.start()
    t_start = time.perf_counter()

    # Чтение данных из файла
    try:
        data = utils.read_data_from_file('alg_lab3/task6/textf/input.txt')
        arr_a = data[1]  # Первый массив
        arr_b = data[2]  # Второй массив
    except Exception as e:
        print(f"Ошибка при чтении данных из файла: {e}")
        return

    # Вычисление суммы каждого десятого произведения
    try:
        result = sum_of_every_tenth_product(arr_a, arr_b)
    except Exception as e:
        print(f"Ошибка при вычислении суммы каждого десятого произведения: {e}")
        return

    # Запись результата в файл
    try:
        utils.write_data_to_file('alg_lab3/task6/textf/output.txt', [result])
    except Exception as e:
        print(f"Ошибка при записи данных в файл: {e}")
        return

    # Измерение времени и памяти
    elapsed_time = time.perf_counter() - t_start
    memory_used = tracemalloc.get_traced_memory()[1] / (1024 ** 2)

    # Останавливаем отслеживание памяти
    tracemalloc.stop()

    # Вывод результатов
    print('Тест примера')
    print(f'Время работы: {elapsed_time:.6f} секунд')
    print(f"Память: {memory_used:.2f} МБ")


def test_sum_of_every_tenth_product():
    """
    Тестирование функции sum_of_every_tenth_product на различных примерах.
    """
    # Пример 1: Стандартный случай
    arr_a = [7, 1, 4, 9]
    arr_b = [2, 7, 8, 11]
    expected = 51  # Ожидаемый результат
    assert sum_of_every_tenth_product(arr_a, arr_b) == expected, "Тест 1 не пройден!"

    # Пример 2: Пустые массивы
    arr_a = []
    arr_b = []
    expected = 0  # Если массивы пустые, результат будет 0
    assert sum_of_every_tenth_product(arr_a, arr_b) == expected, "Тест 2 не пройден!"

    # Пример 3: Массивы с одним элементом
    arr_a = [5]
    arr_b = [5]
    expected = 25  # 5 * 5 = 25
    assert sum_of_every_tenth_product(arr_a, arr_b) == expected, "Тест 3 не пройден!"

    # Пример 4: Массивы с одинаковыми значениями
    arr_a = [1, 1, 1]
    arr_b = [1, 1, 1]
    expected = 1  # 1 * 1, и так каждый десятый — это все те же единицы
    assert sum_of_every_tenth_product(arr_a, arr_b) == expected, "Тест 4 не пройден!"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    # Запуск функции для вычисления суммы каждого десятого произведения
    run_sum_of_every_tenth_product()

    # Запуск тестов
    test_sum_of_every_tenth_product()
